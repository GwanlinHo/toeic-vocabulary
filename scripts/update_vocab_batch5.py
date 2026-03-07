import json

# 第 201-250 個高品質單字對應表 (綠色等級)
enriched_data_5 = {
    "commodity": {"phonetic": "/kəˈmɑːdəti/", "pos": "n.", "meaning": "商品；貨物", "phrases": ["basic commodity", "commodity market"], "synonyms": ["product", "good"], "antonyms": [], "example": "Coffee is one of the world's most actively traded commodities."},
    "commute": {"phonetic": "/kəˈmjuːt/", "pos": "v./n.", "meaning": "通勤", "phrases": ["daily commute", "commute to work"], "synonyms": ["travel"], "antonyms": [], "example": "Many people commute from the suburbs to the city for work every day."},
    "commuter": {"phonetic": "/kəˈmjuːtər/", "pos": "n.", "meaning": "通勤者", "phrases": ["commuter train", "long-distance commuter"], "synonyms": [], "antonyms": [], "example": "The commuter train was delayed this morning due to technical problems."},
    "complain": {"phonetic": "/kəmˈpleɪn/", "pos": "v.", "meaning": "抱怨；投訴", "phrases": ["complain about", "formally complain"], "synonyms": ["protest", "object"], "antonyms": ["praise", "compliment"], "example": "The customer called to complain about the poor service at the restaurant."},
    "consumption": {"phonetic": "/kənˈsʌmpʃn/", "pos": "n.", "meaning": "消耗；消費", "phrases": ["energy consumption", "domestic consumption"], "synonyms": ["usage", "use"], "antonyms": [], "example": "We need to reduce our energy consumption to lower our monthly bills."},
    "coverage": {"phonetic": "/ˈkʌvərɪdʒ/", "pos": "n.", "meaning": "保險範圍；新聞報導", "phrases": ["insurance coverage", "media coverage"], "synonyms": ["reporting", "protection"], "antonyms": [], "example": "You should check if your insurance policy provides enough coverage for medical expenses."},
    "crop": {"phonetic": "/krɑːp/", "pos": "n./v.", "meaning": "農作物；收成", "phrases": ["cash crop", "crop failure"], "synonyms": ["harvest", "yield"], "antonyms": [], "example": "The heavy rain has caused serious damage to the local farmers' crops."},
    "cuisine": {"phonetic": "/kwɪˈziːn/", "pos": "n.", "meaning": "烹飪；菜餚", "phrases": ["local cuisine", "fine cuisine"], "synonyms": ["cooking", "food"], "antonyms": [], "example": "The restaurant is famous for its delicious and authentic Italian cuisine."},
    "customs": {"phonetic": "/ˈkʌstəmz/", "pos": "n.", "meaning": "海關；關稅", "phrases": ["pass through customs", "customs duty"], "synonyms": [], "antonyms": [], "example": "It took nearly an hour for the passengers to pass through customs at the airport."},
    "depart": {"phonetic": "/dɪˈpɑːrt/", "pos": "v.", "meaning": "出發；離開", "phrases": ["depart from", "scheduled to depart"], "synonyms": ["leave", "go"], "antonyms": ["arrive"], "example": "The train is scheduled to depart from platform five in ten minutes."},
    "departure": {"phonetic": "/dɪˈpɑːrtʃər/", "pos": "n.", "meaning": "出發；離開", "phrases": ["departure lounge", "time of departure"], "synonyms": ["leaving", "exit"], "antonyms": ["arrival"], "example": "Please check the departure board for your flight information and gate number."},
    "diet": {"phonetic": "/ˈdaɪət/", "pos": "n./v.", "meaning": "飲食；節食", "phrases": ["balanced diet", "go on a diet"], "synonyms": ["nutrition", "food"], "antonyms": [], "example": "A healthy and balanced diet is essential for maintaining good health."},
    "dietician": {"phonetic": "/ˌdaɪəˈtɪʃn/", "pos": "n.", "meaning": "營養師", "phrases": ["registered dietician"], "synonyms": ["nutritionist"], "antonyms": [], "example": "The dietician recommended a low-fat diet to help the patient lose weight."},
    "downtown": {"phonetic": "/ˌdaʊnˈtaʊn/", "pos": "adj./adv./n.", "meaning": "市中心的", "phrases": ["downtown area", "go downtown"], "synonyms": ["city center"], "antonyms": ["suburbs"], "example": "Our new office is located in a modern building in the downtown area."},
    "entertain": {"phonetic": "/ˌentərˈteɪn/", "pos": "v.", "meaning": "招待；娛樂", "phrases": ["entertain guests", "entertaining"], "synonyms": ["host", "amuse"], "antonyms": ["bore"], "example": "We often entertain our international clients at fine restaurants in the city."},
    "examination": {"phonetic": "/ɪɡˌzæmɪˈneɪʃn/", "pos": "n.", "meaning": "檢查；考試", "phrases": ["medical examination", "entrance examination"], "synonyms": ["test", "inspection"], "antonyms": [], "example": "The doctor carried out a thorough physical examination of the patient."},
    "examinee": {"phonetic": "/ɪɡˌzæmɪˈniː/", "pos": "n.", "meaning": "應試者", "phrases": [], "synonyms": ["candidate"], "antonyms": ["examiner"], "example": "All examinees are required to show their ID cards before entering the room."},
    "examiner": {"phonetic": "/ɪɡˈzæmɪnər/", "pos": "n.", "meaning": "主考官；檢查員", "phrases": ["external examiner"], "synonyms": ["inspector"], "antonyms": ["examinee"], "example": "The examiner will explain the rules of the test before you begin writing."},
    "express": {"phonetic": "/ɪkˈspres/", "pos": "v./adj./n.", "meaning": "表達；快速的；快遞", "phrases": ["express mail", "express interest"], "synonyms": ["state", "fast"], "antonyms": ["slow"], "example": "If you need the documents urgently, we can send them by express mail."},
    "facilitator": {"phonetic": "/fəˈsɪlɪteɪtər/", "pos": "n.", "meaning": "協調者；促成者", "phrases": ["meeting facilitator"], "synonyms": ["coordinator"], "antonyms": [], "example": "The facilitator led the discussion and ensured that everyone had a chance to speak."},
    "ferry": {"phonetic": "/ˈferi/", "pos": "n./v.", "meaning": "渡輪", "phrases": ["passenger ferry", "ferry terminal"], "synonyms": ["boat", "ship"], "antonyms": [], "example": "The ferry carries passengers and vehicles across the bay every thirty minutes."},
    "field": {"phonetic": "/fiːld/", "pos": "n.", "meaning": "領域；田地", "phrases": ["field trip", "in the field of"], "synonyms": ["area", "specialty"], "antonyms": [], "example": "He is widely recognized as an expert in the field of renewable energy."},
    "a wheat field": {"phonetic": "/ə wiːt fiːld/", "pos": "n.", "meaning": "麥田", "phrases": [], "synonyms": [], "antonyms": [], "example": "The golden wheat field stretched as far as the eye could see."},
    "florist": {"phonetic": "/ˈflɔːrɪst/", "pos": "n.", "meaning": "花店人員；花商", "phrases": ["local florist"], "synonyms": [], "antonyms": [], "example": "I ordered a bouquet of roses from the florist for my wife's birthday."},
    "grain": {"phonetic": "/ɡreɪn/", "pos": "n.", "meaning": "穀物；顆粒", "phrases": ["whole grain", "grain of sand"], "synonyms": ["cereal"], "antonyms": [], "example": "The country is a major exporter of wheat, corn, and other types of grain."},
    "gratuity": {"phonetic": "/ɡrəˈtuːəti/", "pos": "n.", "meaning": "小費", "phrases": ["suggested gratuity", "included gratuity"], "synonyms": ["tip"], "antonyms": [], "example": "The restaurant adds a 15% gratuity to the bill for groups of six or more people."},
    "greenhouse": {"phonetic": "/ˈɡriːnhaʊs/", "pos": "n.", "meaning": "溫室", "phrases": ["greenhouse effect", "greenhouse gas"], "synonyms": ["glasshouse"], "antonyms": [], "example": "Plants that need warmer temperatures are grown in the company's greenhouse."},
    "grocer": {"phonetic": "/ˈɡroʊsər/", "pos": "n.", "meaning": "食品雜貨商", "phrases": ["local grocer"], "synonyms": [], "antonyms": [], "example": "Our local grocer sells fresh fruits and vegetables from nearby farms."},
    "groceries": {"phonetic": "/ˈɡroʊsəriz/", "pos": "n.", "meaning": "食品雜貨(複數)", "phrases": ["buy groceries", "grocery bag"], "synonyms": ["provisions"], "antonyms": [], "example": "We usually go to the supermarket to buy our weekly groceries on Saturdays."},
    "grocery": {"phonetic": "/ˈɡroʊsəri/", "pos": "n.", "meaning": "食品雜貨店", "phrases": ["grocery store"], "synonyms": ["supermarket"], "antonyms": [], "example": "The nearest grocery store is just a five-minute walk from my apartment."},
    "gymnasium": {"phonetic": "/dʒɪmˈneɪziəm/", "pos": "n.", "meaning": "體育館；健身房", "phrases": ["school gymnasium"], "synonyms": ["gym"], "antonyms": [], "example": "The new sports complex includes a large gymnasium and a swimming pool."},
    "incinerator": {"phonetic": "/ɪnˈsɪnəreɪtər/", "pos": "n.", "meaning": "焚化爐", "phrases": ["waste incinerator"], "synonyms": [], "antonyms": [], "example": "The city has invested in a modern incinerator to handle its domestic waste."},
    "indulgence": {"phonetic": "/ɪnˈdʌldʒəns/", "pos": "n.", "meaning": "放縱；嗜好", "phrases": ["self-indulgence"], "synonyms": ["gratification"], "antonyms": ["restraint"], "example": "Eating a large chocolate cake was a rare indulgence for him."},
    "itinerary": {"phonetic": "/aɪˈtɪnəreri/", "pos": "n.", "meaning": "行程；旅遊計畫", "phrases": ["travel itinerary", "detailed itinerary"], "synonyms": ["schedule", "agenda"], "antonyms": [], "example": "Please review your travel itinerary for the flight and hotel details."},
    "leaflet": {"phonetic": "/ˈliːflət/", "pos": "n.", "meaning": "傳單；小冊子", "phrases": ["hand out leaflets", "advertising leaflet"], "synonyms": ["pamphlet", "flyer"], "antonyms": [], "example": "The company distributed leaflets in the city center to promote its new service."},
    "legacy": {"phonetic": "/ˈleɡəsi/", "pos": "n.", "meaning": "遺產；遺留物", "phrases": ["leave a legacy", "cultural legacy"], "synonyms": ["inheritance", "heritage"], "antonyms": [], "example": "The former CEO left a legacy of innovation and excellence in the company."},
    "lounge": {"phonetic": "/laʊndʒ/", "pos": "n./v.", "meaning": "休息室；閒逛", "phrases": ["departure lounge", "airport lounge"], "synonyms": ["waiting room"], "antonyms": [], "example": "Passengers can wait for their flights in the comfortable departure lounge."},
    "luggage": {"phonetic": "/ˈlʌɡɪdʒ/", "pos": "n.", "meaning": "行李", "phrases": ["luggage tag", "excess luggage"], "synonyms": ["baggage"], "antonyms": [], "example": "The porter helped the guests carry their heavy luggage to their rooms."},
    "medium": {"phonetic": "/ˈmiːdiəm/", "pos": "n./adj.", "meaning": "媒介；中等的", "phrases": ["advertising medium", "medium size"], "synonyms": ["means", "average"], "antonyms": [], "example": "Television is still a very effective advertising medium for many companies."},
    "metropolitan": {"phonetic": "/ˌmetrəˈpɑːlɪtən/", "pos": "adj.", "meaning": "大都會的", "phrases": ["metropolitan area"], "synonyms": ["urban"], "antonyms": ["rural"], "example": "The metropolitan area has seen a rapid increase in population over the last decade."},
    "nationality": {"phonetic": "/ˌnæʃəˈnæləti/", "pos": "n.", "meaning": "國籍", "phrases": ["dual nationality", "of British nationality"], "synonyms": [], "antonyms": [], "example": "Please state your nationality and passport number on the application form."},
    "necessity": {"phonetic": "/nəˈsesəti/", "pos": "n.", "meaning": "必需品；必要性", "phrases": ["daily necessity", "of necessity"], "synonyms": ["essential", "requirement"], "antonyms": ["luxury"], "example": "The internet has become a necessity for most businesses in the modern world."},
    "occupation": {"phonetic": "/ˌɑːkjuˈpeɪʃn/", "pos": "n.", "meaning": "職業；佔用", "phrases": ["state your occupation", "current occupation"], "synonyms": ["job", "profession"], "antonyms": [], "example": "Please list your previous work experience and current occupation on your CV."},
    "outdoor": {"phonetic": "/ˈaʊtdɔːr/", "pos": "adj.", "meaning": "戶外的", "phrases": ["outdoor activities", "outdoor seating"], "synonyms": ["outside", "open-air"], "antonyms": ["indoor"], "example": "The restaurant has a lovely outdoor seating area that is perfect for summer."},
    "passenger": {"phonetic": "/ˈpæsɪndʒər/", "pos": "n.", "meaning": "乘客", "phrases": ["passenger train", "airline passenger"], "synonyms": ["traveler"], "antonyms": [], "example": "The flight was delayed, leaving hundreds of passengers stranded at the airport."},
    "perishable": {"phonetic": "/ˈperɪʃəbl/", "pos": "adj./n.", "meaning": "易腐壞的(食物)", "phrases": ["perishable goods", "highly perishable"], "synonyms": ["degradable"], "antonyms": ["non-perishable"], "example": "These perishable goods must be kept in a cold storage facility to stay fresh."},
    "pharmacist": {"phonetic": "/ˈfɑːrməsɪst/", "pos": "n.", "meaning": "藥劑師", "phrases": ["local pharmacist"], "synonyms": ["druggist"], "antonyms": [], "example": "The pharmacist explained how to take the medicine correctly and safely."},
    "photographer": {"phonetic": "/fəˈtɑːɡrəfər/", "pos": "n.", "meaning": "攝影師", "phrases": ["professional photographer"], "synonyms": [], "antonyms": [], "example": "The company hired a professional photographer to take pictures for its annual report."},
    "plug": {"phonetic": "/plʌɡ/", "pos": "n./v.", "meaning": "插頭；插上電源", "phrases": ["plug in", "electric plug"], "synonyms": [], "antonyms": ["unplug"], "example": "Make sure the power plug is properly connected before you turn on the machine."}
}

with open('data_green.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_5:
        item.update(enriched_data_5[word])

with open('data_green.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修第 201-250 個高品質單字，綠色等級已全部完成！")
