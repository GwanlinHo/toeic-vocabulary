#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""字庫清理 + 依頻率重新分級(保守, 保護商務詞)。
用法: uv run --with wordfreq python scripts/clean_vocab.py [--write]
  無 --write: 只產出報告與 /tmp/clean_out/*.json 供審(不動原檔)。
  有 --write: 寫回 data_*.json(原檔由 git 保存可還原)。
規則:
  自動安全: 去重、大小寫正規化、修 `~` 分隔符、依頻率重新分級。
  垃圾移除(策展, 保守): 明確拼錯/代碼/破碎文法/離題(化學/物理/古語等), 且不在商務白名單。
  商務低頻詞(nearshoring/Incoterms/BATNA…)一律保留。
"""
import json, re, os, sys
from collections import defaultdict
from wordfreq import zipf_frequency

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['data_green.json', 'data_blue.json', 'data_gold.json']
TIER_ORDER = ['green', 'blue', 'gold']

# 確認為垃圾(拼錯/離題/古僻)——人工檢視後列入; 保守, 只放明確的。
GARBAGE_WORDS = {
    'surmize',            # 拼錯(surmise)
    'slantwise', 'demonically', 'demonstratively', 'discontentedly', 'primitively',
    'solvate', 'aliment', 'efface', 'baseness', 'outpour',
    'tortfeasor', 'appellee',                      # 純法律冷僻
    'astronomer', 'myths', 'mythology', 'mineralogy',  # 明顯離題
}
# 商務白名單: 低頻但正當 TOEIC 商務詞, 永不移除
BUSINESS_KEEP = {
    'nearshoring', 'reshoring', 'insourcing', 'stockout', 'backorder', 'overbook',
    'incoterms', 'batna', 'lifo', 'fifo', 'demurrage', 'touchpoint', 'greenwashing',
    'flexitime', 'reconfirmation', 'anonymization', 'pseudonymization', 'tokenization',
    'containerization', 'computerize', 'synergize', 'lucratively', 'nonintrusive',
    'arrear', 'examinee', 'appraisal', 'b2b', 'b2c', 'mute/unmute',
}
DIGIT_KEEP = {'b2b', 'b2c', '24/7', '9-to-5'}


def load(f): return json.load(open(os.path.join(BASE, f), encoding='utf-8'))

def zipf_of(word):
    w = word.strip()
    if not w: return 0.0
    if ' ' in w:
        toks = [t for t in re.split(r'\s+', w) if t.isalpha()]
        return min((zipf_frequency(t, 'en') for t in toks), default=3.0)
    return zipf_frequency(w.lower(), 'en')

def norm_word(word):
    """正規化: 修 `~`→空格; 首字母大寫且非全大寫縮寫 -> 小寫。回傳 (新字, 是否改動)。"""
    w0 = word.strip()
    w = w0.replace('~', ' ').replace('  ', ' ').strip()
    if not w.isupper() and w and w[0].isupper():
        w = w[0].lower() + w[1:]
    return w, (w != w0)

def classify_garbage(word, meaning):
    lw = word.strip().lower()
    if lw in BUSINESS_KEEP: return None
    if lw in GARBAGE_WORDS: return 'confirmed_garbage'
    if re.search(r'\d', word) and lw not in DIGIT_KEEP: return 'code_or_digit'
    # 破碎所有格: 只抓 xxx's 其中 xxx 非 one/sb/someone 佔位(如 appreciation's ceremony);
    # come to one's assistance / get one's goat / under sb's guidance 為正當慣用語, 保留。
    poss = re.findall(r"(\w+)'s\b", word.lower())
    if poss and any(tok not in ('one', 'sb', 'sb.', 'someone', 'somebody') for tok in poss):
        return 'broken_possessive'
    return None

def main():
    write = '--write' in sys.argv
    entries = []
    for f in FILES:
        for x in load(f):
            x['_orig'] = f.replace('data_', '').replace('.json', '')
            entries.append(x)
    total0 = len(entries)
    rep = {'cap_fixed': [], 'removed': defaultdict(list)}

    # 1) 正規化(修 ~ + 大小寫)
    for x in entries:
        nw, ch = norm_word(x['word'])
        if ch: rep['cap_fixed'].append((x['word'], nw)); x['word'] = nw

    # 2) 策展垃圾移除
    kept = []
    for x in entries:
        g = classify_garbage(x['word'], x.get('meaning', ''))
        if g: rep['removed'][g].append(x['word'])
        else: kept.append(x)

    # 3) 去重(保留資料最完整者)
    def rich(x): return len(str(x.get('meaning',''))) + len(str(x.get('example',''))) + \
                        len(x.get('phrases',[])) + len(x.get('synonyms',[])) + len(x.get('antonyms',[]))
    bykey = defaultdict(list)
    for x in kept: bykey[x['word'].strip().lower()].append(x)
    deduped = []
    for k, xs in bykey.items():
        if len(xs) > 1: rep['removed']['duplicate'].append(k); xs = [max(xs, key=rich)]
        deduped.append(xs[0])

    # 4) 依頻率重新分級(green 高頻→gold 低頻; 維持原比例 800:2000:1600)
    for x in deduped: x['_z'] = zipf_of(x['word'])
    n = len(deduped); g_n = round(n*800/4400); b_n = round(n*2000/4400)
    deduped.sort(key=lambda x: (-x['_z'], x['word'].lower()))
    for i, x in enumerate(deduped):
        x['level'] = 'green' if i < g_n else ('blue' if i < g_n+b_n else 'gold')

    out = defaultdict(list)
    for x in deduped:
        for kk in ('_orig','_z'): x.pop(kk, None)
        out[x['level']].append(x)

    od = '/tmp/clean_out'; os.makedirs(od, exist_ok=True)
    for t in TIER_ORDER:
        json.dump(out[t], open(f"{od}/data_{t}.json",'w',encoding='utf-8'), ensure_ascii=False, indent=2)
        if write:
            json.dump(out[t], open(os.path.join(BASE,f"data_{t}.json"),'w',encoding='utf-8'), ensure_ascii=False, indent=2)

    rm = sum(len(v) for v in rep['removed'].values())
    print(f"=== 清理報告 ===")
    print(f"清理前 {total0} -> 後 {n} (移除 {rm}, 大小寫/~修正 {len(rep['cap_fixed'])})")
    print(f"分級: green={len(out['green'])} blue={len(out['blue'])} gold={len(out['gold'])}")
    print("\n移除明細(可調):")
    for r, ws in rep['removed'].items():
        print(f"  {r}: {len(ws)}  例: {ws[:12]}")
    print(f"\n修正例: {rep['cap_fixed'][:6]}")
    print(f"\n輸出 {od}/  ({'已寫回原檔' if write else '未寫回, 加 --write 才寫'})")

if __name__ == "__main__":
    main()
