#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""字庫合理性稽核(超越結構檢查, 判斷『這字是否 TOEIC 該有的字』)。
用法: uv run --with wordfreq python scripts/audit_vocab.py
產出四大指標:
  [1] 重複(跨檔/檔內)         — 同字不應橫跨多個分級
  [2] 大小寫異常              — 單字首字母大寫 = 批量生成/爬取痕跡
  [3] 字母群聚(生成痕跡)      — 連續多個同前綴且字母序 = 掃字典生成而非依頻率選字
  [4] 詞頻(罕見字揪出)        — TOEIC 為高頻商務英文; Zipf<3.0 罕見、<2.5 極罕見(多為misspell/非詞/離題)
無 wordfreq 時自動略過 [4]。此腳本唯讀, 不修改任何資料。
"""
import json, re, sys, os
from collections import Counter

FILES = ['data_green.json', 'data_blue.json', 'data_gold.json']
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(f):
    return json.load(open(os.path.join(BASE, f), encoding='utf-8'))

def alpha_clusters(words, min_run=6):
    ws = [w.strip() for w in words]
    runs, i = [], 0
    while i < len(ws):
        j = i
        while (j + 1 < len(ws) and ws[j+1][:3].lower() == ws[i][:3].lower()
               and ws[j+1].lower() >= ws[j].lower()):
            j += 1
        if j - i + 1 >= min_run:
            runs.append((ws[i], ws[j], j - i + 1))
        i = j + 1
    return runs

def main():
    try:
        from wordfreq import zipf_frequency
        have_wf = True
    except Exception:
        have_wf = False

    allw = []
    counts = {}
    for f in FILES:
        d = load(f); counts[f] = len(d)
        for x in d: x['_file'] = f
        allw += d
    total = len(allw)
    print(f"總詞條 = {total}  分級 = {counts}")
    print(f"(對照: 權威 TSL 約 1200 字; 一般 TOEIC 高頻表 600-1200)")

    # [1] 重複
    c = Counter(x['word'].strip().lower() for x in allw)
    dups = [w for w, n in c.items() if n > 1]
    print(f"\n[1] 重複(小寫) = {len(dups)} 個  例: {dups[:8]}")

    # [2] 大小寫異常
    cap = [x['word'] for x in allw if re.match(r'^[A-Z][a-z]+$', x['word'].strip())]
    print(f"[2] 單字首字母大寫異常 = {len(cap)} 個 ({100*len(cap)//total}%)  例: {cap[:10]}")

    # [3] 字母群聚
    print("[3] 字母群聚(連續>=6同前綴, 生成痕跡):")
    for f in FILES:
        r = alpha_clusters([x['word'] for x in load(f)])
        print(f"      {f}: {len(r)} 段  例: {[(a,'..',b,n) for a,b,n in r[:3]]}")

    # [4] 詞頻
    if have_wf:
        def z(w):
            w = w.strip()
            if ' ' in w:
                toks = [t for t in re.split(r'\s+', w) if t.isalpha()]
                return min((zipf_frequency(t, 'en') for t in toks), default=0)
            return zipf_frequency(w.lower(), 'en')
        scored = [(x['word'], x['_file'], z(x['word'])) for x in allw]
        rare = [s for s in scored if s[2] < 3.0]
        vrare = sorted([s for s in scored if s[2] < 2.5], key=lambda t: t[2])
        print(f"\n[4] 詞頻(Zipf): 罕見(<3.0) = {len(rare)} ({100*len(rare)//total}%), "
              f"極罕見(<2.5) = {len(vrare)}")
        print(f"      極罕見例(疑非TOEIC/misspell/非詞): {[w for w,_,_ in vrare[:15]]}")
        for f in FILES:
            fw = [s for s in scored if s[1] == f]
            fr = [s for s in fw if s[2] < 3.0]
            print(f"      {f}: 罕見比例 {100*len(fr)//max(1,len(fw))}% ({len(fr)}/{len(fw)})")
    else:
        print("\n[4] (未安裝 wordfreq, 略過詞頻分析; 請用 `uv run --with wordfreq` 執行)")

    print("\n判讀原則: 重複與大小寫異常應趨近 0; 字母群聚段數越多代表生成灌水越嚴重;")
    print("          罕見比例越高代表越多非 TOEIC 填充字。改善後重跑本稽核即可量化進步。")

if __name__ == "__main__":
    main()
