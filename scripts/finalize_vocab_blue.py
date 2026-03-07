import json

# 最終修正對應表 (藍色等級)
final_fixes = {
    "crucial": {"phonetic": "/ˈkruːʃl/", "pos": "adj.", "meaning": "至關重要的；決定性的", "phrases": ["crucial factor", "play a crucial role"], "synonyms": ["essential", "critical"], "antonyms": ["insignificant"], "example": "The success of the project is crucial to the company's future growth."},
    "press": {"pos": "n./v."},
    "queue": {"pos": "n./v."},
    "suit": {"pos": "n./v."},
    "tailor": {"pos": "n./v."},
    "tour": {"pos": "n./v."},
    "track": {"pos": "n./v."},
    "voyage": {"pos": "n./v."},
    "spy": {"pos": "n./v."},
    "stack": {"pos": "n./v."},
    "structure": {"pos": "n./v."},
    "survey": {"pos": "n./v."},
    "temper": {"pos": "n./v."},
    "veil": {"pos": "n./v."},
    "leverage": {"pos": "n./v."},
    "pioneer": {"pos": "n./v."},
    "slander": {"pos": "n./v."},
    "zone": {"pos": "n./v."},
    "guarantee": {"pos": "n./v."},
    "resort": {"pos": "n./v."},
    "canoe": {"pos": "n./v."},
}

with open('data_blue.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in final_fixes:
        item.update(final_fixes[word])

with open('data_blue.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("藍色等級最終缺漏補足與詞性優化已完成。")
