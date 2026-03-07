import json
import os

def update_vocab():
    # 第二批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Brokerage", "phonetic": "/ˈbroʊkərɪdʒ/", "pos": "n.", "meaning": "經紀業務, 佣金", "level": "blue", "phrases": ["brokerage firm", "real estate brokerage"], "synonyms": ["commission", "agency"], "antonyms": [], "example": "The brokerage firm charges a 2% commission on all stock trades."},
        {"word": "Carousel", "phonetic": "/ˌkærəˈsel/", "pos": "n.", "meaning": "行李轉盤, 旋轉木馬", "level": "blue", "phrases": ["baggage carousel", "luggage carousel"], "synonyms": ["conveyor belt"], "antonyms": [], "example": "Please wait for your luggage at baggage carousel number five."},
        {"word": "Commodity", "phonetic": "/kəˈmɑːdəti/", "pos": "n.", "meaning": "商品, 日用品", "level": "blue", "phrases": ["staple commodity", "commodity market"], "synonyms": ["product", "merchandise"], "antonyms": [], "example": "Oil is one of the most actively traded commodities in the global market."},
        {"word": "Compliance", "phonetic": "/kəmˈplaɪəns/", "pos": "n.", "meaning": "合規, 順從", "level": "blue", "phrases": ["regulatory compliance", "in compliance with"], "synonyms": ["adherence", "conformity"], "antonyms": ["defiance", "violation"], "example": "All factory operations are in strict compliance with environmental regulations."},
        {"word": "Consortium", "phonetic": "/kənˈsɔːrtiəm/", "pos": "n.", "meaning": "財團, 聯盟, 協會", "level": "blue", "phrases": ["international consortium", "banking consortium"], "synonyms": ["syndicate", "alliance"], "antonyms": [], "example": "A consortium of international banks provided the funding for the new infrastructure project."},
        {"word": "Contingency", "phonetic": "/kənˈtɪndʒənsi/", "pos": "n.", "meaning": "偶發事件, 應急費用", "level": "blue", "phrases": ["contingency plan", "contingency fund"], "synonyms": ["possibility", "eventuality"], "antonyms": ["certainty"], "example": "We have developed a contingency plan in case the supply chain is disrupted."},
        {"word": "Courier", "phonetic": "/ˈkɜːriər/", "pos": "n.", "meaning": "信差, 快遞員", "level": "blue", "phrases": ["express courier", "courier service"], "synonyms": ["messenger", "carrier"], "antonyms": [], "example": "The legal documents were sent via express courier to ensure next-day delivery."},
        {"word": "Deductible", "phonetic": "/dɪˈdʌktəbl/", "pos": "adj./n.", "meaning": "可扣除的, (保險)自付額", "level": "blue", "phrases": ["tax deductible", "insurance deductible"], "synonyms": [], "antonyms": [], "example": "Business travel expenses are usually tax deductible under the current law."},
        {"word": "Default", "phonetic": "/dɪˈfɔːlt/", "pos": "v./n.", "meaning": "違約, 預設值", "level": "blue", "phrases": ["default on a loan", "by default"], "synonyms": ["failure", "omission"], "antonyms": ["fulfillment", "payment"], "example": "The company may be forced to file for bankruptcy if it defaults on its bond payments."},
        {"word": "Deficit", "phonetic": "/ˈdefɪsɪt/", "pos": "n.", "meaning": "赤字, 虧損", "level": "blue", "phrases": ["trade deficit", "budget deficit"], "synonyms": ["shortage", "shortfall"], "antonyms": ["surplus", "excess"], "example": "The government is struggling to reduce the widening trade deficit with its major partners."},
        {"word": "Delegate", "phonetic": "/ˈdelɪɡət/", "pos": "v./n.", "meaning": "委派, 授權, 代表", "level": "blue", "phrases": ["delegate authority", "conference delegate"], "synonyms": ["assign", "entrust"], "antonyms": ["keep", "retain"], "example": "Effective managers know how to delegate tasks to their team members appropriately."},
        {"word": "Depreciation", "phonetic": "/dɪˌpriːʃiˈeɪʃn/", "pos": "n.", "meaning": "貶值, 折舊", "level": "blue", "phrases": ["currency depreciation", "annual depreciation"], "synonyms": ["devaluation", "reduction"], "antonyms": ["appreciation"], "example": "The depreciation of the local currency has made imported goods significantly more expensive."},
        {"word": "Discrepancy", "phonetic": "/dɪˈskrepənsi/", "pos": "n.", "meaning": "差異, 不一致", "level": "blue", "phrases": ["significant discrepancy", "price discrepancy"], "synonyms": ["inconsistency", "variance"], "antonyms": ["consistency", "agreement"], "example": "The accountant found a major discrepancy between the physical inventory and the digital records."},
        {"word": "Dividend", "phonetic": "/ˈdɪvɪdend/", "pos": "n.", "meaning": "紅利, 股息", "level": "blue", "phrases": ["annual dividend", "dividend yield"], "synonyms": ["bonus", "share"], "antonyms": [], "example": "The company's board of directors approved a dividend payment of $0.50 per share."},
        {"word": "Endorsement", "phonetic": "/ɪnˈdɔːrsmənt/", "pos": "n.", "meaning": "背書, 贊同, 代言", "level": "blue", "phrases": ["celebrity endorsement", "official endorsement"], "synonyms": ["approval", "sanction"], "antonyms": ["disapproval", "rejection"], "example": "The new fitness app received an official endorsement from the national health association."},
        {"word": "Equity", "phonetic": "/ˈekwəti/", "pos": "n.", "meaning": "公平, 股權", "level": "blue", "phrases": ["private equity", "brand equity"], "synonyms": ["fairness", "justice", "ownership"], "antonyms": ["injustice", "inequality"], "example": "The employees were offered equity in the company as part of their compensation package."},
        {"word": "Excursion", "phonetic": "/ɪkˈskɜːrʒn/", "pos": "n.", "meaning": "遠足, 短途旅行", "level": "blue", "phrases": ["day excursion", "business excursion"], "synonyms": ["trip", "outing"], "antonyms": [], "example": "The conference organizers arranged a day excursion to the nearby historic landmarks."},
        {"word": "Expenditure", "phonetic": "/ɪkˈspendɪtʃər/", "pos": "n.", "meaning": "支出, 花費", "level": "blue", "phrases": ["capital expenditure", "public expenditure"], "synonyms": ["spending", "outlay"], "antonyms": ["income", "revenue"], "example": "The company is looking for ways to reduce its annual expenditure on office supplies."},
        {"word": "Feasibility", "phonetic": "/ˌfiːzəˈbɪləti/", "pos": "n.", "meaning": "可行性", "level": "blue", "phrases": ["feasibility study", "technical feasibility"], "synonyms": ["viability", "practicability"], "antonyms": ["impossibility"], "example": "The committee is conducting a feasibility study to determine if the new project is worth the investment."},
        {"word": "Fluctuate", "phonetic": "/ˈflʌktʃueɪt/", "pos": "v.", "meaning": "波動, 起伏", "level": "blue", "phrases": ["fluctuate wildly", "market fluctuations"], "synonyms": ["vary", "waver"], "antonyms": ["stabilize", "remain constant"], "example": "The price of raw materials continues to fluctuate due to the unstable political situation."}
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
