import json

# 金色等級補漏第 6 部分
gap_fill_gold_6 = {
    "aim": {"phonetic": "/eɪm/", "pos": "n./v.", "meaning": "目標；針對；目的", "phrases": ["aim at", "primary aim"], "synonyms": ["goal", "objective", "target"], "antonyms": [], "example": "Our primary aim is to increase our market share in the next two years."},
    "controversial": {"phonetic": "/ˌkɑːntrəˈvɜːrʃl/", "pos": "adj.", "meaning": "有爭議的", "phrases": ["controversial issue"], "synonyms": ["disputed", "contentious"], "antonyms": ["undisputed", "uncontroversial"], "example": "The government's decision to increase taxes proved to be highly controversial."},
    "presentation": {"phonetic": "/ˌpriːzenˈteɪʃn/", "pos": "n.", "meaning": "簡報；報告；陳述", "phrases": ["give a presentation"], "synonyms": ["demonstration", "report"], "antonyms": [], "example": "The marketing team gave an impressive presentation on the new product launch."},
    "mystery": {"phonetic": "/ˈmɪstəri/", "pos": "n.", "meaning": "神秘；謎", "phrases": ["solve a mystery"], "synonyms": ["secret", "puzzle"], "antonyms": ["clarity"], "example": "The cause of the fire in the warehouse remains a mystery to the investigators."},
    "mysterious": {"phonetic": "/mɪˈstɪriəs/", "pos": "adj.", "meaning": "神秘的", "phrases": ["mysterious circumstances"], "synonyms": ["enigmatic", "strange"], "antonyms": ["obvious", "clear"], "example": "The CEO's sudden disappearance under mysterious circumstances shocked the entire company."},
    "be little/nothing short of": {"phonetic": "/bi ˈlɪtl ʃɔːrt əv/", "pos": "phr.", "meaning": "簡直是；無異於", "phrases": [], "synonyms": ["be equivalent to"], "antonyms": [], "example": "The company's recovery from bankruptcy was little short of a miracle."},
    "amateur": {"phonetic": "/ˈæmətər/", "pos": "n./adj.", "meaning": "業餘者；業餘的", "phrases": ["amateur photographer"], "synonyms": ["non-professional"], "antonyms": ["professional"], "example": "The competition is open to both professional and amateur artists."},
    "tension": {"phonetic": "/ˈtenʃn/", "pos": "n.", "meaning": "張力；緊張局勢", "phrases": ["reduce tension", "high tension"], "synonyms": ["stress", "strain", "pressure"], "antonyms": ["relaxation"], "example": "There has been increasing tension between the management and the union leaders."},
    "path": {"phonetic": "/pæθ/", "pos": "n.", "meaning": "小徑；路線；途徑", "phrases": ["career path"], "synonyms": ["trail", "route", "way"], "antonyms": [], "example": "The company is exploring different paths to achieve sustainable growth."},
    "shoot": {"phonetic": "/ʃuːt/", "pos": "v./n.", "meaning": "拍攝；射擊；發芽", "phrases": ["photo shoot", "shoot a video"], "synonyms": ["film", "fire"], "antonyms": [], "example": "The marketing team spent the whole day shooting a new commercial for the product."},
    "a mixed reaction": {"phonetic": "/ə mɪkst riˈækʃn/", "pos": "n. phr.", "meaning": "反應不一；毀譽參半", "phrases": [], "synonyms": [], "antonyms": [], "example": "The new office design received a mixed reaction from the employees."},
    "column": {"phonetic": "/ˈkɑːləm/", "pos": "n.", "meaning": "專欄；圓柱；縱列", "phrases": ["newspaper column"], "synonyms": ["pillar", "post"], "antonyms": [], "example": "He writes a weekly column on business trends for a national newspaper."},
    "thoughtful": {"phonetic": "/ˈθɔːtf l/", "pos": "adj.", "meaning": "深思熟慮的；體貼的", "phrases": ["thoughtful gesture"], "synonyms": ["considerate", "pensive"], "antonyms": ["thoughtless", "careless"], "example": "The manager's thoughtful approach to the problem was appreciated by the whole team."},
    "take up": {"phonetic": "/teɪk ʌp/", "pos": "v. phr.", "meaning": "開始從事；佔用(時間/空間)", "phrases": ["take up a hobby"], "synonyms": ["start", "occupy"], "antonyms": ["give up"], "example": "The new filing system will take up much less space in the office."},
    "carry out": {"phonetic": "/ˈkæri aʊt/", "pos": "v. phr.", "meaning": "執行；進行", "phrases": ["carry out research", "carry out an investigation"], "synonyms": ["execute", "perform", "conduct"], "antonyms": [], "example": "The auditors will carry out a thorough review of the company's financial records."},
    "marital": {"phonetic": "/ˈmærɪtl/", "pos": "adj.", "meaning": "婚姻的", "phrases": ["marital status"], "synonyms": ["matrimonial"], "antonyms": [], "example": "The survey included questions about the participants' marital status and age."},
    "without a second thought": {"phonetic": "/wɪˈðaʊt ə ˈsekənd θɔːt/", "pos": "phr.", "meaning": "毫不猶豫地", "phrases": [], "synonyms": ["immediately"], "antonyms": [], "example": "She accepted the job offer without a second thought because it was her dream position."},
    "enchanting": {"phonetic": "/ɪnˈtʃæntɪŋ/", "pos": "adj.", "meaning": "迷人的；迷人的", "phrases": ["enchanting view"], "synonyms": ["charming", "captivating"], "antonyms": ["repulsive"], "example": "The island is known for its enchanting beaches and warm tropical climate."},
    "gear": {"phonetic": "/ɡɪr/", "pos": "n./v.", "meaning": "裝備；齒輪；調整", "phrases": ["camping gear", "gear up for"], "synonyms": ["equipment", "machinery"], "antonyms": [], "example": "The company is gearing up for the launch of its new international marketing campaign."},
    "strip": {"phonetic": "/strɪp/", "pos": "v./n.", "meaning": "剝奪；脫掉；長條", "phrases": ["strip of land", "strip away"], "synonyms": ["remove", "peel", "band"], "antonyms": [], "example": "The workers had to strip the old wallpaper before painting the office walls."},
    "enclosed": {"phonetic": "/ɪnˈkloʊzd/", "pos": "adj./v. (past)", "meaning": "隨函附上的；圍住的", "phrases": ["enclosed space"], "synonyms": ["attached", "surrounded"], "antonyms": [], "example": "Please find the signed contract enclosed with this letter."},
    "faulty": {"phonetic": "/ˈfɔːlti/", "pos": "adj.", "meaning": "有缺陷的；故障的", "phrases": ["faulty equipment"], "synonyms": ["defective", "broken"], "antonyms": ["perfect", "functional"], "example": "The customer returned the product because it was found to be faulty."},
    "detergent": {"phonetic": "/dɪˈtɜːrdʒənt/", "pos": "n.", "meaning": "清潔劑；洗滌劑", "phrases": ["laundry detergent"], "synonyms": ["cleaner"], "antonyms": [], "example": "You should use a mild detergent to clean the delicate fabric of the curtains."},
    "malfunction": {"phonetic": "/ˌmælˈfʌŋkʃn/", "pos": "n./v.", "meaning": "故障；功能障礙", "phrases": ["equipment malfunction"], "synonyms": ["failure", "breakdown"], "antonyms": ["function"], "example": "The flight was delayed due to a minor technical malfunction in the engine."},
    "optimistic": {"phonetic": "/ˌɑːptɪˈmɪstɪk/", "pos": "adj.", "meaning": "樂觀的", "phrases": ["optimistic outlook"], "synonyms": ["hopeful", "positive"], "antonyms": ["pessimistic"], "example": "The CEO remains optimistic about the company's future growth in Asia."},
    "pessimistic": {"phonetic": "/ˌpesɪˈmɪstɪk/", "pos": "adj.", "meaning": "悲觀的", "phrases": ["pessimistic view"], "synonyms": ["gloomy", "negative"], "antonyms": ["optimistic"], "example": "Despite the current challenges, we should avoid taking a pessimistic view of the market."},
    "from scratch": {"phonetic": "/frəm skrætʃ/", "pos": "phr.", "meaning": "從零開始；白手起家", "phrases": ["start from scratch"], "synonyms": ["from the beginning"], "antonyms": [], "example": "He decided to start his own technology consulting business from scratch."},
    "draft": {"phonetic": "/dræft/", "pos": "n./v.", "meaning": "草案；匯票；徵兵；起草", "phrases": ["rough draft", "bank draft"], "synonyms": ["outline", "sketch"], "antonyms": ["final copy"], "example": "The legal department is working on the first draft of the partnership agreement."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in gap_fill_gold_6:
        update_info = gap_fill_gold_6[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("完成金色等級補漏第 6 部分 (Aim 到 Draft)。")
