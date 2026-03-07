import json
import os

def update_vocab():
    # 第三批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Acquisition", "phonetic": "/ˌækwɪˈzɪʃn/", "pos": "n.", "meaning": "收購, 獲得", "level": "blue", "phrases": ["merger and acquisition", "recent acquisition"], "synonyms": ["procurement", "gain"], "antonyms": ["divestiture", "loss"], "example": "The tech giant announced its latest acquisition of a promising AI startup yesterday."},
        {"word": "Adverse", "phonetic": "/ədˈvɜːrs/", "pos": "adj.", "meaning": "不利的, 負面的", "level": "blue", "phrases": ["adverse effects", "adverse weather conditions"], "synonyms": ["unfavorable", "negative"], "antonyms": ["beneficial", "favorable"], "example": "The company's stock price dropped due to adverse market conditions."},
        {"word": "Affiliate", "phonetic": "/əˈfɪlieɪt/", "pos": "n./v.", "meaning": "附屬機構, 使隸屬", "level": "blue", "phrases": ["affiliate program", "marketing affiliate"], "synonyms": ["associate", "partner"], "antonyms": [], "example": "Our company has several affiliates in Europe to handle local distribution."},
        {"word": "Amendment", "phonetic": "/əˈmendmənt/", "pos": "n.", "meaning": "修正案, 改正", "level": "blue", "phrases": ["constitutional amendment", "propose an amendment"], "synonyms": ["correction", "revision"], "antonyms": [], "example": "The legal team is drafting an amendment to the existing service contract."},
        {"word": "Backlog", "phonetic": "/ˈbækˌlɔːɡ/", "pos": "n.", "meaning": "積壓的工作, 待辦事項", "level": "blue", "phrases": ["order backlog", "reduce the backlog"], "synonyms": ["reserve", "accumulation"], "antonyms": [], "example": "The factory is working overtime to clear the backlog of orders from the holiday season."},
        {"word": "Breach", "phonetic": "/briːtʃ/", "pos": "v./n.", "meaning": "違反, 破壞, 違約", "level": "blue", "phrases": ["breach of contract", "security breach"], "synonyms": ["violation", "infringement"], "antonyms": ["observance", "compliance"], "example": "Failure to deliver the goods on time will be considered a breach of contract."},
        {"word": "Brochure", "phonetic": "/broʊˈʃʊr/", "pos": "n.", "meaning": "小冊子, 廣告手冊", "level": "blue", "phrases": ["promotional brochure", "travel brochure"], "synonyms": ["booklet", "pamphlet"], "antonyms": [], "example": "The marketing department is designing a new brochure to showcase our latest products."},
        {"word": "Circulation", "phonetic": "/ˌsɜːrkjəˈleɪʃn/", "pos": "n.", "meaning": "發行量, 流通, 循環", "level": "blue", "phrases": ["newspaper circulation", "in circulation"], "synonyms": ["distribution", "diffusion"], "antonyms": [], "example": "The magazine has a monthly circulation of over 500,000 copies."},
        {"word": "Clause", "phonetic": "/klɔːz/", "pos": "n.", "meaning": "條款, 從句", "level": "blue", "phrases": ["confidentiality clause", "termination clause"], "synonyms": ["provision", "stipulation"], "antonyms": [], "example": "The confidentiality clause in the agreement prevents us from disclosing the project details."},
        {"word": "Collateral", "phonetic": "/kəˈlætərəl/", "pos": "n./adj.", "meaning": "抵押品, 附帶的", "level": "blue", "phrases": ["loan collateral", "collateral damage"], "synonyms": ["security", "guarantee"], "antonyms": [], "example": "The bank requires the borrower to provide real estate as collateral for the loan."},
        {"word": "Compulsory", "phonetic": "/kəmˈpʌlsəri/", "pos": "adj.", "meaning": "強制性的, 義務的", "level": "blue", "phrases": ["compulsory education", "compulsory attendance"], "synonyms": ["mandatory", "obligatory"], "antonyms": ["voluntary", "optional"], "example": "Attendance at the annual safety training workshop is compulsory for all staff members."},
        {"word": "Confidential", "phonetic": "/ˌkɑːnfɪˈdenʃl/", "pos": "adj.", "meaning": "機密的, 秘密的", "level": "blue", "phrases": ["confidential information", "strictly confidential"], "synonyms": ["secret", "private"], "antonyms": ["public", "open"], "example": "All employee records are kept in a confidential file in the HR department."},
        {"word": "Consecutive", "phonetic": "/kənˈsekjətɪv/", "pos": "adj.", "meaning": "連續的, 連貫的", "level": "blue", "phrases": ["consecutive days", "third consecutive year"], "synonyms": ["successive", "sequential"], "antonyms": ["intermittent", "discontinuous"], "example": "The company has reported record profits for the third consecutive year."},
        {"word": "Counterfeit", "phonetic": "/ˈkaʊntərfɪt/", "pos": "adj./n./v.", "meaning": "偽造的, 贗品", "level": "blue", "phrases": ["counterfeit goods", "counterfeit money"], "synonyms": ["fake", "forged"], "antonyms": ["authentic", "genuine"], "example": "The authorities seized a large shipment of counterfeit luxury handbags at the port."},
        {"word": "Credential", "phonetic": "/krəˈdenʃl/", "pos": "n.", "meaning": "憑證, 資歷, 證書", "level": "blue", "phrases": ["academic credentials", "login credentials"], "synonyms": ["qualification", "certificate"], "antonyms": [], "example": "The candidate's impressive credentials made her the top choice for the senior management position."},
        {"word": "Cumulative", "phonetic": "/ˈkjuːmjəleɪtɪv/", "pos": "adj.", "meaning": "累積的", "level": "blue", "phrases": ["cumulative total", "cumulative effect"], "synonyms": ["accumulated", "collective"], "antonyms": [], "example": "The cumulative effect of these small changes will lead to significant improvements over time."},
        {"word": "Deadline", "phonetic": "/ˈdedlaɪn/", "pos": "n.", "meaning": "截止日期", "level": "blue", "phrases": ["meet a deadline", "strict deadline"], "synonyms": ["cutoff", "limit"], "antonyms": [], "example": "We are working hard to meet the deadline for the final project submission."},
        {"word": "Defer", "phonetic": "/dɪˈfɜːr/", "pos": "v.", "meaning": "推遲, 延期", "level": "blue", "phrases": ["defer payment", "defer a decision"], "synonyms": ["postpone", "delay"], "antonyms": ["expedite", "advance"], "example": "The board decided to defer the decision until more information becomes available."},
        {"word": "Demographic", "phonetic": "/ˌdeməˈɡræfɪk/", "pos": "adj./n.", "meaning": "人口統計的, 特定族群", "level": "blue", "phrases": ["target demographic", "demographic changes"], "synonyms": [], "antonyms": [], "example": "Our new advertising campaign is specifically designed to reach the younger demographic."},
        {"word": "Deteriorate", "phonetic": "/dɪˈtɪriəreɪt/", "pos": "v.", "meaning": "惡化, 退化", "level": "blue", "phrases": ["deteriorate rapidly", "conditions deteriorate"], "synonyms": ["worsen", "decline"], "antonyms": ["improve", "enhance"], "example": "The relationship between the two companies began to deteriorate after the failed merger."}
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
