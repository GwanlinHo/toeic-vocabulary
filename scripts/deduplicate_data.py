import json
import os

def deduplicate():
    files = ["data_green.json", "data_blue.json", "data_gold.json"]
    seen_words = set()
    
    for file_path in files:
        if not os.path.exists(file_path):
            print(f"跳過 {file_path} (檔案不存在)")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        original_count = len(data)
        cleaned_data = []
        
        for item in data:
            word = str(item.get("word", "")).strip().lower()
            if not word:
                continue
                
            if word not in seen_words:
                seen_words.add(word)
                cleaned_data.append(item)
            else:
                print(f"移除重複單字: '{item.get('word')}' (來源: {file_path})")
                
        if len(cleaned_data) != original_count:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
            print(f"已更新 {file_path}: {original_count} -> {len(cleaned_data)} 單字")
        else:
            print(f"{file_path} 無需變動")

if __name__ == "__main__":
    deduplicate()
