import json

# 第 801-850 個高品質單字對應表 (金色等級)
enriched_data_gold_17 = {
    "diplomat": {"phonetic": "/ˈdɪpləmæt/", "pos": "n.", "meaning": "外交官", "phrases": ["career diplomat"], "synonyms": ["envoy", "ambassador"], "antonyms": [], "example": "The diplomat worked hard to negotiate a peace agreement between the two countries."},
    "be present at": {"phonetic": "/bi ˈpreznt æt/", "pos": "v. phr.", "meaning": "出席；在場", "phrases": [], "synonyms": ["attend"], "antonyms": ["be absent from"], "example": "All department heads are required to be present at the annual general meeting."},
    "unwavering": {"phonetic": "/ʌnˈweɪvərɪŋ/", "pos": "adj.", "meaning": "堅定的；不動搖的", "phrases": ["unwavering support"], "synonyms": ["steadfast", "firm"], "antonyms": ["fickle", "unsteady"], "example": "We are grateful for your unwavering dedication to the company during this difficult period."},
    "contingent": {"phonetic": "/kənˈtɪndʒənt/", "pos": "adj./n.", "meaning": "視情況而定的；代表團", "phrases": ["contingent on"], "synonyms": ["dependent", "conditional", "delegation"], "antonyms": [], "example": "The approval of the loan is contingent on the company providing more financial data."},
    "progressive": {"phonetic": "/prəˈɡresɪv/", "pos": "adj.", "meaning": "進步的；革新的；逐漸的", "phrases": ["progressive policy"], "synonyms": ["innovative", "gradual"], "antonyms": ["conservative", "regressive"], "example": "The company has introduced a progressive policy regarding flexible working hours."},
    "chronological": {"phonetic": "/ˌkrɑːnəˈlɑːdʒɪkl/", "pos": "adj.", "meaning": "按時間順序的", "phrases": ["chronological order"], "synonyms": ["sequential"], "antonyms": [], "example": "Please arrange the documents in chronological order, starting with the oldest one."},
    "uneven": {"phonetic": "/ʌnˈiːvn/", "pos": "adj.", "meaning": "不平坦的；不均勻的；不平等的", "phrases": ["uneven surface"], "synonyms": ["irregular", "rough"], "antonyms": ["even", "smooth"], "example": "The economic recovery has been uneven, with some industries growing faster than others."},
    "corporate head": {"phonetic": "/ˈkɔːrpərət hed/", "pos": "n. phr.", "meaning": "企業首腦；負責人", "phrases": [], "synonyms": ["CEO", "chief executive"], "antonyms": [], "example": "The corporate head will give a keynote speech at the international technology conference."},
    "vice president": {"phonetic": "/vaɪs ˈprezɪdənt/", "pos": "n. phr.", "meaning": "副總裁；副總統", "phrases": ["executive vice president"], "synonyms": ["VP"], "antonyms": [], "example": "She was recently promoted to vice president of marketing for the North American region."},
    "convention": {"phonetic": "/kənˈvenʃn/", "pos": "n.", "meaning": "大會；慣例；習俗", "phrases": ["annual convention", "social convention"], "synonyms": ["conference", "custom"], "antonyms": [], "example": "The annual medical convention will be held in the city center next month."},
    "press pass": {"phonetic": "/pres pæs/", "pos": "n. phr.", "meaning": "記者證", "phrases": [], "synonyms": ["media credentials"], "antonyms": [], "example": "You need to show your press pass to gain access to the restricted area of the conference."},
    "wireless": {"phonetic": "/ˈwaɪərləs/", "pos": "adj./n.", "meaning": "無線的；無線電", "phrases": ["wireless network", "wireless charging"], "synonyms": ["cordless"], "antonyms": ["wired"], "example": "The hotel offers free high-speed wireless internet access in all guest rooms."},
    "animation": {"phonetic": "/ˌænɪˈmeɪʃn/", "pos": "n.", "meaning": "動畫；生氣；活力", "phrases": ["computer animation"], "synonyms": ["cartoon", "liveliness"], "antonyms": [], "example": "The new marketing video features high-quality 3D animation to showcase the product."},
    "reference number": {"phonetic": "/ˈrefrəns ˈnʌmbər/", "pos": "n. phr.", "meaning": "參考編號；案號", "phrases": [], "synonyms": ["tracking number"], "antonyms": [], "example": "Please quote your reference number whenever you contact customer service regarding your order."},
    "protocol": {"phonetic": "/ˈproʊtəkɑːl/", "pos": "n.", "meaning": "協議；禮儀；規程", "phrases": ["safety protocol", "diplomatic protocol"], "synonyms": ["code", "procedure"], "antonyms": [], "example": "All staff members must follow the strict security protocol when entering the laboratory."},
    "commitment": {"phonetic": "/kəˈmɪtmənt/", "pos": "n.", "meaning": "承諾；奉獻", "phrases": ["make a commitment", "long-term commitment"], "synonyms": ["promise", "dedication"], "antonyms": [], "example": "The company is well-known for its commitment to environmental sustainability."},
    "downstairs": {"phonetic": "/ˌdaʊnˈsterz/", "pos": "adv./adj./n.", "meaning": "在樓下；往樓下", "phrases": ["go downstairs"], "synonyms": [], "antonyms": ["upstairs"], "example": "The cafeteria is located downstairs on the first floor of the building."},
    "floor plan": {"phonetic": "/flɔːr plæn/", "pos": "n. phr.", "meaning": "樓層平面圖", "phrases": ["open floor plan"], "synonyms": ["blueprint", "layout"], "antonyms": [], "example": "The real estate agent showed us the floor plan of the new office space."},
    "overturned": {"phonetic": "/ˌoʊvərˈtɜːrnd/", "pos": "adj./v. (past)", "meaning": "翻轉的；傾覆的；推翻(判決)", "phrases": [], "synonyms": ["upset", "reversed"], "antonyms": [], "example": "The court overturned the previous decision after new evidence was presented."},
    "turn over": {"phonetic": "/tɜːrn ˈoʊvər/", "pos": "v. phr.", "meaning": "翻過來；移交；營業額達...", "phrases": ["turn over a new leaf"], "synonyms": ["flip", "hand over"], "antonyms": [], "example": "The manager decided to turn over the responsibility for the project to his assistant."},
    "understaffed": {"phonetic": "/ˌʌndərˈstæft/", "pos": "adj.", "meaning": "人手不足的", "phrases": [], "synonyms": ["shorthanded"], "antonyms": ["overstaffed"], "example": "The customer service department is currently understaffed due to the recent flu outbreak."},
    "shorthanded": {"phonetic": "/ˌʃɔːrtˈhændɪd/", "pos": "adj.", "meaning": "人手短缺的", "phrases": [], "synonyms": ["understaffed"], "antonyms": [], "example": "We are a bit shorthanded today, so please be patient with our response time."},
    "autographed": {"phonetic": "/ˈɔːtəɡræft/", "pos": "adj./v. (past)", "meaning": "親筆簽名的", "phrases": ["autographed copy"], "synonyms": ["signed"], "antonyms": [], "example": "The winner of the competition received an autographed copy of the author's new book."},
    "parcel": {"phonetic": "/ˈpɑːrsl/", "pos": "n./v.", "meaning": "包裹；打包", "phrases": ["post a parcel"], "synonyms": ["package", "bundle"], "antonyms": [], "example": "The courier delivered a large parcel containing the office supplies this morning."},
    "tidy up": {"phonetic": "/ˈtaɪdi ʌp/", "pos": "v. phr.", "meaning": "收拾；整理", "phrases": [], "synonyms": ["clean up", "straighten up"], "antonyms": ["mess up"], "example": "Please tidy up your desk before you leave the office for the weekend."},
    "if that is the case": {"phonetic": "/ɪf ðæt ɪz ðə keɪs/", "pos": "phr.", "meaning": "如果是那樣的話", "phrases": [], "synonyms": ["in that case"], "antonyms": [], "example": "If that is the case, we will need to reconsider our marketing strategy."},
    "pamphlet": {"phonetic": "/ˈpæmflət/", "pos": "n.", "meaning": "小冊子", "phrases": ["informative pamphlet"], "synonyms": ["brochure", "leaflet"], "antonyms": [], "example": "The travel agency gave us a colorful pamphlet about the different tour packages available."},
    "bookcase": {"phonetic": "/ˈbʊkkeɪs/", "pos": "n.", "meaning": "書櫃；書架", "phrases": ["wooden bookcase"], "synonyms": ["bookshelf"], "antonyms": [], "example": "He decided to buy a new bookcase to store his collection of business textbooks."},
    "power outage": {"phonetic": "/ˈpaʊər ˈaʊtɪdʒ/", "pos": "n. phr.", "meaning": "停電", "phrases": ["experience a power outage"], "synonyms": ["blackout", "power failure"], "antonyms": [], "example": "The severe storm caused a major power outage that lasted for several hours."},
    "embassy": {"phonetic": "/ˈembəsi/", "pos": "n.", "meaning": "大使館", "phrases": ["foreign embassy"], "synonyms": [], "antonyms": [], "example": "You need to visit the embassy to apply for a visa before you travel to that country."},
    "remodel": {"phonetic": "/ˌriːˈmɑːdl/", "pos": "v.", "meaning": "改建；改造；翻新", "phrases": ["remodel a kitchen"], "synonyms": ["renovate", "refurbish"], "antonyms": [], "example": "The company is planning to remodel its main lobby to make it more modern and welcoming."},
    "go into effect": {"phonetic": "/ɡoʊ ˈɪntuː ɪˈfekt/", "pos": "v. phr.", "meaning": "生效；實施", "phrases": [], "synonyms": ["take effect", "come into force"], "antonyms": [], "example": "The new safety regulations will go into effect on the first of next month."},
    "push back": {"phonetic": "/pʊʃ bæk/", "pos": "v. phr.", "meaning": "推遲；延後；反擊", "phrases": ["push back a meeting"], "synonyms": ["postpone", "delay"], "antonyms": ["advance", "bring forward"], "example": "The deadline for the project has been pushed back by two weeks."},
    "adjacent to": {"phonetic": "/əˈdʒeɪsnt tuː/", "pos": "adj. phr.", "meaning": "鄰近...；在...隔壁", "phrases": [], "synonyms": ["next to", "beside"], "antonyms": ["far from"], "example": "The parking lot is located adjacent to the main office building."},
    "appreciation's ceremony": {"phonetic": "/əˌpriːʃiˈeɪʃnz ˈserəmoʊni/", "pos": "n. phr.", "meaning": "表揚大會；感謝祭", "phrases": [], "synonyms": ["awards ceremony"], "antonyms": [], "example": "The company held an appreciation's ceremony to honor its long-serving employees."},
    "referral": {"phonetic": "/rɪˈfɜːrəl/", "pos": "n.", "meaning": "推薦；轉介", "phrases": ["employee referral"], "synonyms": ["recommendation"], "antonyms": [], "example": "Many of our new clients come to us through referrals from existing customers."},
    "plumbing": {"phonetic": "/ˈplʌmɪŋ/", "pos": "n.", "meaning": "配管工程；水管系統", "phrases": ["plumbing problems"], "synonyms": [], "antonyms": [], "example": "We had to call a professional to fix the plumbing issues in the office kitchen."},
    "plumb": {"phonetic": "/plʌm/", "pos": "v./n./adj./adv.", "meaning": "測量深度；垂直的；完全地", "phrases": ["plumb the depths"], "synonyms": ["measure", "vertical"], "antonyms": [], "example": "The researchers are trying to plumb the mysteries of the deep ocean."},
    "in the pipe line": {"phonetic": "/ɪn ðə ˈpaɪplaɪn/", "pos": "phr.", "meaning": "在籌劃中；在開發中", "phrases": [], "synonyms": ["in preparation"], "antonyms": [], "example": "The company has several innovative new products in the pipe line for next year."},
    "waive": {"phonetic": "/weɪv/", "pos": "v.", "meaning": "放棄(權利/要求)；免除(費用)", "phrases": ["waive a fee"], "synonyms": ["relinquish", "forgo"], "antonyms": ["claim", "enforce"], "example": "The bank agreed to waive the late fee after the customer explained the situation."},
    "bank": {"phonetic": "/bæŋk/", "pos": "n./v.", "meaning": "銀行；河岸；堆積", "phrases": ["commercial bank", "river bank"], "synonyms": [], "antonyms": [], "example": "I need to go to the bank to deposit some checks this afternoon."},
    "voucher": {"phonetic": "/ˈvaʊtʃər/", "pos": "n.", "meaning": "憑證；代金券", "phrases": ["gift voucher", "travel voucher"], "synonyms": ["coupon", "token"], "antonyms": [], "example": "The hotel gave us a complimentary breakfast voucher during our stay."},
    "courtesy": {"phonetic": "/ˈkɜːrtəsi/", "pos": "n./adj.", "meaning": "禮貌；厚意；免費提供的", "phrases": ["courtesy bus", "common courtesy"], "synonyms": ["politeness", "generosity"], "antonyms": ["rudeness"], "example": "The hotel provides a courtesy shuttle bus to and from the international airport."},
    "paid vacation": {"phonetic": "/peɪd veɪˈkeɪʃn/", "pos": "n. phr.", "meaning": "有薪假", "phrases": ["annual paid vacation"], "synonyms": ["paid leave"], "antonyms": ["unpaid leave"], "example": "Full-time employees are entitled to twenty days of paid vacation every year."},
    "commence": {"phonetic": "/kəˈmens/", "pos": "v.", "meaning": "開始", "phrases": ["commence operations"], "synonyms": ["start", "begin"], "antonyms": ["finish", "complete", "cease"], "example": "The construction work is expected to commence early next month."},
    "council": {"phonetic": "/ˈkaʊnsl/", "pos": "n.", "meaning": "會議；理事會；地方議會", "phrases": ["city council", "student council"], "synonyms": ["committee", "board"], "antonyms": [], "example": "The local council has approved the plans for the new community center."},
    "bullish": {"phonetic": "/ˈbʊlɪʃ/", "pos": "adj.", "meaning": "看漲的；樂觀的", "phrases": ["bullish market"], "synonyms": ["optimistic", "confident"], "antonyms": ["bearish", "pessimistic"], "example": "Many investors remain bullish about the future growth of the technology sector."},
    "sophiscate": {"word": "sophisticate", "phonetic": "/səˈfɪstɪkət/ (n.) /səˈfɪstɪkeɪt/ (v.)", "pos": "n./v.", "meaning": "世故的人；弄複雜", "phrases": [], "synonyms": [], "antonyms": [], "example": "He is a real sophisticate who enjoys fine wine and classical music."},
    "sophiscation": {"word": "sophistication", "phonetic": "/səˌfɪstɪˈkeɪʃn/", "pos": "n.", "meaning": "世故；複雜；精緻", "phrases": ["technological sophistication"], "synonyms": ["complexity", "refinement"], "antonyms": ["simplicity", "naivety"], "example": "The new software system offers a high level of sophistication and flexibility."},
    "inclement": {"phonetic": "/ɪnˈklemənt/", "pos": "adj.", "meaning": "(天氣)惡劣的", "phrases": ["inclement weather"], "synonyms": ["severe", "harsh"], "antonyms": ["mild", "pleasant"], "example": "The outdoor event was canceled due to the inclement weather forecast."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_17:
        update_info = enriched_data_gold_17[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 801-850 個單字。")
