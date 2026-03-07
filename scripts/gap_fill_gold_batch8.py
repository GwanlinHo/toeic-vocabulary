import json

# 金色等級補漏第 8 部分
gap_fill_gold_8 = {
    "a public official": {"phonetic": "/ə ˈpʌblɪk əˈfɪʃl/", "pos": "n. phr.", "meaning": "公職人員；官員", "phrases": ["elected public official"], "synonyms": ["government official"], "antonyms": [], "example": "The report discussed the responsibilities of a public official in maintaining transparency."},
    "pay a visit to sb": {"phonetic": "/peɪ ə ˈvɪzɪt tuː/", "pos": "v. phr.", "meaning": "拜訪某人", "phrases": [], "synonyms": ["visit", "drop by"], "antonyms": [], "example": "Our sales representative will pay a visit to your office tomorrow afternoon."},
    "governor": {"phonetic": "/ˈɡʌvərnər/", "pos": "n.", "meaning": "州長；省長；理事", "phrases": ["state governor"], "synonyms": ["leader", "administrator"], "antonyms": [], "example": "The governor announced a new plan to improve public transportation in the state."},
    "infrastructures": {"phonetic": "/ˈɪnfrəstrʌktʃərz/", "pos": "n.", "meaning": "基礎建設(複數)", "phrases": ["critical infrastructure"], "synonyms": ["foundation", "base"], "antonyms": [], "example": "The government is investing billions of dollars in new infrastructures such as roads and bridges."},
    "pull in": {"phonetic": "/pʊl ɪn/", "pos": "v. phr.", "meaning": "進站；停靠；吸引", "phrases": ["pull in customers"], "synonyms": ["attract", "arrive"], "antonyms": ["pull out"], "example": "The train is expected to pull in to the station in about five minutes."},
    "after-hours": {"phonetic": "/ˈæftər ˈaʊərz/", "pos": "adj./adv.", "meaning": "下班時間後的", "phrases": ["after-hours party"], "synonyms": [], "antonyms": ["during business hours"], "example": "The building has a security guard on duty for any after-hours emergencies."},
    "booth": {"phonetic": "/buːθ/", "pos": "n.", "meaning": "小亭；攤位；隔間", "phrases": ["phone booth", "exhibition booth"], "synonyms": ["stall", "stand"], "antonyms": [], "example": "Our company will have a large booth at the international trade fair next month."},
    "directory": {"phonetic": "/dəˈrektəri/", "pos": "n.", "meaning": "目錄；姓名地址錄", "phrases": ["telephone directory", "company directory"], "synonyms": ["list", "index"], "antonyms": [], "example": "You can find the contact details of all our employees in the company directory."},
    "split the cost/bill with sb": {"word": "split the bill", "phonetic": "/splɪt ðə bɪl/", "pos": "v. phr.", "meaning": "與某人分攤費用", "phrases": [], "synonyms": ["go Dutch"], "antonyms": [], "example": "We decided to split the bill after the business lunch at the Italian restaurant."},
    "split up with sb": {"phonetic": "/splɪt ʌp wɪð/", "pos": "v. phr.", "meaning": "與某人分手；與某人斷絕關係", "phrases": [], "synonyms": ["break up with"], "antonyms": ["get together with"], "example": "After several years of partnership, the two companies decided to split up."},
    "boutique": {"phonetic": "/buːˈtiːk/", "pos": "n.", "meaning": "精品店；精品專賣店", "phrases": ["boutique hotel", "fashion boutique"], "synonyms": [], "antonyms": [], "example": "The hotel features several high-end boutiques selling designer clothing and accessories."},
    "unbeatable": {"phonetic": "/ʌnˈbiːtəbl/", "pos": "adj.", "meaning": "無敵的；無與倫比的", "phrases": ["unbeatable prices"], "synonyms": ["unsurpassable", "matchless"], "antonyms": ["beatable"], "example": "Our store is offering unbeatable prices on all electronics during the holiday sale."},
    "unsurpassable": {"phonetic": "/ˌʌnsərˈpæsəbl/", "pos": "adj.", "meaning": "卓越的；不可超越的", "phrases": [], "synonyms": ["unbeatable", "matchless"], "antonyms": ["mediocre"], "example": "The quality of the craftsmanship in this antique furniture is truly unsurpassable."},
    "surpass": {"phonetic": "/sərˈpæs/", "pos": "v.", "meaning": "超越；勝過", "phrases": ["surpass expectations"], "synonyms": ["exceed", "outdo"], "antonyms": ["fail", "fall short of"], "example": "The company's annual revenue is expected to surpass ten million dollars this year."},
    "indigenous": {"phonetic": "/ɪnˈdɪdʒənəs/", "pos": "adj.", "meaning": "土著的；本土的", "phrases": ["indigenous people"], "synonyms": ["native", "local"], "antonyms": ["foreign", "exotic"], "example": "The researchers are studying the traditional medical practices of the indigenous communities."},
    "hail a cab": {"phonetic": "/heɪl ə kæb/", "pos": "v. phr.", "meaning": "攔計程車", "phrases": [], "synonyms": ["call a taxi"], "antonyms": [], "example": "It was raining so hard that we had to hail a cab to get back to the hotel."},
    "slump": {"phonetic": "/slʌmp/", "pos": "n./v.", "meaning": "暴跌；蕭條；衰落", "phrases": ["economic slump"], "synonyms": ["drop", "decline", "recession"], "antonyms": ["boom", "rise"], "example": "The tourism industry has experienced a major slump due to the international travel restrictions."},
    "tough": {"phonetic": "/tʌf/", "pos": "adj.", "meaning": "堅硬的；艱難的；嚴厲的", "phrases": ["tough decision", "tough competition"], "synonyms": ["hard", "difficult", "strict"], "antonyms": ["easy", "soft", "gentle"], "example": "The manager had to make some tough decisions to reduce the company's costs."},
    "rank": {"phonetic": "/ræŋk/", "pos": "n./v./adj.", "meaning": "等級；階級；排名；繁茂的", "phrases": ["high rank", "rank first"], "synonyms": ["grade", "level", "position"], "antonyms": [], "example": "Our university is currently ranked among the top ten in the country for research."},
    "rise through the ranks": {"phonetic": "/raɪz θruː ðə ræŋks/", "pos": "v. phr.", "meaning": "在公司中晉升；步步高升", "phrases": [], "synonyms": [], "antonyms": [], "example": "She started as a clerk and rose through the ranks to become the CEO of the company."},
    "favorable": {"phonetic": "/ˈfeɪvərəbl/", "pos": "adj.", "meaning": "有利的；贊同的；順利的", "phrases": ["favorable conditions", "favorable review"], "synonyms": ["advantageous", "positive"], "antonyms": ["unfavorable", "negative"], "example": "The company's new product received very favorable reviews from several tech experts."},
    "rebound": {"phonetic": "/rɪˈbaʊnd/", "pos": "v./n.", "meaning": "彈回；(股市)回升；振作", "phrases": ["economic rebound"], "synonyms": ["recovery", "rally"], "antonyms": ["slump", "decline"], "example": "The stock market experienced a significant rebound after the positive economic report was released."},
    "go out of business": {"phonetic": "/ɡoʊ aʊt əv ˈbɪznəs/", "pos": "v. phr.", "meaning": "歇業；破產", "phrases": [], "synonyms": ["go bankrupt", "fail"], "antonyms": ["start a business"], "example": "Many small retail stores in the city center have gone out of business in recent years."},
    "senator": {"phonetic": "/ˈsenətər/", "pos": "n.", "meaning": "參議員", "phrases": ["US senator"], "synonyms": [], "antonyms": [], "example": "The senator gave a speech about the need for more investment in public education."},
    "breaking news": {"phonetic": "/ˈbreɪkɪŋ nuːz/", "pos": "n. phr.", "meaning": "即時新聞；頭條新聞", "phrases": [], "synonyms": [], "antonyms": [], "example": "We interrupt this program to bring you some breaking news about the local election results."},
    "press conference": {"phonetic": "/pres ˈkɑːnfərəns/", "pos": "n. phr.", "meaning": "記者招待會", "phrases": ["hold a press conference"], "synonyms": [], "antonyms": [], "example": "The company held a press conference to announce its plans for the new research facility."},
    "monster": {"phonetic": "/ˈmɑːnstər/", "pos": "n./adj.", "meaning": "怪物；龐然大物；巨大的", "phrases": ["monster hit"], "synonyms": ["giant", "beast"], "antonyms": [], "example": "The new skyscraper is an absolute monster, dominating the city skyline."},
    "bill": {"phonetic": "/bɪl/", "pos": "n./v.", "meaning": "帳單；法案；鈔票；開帳單", "phrases": ["pay a bill", "dollar bill"], "synonyms": ["invoice", "note"], "antonyms": [], "example": "Could you please bring me the bill? I need to get back to the office."},
    "foot/pay the bill": {"word": "foot the bill", "phonetic": "/fʊt ðə bɪl/", "pos": "v. phr.", "meaning": "買單；付帳", "phrases": [], "synonyms": ["pay the bill"], "antonyms": [], "example": "The company offered to foot the bill for all the travel expenses related to the conference."},
    "naval": {"phonetic": "/ˈneɪvl/", "pos": "adj.", "meaning": "海軍的", "phrases": ["naval base", "naval officer"], "synonyms": ["maritime"], "antonyms": [], "example": "The city has a long history as an important naval base for the country's military."},
    "navy": {"phonetic": "/ˈneɪvi/", "pos": "n.", "meaning": "海軍；深藍色", "phrases": ["royal navy", "navy blue"], "synonyms": [], "antonyms": [], "example": "He spent several years serving in the navy before starting his business career."},
    "a junior officer": {"phonetic": "/ə ˈdʒuːniər ˈɑːfɪsər/", "pos": "n. phr.", "meaning": "初級軍官", "phrases": [], "synonyms": [], "antonyms": ["a senior officer"], "example": "As a junior officer, he was responsible for training the new recruits in the department."},
    "a senior officer": {"phonetic": "/ə ˈsiːniər ˈɑːfɪsər/", "pos": "n. phr.", "meaning": "高級軍官", "phrases": [], "synonyms": [], "antonyms": ["a junior officer"], "example": "Several senior officers were present at the opening ceremony of the new research facility."},
    "pay raise": {"phonetic": "/peɪ reɪz/", "pos": "n. phr.", "meaning": "加薪", "phrases": ["receive a pay raise"], "synonyms": ["salary increase"], "antonyms": ["pay cut"], "example": "He was delighted to hear that he would be receiving a five percent pay raise this year."},
    "narrowly": {"phonetic": "/ˈnæroʊli/", "pos": "adv.", "meaning": "勉強地；狹窄地；嚴密地", "phrases": ["narrowly escape", "narrowly avoid"], "synonyms": ["barely", "tightly"], "antonyms": ["widely"], "example": "The proposal was narrowly approved by the board of directors after a long discussion."},
    "adopt": {"phonetic": "/əˈdɑːpt/", "pos": "v.", "meaning": "採用；收養", "phrases": ["adopt a policy", "adopt a child"], "synonyms": ["embrace", "take on"], "antonyms": ["reject", "abandon"], "example": "The company decided to adopt a new strategy to reach more customers in the international market."},
    "adept": {"phonetic": "/əˈdept/", "pos": "adj./n.", "meaning": "熟練的；內行", "phrases": ["adept at something"], "synonyms": ["skillful", "expert", "proficient"], "antonyms": ["incompetent", "clumsy"], "example": "She is extremely adept at managing complex projects and coordinating with multiple teams."},
    "wire": {"phonetic": "/ˈwaɪər/", "pos": "n./v.", "meaning": "電線；金屬絲；電匯；接線", "phrases": ["live wire", "wire money"], "synonyms": ["cable", "telegram"], "antonyms": [], "example": "We can send the funds via wire transfer if you provide your bank details."},
    "telegram": {"phonetic": "/ˈtelɪɡræm/", "pos": "n.", "meaning": "電報", "phrases": ["send a telegram"], "synonyms": ["cable", "wire"], "antonyms": [], "example": "Telegrams were once a popular way to send urgent messages across long distances."},
    "public opinion": {"phonetic": "/ˈpʌblɪk əˈpɪnjən/", "pos": "n. phr.", "meaning": "輿論；公眾意見", "phrases": ["poll public opinion"], "synonyms": [], "antonyms": [], "example": "The government is trying to influence public opinion regarding the new tax policy."},
    "jumbo": {"phonetic": "/ˈdʒʌmboʊ/", "pos": "adj./n.", "meaning": "巨大的；巨型噴射客機", "phrases": ["jumbo jet"], "synonyms": ["huge", "giant", "massive"], "antonyms": ["tiny", "small"], "example": "The airline operates several jumbo jets on its long-haul international routes."},
    "flavor": {"phonetic": "/ˈfleɪvər/", "pos": "n./v.", "meaning": "風味；口味；給...調味", "phrases": ["natural flavor"], "synonyms": ["taste", "savor"], "antonyms": [], "example": "The coffee shop offers a wide range of different flavors, including vanilla and caramel."},
    "preference": {"phonetic": "/ˈprefrəns/", "pos": "n.", "meaning": "偏好；優先權", "phrases": ["personal preference"], "synonyms": ["choice", "favor"], "antonyms": ["dislike"], "example": "Please let us know your seat preference for the flight to London."},
    "acquaint": {"phonetic": "/əˈkweɪnt/", "pos": "v.", "meaning": "使認識；使了解", "phrases": ["acquaint oneself with"], "synonyms": ["familiarize", "inform"], "antonyms": [], "example": "New employees should take some time to acquaint themselves with the company's policies."},
    "Nevertheless": {"phonetic": "/ˌnevərðəˈles/", "pos": "adv.", "meaning": "儘管如此", "phrases": [], "synonyms": ["nonetheless", "however"], "antonyms": [], "example": "The report was long and complex; nevertheless, it provided some very useful insights."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in gap_fill_gold_8:
        update_info = gap_fill_gold_8[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("完成金色等級補漏第 8 部分 (A public official 到 Acquant)。")
