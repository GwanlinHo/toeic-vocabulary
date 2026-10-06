#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""離線替單字加上斷字點（軟連字號 U+00AD），寫入 data_*.json 的 word_shy 欄位。

為什麼要離線做：CSS 的 hyphens:auto 得靠瀏覽器自帶的斷字字典，缺字典會靜默失效
（本機 Chromium 實測完全沒作用），各平台也不一致。改成離線把斷點算好寫進資料，
執行期零成本、所有平台斷點一致，也維持純靜態離線架構。

演算法：Liang（TeX）斷字樣式，字典用系統的 /usr/share/hyphen/hyph_en_GB.dic。
軟連字號是零寬字元，只在需要換行時才顯示成連字號；朗讀與 learnedWords 比對
一律用原本的 word 欄位，不受影響。

用法：scripts/add_hyphenation.py [字典路徑]
"""
import json
import os
import re
import sys

SHY = '­'
DEFAULT_DIC = '/usr/share/hyphen/hyph_en_GB.dic'
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def load_patterns(path):
    """讀 Hunspell 斷字字典，回傳 (樣式表, 左最少字數, 右最少字數)。"""
    left, right = 2, 3
    patterns = {}
    with open(path, encoding='utf-8') as f:
        for lineno, raw in enumerate(f):
            line = raw.strip()
            if lineno == 0 or not line or line.startswith('%'):
                continue  # 第一行是編碼宣告
            if line.startswith('LEFTHYPHENMIN'):
                left = int(line.split()[1]); continue
            if line.startswith('RIGHTHYPHENMIN'):
                right = int(line.split()[1]); continue
            if line[0].isupper() or '=' in line:
                continue  # 其他設定行與非標準斷字規則，一律略過
            key = re.sub(r'\d', '', line)
            values = []
            num = 0
            for ch in line:
                if ch.isdigit():
                    num = int(ch)
                else:
                    values.append(num)
                    num = 0
            values.append(num)
            patterns[key] = values
    return patterns, left, right


def hyphenate(word, patterns, left, right):
    """回傳插入軟連字號後的字串；沒有合法斷點就原樣回傳。"""
    lower = word.lower()
    if not lower.isalpha() or len(lower) < left + right:
        return word
    text = '.' + lower + '.'
    points = [0] * (len(text) + 1)
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            values = patterns.get(text[i:j])
            if values:
                for k, v in enumerate(values):
                    if v > points[i + k]:
                        points[i + k] = v
    # points 的索引比 word 多一個「.」的位移：points[i+1] 對應 word[i] 之後
    out = []
    for i, ch in enumerate(word):
        out.append(ch)
        pos = i + 1  # word 中已輸出的字數
        if pos < left or len(word) - pos < right:
            continue
        if points[pos + 1] % 2 == 1:
            out.append(SHY)
    return ''.join(out)


def hyphenate_phrase(text, patterns, left, right):
    """逐個英文詞斷字，保留原本的空白與標點。"""
    return re.sub(r"[A-Za-z]+",
                  lambda m: hyphenate(m.group(0), patterns, left, right),
                  text)


def main():
    dic = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIC
    if not os.path.exists(dic):
        sys.exit('[X] 找不到斷字字典：%s（Debian 可裝 hyphen-en-gb）' % dic)
    patterns, left, right = load_patterns(dic)
    print('[O] 載入 %d 條斷字樣式（left=%d right=%d）' % (len(patterns), left, right))

    for level in ('green', 'blue', 'gold'):
        path = os.path.join(DATA_DIR, 'data_%s.json' % level)
        with open(path, encoding='utf-8') as f:
            words = json.load(f)
        changed = 0
        for w in words:
            shy = hyphenate_phrase(w['word'], patterns, left, right)
            if shy != w['word']:
                w['word_shy'] = shy
                changed += 1
            else:
                w.pop('word_shy', None)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(words, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('[O] %-6s 共 %4d 字，其中 %4d 字有斷點' % (level, len(words), changed))


if __name__ == '__main__':
    main()
