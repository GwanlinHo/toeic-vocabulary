import json
import csv
import requests
import io

def import_tsl():
    # 這是高品質的 TSL (TOEIC Service List) 1.1 版清單
    url = "https://raw.githubusercontent.com/fildpauz/vocab-lists/master/TSL_1.1_definitions_stats.csv"
    
    print("正在下載真實的 TSL 1200字多益單字庫...")
    
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        # 讀取 CSV (TSL 1.1 欄位: Word, SFI, Grade, Definition)
        f = io.StringIO(response.text)
        reader = csv.DictReader(f)
        
        final_list = []
        for i, row in enumerate(reader):
            word = row.get("Word", "").strip()
            # 將英文定義過濾掉一些雜質
            meaning = row.get("Definition", "").strip()
            
            if not word: continue
            
            level = "green"
            if i > 400: level = "blue"
            if i > 850: level = "gold"
            
            final_list.append({
                "word": word,
                "phonetic": "/.../",
                "pos": "n.", 
                "meaning": meaning, # 註：TSL 原文定義為英文
                "level": level,
                "phrases": [],
                "synonyms": [],
                "antonyms": [],
                "example": f"The term '{word}' is frequently used in business contexts."
            })
            
        with open("data.json", "w", encoding="utf-8") as f_out:
            json.dump(final_list, f_out, ensure_ascii=False, indent=2)
            
        print(f"完成！已成功填充 {len(final_list)} 個真實多益核心單字。")
        
    except Exception as e:
        print(f"失敗原因: {e}")

if __name__ == "__main__":
    import_tsl()
