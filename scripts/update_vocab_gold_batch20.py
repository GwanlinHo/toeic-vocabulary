import json

# 第 951-1000 個高品質單字對應表 (金色等級)
enriched_data_gold_20 = {
    "unravel": {"phonetic": "/ʌnˈrævl/", "pos": "v.", "meaning": "解開；闡明；拆散", "phrases": ["unravel a mystery"], "synonyms": ["untangle", "resolve"], "antonyms": ["tangle"], "example": "Investigators are trying to unravel the complex web of financial transactions."},
    "enhancement": {"phonetic": "/ɪnˈhænsmənt/", "pos": "n.", "meaning": "增強；提升；優化", "phrases": ["quality enhancement"], "synonyms": ["improvement", "upgrade"], "antonyms": ["deterioration"], "example": "The new software update includes several enhancements to the user interface."},
    "trial": {"phonetic": "/ˈtraɪəl/", "pos": "n./v.", "meaning": "審判；試驗；考驗", "phrases": ["trial period", "clinical trial"], "synonyms": ["test", "hearing"], "antonyms": [], "example": "The new drug is currently undergoing clinical trials to ensure its safety."},
    "get in shape": {"phonetic": "/ɡet ɪn ʃeɪp/", "pos": "v. phr.", "meaning": "健身；鍛鍊體態", "phrases": [], "synonyms": ["get fit"], "antonyms": ["get out of shape"], "example": "He joined a gym and started a new diet to get in shape for the summer."},
    "arena": {"phonetic": "/əˈriːnə/", "pos": "n.", "meaning": "競技場；領域", "phrases": ["political arena"], "synonyms": ["stadium", "sphere"], "antonyms": [], "example": "The company is a major player in the international telecommunications arena."},
    "alumnus": {"phonetic": "/əˈlʌmnəs/", "pos": "n.", "meaning": "男校友(單數)", "phrases": ["university alumnus"], "synonyms": ["graduate"], "antonyms": [], "example": "As a prominent alumnus, he was invited to give a speech at the graduation ceremony."},
    "alma mater": {"phonetic": "/ˌælmə ˈmɑːtər/", "pos": "n. phr.", "meaning": "母校", "phrases": [], "synonyms": [], "antonyms": [], "example": "He donated a significant amount of money to his alma mater to fund a new library."},
    "reunite": {"phonetic": "/ˌriːjuˈnaɪt/", "pos": "v.", "meaning": "重聚；統一", "phrases": ["family reunion"], "synonyms": ["rejoin", "unify"], "antonyms": ["separate", "divide"], "example": "The conference provided a great opportunity for former colleagues to reunite and network."},
    "entree": {"phonetic": "/ˈɑːntreɪ/", "pos": "n.", "meaning": "主菜；進入權", "phrases": [], "synonyms": ["main course"], "antonyms": [], "example": "The restaurant's signature entree is a delicious grilled salmon with seasonal vegetables."},
    "bottomless": {"phonetic": "/ˈbɑːtəmləs/", "pos": "adj.", "meaning": "無底的；無限的；(飲料)續杯的", "phrases": ["bottomless pit", "bottomless coffee"], "synonyms": ["unlimited", "infinite"], "antonyms": ["limited", "finite"], "example": "The restaurant offers bottomless drinks with every meal during the lunch hour."},
    "withhold": {"phonetic": "/wɪðˈhoʊld/", "pos": "v.", "meaning": "扣留；保留；抑制", "phrases": ["withhold information", "withholding tax"], "synonyms": ["retain", "keep back"], "antonyms": ["release", "grant"], "example": "The company was accused of withholding critical information from its shareholders."},
    "station": {"phonetic": "/ˈsteɪʃn/", "pos": "n./v.", "meaning": "車站；局；崗位；駐紮", "phrases": ["gas station", "fire station", "work station"], "synonyms": ["post", "base"], "antonyms": [], "example": "Please meet me at the main train station at 10 AM tomorrow morning."},
    "instrumental": {"phonetic": "/ˌɪnstrəˈmentl/", "pos": "adj.", "meaning": "起作用的；樂器的", "phrases": ["be instrumental in"], "synonyms": ["helpful", "essential"], "antonyms": ["insignificant"], "example": "She was instrumental in negotiating the new trade agreement between the two companies."},
    "lodging": {"phonetic": "/ˈlɑːdʒɪŋ/", "pos": "n.", "meaning": "住宿；住所", "phrases": ["board and lodging"], "synonyms": ["accommodation", "housing"], "antonyms": [], "example": "The travel package includes international flights, meals, and luxury lodging."},
    "rear": {"phonetic": "/rɪr/", "pos": "n./adj./v.", "meaning": "後部；後面的；撫養", "phrases": ["rear window", "rear view mirror"], "synonyms": ["back", "hind"], "antonyms": ["front"], "example": "The delivery entrance is located at the rear of the office building."},
    "silverware": {"phonetic": "/ˈsɪlvərwer/", "pos": "n.", "meaning": "銀器；餐具", "phrases": [], "synonyms": ["cutlery", "flatware"], "antonyms": [], "example": "The hotel restaurant uses high-quality silverware for its formal banquet events."},
    "ceiling": {"phonetic": "/ˈsiːlɪŋ/", "pos": "n.", "meaning": "天花板；上限", "phrases": ["price ceiling", "glass ceiling"], "synonyms": ["limit", "roof"], "antonyms": ["floor"], "example": "The government has imposed a price ceiling on basic food items to prevent inflation."},
    "dump": {"phonetic": "/dʌmp/", "pos": "v./n.", "meaning": "傾倒；拋棄；垃圾場", "phrases": ["dumping ground", "data dump"], "synonyms": ["discard", "dispose"], "antonyms": [], "example": "The company was fined for dumping chemical waste into the local river."},
    "polish": {"phonetic": "/ˈpɑːlɪʃ/", "pos": "v./n.", "meaning": "磨光；擦亮；完善", "phrases": ["nail polish", "polish a report"], "synonyms": ["shine", "refine"], "antonyms": ["roughen"], "example": "You should polish your presentation before giving it to the board of directors."},
    "stream in": {"phonetic": "/striːm ɪn/", "pos": "v. phr.", "meaning": "湧入；源源而來", "phrases": [], "synonyms": ["flood in", "pour in"], "antonyms": [], "example": "Orders began to stream in as soon as the new product was announced on the website."},
    "pillar": {"phonetic": "/ˈpɪlər/", "pos": "n.", "meaning": "柱子；支柱", "phrases": ["pillar of society", "central pillar"], "synonyms": ["column", "support"], "antonyms": [], "example": "Small businesses are a central pillar of the local economy, providing many jobs."},
    "erect": {"phonetic": "/ɪˈrekt/", "pos": "v./adj.", "meaning": "建立；豎立；直立的", "phrases": ["erect a building"], "synonyms": ["build", "construct", "upright"], "antonyms": ["demolish"], "example": "The construction team will erect the steel frame of the building next week."},
    "doorway": {"phonetic": "/ˈdɔːrweɪ/", "pos": "n.", "meaning": "門口；出入口", "phrases": ["stand in the doorway"], "synonyms": ["entrance", "entry"], "antonyms": [], "example": "He stood in the doorway and welcomed the guests as they arrived at the party."},
    "garage": {"phonetic": "/ɡəˈrɑːʒ/", "pos": "n./v.", "meaning": "車庫；修車廠", "phrases": ["parking garage"], "synonyms": [], "antonyms": [], "example": "The new office building has a large underground garage for employees and clients."},
    "port": {"phonetic": "/pɔːrt/", "pos": "n.", "meaning": "港口；(電腦)端口", "phrases": ["seaport", "USB port"], "synonyms": ["harbor"], "antonyms": [], "example": "The shipment of raw materials has finally arrived at the city's main port."},
    "expo": {"phonetic": "/ˈekspoʊ/", "pos": "n.", "meaning": "博覽會；展覽會", "phrases": ["trade expo"], "synonyms": ["exposition", "exhibition"], "antonyms": [], "example": "Our company will have a large booth at the international technology expo next month."},
    "marine": {"phonetic": "/məˈriːn/", "pos": "adj./n.", "meaning": "海洋的；航海的；海軍陸戰隊", "phrases": ["marine life", "marine industry"], "synonyms": ["nautical", "maritime"], "antonyms": ["terrestrial"], "example": "The company specializes in manufacturing high-quality marine equipment for ships."},
    "misplace": {"phonetic": "/ˌmɪsˈpleɪs/", "pos": "v.", "meaning": "忘放處；誤放", "phrases": ["misplace keys"], "synonyms": ["lose"], "antonyms": ["find"], "example": "I'm sorry, I seem to have misplaced the folder containing the contract details."},
    "gemstone": {"phonetic": "/ˈdʒemstoʊn/", "pos": "n.", "meaning": "寶石", "phrases": ["precious gemstone"], "synonyms": ["jewel", "gem"], "antonyms": [], "example": "The company imports high-quality gemstones from several countries around the world."},
    "specimen": {"phonetic": "/ˈspesɪmən/", "pos": "n.", "meaning": "樣品；標本", "phrases": ["blood specimen"], "synonyms": ["sample", "example"], "antonyms": [], "example": "The researchers collected several specimens of local plants for further study."},
    "mineral": {"phonetic": "/ˈmɪnərəl/", "pos": "n./adj.", "meaning": "礦物；礦產", "phrases": ["mineral water", "mineral resources"], "synonyms": [], "antonyms": [], "example": "The region is rich in mineral resources, including iron ore and coal."},
    "glow": {"phonetic": "/ɡloʊ/", "pos": "v./n.", "meaning": "發光；紅潤；光輝", "phrases": ["soft glow"], "synonyms": ["shine", "radiate"], "antonyms": ["darkness"], "example": "The city center is filled with the glow of colorful lights during the festive season."},
    "stunning": {"phonetic": "/ˈstʌnɪŋ/", "pos": "adj.", "meaning": "令人驚艷的；極好的", "phrases": ["stunning view"], "synonyms": ["breathtaking", "amazing"], "antonyms": ["ordinary", "ugly"], "example": "The new office building features a stunning contemporary design with lots of glass."},
    "telescope": {"phonetic": "/ˈtelɪskoʊp/", "pos": "n./v.", "meaning": "望遠鏡；縮短", "phrases": ["space telescope"], "synonyms": [], "antonyms": [], "example": "The university's observatory is equipped with a very powerful research telescope."},
    "sterilize": {"phonetic": "/ˈsterəlaɪz/", "pos": "v.", "meaning": "殺菌；消毒；使絕育", "phrases": [], "synonyms": ["disinfect", "sanitize"], "antonyms": ["contaminate"], "example": "It is important to properly sterilize all medical instruments before use."},
    "sanitize": {"phonetic": "/ˈsænɪtaɪz/", "pos": "v.", "meaning": "消毒；衛生處理；淨化(資訊)", "phrases": [], "synonyms": ["disinfect", "clean"], "antonyms": ["dirty"], "example": "The food processing facility is sanitized every night to ensure product safety."},
    "contamination": {"phonetic": "/kənˌtæmɪˈneɪʃn/", "pos": "n.", "meaning": "污染；弄髒", "phrases": ["water contamination"], "synonyms": ["pollution", "impurity"], "antonyms": ["purity", "cleanness"], "example": "The factory was closed following reports of chemical contamination in the local area."},
    "faucet": {"phonetic": "/ˈfɔːsɪt/", "pos": "n.", "meaning": "水龍頭", "phrases": ["kitchen faucet", "leaky faucet"], "synonyms": ["tap"], "antonyms": [], "example": "We had to call a plumber to fix the leaky faucet in the office kitchen."},
    "artwork": {"phonetic": "/ˈɑːrtwɜːrk/", "pos": "n.", "meaning": "藝術品；美術設計", "phrases": ["original artwork"], "synonyms": [], "antonyms": [], "example": "The walls of the hotel lobby are decorated with beautiful modern artwork."},
    "stool": {"phonetic": "/stuːl/", "pos": "n.", "meaning": "凳子；大便", "phrases": ["bar stool"], "synonyms": ["seat"], "antonyms": [], "example": "There are several high stools at the counter for customers to sit on."},
    "balcony": {"phonetic": "/ˈbælkəni/", "pos": "n.", "meaning": "陽台", "phrases": ["balcony view"], "synonyms": ["veranda", "terrace"], "antonyms": [], "example": "Our new office has a small balcony where we can go to get some fresh air."},
    "in rows": {"phonetic": "/ɪn roʊz/", "pos": "phr.", "meaning": "成排地", "phrases": ["arranged in rows"], "synonyms": [], "antonyms": [], "example": "The chairs in the conference hall were neatly arranged in rows of ten."},
    "trailer": {"phonetic": "/ˈtreɪlər/", "pos": "n.", "meaning": "預告片；拖車", "phrases": ["movie trailer", "tractor trailer"], "synonyms": [], "antonyms": [], "example": "The company released a short trailer to promote its new mobile game."},
    "ramp": {"phonetic": "/ræmp/", "pos": "n./v.", "meaning": "斜坡；坡道；大幅增加(ramp up)", "phrases": ["wheelchair ramp", "ramp up production"], "synonyms": ["slope", "incline"], "antonyms": [], "example": "The company is planning to ramp up production to meet the increasing demand."},
    "subtract": {"phonetic": "/səbˈtrækt/", "pos": "v.", "meaning": "減去；扣除", "phrases": [], "synonyms": ["deduct", "remove"], "antonyms": ["add"], "example": "You need to subtract any discounts before you calculate the total amount due."},
    "solicitation": {"phonetic": "/səˌlɪsɪˈteɪʃn/", "pos": "n.", "meaning": "懇求；徵求；拉客", "phrases": ["no solicitation"], "synonyms": ["request", "appeal"], "antonyms": [], "example": "The building has a strict policy against any form of unauthorized solicitation."},
    "gloomy": {"phonetic": "/ˈɡluːmi/", "pos": "adj.", "meaning": "陰暗的；憂鬱的；慘淡的", "phrases": ["gloomy forecast"], "synonyms": ["dark", "depressing", "somber"], "antonyms": ["bright", "cheerful", "optimistic"], "example": "Despite the gloomy economic outlook, the company is still planning to expand."},
    "derive from": {"phonetic": "/dɪˈraɪv frəm/", "pos": "v. phr.", "meaning": "源自於；衍生自", "phrases": [], "synonyms": ["stem from", "originate from"], "antonyms": [], "example": "Many modern medical treatments are derived from natural plant extracts."},
    "associate": {"phonetic": "/əˈsoʊʃieɪt/ (v.) /əˈsoʊʃiət/ (n.)", "pos": "v./n./adj.", "meaning": "聯想；夥伴；副的", "phrases": ["business associate", "associate professor"], "synonyms": ["partner", "colleague", "connect"], "antonyms": ["disconnect"], "example": "He met with several business associates to discuss the details of the new project."},
    "farewell": {"phonetic": "/ˌferˈwel/", "pos": "n./int.", "meaning": "告別；辭行", "phrases": ["farewell party"], "synonyms": ["goodbye", "departure"], "antonyms": ["welcome", "greeting"], "example": "We held a special farewell lunch for the manager before he left for his new job."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_20:
        update_info = enriched_data_gold_20[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 951-1000 個單字。")
