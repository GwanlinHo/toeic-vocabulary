import json

# 金色等級補漏第 7 部分
gap_fill_gold_7 = {
    "Put sth on hold": {"word": "put on hold", "phonetic": "/pʊt ɑːn hoʊld/", "pos": "v. phr.", "meaning": "擱置；推遲", "phrases": [], "synonyms": ["postpone", "delay"], "antonyms": ["proceed"], "example": "The board decided to put the project on hold until more funding is available."},
    "cut back on": {"phonetic": "/kʌt bæk ɑːn/", "pos": "v. phr.", "meaning": "削減；減少", "phrases": ["cut back on spending"], "synonyms": ["reduce", "decrease"], "antonyms": ["increase"], "example": "The company needs to cut back on unnecessary expenses to improve its profits."},
    "dry up": {"phonetic": "/draɪ ʌp/", "pos": "v. phr.", "meaning": "乾涸；枯竭", "phrases": ["funding dries up"], "synonyms": ["deplete", "exhaust"], "antonyms": [], "example": "Investment in the sector began to dry up following the news of the economic crisis."},
    "recede": {"phonetic": "/rɪˈsiːd/", "pos": "v.", "meaning": "後退；退去；(希望等)變得渺茫", "phrases": ["receding hairline"], "synonyms": ["withdraw", "retreat"], "antonyms": ["advance", "proceed"], "example": "The flood waters finally began to recede after several days of sunshine."},
    "economic recession": {"phonetic": "/ˌekəˈnɑːmɪk rɪˈseʃn/", "pos": "n. phr.", "meaning": "經濟衰退", "phrases": ["during a recession"], "synonyms": ["downturn", "slump"], "antonyms": ["boom", "prosperity"], "example": "Many small businesses struggled to survive during the recent economic recession."},
    "dust off": {"phonetic": "/dʌst ɔːf/", "pos": "v. phr.", "meaning": "擦去灰塵；重新起用(舊計畫)", "phrases": [], "synonyms": ["revive", "restore"], "antonyms": [], "example": "The management decided to dust off an old project proposal from three years ago."},
    "congestion": {"phonetic": "/kənˈdʒestʃən/", "pos": "n.", "meaning": "擁擠；堵塞", "phrases": ["traffic congestion"], "synonyms": ["crowding", "jam"], "antonyms": [], "example": "The new overpass has significantly reduced traffic congestion in the city center."},
    "contribute to": {"phonetic": "/kənˈtrɪbjuːt tuː/", "pos": "v. phr.", "meaning": "貢獻；促成；導致", "phrases": ["contribute to a cause"], "synonyms": ["lead to", "promote"], "antonyms": [], "example": "Innovation and teamwork have greatly contributed to the company's success."},
    "cutback": {"phonetic": "/ˈkʌtbæk/", "pos": "n.", "meaning": "削減；裁減", "phrases": ["budget cutbacks"], "synonyms": ["reduction", "decrease"], "antonyms": ["expansion", "increase"], "example": "The company announced significant cutbacks in its marketing budget for next year."},
    "level off": {"phonetic": "/ˈlevl ɔːf/", "pos": "v. phr.", "meaning": "趨於平緩；穩定下來", "phrases": [], "synonyms": ["stabilize"], "antonyms": ["fluctuate"], "example": "After a period of rapid growth, house prices in the city have started to level off."},
    "A solid line": {"phonetic": "/ə ˈsɑːlɪd laɪn/", "pos": "n. phr.", "meaning": "實線", "phrases": [], "synonyms": [], "antonyms": ["a broken line"], "example": "Drivers are not allowed to cross the solid line on this stretch of the highway."},
    "A broken line": {"phonetic": "/ə ˈbroʊkən laɪn/", "pos": "n. phr.", "meaning": "虛線", "phrases": [], "synonyms": ["dashed line"], "antonyms": ["a solid line"], "example": "You can only overtake other vehicles where there is a broken line on the road."},
    "lawn": {"phonetic": "/lɔːn/", "pos": "n.", "meaning": "草地；草坪", "phrases": ["mow the lawn"], "synonyms": ["grass", "turf"], "antonyms": [], "example": "The hotel has a beautiful green lawn where guests can sit and relax in the sun."},
    "throwback": {"phonetic": "/ˈθroʊbæk/", "pos": "n.", "meaning": "復古；退化；回歸", "phrases": ["throwback to the past"], "synonyms": ["reversion"], "antonyms": [], "example": "The design of the new office building is a throwback to the classic style of the 1920s."},
    "court": {"phonetic": "/kɔːrt/", "pos": "n./v.", "meaning": "法院；球場；遊說；追求", "phrases": ["take to court", "tennis court"], "synonyms": ["tribunal", "woo", "seek"], "antonyms": [], "example": "The case will be heard in the high court early next month."},
    "brainstorm": {"phonetic": "/ˈbreɪnstɔːrm/", "pos": "v./n.", "meaning": "腦力激盪；集思廣益", "phrases": ["brainstorming session"], "synonyms": ["deliberate", "ponder"], "antonyms": [], "example": "The marketing team met to brainstorm ideas for the new advertising campaign."},
    "pesticide": {"phonetic": "/ˈpestɪsaɪd/", "pos": "n.", "meaning": "殺蟲劑", "phrases": ["organic pesticide"], "synonyms": ["insecticide"], "antonyms": [], "example": "The farmers are being encouraged to use natural alternatives to chemical pesticides."},
    "strain": {"phonetic": "/streɪn/", "pos": "n./v.", "meaning": "壓力；張力；拉傷；濾過", "phrases": ["under strain", "muscle strain"], "synonyms": ["stress", "tension", "exert"], "antonyms": ["relaxation"], "example": "The sudden increase in workload has put a lot of strain on the employees."},
    "marginal": {"phonetic": "/ˈmɑːrdʒɪnl/", "pos": "adj.", "meaning": "微小的；邊緣的", "phrases": ["marginal increase"], "synonyms": ["slight", "minor"], "antonyms": ["significant", "major"], "example": "The improvements in efficiency have resulted in a marginal decrease in costs."},
    "emission": {"phonetic": "/iˈmɪʃn/", "pos": "n.", "meaning": "排放；散發", "phrases": ["carbon emissions", "emission standards"], "synonyms": ["release", "discharge"], "antonyms": ["absorption"], "example": "The government is introducing stricter regulations to reduce carbon emissions from factories."},
    "thrill": {"phonetic": "/θrɪl/", "pos": "n./v.", "meaning": "興奮；使激動", "phrases": ["thrill seeker"], "synonyms": ["excitement", "elation"], "antonyms": ["boredom"], "example": "The employees were thrilled to hear that they would all be receiving a bonus."},
    "sue sb for sth": {"word": "sue", "phonetic": "/suː/", "pos": "v. phr.", "meaning": "控告某人某事", "phrases": ["sue for damages"], "synonyms": ["litigate", "prosecute"], "antonyms": [], "example": "The company decided to sue its former partner for breach of contract."},
    "wilderness": {"phonetic": "/ˈwɪldərnəs/", "pos": "n.", "meaning": "荒野；荒漠", "phrases": ["into the wilderness"], "synonyms": ["wasteland", "wilds"], "antonyms": ["civilization"], "example": "The national park features thousands of hectares of beautiful mountain wilderness."},
    "organic": {"phonetic": "/ɔːrˈɡænɪk/", "pos": "adj.", "meaning": "有機的；器官的；組織的", "phrases": ["organic food", "organic growth"], "synonyms": ["natural", "biological"], "antonyms": ["inorganic", "artificial"], "example": "Demand for organic products has increased significantly over the last few years."},
    "genetic": {"phonetic": "/dʒəˈnetɪk/", "pos": "adj.", "meaning": "基因的；遺傳的", "phrases": ["genetic engineering"], "synonyms": ["hereditary"], "antonyms": [], "example": "Researchers are studying the genetic factors that contribute to heart disease."},
    "given": {"phonetic": "/ˈɡɪvn/", "pos": "adj./prep./n.", "meaning": "考慮到；特定的；假設", "phrases": ["given that", "at a given time"], "synonyms": ["considering", "fixed"], "antonyms": [], "example": "Given the current economic climate, the company's performance has been excellent."},
    "plaza": {"phonetic": "/ˈplæzə/", "pos": "n.", "meaning": "廣場；購物中心", "phrases": ["city plaza", "shopping plaza"], "synonyms": ["square", "mall"], "antonyms": [], "example": "The new office building is located right next to the city's main shopping plaza."},
    "beforehand": {"phonetic": "/bɪˈfɔːrhænd/", "pos": "adv.", "meaning": "預先；事先", "phrases": ["prepare beforehand"], "synonyms": ["in advance", "ahead of time"], "antonyms": ["afterwards"], "example": "Please make sure you read the report beforehand so we can discuss it at the meeting."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in gap_fill_gold_7:
        update_info = gap_fill_gold_7[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("完成金色等級補漏第 7 部分 (Put sth on hold 到 A broken line)。")
