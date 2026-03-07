import json
import os

def update_vocab():
    # 第五批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Expedite", "phonetic": "/ˈekspədaɪt/", "pos": "v.", "meaning": "加速, 促進", "level": "blue", "phrases": ["expedite the process", "expedited shipping"], "synonyms": ["accelerate", "hasten"], "antonyms": ["delay", "hinder"], "example": "We are looking for ways to expedite the delivery of the components to avoid further production delays."},
        {"word": "Facilitate", "phonetic": "/fəˈsɪlɪteɪt/", "pos": "v.", "meaning": "促進, 使便利", "level": "blue", "phrases": ["facilitate communication", "facilitate a meeting"], "synonyms": ["ease", "assist"], "antonyms": ["obstruct", "complicate"], "example": "The new online portal is designed to facilitate communication between the regional offices and headquarters."},
        {"word": "Forfeit", "phonetic": "/ˈfɔːrfɪt/", "pos": "v./n.", "meaning": "沒收, 喪失, 罰金", "level": "blue", "phrases": ["forfeit the deposit", "forfeit the right"], "synonyms": ["relinquish", "surrender"], "antonyms": ["retain", "keep"], "example": "Clients who cancel their reservations less than 24 hours in advance will forfeit their initial deposit."},
        {"word": "Fragile", "phonetic": "/ˈfrædʒl/", "pos": "adj.", "meaning": "易碎的, 脆弱的", "level": "blue", "phrases": ["fragile items", "fragile recovery"], "synonyms": ["delicate", "brittle"], "antonyms": ["sturdy", "durable"], "example": "Please handle this box with care as it contains fragile laboratory equipment."},
        {"word": "Freight", "phonetic": "/freɪt/", "pos": "n./v.", "meaning": "貨運, 貨物", "level": "blue", "phrases": ["air freight", "freight forwarder"], "synonyms": ["cargo", "shipment"], "antonyms": [], "example": "The cost of air freight has increased significantly due to the recent rise in fuel prices."},
        {"word": "Grievance", "phonetic": "/ˈɡriːvəns/", "pos": "n.", "meaning": "不滿, 投訴, 抱怨", "level": "blue", "phrases": ["file a grievance", "employee grievance"], "synonyms": ["complaint", "objection"], "antonyms": [], "example": "The HR department has established a formal procedure for employees to file grievances regarding workplace conditions."},
        {"word": "Haggle", "phonetic": "/ˈhæɡl/", "pos": "v.", "meaning": "討價還價", "level": "blue", "phrases": ["haggle over the price", "stop haggling"], "synonyms": ["bargain", "negotiate"], "antonyms": [], "example": "In many local markets, it is customary for customers to haggle with vendors over the price of goods."},
        {"word": "Handicap", "phonetic": "/ˈhændikæp/", "pos": "n./v.", "meaning": "障礙, 不利條件, 妨礙", "level": "blue", "phrases": ["physical handicap", "severely handicapped"], "synonyms": ["disadvantage", "obstacle"], "antonyms": ["advantage", "benefit"], "example": "The lack of reliable high-speed internet is a significant handicap for businesses in remote areas."},
        {"word": "Hazardous", "phonetic": "/ˈhæzərdəs/", "pos": "adj.", "meaning": "危險的, 有害的", "level": "blue", "phrases": ["hazardous waste", "hazardous materials"], "synonyms": ["dangerous", "risky"], "antonyms": ["safe", "harmless"], "example": "Special training is required for all employees who handle hazardous chemicals in the manufacturing plant."},
        {"word": "Improvise", "phonetic": "/ˈɪmprəvaɪz/", "pos": "v.", "meaning": "即興創作, 臨時湊合", "level": "blue", "phrases": ["improvise a solution", "improvised speech"], "synonyms": ["extemporize", "ad-lib"], "antonyms": ["prepare", "rehearse"], "example": "When the projector failed, the presenter had to improvise using a whiteboard and markers."},
        {"word": "Incentive", "phonetic": "/ɪnˈsentɪv/", "pos": "n.", "meaning": "動機, 激勵, 獎勵", "level": "blue", "phrases": ["tax incentive", "financial incentive"], "synonyms": ["motivation", "stimulus"], "antonyms": ["deterrent", "discouragement"], "example": "The government is offering tax incentives to companies that invest in renewable energy sources."},
        {"word": "Incidental", "phonetic": "/ˌɪnsɪˈdentl/", "pos": "adj.", "meaning": "附帶的, 偶然的", "level": "blue", "phrases": ["incidental expenses", "incidental music"], "synonyms": ["secondary", "subordinate"], "antonyms": ["essential", "primary"], "example": "The budget covers major project costs but does not include incidental expenses like travel and meals."},
        {"word": "Indispensable", "phonetic": "/ˌɪndɪˈspensəbl/", "pos": "adj.", "meaning": "不可或缺的", "level": "blue", "phrases": ["indispensable tool", "prove indispensable"], "synonyms": ["essential", "vital"], "antonyms": ["dispensable", "unnecessary"], "example": "The new project management software has become an indispensable tool for our development team."},
        {"word": "Infrastructure", "phonetic": "/ˈɪnfrəstrʌktʃər/", "pos": "n.", "meaning": "基礎設施, 公共建設", "level": "blue", "phrases": ["critical infrastructure", "infrastructure project"], "synonyms": ["foundation", "framework"], "antonyms": [], "example": "Significant investment is needed to modernize the city's aging transportation infrastructure."},
        {"word": "Inherit", "phonetic": "/ɪnˈherɪt/", "pos": "v.", "meaning": "繼承", "level": "blue", "phrases": ["inherit a fortune", "inherit a problem"], "synonyms": ["succeed to"], "antonyms": ["bequeath"], "example": "The new CEO inherited a company that was struggling with significant financial debt."},
        {"word": "Initiate", "phonetic": "/ɪˈnɪʃieɪt/", "pos": "v.", "meaning": "發起, 開始, 接納", "level": "blue", "phrases": ["initiate a project", "initiate contact"], "synonyms": ["commence", "launch"], "antonyms": ["terminate", "conclude"], "example": "The department plans to initiate a new series of professional development workshops next month."},
        {"word": "Innovative", "phonetic": "/ˈɪnəveɪtɪv/", "pos": "adj.", "meaning": "創新的, 新穎的", "level": "blue", "phrases": ["innovative design", "innovative approach"], "synonyms": ["original", "groundbreaking"], "antonyms": ["traditional", "conventional"], "example": "The company is known for its innovative approach to sustainable packaging solutions."},
        {"word": "Insight", "phonetic": "/ˈɪnsaɪt/", "pos": "n.", "meaning": "洞察力, 見解", "level": "blue", "phrases": ["valuable insight", "gain insight into"], "synonyms": ["understanding", "perception"], "antonyms": [], "example": "The market research report provides valuable insights into current consumer spending habits."},
        {"word": "Inspection", "phonetic": "/ɪnˈspekʃn/", "pos": "n.", "meaning": "檢查, 視察", "level": "blue", "phrases": ["safety inspection", "routine inspection"], "synonyms": ["scrutiny", "examination"], "antonyms": [], "example": "The facility underwent a rigorous safety inspection by the local health department last week."},
        {"word": "Installment", "phonetic": "/ɪnˈstɔːlmənt/", "pos": "n.", "meaning": "分期付款, (連載)一期", "level": "blue", "phrases": ["monthly installments", "pay in installments"], "synonyms": [], "antonyms": [], "example": "Customers have the option to pay for the new equipment in twelve equal monthly installments."}
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
