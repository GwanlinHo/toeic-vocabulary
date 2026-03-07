import json

# 金色等級補漏第 5 部分
gap_fill_gold_5 = {
    "correspondence": {"phonetic": "/ˌkɔːrəˈspɑːndəns/", "pos": "n.", "meaning": "通信；信件", "phrases": ["business correspondence"], "synonyms": ["letters", "communication"], "antonyms": [], "example": "The company keeps a copy of all its professional correspondence for five years."},
    "make an appointment with sb for sth": {"word": "make an appointment", "phonetic": "/meɪk ən əˈpɔɪntmənt/", "pos": "v. phr.", "meaning": "預約", "phrases": [], "synonyms": ["book a meeting"], "antonyms": [], "example": "I need to make an appointment with the manager to discuss the new contract."},
    "intact": {"phonetic": "/ɪnˈtækt/", "pos": "adj.", "meaning": "完整無缺的；未受損的", "phrases": ["remain intact"], "synonyms": ["unbroken", "undamaged"], "antonyms": ["damaged", "broken"], "example": "Fortunately, all the equipment in the warehouse remained intact after the storm."},
    "soiled": {"phonetic": "/sɔɪld/", "pos": "adj.", "meaning": "弄髒的；汙損的", "phrases": ["soiled clothing"], "synonyms": ["dirty", "stained"], "antonyms": ["clean", "spotless"], "example": "The hotel was criticized for providing soiled towels to its guests."},
    "official": {"phonetic": "/əˈfɪʃl/", "pos": "adj./n.", "meaning": "正式的；官方的；官員", "phrases": ["government official", "official announcement"], "synonyms": ["formal", "authorized"], "antonyms": ["unofficial"], "example": "The company will make an official announcement regarding the merger tomorrow morning."},
    "unwind": {"phonetic": "/ˌʌnˈwaɪnd/", "pos": "v.", "meaning": "放鬆；展開", "phrases": ["unwind after work"], "synonyms": ["relax", "loosen"], "antonyms": ["wind", "tense"], "example": "She likes to listen to classical music to unwind after a long and stressful day at the office."},
    "get away from": {"phonetic": "/ɡet əˈweɪ frəm/", "pos": "v. phr.", "meaning": "逃離；遠離", "phrases": ["get away from it all"], "synonyms": ["escape", "leave"], "antonyms": [], "example": "He decided to take a short vacation to get away from the noise and stress of the city."},
    "It pays to V": {"phonetic": "/ɪt peɪz tuː/", "pos": "phr.", "meaning": "做某事是值得的；有好處的", "phrases": [], "synonyms": ["it is worthwhile to"], "antonyms": [], "example": "It pays to do thorough market research before launching a new product."},
    "code": {"phonetic": "/koʊd/", "pos": "n./v.", "meaning": "編碼；法規；行為準則", "phrases": ["postal code", "building code", "dress code"], "synonyms": ["rule", "cipher"], "antonyms": [], "example": "The company has a strict dress code that all employees are expected to follow."},
    "decode": {"phonetic": "/ˌdiːˈkoʊd/", "pos": "v.", "meaning": "解碼；譯解", "phrases": [], "synonyms": ["decipher", "interpret"], "antonyms": ["encode"], "example": "The software is designed to quickly decode encrypted data files."},
    "remedy": {"phonetic": "/ˈremədi/", "pos": "n./v.", "meaning": "補救方法；藥品；糾正", "phrases": ["legal remedy"], "synonyms": ["solution", "cure", "fix"], "antonyms": [], "example": "The management is working hard to find a remedy for the recurring technical issues."},
    "grill": {"phonetic": "/ɡrɪl/", "pos": "n./v.", "meaning": "烤架；烤；拷問", "phrases": ["grill someone about something"], "synonyms": ["barbecue", "question"], "antonyms": [], "example": "We decided to grill some steaks on the balcony for our end-of-year office party."},
    "grease": {"phonetic": "/ɡriːs/", "pos": "n./v.", "meaning": "油脂；潤滑脂；塗油", "phrases": ["grease the wheels"], "synonyms": ["oil", "fat"], "antonyms": [], "example": "The technician used a specialized grease to lubricate the gears of the machine."},
    "greasy": {"phonetic": "/ˈɡriːsi/", "pos": "adj.", "meaning": "油膩的", "phrases": ["greasy food"], "synonyms": ["oily"], "antonyms": ["dry"], "example": "You should avoid eating too much greasy food if you want to stay healthy."},
    "revoke": {"phonetic": "/rɪˈvoʊk/", "pos": "v.", "meaning": "撤銷；廢除", "phrases": ["revoke a license"], "synonyms": ["cancel", "annul", "rescind"], "antonyms": ["grant", "issue"], "example": "The government decided to revoke the company's business license following the scandal."},
    "untensil": {"word": "utensil", "phonetic": "/juːˈtensl/", "pos": "n.", "meaning": "器具；用具", "phrases": ["kitchen utensils"], "synonyms": ["tool", "implement"], "antonyms": [], "example": "The store sells a wide variety of high-quality stainless steel kitchen utensils."},
    "A tourist attraction": {"phonetic": "/ə ˈtʊrɪst əˈtrækʃn/", "pos": "n. phr.", "meaning": "觀光景點", "phrases": ["popular tourist attraction"], "synonyms": [], "antonyms": [], "example": "The ancient ruins are the most popular tourist attraction in the region."},
    "inn": {"phonetic": "/ɪn/", "pos": "n.", "meaning": "小旅館；客棧", "phrases": ["country inn"], "synonyms": ["hotel", "lodge"], "antonyms": [], "example": "They decided to stay at a traditional country inn during their weekend excursion."},
    "gala": {"phonetic": "/ˈɡeɪlə/", "pos": "n.", "meaning": "盛會；慶祝活動", "phrases": ["charity gala", "gala dinner"], "synonyms": ["celebration", "festival"], "antonyms": [], "example": "The company held a magnificent gala dinner to celebrate its twentieth anniversary."},
    "sophisticated": {"phonetic": "/səˈfɪstɪkeɪtɪd/", "pos": "adj.", "meaning": "世故的；精密的；先進的", "phrases": ["sophisticated software"], "synonyms": ["advanced", "complex", "refined"], "antonyms": ["simple", "naive"], "example": "The new security system is highly sophisticated and uses facial recognition technology."},
    "keep~in mind": {"word": "keep in mind", "phonetic": "/kiːp ɪn maɪnd/", "pos": "v. phr.", "meaning": "記住；考量", "phrases": [], "synonyms": ["remember", "bear in mind"], "antonyms": ["forget"], "example": "Please keep in mind that the deadline for the project is Friday afternoon."},
    "pop": {"phonetic": "/pɑːp/", "pos": "v./n./adj.", "meaning": "發出砰的一聲；流行的；突然出現", "phrases": ["pop up", "pop music"], "synonyms": ["burst", "popular"], "antonyms": [], "example": "A message will pop up on your screen once the software update is finished."},
    "crunch": {"phonetic": "/krʌntʃ/", "pos": "v./n.", "meaning": "嘎吱地咬；計算(大量數據)；緊縮", "phrases": ["crunch numbers", "credit crunch"], "synonyms": ["grind", "crisis"], "antonyms": [], "example": "The accountants spent the whole day crunching numbers for the annual financial report."},
    "sound": {"phonetic": "/saʊnd/", "pos": "n./v./adj.", "meaning": "聲音；聽起來；健全的；可靠的", "phrases": ["sound advice", "financially sound"], "synonyms": ["noise", "stable", "solid"], "antonyms": ["unstable"], "example": "The company is financially sound and has a very positive outlook for the future."},
    "faculty": {"phonetic": "/ˈfæklti/", "pos": "n.", "meaning": "全體教職員；官能；能力", "phrases": ["university faculty"], "synonyms": ["staff", "ability"], "antonyms": [], "example": "The university is known for its world-class faculty in the field of economics."},
    "abundant": {"phonetic": "/əˈbʌndənt/", "pos": "adj.", "meaning": "豐富的；充沛的", "phrases": ["abundant resources"], "synonyms": ["plentiful", "ample"], "antonyms": ["scarce", "meager"], "example": "The region is rich in mineral resources and has an abundant supply of water."},
    "unheeded": {"phonetic": "/ˌʌnˈhiːdɪd/", "pos": "adj.", "meaning": "未受注意的；被忽視的", "phrases": ["go unheeded"], "synonyms": ["ignored", "disregarded"], "antonyms": ["heeded", "noticed"], "example": "The manager's warnings about the potential risks went unheeded by the board."},
    "reviewer": {"phonetic": "/rɪˈvjuːər/", "pos": "n.", "meaning": "評論者；審查員", "phrases": ["book reviewer", "peer reviewer"], "synonyms": ["critic"], "antonyms": [], "example": "The new restaurant received a positive review from a famous local food reviewer."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in gap_fill_gold_5:
        update_info = gap_fill_gold_5[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("完成金色等級補漏第 5 部分 (Correspondence 到 Reviewer)。")
