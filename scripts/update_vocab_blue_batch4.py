import json
import os

def update_vocab():
    # 第四批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Downsize", "phonetic": "/ˈdaʊnsaɪz/", "pos": "v.", "meaning": "裁員, 縮小規模", "level": "blue", "phrases": ["corporate downsizing", "downsize the workforce"], "synonyms": ["reduce", "cut back"], "antonyms": ["expand", "enlarge"], "example": "The company decided to downsize its middle management to reduce operational costs."},
        {"word": "Drastic", "phonetic": "/ˈdræstɪk/", "pos": "adj.", "meaning": "劇烈的, 徹底的", "level": "blue", "phrases": ["drastic measures", "drastic change"], "synonyms": ["extreme", "severe"], "antonyms": ["mild", "slight"], "example": "The government had to take drastic measures to stabilize the falling currency."},
        {"word": "Durable", "phonetic": "/ˈdʊrəbl/", "pos": "adj.", "meaning": "耐用的, 持久的", "level": "blue", "phrases": ["durable goods", "durable relationship"], "synonyms": ["sturdy", "long-lasting"], "antonyms": ["fragile", "perishable"], "example": "These outdoor furniture pieces are made from highly durable materials that resist weathering."},
        {"word": "Eligible", "phonetic": "/ˈelɪdʒəbl/", "pos": "adj.", "meaning": "有資格的, 合適的", "level": "blue", "phrases": ["eligible for a promotion", "eligible candidate"], "synonyms": ["qualified", "suitable"], "antonyms": ["ineligible", "unqualified"], "example": "Full-time employees are eligible for the company's comprehensive health insurance plan."},
        {"word": "Embark", "phonetic": "/ɪmˈbɑːrk/", "pos": "v.", "meaning": "著手, 開始, 上船/飛機", "level": "blue", "phrases": ["embark on a project", "embark on a journey"], "synonyms": ["commence", "undertake"], "antonyms": ["conclude", "finish"], "example": "The organization is about to embark on a major fundraising campaign for the new library."},
        {"word": "Enclose", "phonetic": "/ɪnˈkloʊz/", "pos": "v.", "meaning": "隨函附上, 把...圍起來", "level": "blue", "phrases": ["please find enclosed", "enclose a check"], "synonyms": ["attach", "insert"], "antonyms": [], "example": "I enclose a copy of the signed contract for your personal records."},
        {"word": "Endeavor", "phonetic": "/ɪnˈdevər/", "pos": "v./n.", "meaning": "努力, 盡力", "level": "blue", "phrases": ["scientific endeavor", "make every endeavor"], "synonyms": ["strive", "attempt"], "antonyms": [], "example": "We will endeavor to resolve the technical issues as quickly as possible."},
        {"word": "Enforce", "phonetic": "/ɪnˈfɔːrs/", "pos": "v.", "meaning": "執行, 強制, 實施", "level": "blue", "phrases": ["law enforcement", "enforce regulations"], "synonyms": ["implement", "administer"], "antonyms": ["disregard", "ignore"], "example": "The security guards are hired to enforce the building's safety and access rules."},
        {"word": "Enhance", "phonetic": "/ɪnˈhæns/", "pos": "v.", "meaning": "提升, 增加, 強化", "level": "blue", "phrases": ["enhance productivity", "enhance the image"], "synonyms": ["improve", "boost"], "antonyms": ["diminish", "reduce"], "example": "The new software update is designed to enhance the overall user experience and performance."},
        {"word": "Entail", "phonetic": "/ɪnˈteɪl/", "pos": "v.", "meaning": "牽涉, 需要, 使必要", "level": "blue", "phrases": ["entail risks", "what the job entails"], "synonyms": ["involve", "require"], "antonyms": [], "example": "The proposed expansion will entail a significant increase in the company's annual budget."},
        {"word": "Enterprise", "phonetic": "/ˈentərpraɪz/", "pos": "n.", "meaning": "企業, 公司, 事業心", "level": "blue", "phrases": ["private enterprise", "joint enterprise"], "synonyms": ["corporation", "venture"], "antonyms": [], "example": "The government is encouraging the development of small and medium-sized enterprises (SMEs)."},
        {"word": "Entrepreneur", "phonetic": "/ˌɑːntrəprəˈnɜːr/", "pos": "n.", "meaning": "企業家, 創業者", "level": "blue", "phrases": ["aspiring entrepreneur", "serial entrepreneur"], "synonyms": ["businessperson", "founder"], "antonyms": [], "example": "Successful entrepreneurs are often characterized by their willingness to take calculated risks."},
        {"word": "Eradicate", "phonetic": "/ɪˈrædɪkeɪt/", "pos": "v.", "meaning": "根除, 杜絕", "level": "blue", "phrases": ["eradicate poverty", "eradicate corruption"], "synonyms": ["eliminate", "wipe out"], "antonyms": ["promote", "create"], "example": "The new management team is determined to eradicate corruption within the organization."},
        {"word": "Escalate", "phonetic": "/ˈeskəleɪt/", "pos": "v.", "meaning": "升級, 擴大, 惡化", "level": "blue", "phrases": ["escalate the issue", "escalating costs"], "synonyms": ["intensify", "increase"], "antonyms": ["diminish", "de-escalate"], "example": "If the problem is not resolved locally, it will be escalated to the regional manager."},
        {"word": "Estate", "phonetic": "/ɪˈsteɪt/", "pos": "n.", "meaning": "地產, 遺產, 莊園", "level": "blue", "phrases": ["real estate", "industrial estate"], "synonyms": ["property", "assets"], "antonyms": [], "example": "The agent specializes in high-end real estate in the downtown financial district."},
        {"word": "Eviction", "phonetic": "/ɪˈvɪkʃn/", "pos": "n.", "meaning": "驅逐, 趕出", "level": "blue", "phrases": ["eviction notice", "face eviction"], "synonyms": ["expulsion", "removal"], "antonyms": [], "example": "The tenant was served an eviction notice for failing to pay rent for four consecutive months."},
        {"word": "Exacerbate", "phonetic": "/ɪɡˈzæsərbeɪt/", "pos": "v.", "meaning": "使惡化, 加重", "level": "blue", "phrases": ["exacerbate the problem", "exacerbate tensions"], "synonyms": ["worsen", "aggravate"], "antonyms": ["alleviate", "mitigate"], "example": "The sudden increase in fuel prices will only exacerbate the current economic crisis."},
        {"word": "Exceed", "phonetic": "/ɪkˈsiːd/", "pos": "v.", "meaning": "超過, 勝過", "level": "blue", "phrases": ["exceed expectations", "exceed the limit"], "synonyms": ["surpass", "outperform"], "antonyms": ["fall short", "fail"], "example": "The quarterly sales figures are expected to exceed the company's initial projections."},
        {"word": "Excerpt", "phonetic": "/ˈeksɜːrpt/", "pos": "n./v.", "meaning": "摘錄, 節錄", "level": "blue", "phrases": ["an excerpt from the report", "brief excerpt"], "synonyms": ["extract", "selection"], "antonyms": [], "example": "The newsletter contains a brief excerpt from the CEO's keynote speech at the conference."},
        {"word": "Exclude", "phonetic": "/ɪkˈskluːd/", "pos": "v.", "meaning": "排除, 不包括", "level": "blue", "phrases": ["exclude from the list", "tax excluded"], "synonyms": ["omit", "eliminate"], "antonyms": ["include", "incorporate"], "example": "The total price listed in the catalog excludes shipping and handling charges."}
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
