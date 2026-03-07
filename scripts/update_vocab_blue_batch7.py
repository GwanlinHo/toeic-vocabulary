import json
import os

def update_vocab():
    # 第七批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Memorandum", "phonetic": "/ˌmeməˈrændəm/", "pos": "n.", "meaning": "備忘錄, (法律)協議備忘錄", "level": "blue", "phrases": ["internal memorandum", "sign a memorandum"], "synonyms": ["memo", "note"], "antonyms": [], "example": "The CEO sent a memorandum to all department heads outlining the new cost-cutting measures."},
        {"word": "Negotiable", "phonetic": "/nɪˈɡoʊʃiəbl/", "pos": "adj.", "meaning": "可協商的", "level": "blue", "phrases": ["non-negotiable terms", "negotiable price"], "synonyms": ["debatable", "flexible"], "antonyms": ["fixed", "rigid"], "example": "The salary for the senior position is negotiable based on the candidate's experience and qualifications."},
        {"word": "Nominate", "phonetic": "/ˈnɑːmɪneɪt/", "pos": "v.", "meaning": "提名, 任命", "level": "blue", "phrases": ["nominate a candidate", "be nominated for"], "synonyms": ["appoint", "propose"], "antonyms": [], "example": "The board of directors plans to nominate several new members at the upcoming annual general meeting."},
        {"word": "Notification", "phonetic": "/ˌnoʊtɪfɪˈkeɪʃn/", "pos": "n.", "meaning": "通知, 告示", "level": "blue", "phrases": ["official notification", "receive notification"], "synonyms": ["announcement", "notice"], "antonyms": [], "example": "We will send you a formal notification as soon as a final decision has been made regarding your application."},
        {"word": "Obligation", "phonetic": "/ˌɑːblɪˈɡeɪʃn/", "pos": "n.", "meaning": "義務, 責任, 債務", "level": "blue", "phrases": ["legal obligation", "under no obligation"], "synonyms": ["duty", "responsibility"], "antonyms": [], "example": "The company has a legal obligation to provide a safe working environment for all its employees."},
        {"word": "Obstacle", "phonetic": "/ˈɑːbstəkl/", "pos": "n.", "meaning": "障礙, 阻礙", "level": "blue", "phrases": ["overcome obstacles", "major obstacle"], "synonyms": ["barrier", "hurdle"], "antonyms": ["aid", "assistance"], "example": "Lack of adequate funding remains the major obstacle to the completion of the infrastructure project."},
        {"word": "Occupation", "phonetic": "/ˌɑːkjuˈpeɪʃn/", "pos": "n.", "meaning": "職業, 佔用", "level": "blue", "phrases": ["current occupation", "occupational hazard"], "synonyms": ["profession", "job"], "antonyms": [], "example": "Please state your name, address, and current occupation on the registration form."},
        {"word": "Off-shore", "phonetic": "/ˌɔːfˈʃɔːr/", "pos": "adj.", "meaning": "海外的, 離岸的", "level": "blue", "phrases": ["off-shore banking", "off-shore accounts"], "synonyms": ["overseas", "foreign"], "antonyms": ["inland", "domestic"], "example": "The company decided to move its manufacturing operations to an off-shore location to reduce costs."},
        {"word": "Ongoing", "phonetic": "/ˈɑːnɡoʊɪŋ/", "pos": "adj.", "meaning": "進行中的, 持續的", "level": "blue", "phrases": ["ongoing project", "ongoing investigation"], "synonyms": ["continuous", "underway"], "antonyms": ["finished", "completed"], "example": "The IT department is providing ongoing support to help staff members adjust to the new software system."},
        {"word": "Operational", "phonetic": "/ˌɑːpəˈreɪʃənl/", "pos": "adj.", "meaning": "營運的, 可使用的", "level": "blue", "phrases": ["fully operational", "operational costs"], "synonyms": ["functional", "working"], "antonyms": ["defunct", "broken"], "example": "The new distribution center is expected to be fully operational by the beginning of next month."},
        {"word": "Orientation", "phonetic": "/ˌɔːriənˈteɪʃn/", "pos": "n.", "meaning": "新進員工培訓, 方向, 定位", "level": "blue", "phrases": ["employee orientation", "sexual orientation"], "synonyms": ["introduction", "familiarization"], "antonyms": [], "example": "All new hires are required to attend a one-day orientation session to learn about company policies."},
        {"word": "Outcome", "phonetic": "/ˈaʊtkʌm/", "pos": "n.", "meaning": "結果, 後果", "level": "blue", "phrases": ["successful outcome", "unpredictable outcome"], "synonyms": ["result", "consequence"], "antonyms": [], "example": "The final outcome of the negotiation will depend on both parties' willingness to compromise."},
        {"word": "Outsource", "phonetic": "/ˈaʊtsɔːrs/", "pos": "v.", "meaning": "外包", "level": "blue", "phrases": ["outsource production", "outsource IT services"], "synonyms": [], "antonyms": ["insource"], "example": "The company decided to outsource its customer support operations to a specialized firm in India."},
        {"word": "Outstanding", "phonetic": "/aʊtˈstændɪŋ/", "pos": "adj.", "meaning": "傑出的, 未償付的", "level": "blue", "phrases": ["outstanding performance", "outstanding balance"], "synonyms": ["exceptional", "unpaid"], "antonyms": ["ordinary", "paid"], "example": "The bank sent a reminder to the customer regarding her outstanding credit card balance."},
        {"word": "Overlap", "phonetic": "/ˌoʊvərˈlæp/", "pos": "v./n.", "meaning": "重疊, 部分一致", "level": "blue", "phrases": ["significant overlap", "schedule overlap"], "synonyms": ["coincide"], "antonyms": [], "example": "There is a significant overlap in the responsibilities of the marketing and sales departments."},
        {"word": "Oversight", "phonetic": "/ˈoʊvərsaɪt/", "pos": "n.", "meaning": "監督, 疏忽", "level": "blue", "phrases": ["supervisory oversight", "due to an oversight"], "synonyms": ["supervision", "omission"], "antonyms": [], "example": "The committee is responsible for providing oversight of the project's financial management."},
        {"word": "Paramount", "phonetic": "/ˈpærəmaʊnt/", "pos": "adj.", "meaning": "至高無上的, 最重要的", "level": "blue", "phrases": ["of paramount importance", "paramount concern"], "synonyms": ["supreme", "primary"], "antonyms": ["insignificant", "minor"], "example": "Ensuring the safety of our passengers is of paramount importance to the airline."},
        {"word": "Participate", "phonetic": "/pɑːrˈtɪsɪpeɪt/", "pos": "v.", "meaning": "參加, 參與", "level": "blue", "phrases": ["participate in a meeting", "active participation"], "synonyms": ["engage", "take part"], "antonyms": ["withdraw", "abstain"], "example": "Employees are encouraged to participate in the company's annual volunteer program."},
        {"word": "Partnership", "phonetic": "/ˈpɑːrtnərʃɪp/", "pos": "n.", "meaning": "合夥關係, 夥伴關係", "level": "blue", "phrases": ["strategic partnership", "form a partnership"], "synonyms": ["alliance", "collaboration"], "antonyms": [], "example": "The two tech companies entered into a strategic partnership to develop new software solutions."},
        {"word": "Patent", "phonetic": "/ˈpætnt/", "pos": "n./v./adj.", "meaning": "專利, 獲取專利, 顯而易見的", "level": "blue", "phrases": ["apply for a patent", "patent infringement"], "synonyms": ["copyright", "license"], "antonyms": [], "example": "The pharmaceutical company was granted a 20-year patent for its new life-saving drug."}
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
