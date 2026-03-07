import json

# 第 151-200 個高品質單字對應表 (綠色等級)
enriched_data_4 = {
    "revive": {"phonetic": "/rɪˈvaɪv/", "pos": "v.", "meaning": "復興；使甦醒", "phrases": ["revive the economy", "revive interest"], "synonyms": ["restore", "renew"], "antonyms": ["suppress"], "example": "The company's new marketing strategy is expected to revive its declining sales."},
    "rule": {"phonetic": "/ruːl/", "pos": "n./v.", "meaning": "規則；統治", "phrases": ["as a rule", "rule out"], "synonyms": ["regulation", "law"], "antonyms": [], "example": "As a general rule, all employees should be at their desks by 9 AM."},
    "rush": {"phonetic": "/rʌʃ/", "pos": "v./n.", "meaning": "衝；匆忙", "phrases": ["rush hour", "in a rush"], "synonyms": ["hurry", "dash"], "antonyms": ["stroll"], "example": "Please do not rush the project; we need to ensure everything is correct."},
    "salvage": {"phonetic": "/ˈsælvɪdʒ/", "pos": "v./n.", "meaning": "搶救；挽回", "phrases": ["salvage operation", "salvage a reputation"], "synonyms": ["rescue", "save"], "antonyms": ["abandon"], "example": "The company is trying to salvage what it can from the failed merger."},
    "satisfy": {"phonetic": "/ˈsætɪsfaɪ/", "pos": "v.", "meaning": "使滿意；符合(要求)", "phrases": ["satisfy requirements", "highly satisfied"], "synonyms": ["content", "fulfill"], "antonyms": ["dissatisfy"], "example": "The new design aims to satisfy the growing demands of our customers."},
    "scratch": {"phonetic": "/skrætʃ/", "pos": "n./v.", "meaning": "抓痕；從零開始", "phrases": ["start from scratch", "up to scratch"], "synonyms": ["scrape"], "antonyms": [], "example": "We had to start the whole project from scratch after the data was lost."},
    "season": {"phonetic": "/ˈsiːzn/", "pos": "n.", "meaning": "季節；旺季", "phrases": ["peak season", "off season"], "synonyms": ["period"], "antonyms": [], "example": "Hotel rates are much higher during the peak tourist season."},
    "section": {"phonetic": "/ˈsekʃn/", "pos": "n.", "meaning": "部分；部門", "phrases": ["cross section", "smoking section"], "synonyms": ["part", "division"], "antonyms": ["whole"], "example": "Please complete the personal information section of the application form."},
    "seek": {"phonetic": "/siːk/", "pos": "v.", "meaning": "尋找；追求", "phrases": ["seek help", "seek employment"], "synonyms": ["search for", "look for"], "antonyms": [], "example": "The company is currently seeking a new manager for its overseas branch."},
    "sense": {"phonetic": "/sens/", "pos": "n./v.", "meaning": "感官；意識到", "phrases": ["make sense", "common sense"], "synonyms": ["feeling", "perception"], "antonyms": [], "example": "It makes sense to postpone the meeting until we have all the data."},
    "separate": {"phonetic": "/ˈseprət/", "pos": "adj./v.", "meaning": "分開的；分隔", "phrases": ["separate room", "keep separate"], "synonyms": ["detached", "divide"], "antonyms": ["connected", "join"], "example": "Please keep the business expenses separate from your personal ones."},
    "shape": {"phonetic": "/ʃeɪp/", "pos": "n./v.", "meaning": "形狀；塑造", "phrases": ["in good shape", "take shape"], "synonyms": ["form", "condition"], "antonyms": [], "example": "The new project is finally beginning to take shape after months of planning."},
    "signify": {"phonetic": "/ˈsɪɡnɪfaɪ/", "pos": "v.", "meaning": "表示；意味著", "phrases": ["signify approval", "signify importance"], "synonyms": ["indicate", "mean"], "antonyms": [], "example": "A nod of the head usually signifies agreement in many cultures."},
    "skirt": {"phonetic": "/skɜːrt/", "pos": "n./v.", "meaning": "裙子；繞開", "phrases": ["skirt the issue", "mini skirt"], "synonyms": ["avoid", "bypass"], "antonyms": ["confront"], "example": "The manager tried to skirt the issue of pay raises during the meeting."},
    "space": {"phonetic": "/speɪs/", "pos": "n.", "meaning": "空間；空位", "phrases": ["office space", "storage space"], "synonyms": ["room", "area"], "antonyms": [], "example": "We need to find a larger office space to accommodate our growing team."},
    "solicit": {"phonetic": "/səˈlɪsɪt/", "pos": "v.", "meaning": "懇求；徵求", "phrases": ["solicit feedback", "solicit donations"], "synonyms": ["request", "seek"], "antonyms": [], "example": "The company is soliciting feedback from its customers about the new service."},
    "solace": {"phonetic": "/ˈsɑːləs/", "pos": "n./v.", "meaning": "安慰；慰藉", "phrases": ["find solace in", "offer solace"], "synonyms": ["comfort", "consolation"], "antonyms": ["distress"], "example": "He found solace in his work after the loss of his father."},
    "additive": {"phonetic": "/ˈædətɪv/", "pos": "n.", "meaning": "添加劑", "phrases": ["food additive", "fuel additive"], "synonyms": ["addition"], "antonyms": [], "example": "The company uses natural additives instead of chemicals in its products."},
    "airways": {"phonetic": "/ˈerweɪz/", "pos": "n.", "meaning": "航線；航空公司", "phrases": ["international airways"], "synonyms": ["airline"], "antonyms": [], "example": "British Airways is one of the largest airlines in the world."},
    "aisle": {"phonetic": "/aɪl/", "pos": "n.", "meaning": "走道", "phrases": ["aisle seat", "walk down the aisle"], "synonyms": ["passageway", "corridor"], "antonyms": [], "example": "Would you prefer an aisle seat or a window seat for your flight?"},
    "alleviate": {"phonetic": "/əˈliːvieɪt/", "pos": "v.", "meaning": "減輕；緩和", "phrases": ["alleviate pain", "alleviate poverty"], "synonyms": ["ease", "relieve"], "antonyms": ["aggravate", "worsen"], "example": "The new bridge was built to alleviate the traffic congestion in the city center."},
    "altitude": {"phonetic": "/ˈæltɪtuːd/", "pos": "n.", "meaning": "高度；海拔", "phrases": ["high altitude", "cruising altitude"], "synonyms": ["height", "elevation"], "antonyms": [], "example": "The plane reached its cruising altitude of 35,000 feet."},
    "anchor": {"phonetic": "/ˈæŋkər/", "pos": "n./v.", "meaning": "錨；主播；固定", "phrases": ["news anchor", "drop anchor"], "synonyms": ["fix", "secure"], "antonyms": [], "example": "The news anchor reported the story on the evening broadcast."},
    "apparel": {"phonetic": "/əˈpærəl/", "pos": "n.", "meaning": "衣服；服裝", "phrases": ["sports apparel", "ready-to-wear apparel"], "synonyms": ["clothing", "garments"], "antonyms": [], "example": "The store specializes in high-quality outdoor apparel and equipment."},
    "appealing": {"phonetic": "/əˈpiːlɪŋ/", "pos": "adj.", "meaning": "有吸引力的", "phrases": ["visually appealing", "appealing offer"], "synonyms": ["attractive", "inviting"], "antonyms": ["repulsive", "unattractive"], "example": "The company's new website design is very visually appealing."},
    "appearance": {"phonetic": "/əˈpɪrəns/", "pos": "n.", "meaning": "外觀；出現", "phrases": ["personal appearance", "make an appearance"], "synonyms": ["look", "emergence"], "antonyms": ["disappearance"], "example": "The CEO made a brief appearance at the annual staff party."},
    "attendant": {"phonetic": "/əˈtendənt/", "pos": "n.", "meaning": "服務人員", "phrases": ["flight attendant", "parking attendant"], "synonyms": ["assistant", "helper"], "antonyms": [], "example": "The flight attendant served drinks and snacks to the passengers."},
    "auction": {"phonetic": "/ˈɔːkʃn/", "pos": "n./v.", "meaning": "拍賣", "phrases": ["online auction", "put up for auction"], "synonyms": ["public sale"], "antonyms": [], "example": "The antique furniture was sold at an auction for a record price."},
    "audience": {"phonetic": "/ˈɔːdiəns/", "pos": "n.", "meaning": "觀眾；聽眾", "phrases": ["target audience", "live audience"], "synonyms": ["spectators", "listeners"], "antonyms": [], "example": "The speaker kept the audience engaged throughout the entire presentation."},
    "audio": {"phonetic": "/ˈɔːdioʊ/", "pos": "n./adj.", "meaning": "音訊", "phrases": ["audio equipment", "audio-visual"], "synonyms": ["sound"], "antonyms": ["visual"], "example": "Please check the audio settings on your computer if you cannot hear the sound."},
    "automobile": {"phonetic": "/ˈɔːtəməbiːl/", "pos": "n.", "meaning": "汽車", "phrases": ["automobile industry", "automobile insurance"], "synonyms": ["car", "vehicle"], "antonyms": [], "example": "The company is a leading manufacturer in the global automobile industry."},
    "baggage": {"phonetic": "/ˈbæɡɪdʒ/", "pos": "n.", "meaning": "行李", "phrases": ["baggage claim", "excess baggage"], "synonyms": ["luggage"], "antonyms": [], "example": "Please collect your checked baggage from the carousel in the arrival hall."},
    "banquet": {"phonetic": "/ˈbæŋkwɪt/", "pos": "n.", "meaning": "宴會", "phrases": ["awards banquet", "banquet hall"], "synonyms": ["feast", "dinner"], "antonyms": [], "example": "The company held a lavish banquet to celebrate its 50th anniversary."},
    "bargain": {"phonetic": "/ˈbɑːrɡən/", "pos": "n./v.", "meaning": "便宜貨；討價還價", "phrases": ["real bargain", "bargain hunter"], "synonyms": ["deal", "negotiate"], "antonyms": [], "example": "This designer jacket was a real bargain at only fifty dollars."},
    "beverage": {"phonetic": "/ˈbevərɪdʒ/", "pos": "n.", "meaning": "飲料", "phrases": ["alcoholic beverage", "hot beverage"], "synonyms": ["drink"], "antonyms": [], "example": "The flight attendant will be serving hot and cold beverages shortly."},
    "board": {"phonetic": "/bɔːrd/", "pos": "n./v.", "meaning": "董事會；木板；登機", "phrases": ["board of directors", "board a plane"], "synonyms": ["committee", "get on"], "antonyms": ["disembark"], "example": "The board of directors is meeting today to discuss the merger proposal."},
    "book": {"phonetic": "/bʊk/", "pos": "v./n.", "meaning": "預訂；書", "phrases": ["book a flight", "fully booked"], "synonyms": ["reserve"], "antonyms": ["cancel"], "example": "You should book your hotel room well in advance during the peak season."},
    "broadcast": {"phonetic": "/ˈbrɔːdkæst/", "pos": "v./n.", "meaning": "廣播；播放", "phrases": ["live broadcast", "news broadcast"], "synonyms": ["air", "transmit"], "antonyms": [], "example": "The championship game will be broadcast live to millions of viewers worldwide."},
    "brochure": {"phonetic": "/broʊˈʃʊr/", "pos": "n.", "meaning": "宣傳手冊", "phrases": ["travel brochure", "product brochure"], "synonyms": ["pamphlet", "booklet"], "antonyms": [], "example": "You can find more information about our services in this colorful brochure."},
    "cab": {"phonetic": "/kæb/", "pos": "n.", "meaning": "計程車", "phrases": ["take a cab", "cab driver"], "synonyms": ["taxi"], "antonyms": [], "example": "It's raining outside, so I think I'll take a cab to the airport."},
    "carpet": {"phonetic": "/ˈkɑːrpɪt/", "pos": "n./v.", "meaning": "地毯", "phrases": ["wall-to-wall carpet", "red carpet"], "synonyms": ["rug"], "antonyms": [], "example": "We need to have the office carpet cleaned before the important meeting."},
    "cart": {"phonetic": "/kɑːrt/", "pos": "n./v.", "meaning": "手推車", "phrases": ["shopping cart", "luggage cart"], "synonyms": ["trolley"], "antonyms": [], "example": "Please return your shopping cart to the designated area after use."},
    "cart about": {"phonetic": "/kɑːrt əˈbaʊt/", "pos": "v.", "meaning": "搬運", "phrases": [], "synonyms": ["carry around"], "antonyms": [], "example": "He had to cart about heavy boxes all day during the office move."},
    "In case": {"phonetic": "/ɪn keɪs/", "pos": "conj.", "meaning": "以防萬一", "phrases": ["just in case"], "synonyms": [], "antonyms": [], "example": "Take an umbrella with you just in case it rains this afternoon."},
    "In any case": {"phonetic": "/ɪn ˈeni keɪs/", "pos": "adv.", "meaning": "無論如何", "phrases": [], "synonyms": ["anyway", "regardless"], "antonyms": [], "example": "The flight might be delayed, but in any case, we should get to the airport on time."},
    "cast": {"phonetic": "/kæst/", "pos": "n./v.", "meaning": "演員陣容；投射", "phrases": ["cast a vote", "all-star cast"], "synonyms": ["actors", "throw"], "antonyms": [], "example": "The movie features an all-star cast of award-winning actors."},
    "cater": {"phonetic": "/ˈkeɪtər/", "pos": "v.", "meaning": "提供飲食；迎合(需求)", "phrases": ["cater for", "catering service"], "synonyms": ["provide", "serve"], "antonyms": [], "example": "The hotel can cater for large groups of people for business conferences."},
    "chain": {"phonetic": "/tʃeɪn/", "pos": "n.", "meaning": "鏈條；連鎖店", "phrases": ["supply chain", "supermarket chain"], "synonyms": ["series", "network"], "antonyms": [], "example": "The company operates a large chain of coffee shops across the country."},
    "chop": {"phonetic": "/tʃɑːp/", "pos": "v.", "meaning": "砍；切", "phrases": ["chop up"], "synonyms": ["cut", "slice"], "antonyms": [], "example": "The chef is busy chopping up vegetables for the evening meal."},
    "collectible": {"phonetic": "/kəˈlektəbl/", "pos": "n./adj.", "meaning": "收藏品；值得收藏的", "phrases": ["rare collectible"], "synonyms": ["collector's item"], "antonyms": [], "example": "These limited-edition stamps are highly sought after by collectors as rare collectibles."}
}

with open('data_green.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_4:
        item.update(enriched_data_4[word])

with open('data_green.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修第 151-200 個高品質單字。")
