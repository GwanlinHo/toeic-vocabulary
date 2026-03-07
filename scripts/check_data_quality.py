import json
import os

def check_data_quality(file_path):
    print(f"--- 正在檢查 {file_path} ---")
    if not os.path.exists(file_path):
        print("錯誤：檔案不存在。")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"錯誤：JSON 格式毀損！{e}")
            return

    required_keys = ["word", "phonetic", "pos", "meaning", "level", "phrases", "synonyms", "antonyms", "example"]
    errors = []
    seen_words = {}
    
    for i, item in enumerate(data):
        # 1. 檢查 Key 缺失
        for key in required_keys:
            if key not in item:
                errors.append(f"索引 {i}: 缺失欄位 '{key}' (單字: {item.get('word', 'Unknown')})")
        
        # 2. 檢查空值
        if not item.get("word"):
            errors.append(f"索引 {i}: 'word' 欄位為空")
        if not item.get("meaning"):
            errors.append(f"索引 {i}: 'meaning' 欄位為空 (單字: {item.get('word')})")
        if not item.get("example"):
            errors.append(f"索引 {i}: 'example' 欄位為空 (單字: {item.get('word')})")

        # 3. 檢查重複 (不分大小寫)
        word = str(item.get("word")).strip().lower()
        if word in seen_words:
            errors.append(f"重複單字: '{item.get('word')}' (出現在索引 {seen_words[word]} 和 {i})")
        else:
            seen_words[word] = i

        # 4. 檢查等級是否一致
        if item.get("level") != "blue":
            errors.append(f"索引 {i}: 等級錯誤，預期為 'blue' 但得到 '{item.get('level')}' (單字: {item.get('word')})")

    if not errors:
        print(f"✅ 檢查完成！總計 {len(data)} 個單字，未發現任何錯誤。")
    else:
        print(f"❌ 發現 {len(errors)} 個錯誤：")
        for err in errors[:20]: # 只顯示前 20 個
            print(f"  - {err}")
        if len(errors) > 20:
            print(f"  ... 以及其他 {len(errors) - 20} 個錯誤")

if __name__ == "__main__":
    check_data_quality("data_blue.json")
