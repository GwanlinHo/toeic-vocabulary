import json
import os

def update_vocab():
    # 第八批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Pending", "phonetic": "/ˈpendɪŋ/", "pos": "adj.", "meaning": "待定的, 懸而未決的", "level": "blue", "phrases": ["pending approval", "patent pending"], "synonyms": ["undecided", "imminent"], "antonyms": ["settled", "decided"], "example": "The merger is currently pending approval from the national competition authority."},
        {"word": "Personnel", "phonetic": "/ˌpɜːrsəˈnel/", "pos": "n.", "meaning": "人員, 員工, 人事部門", "level": "blue", "phrases": ["personnel manager", "medical personnel"], "synonyms": ["staff", "workforce"], "antonyms": [], "example": "All unauthorized personnel are strictly prohibited from entering the server room."},
        {"word": "Pharmaceutical", "phonetic": "/ˌfɑːrməˈsuːtɪkl/", "pos": "adj./n.", "meaning": "製藥的, 藥物", "level": "blue", "phrases": ["pharmaceutical industry", "pharmaceutical company"], "synonyms": ["medicinal"], "antonyms": [], "example": "The pharmaceutical company is investing heavily in the research and development of new vaccines."},
        {"word": "Pipeline", "phonetic": "/ˈpaɪplaɪn/", "pos": "n.", "meaning": "管道, 在處理中的計畫", "level": "blue", "phrases": ["in the pipeline", "oil pipeline"], "synonyms": [], "antonyms": [], "example": "We have several innovative products in the pipeline that are expected to launch late next year."},
        {"word": "Portfolio", "phonetic": "/pɔːrtˈfoʊlioʊ/", "pos": "n.", "meaning": "作品集, 投資組合, 職責", "level": "blue", "phrases": ["investment portfolio", "design portfolio"], "synonyms": [], "antonyms": [], "example": "Investors are advised to diversify their portfolios to minimize potential risks in the market."},
        {"word": "Postpone", "phonetic": "/poʊˈspoʊn/", "pos": "v.", "meaning": "延期, 推遲", "level": "blue", "phrases": ["postpone a meeting", "indefinitely postponed"], "synonyms": ["delay", "defer"], "antonyms": ["advance", "expedite"], "example": "The outdoor event was postponed until next week due to the heavy rain forecast."},
        {"word": "Potential", "phonetic": "/pəˈtenʃl/", "pos": "adj./n.", "meaning": "潛在的, 潛力", "level": "blue", "phrases": ["potential customer", "full potential"], "synonyms": ["possible", "prospective"], "antonyms": ["actual", "existing"], "example": "The new marketing strategy is aimed at attracting potential customers from the younger demographic."},
        {"word": "Precaution", "phonetic": "/prɪˈkɔːʃn/", "pos": "n.", "meaning": "預防措施", "level": "blue", "phrases": ["safety precautions", "take precautions"], "synonyms": ["safeguard", "preventative measure"], "antonyms": [], "example": "As a precaution, the building was evacuated immediately after the fire alarm went off."},
        {"word": "Predecessor", "phonetic": "/ˈpredəsesər/", "pos": "n.", "meaning": "前任, 前輩, 原先的東西", "level": "blue", "phrases": ["immediate predecessor", "illustrious predecessor"], "synonyms": ["ancestor", "forerunner"], "antonyms": ["successor"], "example": "The new model is significantly more energy-efficient than its predecessor."},
        {"word": "Preliminary", "phonetic": "/prɪˈlɪmɪneri/", "pos": "adj.", "meaning": "初步的, 預備的", "level": "blue", "phrases": ["preliminary report", "preliminary investigation"], "synonyms": ["initial", "introductory"], "antonyms": ["final", "concluding"], "example": "The preliminary results of the market survey indicate a strong demand for organic products."},
        {"word": "Premium", "phonetic": "/ˈpriːmiəm/", "pos": "n./adj.", "meaning": "獎金, 保險費, 優質的", "level": "blue", "phrases": ["insurance premium", "premium quality"], "synonyms": ["bonus", "superior"], "antonyms": ["inferior", "basic"], "example": "Customers are often willing to pay a premium for products that are environmentally friendly."},
        {"word": "Prestige", "phonetic": "/preˈstiːʒ/", "pos": "n.", "meaning": "聲望, 威信", "level": "blue", "phrases": ["high prestige", "gain prestige"], "synonyms": ["reputation", "status"], "antonyms": ["disrepute", "insignificance"], "example": "The award has added significant prestige to the university's architecture department."},
        {"word": "Prioritize", "phonetic": "/praɪˈɔːrətaɪz/", "pos": "v.", "meaning": "優先考慮, 確定優先順序", "level": "blue", "phrases": ["prioritize tasks", "prioritize safety"], "synonyms": [], "antonyms": [], "example": "With so many projects underway, it is essential to prioritize the most urgent tasks."},
        {"word": "Procedure", "phonetic": "/prəˈsiːdʒər/", "pos": "n.", "meaning": "程序, 步驟, 手續", "level": "blue", "phrases": ["standard procedure", "follow a procedure"], "synonyms": ["process", "method"], "antonyms": [], "example": "The technician explained the step-by-step procedure for replacing the broken part."},
        {"word": "Productive", "phonetic": "/prəˈdʌktɪv/", "pos": "adj.", "meaning": "富有成效的, 多產的", "level": "blue", "phrases": ["productive meeting", "highly productive"], "synonyms": ["fruitful", "efficient"], "antonyms": ["unproductive", "useless"], "example": "The morning session was very productive, and we managed to resolve several key issues."},
        {"word": "Proficient", "phonetic": "/prəˈfɪʃnt/", "pos": "adj.", "meaning": "精通的, 熟練的", "level": "blue", "phrases": ["proficient in English", "highly proficient"], "synonyms": ["skilled", "expert"], "antonyms": ["incompetent", "unskilled"], "example": "Candidates must be proficient in at least two foreign languages to be considered for the role."},
        {"word": "Projection", "phonetic": "/prəˈdʒekʃn/", "pos": "n.", "meaning": "預測, 推測, 投影", "level": "blue", "phrases": ["financial projections", "sales projection"], "synonyms": ["forecast", "estimate"], "antonyms": [], "example": "The company's latest financial projections suggest a steady growth over the next five years."},
        {"word": "Promising", "phonetic": "/ˈprɑːmɪsɪŋ/", "pos": "adj.", "meaning": "有前途的, 大有希望的", "level": "blue", "phrases": ["promising start", "promising candidate"], "synonyms": ["encouraging", "hopeful"], "antonyms": ["unpromising", "discouraging"], "example": "The initial tests of the new drug have shown very promising results in clinical trials."},
        {"word": "Prompt", "phonetic": "/prɑːmpt/", "pos": "adj./v.", "meaning": "及時的, 迅速的, 促使", "level": "blue", "phrases": ["prompt reply", "prompt delivery"], "synonyms": ["quick", "immediate"], "antonyms": ["slow", "delayed"], "example": "Thank you for your prompt response to our inquiry regarding the shipping delay."},
        {"word": "Proofread", "phonetic": "/ˈpruːfriːd/", "pos": "v.", "meaning": "校對", "level": "blue", "phrases": ["proofread the manuscript", "carefully proofread"], "synonyms": ["edit", "review"], "antonyms": [], "example": "Please proofread the final draft of the contract carefully before sending it to the client."}
    ]
    
    file_path = "data_blue.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                current_data = json.load(f)
            except:
                current_data = []
    else:
        current_data = []

    # 避免重複 (根據 word)
    existing_words = {item['word'].lower() for item in current_data}
    added_count = 0
    for item in new_data:
        if item['word'].lower() not in existing_words:
            current_data.append(item)
            added_count += 1
            
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(current_data, f, ensure_ascii=False, indent=2)
        
    print(f"成功合併！新增了 {added_count} 個單字到 {file_path}，目前總計 {len(current_data)} 個單字。")

if __name__ == "__main__":
    update_vocab()
