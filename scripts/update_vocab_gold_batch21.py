import json

# 第 1001-1050 個高品質單字對應表 (金色等級)
enriched_data_gold_21 = {
    "memorabilia": {"phonetic": "/ˌmemərəˈbɪliə/", "pos": "n.", "meaning": "紀念品；收藏品(複數)", "phrases": ["sports memorabilia"], "synonyms": ["keepsakes", "souvenirs"], "antonyms": [], "example": "The museum features a large collection of movie memorabilia from the 1950s."},
    "outgoing": {"phonetic": "/ˈaʊtɡoʊɪŋ/", "pos": "adj.", "meaning": "外向的；即將離職的；外發的", "phrases": ["outgoing president", "outgoing mail"], "synonyms": ["sociable", "departing"], "antonyms": ["incoming", "shy"], "example": "The outgoing manager will train her successor before she leaves the company next month."},
    "obsolete": {"phonetic": "/ˌɑːbsəˈliːt/", "pos": "adj.", "meaning": "過時的；廢棄的", "phrases": ["become obsolete"], "synonyms": ["outdated", "outmoded"], "antonyms": ["modern", "current"], "example": "The old computer system has become obsolete and needs to be replaced immediately."},
    "inauguration": {"phonetic": "/ɪˌnɔːɡjəˈreɪʃn/", "pos": "n.", "meaning": "就職典禮；開幕式", "phrases": ["presidential inauguration"], "synonyms": ["initiation", "launch"], "antonyms": [], "example": "The inauguration of the new research facility will take place next Friday afternoon."},
    "media coverage": {"phonetic": "/ˈmiːdiə ˈkʌvərɪdʒ/", "pos": "n. phr.", "meaning": "媒體報導", "phrases": ["extensive media coverage"], "synonyms": ["press coverage"], "antonyms": [], "example": "The company's new product launch received extensive media coverage across the country."},
    "applicable": {"phonetic": "/ˈæplɪkəbl/", "pos": "adj.", "meaning": "適用的；合適的", "phrases": ["where applicable"], "synonyms": ["relevant", "appropriate"], "antonyms": ["inapplicable", "irrelevant"], "example": "The new safety regulations are applicable to all employees working in the factory."},
    "eloquent": {"phonetic": "/ˈeləkwənt/", "pos": "adj.", "meaning": "雄辯的；口才流利的", "phrases": ["eloquent speaker"], "synonyms": ["articulate", "persuasive"], "antonyms": ["inarticulate"], "example": "The CEO gave an eloquent speech about the company's future vision and goals."},
    "tableware": {"phonetic": "/ˈteɪblwer/", "pos": "n.", "meaning": "餐具", "phrases": ["ceramic tableware"], "synonyms": ["dinnerware"], "antonyms": [], "example": "The department store sells a wide range of high-quality ceramic tableware and glasses."},
    "be packed with": {"phonetic": "/bi pækt wɪð/", "pos": "v. phr.", "meaning": "充滿...；擠滿...", "phrases": [], "synonyms": ["be full of", "be crowded with"], "antonyms": ["be empty of"], "example": "The conference hall was packed with delegates from all over the world."},
    "solitary": {"phonetic": "/ˈsɑːləteri/", "pos": "adj.", "meaning": "單獨的；獨居的", "phrases": ["solitary worker"], "synonyms": ["alone", "isolated", "single"], "antonyms": ["social", "gregarious"], "example": "He prefers a solitary working environment where he can focus on his research."},
    "petroleum": {"phonetic": "/pəˈtroʊliəm/", "pos": "n.", "meaning": "石油", "phrases": ["petroleum industry"], "synonyms": ["crude oil"], "antonyms": [], "example": "The country's economy is heavily dependent on the export of petroleum and natural gas."},
    "provided that": {"phonetic": "/prəˈvaɪdɪd ðæt/", "pos": "conj. phr.", "meaning": "只要；如果", "phrases": [], "synonyms": ["as long as", "on condition that"], "antonyms": [], "example": "You can work from home provided that you attend all the weekly team meetings."},
    "courting": {"phonetic": "/ˈkɔːrtɪŋ/", "pos": "v./n.", "meaning": "求愛；追求；設法獲得", "phrases": ["courting disaster"], "synonyms": ["seeking", "wooing"], "antonyms": [], "example": "The startup is currently courting several international investors to fund its expansion."},
    "census": {"phonetic": "/ˈsensəs/", "pos": "n.", "meaning": "人口普查", "phrases": ["national census"], "synonyms": ["count", "survey"], "antonyms": [], "example": "The government conducts a national census every ten years to gather demographic data."},
    "suburban": {"phonetic": "/səˈbɜːrbən/", "pos": "adj.", "meaning": "郊區的", "phrases": ["suburban area"], "synonyms": [], "antonyms": ["urban"], "example": "Many families prefer living in suburban areas because of the lower cost of housing."},
    "rehearse": {"phonetic": "/rɪˈhɜːrs/", "pos": "v.", "meaning": "排練；演習；詳述", "phrases": ["rehearse a presentation"], "synonyms": ["practice", "prepare"], "antonyms": [], "example": "The marketing team spent all afternoon rehearsing their presentation for the big client."},
    "roomy": {"phonetic": "/ˈruːmi/", "pos": "adj.", "meaning": "寬敞的", "phrases": ["roomy office"], "synonyms": ["spacious", "commodious"], "antonyms": ["cramped", "small"], "example": "Our new office is very roomy and has enough space for twenty more desks."},
    "devise": {"phonetic": "/dɪˈvaɪz/", "pos": "v.", "meaning": "設計；想出；策劃", "phrases": ["devise a strategy"], "synonyms": ["invent", "formulate", "plan"], "antonyms": [], "example": "The engineering team is trying to devise a more efficient way to process the data."},
    "device": {"phonetic": "/dɪˈvaɪs/", "pos": "n.", "meaning": "裝置；設備；手段", "phrases": ["electronic device", "mobile device"], "synonyms": ["apparatus", "gadget", "tool"], "antonyms": [], "example": "The new mobile device is designed to be lightweight and extremely powerful."},
    "proofread": {"phonetic": "/ˈpruːfriːd/", "pos": "v.", "meaning": "校對", "phrases": ["proofread a report"], "synonyms": ["correct", "edit"], "antonyms": [], "example": "Please remember to proofread your report carefully before you submit it to the manager."},
    "outlet": {"phonetic": "/ˈaʊtlet/", "pos": "n.", "meaning": "出口；銷路；電源插座；暢貨中心", "phrases": ["retail outlet", "electrical outlet", "factory outlet"], "synonyms": ["store", "socket", "vent"], "antonyms": [], "example": "The company is planning to open ten new retail outlets in the city center this year."},
    "archaeologist": {"phonetic": "/ˌɑːrkiˈɑːlədʒɪst/", "pos": "n.", "meaning": "考古學家", "phrases": [], "synonyms": [], "antonyms": [], "example": "The archaeologist discovered the remains of an ancient city during the excavation."},
    "souvenir": {"phonetic": "/ˌsuːvəˈnɪr/", "pos": "n.", "meaning": "紀念品", "phrases": ["buy souvenirs"], "synonyms": ["keepsake", "memento"], "antonyms": [], "example": "Many tourists buy traditional handicrafts as souvenirs when they visit the island."},
    "attire": {"phonetic": "/əˈtaɪər/", "pos": "n.", "meaning": "服裝；衣著", "phrases": ["business attire", "formal attire"], "synonyms": ["clothing", "garment"], "antonyms": [], "example": "The company expects all employees to wear appropriate business attire at all times."},
    "segregation": {"phonetic": "/ˌseɡrɪˈɡeɪʃn/", "pos": "n.", "meaning": "隔離；分離", "phrases": ["waste segregation"], "synonyms": ["separation", "isolation"], "antonyms": ["integration", "unification"], "example": "The new policy includes strict regulations regarding the segregation of different types of waste."},
    "yacht": {"phonetic": "/jɑːt/", "pos": "n.", "meaning": "遊艇", "phrases": ["luxury yacht"], "synonyms": ["boat"], "antonyms": [], "example": "The billionaire invited his business associates for a meeting on his luxury yacht."},
    "pier": {"phonetic": "/pɪr/", "pos": "n.", "meaning": "碼頭；橋墩", "phrases": ["fishing pier"], "synonyms": ["wharf", "dock"], "antonyms": [], "example": "The ferry departs from the main pier in the city center every thirty minutes."},
    "shoreline": {"phonetic": "/ˈʃɔːrlaɪn/", "pos": "n.", "meaning": "海岸線", "phrases": ["rugged shoreline"], "synonyms": ["coastline"], "antonyms": [], "example": "The hotel is located right on the shoreline, offering spectacular views of the ocean."},
    "haul": {"phonetic": "/hɔːl/", "pos": "v./n.", "meaning": "拖曳；搬運；旅程", "phrases": ["long haul flight"], "synonyms": ["pull", "drag", "tow"], "antonyms": [], "example": "The truck was used to haul heavy construction materials to the site."},
    "bouquet": {"phonetic": "/buˈkeɪ/", "pos": "n.", "meaning": "花束；酒香", "phrases": ["a bouquet of flowers"], "synonyms": ["bunch", "fragrance"], "antonyms": [], "example": "The manager presented her with a large bouquet of flowers on her tenth anniversary with the company."},
    "reverse": {"phonetic": "/rɪˈvɜːrs/", "pos": "v./n./adj.", "meaning": "倒轉；相反；背面", "phrases": ["reverse the decision", "in reverse"], "synonyms": ["invert", "opposite"], "antonyms": ["forward"], "example": "The company decided to reverse its decision to close the local branch office."},
    "portfolio": {"phonetic": "/pɔːrtˈfoʊlioʊ/", "pos": "n.", "meaning": "投資組合；作品集", "phrases": ["investment portfolio", "design portfolio"], "synonyms": [], "antonyms": [], "example": "The investor has a diversified portfolio that includes stocks, bonds, and real estate."},
    "turnout": {"phonetic": "/ˈtɜːrnaʊt/", "pos": "n.", "meaning": "出席人數；產量", "phrases": ["high turnout"], "synonyms": ["attendance"], "antonyms": [], "example": "There was a very high turnout at the annual general meeting this year."},
    "iceberg": {"phonetic": "/ˈaɪsbɜːrɡ/", "pos": "n.", "meaning": "冰山", "phrases": ["tip of the iceberg"], "synonyms": [], "antonyms": [], "example": "The reported financial losses are just the tip of the iceberg according to the auditors."},
    "archway": {"phonetic": "/ˈɑːrtʃweɪ/", "pos": "n.", "meaning": "拱門", "phrases": ["stone archway"], "synonyms": ["arch"], "antonyms": [], "example": "He walked through the large stone archway into the main courtyard of the hotel."},
    "gaze": {"phonetic": "/ɡeɪz/", "pos": "v./n.", "meaning": "凝視；注視", "phrases": ["gaze at something"], "synonyms": ["stare", "look"], "antonyms": ["glance"], "example": "The CEO stood by the window and gazed out at the city skyline while he waited."},
    "lamppost": {"phonetic": "/ˈlæmppoʊst/", "pos": "n.", "meaning": "燈柱；路燈杆", "phrases": [], "synonyms": ["street lamp"], "antonyms": [], "example": "The street was lit by several old-fashioned iron lampposts along the sidewalk."},
    "deck": {"phonetic": "/dek/", "pos": "n./v.", "meaning": "甲板；露台；裝飾", "phrases": ["observation deck"], "synonyms": ["platform", "terrace"], "antonyms": [], "example": "The building features an observation deck on the top floor with views of the entire city."},
    "pull up": {"phonetic": "/pʊl ʌp/", "pos": "v. phr.", "meaning": "停車；拉上來；調出(視窗)", "phrases": [], "synonyms": ["stop", "draw up"], "antonyms": ["drive off"], "example": "The delivery truck pulled up in front of the warehouse and started unloading the goods."},
    "receiver": {"phonetic": "/rɪˈsiːvər/", "pos": "n.", "meaning": "接收器；聽筒；接球手；受託人", "phrases": ["telephone receiver"], "synonyms": ["handset"], "antonyms": ["sender", "transmitter"], "example": "He picked up the receiver and answered the phone on the second ring."},
    "chimney": {"phonetic": "/ˈtʃɪmni/", "pos": "n.", "meaning": "煙囪", "phrases": ["factory chimney"], "synonyms": ["vent", "stack"], "antonyms": [], "example": "The old factory chimney is a well-known landmark in the local industrial area."},
    "multistory": {"phonetic": "/ˈmʌltistɔːri/", "pos": "adj.", "meaning": "多層的", "phrases": ["multistory car park"], "synonyms": ["multi-level"], "antonyms": ["single-story"], "example": "The new multistory office building is expected to be completed by next summer."},
    "cargo": {"phonetic": "/ˈkɑːrɡoʊ/", "pos": "n.", "meaning": "貨物", "phrases": ["cargo plane", "precious cargo"], "synonyms": ["freight", "goods"], "antonyms": [], "example": "The ship is carrying a massive cargo of electronics and machinery from Asia."},
    "sanctuary": {"phonetic": "/ˈsæŋktʃueri/", "pos": "n.", "meaning": "避難所；保護區；聖殿", "phrases": ["wildlife sanctuary"], "synonyms": ["refuge", "shelter"], "antonyms": [], "example": "The local government has established a new wildlife sanctuary to protect endangered birds."},
    "inaugural": {"phonetic": "/ɪˈnɔːɡjərəl/", "pos": "adj.", "meaning": "就職的；開幕的；首次的", "phrases": ["inaugural flight", "inaugural speech"], "synonyms": ["first", "initial", "opening"], "antonyms": ["final", "closing"], "example": "The airline's inaugural flight to London will take place next Wednesday."},
    "fume": {"phonetic": "/fjuːm/", "pos": "n./v.", "meaning": "煙霧；臭氣；發怒", "phrases": ["exhaust fumes"], "synonyms": ["smoke", "gas", "seethe"], "antonyms": [], "example": "Many residents have complained about the exhaust fumes from the nearby highway."},
    "take charge of": {"phonetic": "/teɪk tʃɑːrdʒ əv/", "pos": "v. phr.", "meaning": "接管；負責", "phrases": [], "synonyms": ["lead", "manage", "take control of"], "antonyms": [], "example": "The senior manager decided to take charge of the project to ensure its success."},
    "relief effort": {"phonetic": "/rɪˈliːf ˈefərt/", "pos": "n. phr.", "meaning": "救援行動", "phrases": ["disaster relief effort"], "synonyms": [], "antonyms": [], "example": "The international community is coordinating a massive relief effort for the victims of the flood."},
    "hardness": {"phonetic": "/ˈhɑːrdnəs/", "pos": "n.", "meaning": "硬度；困難", "phrases": ["water hardness"], "synonyms": ["firmness", "difficulty"], "antonyms": ["softness", "easiness"], "example": "The durability of the new building material depends on its surface hardness."},
    "primitively": {"phonetic": "/ˈprɪmətɪvli/", "pos": "adv.", "meaning": "原始地；簡單地", "phrases": [], "synonyms": ["simply", "crudely"], "antonyms": ["sophisticatedly"], "example": "Some small island communities still live primitively, relying on traditional farming and fishing."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_21:
        update_info = enriched_data_gold_21[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 1001-1050 個單字。")
