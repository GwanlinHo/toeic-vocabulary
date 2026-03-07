import json

# 金色等級補漏第 3 部分
gap_fill_gold_3 = {
    "quotation": {"phonetic": "/kwoʊˈteɪʃn/", "pos": "n.", "meaning": "報價；引文", "phrases": ["written quotation"], "synonyms": ["estimate", "quote"], "antonyms": [], "example": "We received three different quotations for the office renovation project."},
    "reserve": {"phonetic": "/rɪˈzɜːrv/", "pos": "v./n.", "meaning": "預訂；保留；保護區", "phrases": ["reserve a table", "nature reserve"], "synonyms": ["book", "keep", "save"], "antonyms": ["release"], "example": "Please reserve a seat for me on the morning flight to New York."},
    "sector": {"phonetic": "/ˈsektər/", "pos": "n.", "meaning": "部門；領域；扇形", "phrases": ["public sector", "private sector", "technology sector"], "synonyms": ["segment", "area", "division"], "antonyms": [], "example": "The country's technology sector has seen rapid growth over the last decade."},
    "volatile": {"phonetic": "/ˈvɑːlətl/", "pos": "adj.", "meaning": "不穩定的；易變的；揮發性的", "phrases": ["volatile market"], "synonyms": ["unstable", "unpredictable"], "antonyms": ["stable", "constant"], "example": "The stock market remained highly volatile throughout the day due to political news."},
    "fare": {"phonetic": "/fer/", "pos": "n./v.", "meaning": "車費；餐點；進展", "phrases": ["bus fare", "air fare"], "synonyms": ["charge", "price"], "antonyms": [], "example": "The local government has announced a small increase in bus fares starting next month."},
    "a one-way fare": {"phonetic": "/ə wʌnˈweɪ fer/", "pos": "n. phr.", "meaning": "單程票價", "phrases": [], "synonyms": ["single fare"], "antonyms": ["round-trip fare"], "example": "A one-way fare to the city center costs five dollars on the express train."},
    "a round-trip fare": {"phonetic": "/ə ˌraʊndˈtrɪp fer/", "pos": "n. phr.", "meaning": "來回票價", "phrases": [], "synonyms": ["return fare"], "antonyms": ["one-way fare"], "example": "The airline is offering a special round-trip fare for travel during the holiday season."},
    "dairy": {"phonetic": "/ˈderi/", "pos": "n./adj.", "meaning": "乳製品；乳製的", "phrases": ["dairy product", "dairy farm"], "synonyms": [], "antonyms": [], "example": "Many supermarkets now offer a wide selection of organic dairy products."},
    "stormy": {"phonetic": "/ˈstɔːrmi/", "pos": "adj.", "meaning": "暴風雨的；激烈的", "phrases": ["stormy weather", "stormy meeting"], "synonyms": ["turbulent", "tempestuous"], "antonyms": ["calm", "peaceful"], "example": "The outdoor event was canceled because of the stormy weather forecast."},
    "hectare": {"phonetic": "/ˈhekter/", "pos": "n.", "meaning": "公頃", "phrases": [], "synonyms": [], "antonyms": [], "example": "The new nature reserve covers an area of over five hundred hectares."},
    "wipe out": {"phonetic": "/waɪp aʊt/", "pos": "v. phr.", "meaning": "徹底毀滅；擦去；消滅", "phrases": ["wipe out debts"], "synonyms": ["destroy", "eliminate", "eradicate"], "antonyms": ["create", "save"], "example": "The flood managed to wipe out all the crops in the low-lying areas of the region."},
    "a further +數字+複數名詞": {"word": "a further", "phonetic": "/ə ˈfɜːrðər/", "pos": "phr.", "meaning": "另外的...；進一步的...", "phrases": [], "synonyms": ["an additional"], "antonyms": [], "example": "The project will require a further ten months to complete according to the new plan."},
    "poultry": {"phonetic": "/ˈpoʊltri/", "pos": "n.", "meaning": "家禽", "phrases": ["poultry farm"], "synonyms": ["fowl"], "antonyms": [], "example": "The government has introduced new regulations regarding the health and safety of poultry."},
    "urge": {"phonetic": "/ɜːrdʒ/", "pos": "v./n.", "meaning": "敦促；催促；衝動", "phrases": ["urge someone to do something"], "synonyms": ["press", "encourage", "desire"], "antonyms": ["deter", "discourage"], "example": "The manager urged all employees to follow the new safety procedures at all times."},
    "overproduction": {"phonetic": "/ˌoʊvərprəˈdʌkʃn/", "pos": "n.", "meaning": "過度生產；生產過剩", "phrases": [], "synonyms": ["surplus"], "antonyms": ["shortage"], "example": "Overproduction has led to a significant drop in the market price of the commodity."},
    "in terms of": {"phonetic": "/ɪn tɜːrmz əv/", "pos": "phr.", "meaning": "在...方面；就...而言", "phrases": [], "synonyms": ["regarding", "with respect to"], "antonyms": [], "example": "The company's performance has improved significantly in terms of international sales."},
    "severe": {"phonetic": "/sɪˈvɪr/", "pos": "adj.", "meaning": "嚴重的；嚴格的；嚴厲的", "phrases": ["severe weather", "severe punishment"], "synonyms": ["serious", "harsh", "strict"], "antonyms": ["mild", "gentle", "slight"], "example": "The region has experienced severe droughts over the last several years."},
    "lift": {"phonetic": "/lɪft/", "pos": "v./n.", "meaning": "舉起；解除；搭便車；電梯(常用於英式)", "phrases": ["lift a ban", "give someone a lift"], "synonyms": ["raise", "remove", "elevator"], "antonyms": ["lower", "drop"], "example": "The government has decided to lift the trade embargo on the country."},
    "be referred to as": {"phonetic": "/bi rɪˈfɜːrd tuː æz/", "pos": "v. phr.", "meaning": "被稱為...", "phrases": [], "synonyms": ["be called", "be known as"], "antonyms": [], "example": "This type of marketing strategy is often referred to as a 'guerrilla' campaign."},
    "precious": {"phonetic": "/ˈpreʃəs/", "pos": "adj.", "meaning": "珍貴的；寶貴的", "phrases": ["precious stone", "precious metal"], "synonyms": ["valuable", "priceless"], "antonyms": ["worthless", "cheap"], "example": "The museum features a large collection of precious jewels and artifacts."},
    "wealthy": {"phonetic": "/ˈwelθi/", "pos": "adj.", "meaning": "富有的；富裕的", "phrases": ["wealthy family"], "synonyms": ["rich", "affluent"], "antonyms": ["poor", "impoverished"], "example": "Many wealthy investors are interested in funding the new technology startup."},
    "cause a sensation": {"phonetic": "/kɔːz ə senˈseɪʃn/", "pos": "v. phr.", "meaning": "引起轟動", "phrases": [], "synonyms": ["create a stir"], "antonyms": [], "example": "The news of the sudden merger caused a sensation in the international business world."},
    "prevailing": {"phonetic": "/prɪˈveɪlɪŋ/", "pos": "adj.", "meaning": "流行的；盛行的；主要的", "phrases": ["prevailing wind", "prevailing attitude"], "synonyms": ["current", "dominant", "popular"], "antonyms": [], "example": "The company's new strategy is based on the prevailing trends in the global market."},
    "prosper": {"phonetic": "/ˈprɑːspər/", "pos": "v.", "meaning": "繁榮；成功；興旺", "phrases": [], "synonyms": ["flourish", "thrive", "succeed"], "antonyms": ["fail", "decline"], "example": "Small businesses can prosper if they focus on providing excellent customer service."},
    "hindrance": {"phonetic": "/ˈhɪndrəns/", "pos": "n.", "meaning": "障礙；阻礙物", "phrases": ["be a hindrance to"], "synonyms": ["obstacle", "barrier"], "antonyms": ["help", "aid", "advantage"], "example": "Lack of funding has proven to be a major hindrance to the progress of the research project."},
    "miracle": {"phonetic": "/ˈmɪrəkl/", "pos": "n.", "meaning": "奇蹟", "phrases": ["miracle drug", "economic miracle"], "synonyms": ["wonder"], "antonyms": [], "example": "The company's rapid growth over the last year is considered a minor miracle in the industry."},
    "landmark": {"phonetic": "/ˈlændmɑːrk/", "pos": "n./adj.", "meaning": "地標；里程碑；具里程碑意義的", "phrases": ["landmark decision", "historical landmark"], "synonyms": ["milestone", "monument"], "antonyms": [], "example": "The signing of the treaty was a landmark event in the history of international relations."},
    "confrontation": {"phonetic": "/ˌkɑːnfrənˈteɪʃn/", "pos": "n.", "meaning": "對抗；對峙", "phrases": ["avoid confrontation"], "synonyms": ["conflict", "clash"], "antonyms": ["agreement", "harmony"], "example": "The union leaders are trying to resolve the dispute without further confrontation with management."},
    "confront": {"phonetic": "/kənˈfrʌnt/", "pos": "v.", "meaning": "面對；對抗", "phrases": ["confront a problem"], "synonyms": ["face", "encounter"], "antonyms": ["avoid", "evade"], "example": "The manager decided to confront the employee about her recurring lateness."},
    "biography": {"phonetic": "/baɪˈɑːɡrəfi/", "pos": "n.", "meaning": "傳記", "phrases": ["official biography"], "synonyms": ["life story"], "antonyms": [], "example": "He decided to write a biography of the company's founder to celebrate its fiftieth anniversary."},
    "discourage": {"phonetic": "/dɪˈskɜːrɪdʒ/", "pos": "v.", "meaning": "勸阻；使氣餒", "phrases": ["discourage from doing something"], "synonyms": ["deter", "dissuade"], "antonyms": ["encourage", "persuade"], "example": "The high cost of living in the city may discourage young professionals from moving there."},
    "interfere in": {"phonetic": "/ˌɪntərˈfɪr ɪn/", "pos": "v. phr.", "meaning": "干涉；介入", "phrases": [], "synonyms": ["meddle in"], "antonyms": [], "example": "The government promised not to interfere in the internal affairs of the company."},
    "compliment sb on sth": {"phonetic": "/ˈkɑːmplɪment ˈsʌmbədi ɑːn/", "pos": "v. phr.", "meaning": "稱讚某人某事", "phrases": [], "synonyms": ["praise for"], "antonyms": ["criticize for"], "example": "The manager complimented the team on their hard work and dedication to the project."},
    "punctual": {"phonetic": "/ˈpʌŋktʃuəl/", "pos": "adj.", "meaning": "準時的", "phrases": ["be punctual for"], "synonyms": ["on time", "prompt"], "antonyms": ["late", "tardy"], "example": "It is important to be punctual for meetings to show respect for everyone's time."},
    "dependable": {"phonetic": "/dɪˈpendəbl/", "pos": "adj.", "meaning": "可靠的；可信任的", "phrases": ["dependable person"], "synonyms": ["reliable", "trustworthy"], "antonyms": ["unreliable", "undependable"], "example": "We are looking for a dependable person to manage the office while the manager is away."},
    "clock in/out": {"phonetic": "/klɑːk ɪn/", "pos": "v. phr.", "meaning": "上下班打卡", "phrases": [], "synonyms": ["punch in/out"], "antonyms": [], "example": "Employees are required to clock in as soon as they arrive at the factory in the morning."},
    "factory floor": {"phonetic": "/ˈfæktri flɔːr/", "pos": "n. phr.", "meaning": "工廠車間", "phrases": ["working on the factory floor"], "synonyms": ["shop floor"], "antonyms": [], "example": "The manager spent the whole morning visiting the workers on the factory floor."},
    "regularly scheduled section meetings": {"phonetic": "/ˈreɡjələrli ˈskedʒuːld ˈsekʃn ˈmiːtɪŋz/", "pos": "n. phr.", "meaning": "定期部門會議", "phrases": [], "synonyms": [], "antonyms": [], "example": "All staff members are expected to attend the regularly scheduled section meetings every Monday morning."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in gap_fill_gold_3:
        update_info = gap_fill_gold_3[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("完成金色等級補漏第 3 部分 (Quotation 到 Regularly scheduled section meetings)。")
