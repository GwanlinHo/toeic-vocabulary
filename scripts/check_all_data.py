import json
import os

def check_all_data():
    files = ["data_green.json", "data_blue.json", "data_gold.json"]
    required_keys = ["word", "phonetic", "pos", "meaning", "level", "phrases", "synonyms", "antonyms", "example"]
    
    total_errors = 0
    all_seen_words = {} # 用於跨檔案重複檢查

    for file_path in files:
        print(f"--- 正在檢查 {file_path} ---")
        if not os.path.exists(file_path):
            print(f"警告：檔案 {file_path} 不存在，跳過。")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"❌ 錯誤：JSON 格式毀損！{e}")
                total_errors += 1
                continue

        errors = []
        file_level = file_path.split("_")[1].split(".")[0] # green, blue, gold
        
        for i, item in enumerate(data):
            # 1. 檢查 Key 缺失
            for key in required_keys:
                if key not in item:
                    errors.append(f"索引 {i}: 缺失欄位 '{key}' (單字: {item.get('word', 'Unknown')})")
            
            # 2. 檢查空值
            word_raw = item.get("word")
            if not word_raw:
                errors.append(f"索引 {i}: 'word' 欄位為空")
                continue
            
            word = str(word_raw).strip().lower()
            
            if not item.get("meaning"):
                errors.append(f"索引 {i}: 'meaning' 欄位為空 (單字: {word_raw})")
            if not item.get("example"):
                errors.append(f"索引 {i}: 'example' 欄位為空 (單字: {word_raw})")

            # 3. 檢查重複
            if word in all_seen_words:
                errors.append(f"重複單字: '{word_raw}' (先前出現在 {all_seen_words[word]}，現在又在 {file_path} 索引 {i})")
            else:
                all_seen_words[word] = file_path

            # 4. 檢查等級一致性
            if item.get("level") != file_level:
                errors.append(f"索引 {i}: 等級標籤 '{item.get('level')}' 與檔案名 {file_level} 不符 (單字: {word_raw})")

        if not errors:
            print(f"✅ {file_path} 檢查通過！(單字數: {len(data)})")
        else:
            print(f"❌ {file_path} 發現 {len(errors)} 個錯誤：")
            for err in errors[:10]:
                print(f"  - {err}")
            total_errors += len(errors)

    print("\n--- 檢查總結 ---")
    if total_errors == 0:
        print(f"💯 所有單字庫格式正確，且無跨檔案重複。總計單字量: {len(all_seen_words)}")
    else:
        print(f"⚠️ 總計發現 {total_errors} 個問題，請修正。")

if __name__ == "__main__":
    check_all_data()
