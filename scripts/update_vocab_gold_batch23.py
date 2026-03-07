import json

# 第 1101-1150 個高品質單字對應表 (金色等級)
enriched_data_gold_23 = {
    "legible": {"phonetic": "/ˈledʒəbl/", "pos": "adj.", "meaning": "清晰易讀的", "phrases": ["legible handwriting"], "synonyms": ["readable", "clear"], "antonyms": ["illegible"], "example": "Please ensure that your name and address are legible on the application form."},
    "optimal": {"phonetic": "/ˈɑːptɪməl/", "pos": "adj.", "meaning": "最理想的；最佳的", "phrases": ["optimal solution", "optimal performance"], "synonyms": ["best", "ideal"], "antonyms": ["worst"], "example": "The design was optimized to achieve the optimal balance between performance and cost."},
    "conducive": {"phonetic": "/kənˈduːsɪv/", "pos": "adj.", "meaning": "有助於...的", "phrases": ["conducive to success"], "synonyms": ["helpful", "beneficial"], "antonyms": ["unhelpful"], "example": "A quiet environment is conducive to concentration and productive work."},
    "enviable": {"phonetic": "/ˈenviəbl/", "pos": "adj.", "meaning": "令人羨慕的", "phrases": ["enviable position"], "synonyms": ["desirable"], "antonyms": ["unenviable"], "example": "The company has an enviable reputation for innovation and quality."},
    "occupancy": {"phonetic": "/ˈɑːkjəpənsi/", "pos": "n.", "meaning": "佔用；入住率", "phrases": ["occupancy rate"], "synonyms": ["tenancy", "possession"], "antonyms": ["vacancy"], "example": "The hotel has maintained a high occupancy rate throughout the peak summer season."},
    "condominium": {"phonetic": "/ˌkɑːndəˈmɪniəm/", "pos": "n.", "meaning": "公寓大樓；公寓房", "phrases": ["luxury condominium"], "synonyms": ["condo", "apartment"], "antonyms": [], "example": "They decided to buy a modern condominium in the city center near their office."},
    "dormitory": {"phonetic": "/ˈdɔːrmətɔːri/", "pos": "n.", "meaning": "宿舍", "phrases": ["university dormitory"], "synonyms": ["dorm", "residence hall"], "antonyms": [], "example": "Most of the international students live in the university dormitories during their first year."},
    "recipe": {"phonetic": "/ˈresəpi/", "pos": "n.", "meaning": "食譜；秘訣", "phrases": ["recipe for success"], "synonyms": ["formula", "method"], "antonyms": [], "example": "Strong leadership and teamwork are the secret recipe for the company's success."},
    "manage to": {"phonetic": "/ˈmænɪdʒ tuː/", "pos": "v. phr.", "meaning": "設法做到", "phrases": [], "synonyms": ["succeed in", "contrive"], "antonyms": ["fail to"], "example": "Despite the heavy traffic, we managed to arrive at the airport just in time."},
    "As if": {"phonetic": "/æz ɪf/", "pos": "conj. phr.", "meaning": "彷彿；好像", "phrases": [], "synonyms": ["as though"], "antonyms": [], "example": "He spoke as if he knew all the details of the project already."},
    "refined": {"phonetic": "/rɪˈfaɪnd/", "pos": "adj.", "meaning": "精煉的；文雅的；完善的", "phrases": ["refined oil", "refined manners"], "synonyms": ["polished", "elegant", "processed"], "antonyms": ["crude", "rough"], "example": "The design of the new model is more refined and sophisticated than the previous one."},
    "outreach": {"phonetic": "/ˈaʊtriːtʃ/", "pos": "n./v.", "meaning": "擴大服務範圍；外展活動", "phrases": ["community outreach"], "synonyms": [], "antonyms": [], "example": "The company's community outreach program provides funding for local schools."},
    "outage": {"phonetic": "/ˈaʊtɪdʒ/", "pos": "n.", "meaning": "中斷；停電", "phrases": ["power outage", "network outage"], "synonyms": ["failure", "breakdown"], "antonyms": [], "example": "The technical team is working to resolve the server outage as quickly as possible."},
    "fierce": {"phonetic": "/fɪrs/", "pos": "adj.", "meaning": "兇猛的；激烈的", "phrases": ["fierce competition"], "synonyms": ["intense", "ferocious"], "antonyms": ["gentle", "mild"], "example": "The company faces fierce competition from international rivals in the industry."},
    "lot": {"phonetic": "/lɑːt/", "pos": "n./pron.", "meaning": "一塊地；大量；籤", "phrases": ["parking lot", "a lot of"], "synonyms": ["plot", "batch"], "antonyms": [], "example": "The construction company is planning to build a new office complex on this empty lot."},
    "onset": {"phonetic": "/ˈɑːnset/", "pos": "n.", "meaning": "開始；(不愉快的事)發生", "phrases": ["the onset of winter"], "synonyms": ["beginning", "start", "outset"], "antonyms": ["end", "conclusion"], "example": "The early onset of the economic recession affected many small businesses."},
    "count on": {"phonetic": "/kaʊnt ɑːn/", "pos": "v. phr.", "meaning": "依靠；指望", "phrases": [], "synonyms": ["rely on", "depend on"], "antonyms": [], "example": "You can always count on our customer service team to provide helpful advice."},
    "biweekly": {"phonetic": "/baɪˈwiːkli/", "pos": "adj./adv.", "meaning": "每兩週一次的；一週兩次的", "phrases": ["biweekly meeting"], "synonyms": ["fortnightly"], "antonyms": [], "example": "The management holds a biweekly meeting to discuss the project's progress."},
    "studio apartment": {"phonetic": "/ˈstuːdioʊ əˈpɑːrtmənt/", "pos": "n. phr.", "meaning": "套房公寓；一居室公寓", "phrases": [], "synonyms": ["studio flat"], "antonyms": [], "example": "He rented a small studio apartment near the university while he was studying."},
    "prestigious": {"phonetic": "/preˈstɪdʒəs/", "pos": "adj.", "meaning": "有聲望的；受尊敬的", "phrases": ["prestigious award", "prestigious university"], "synonyms": ["renowned", "distinguished"], "antonyms": ["obscure", "unknown"], "example": "Winning the prestigious 'Innovator of the Year' award was a major achievement for the firm."},
    "ordinance": {"phonetic": "/ˈɔːrdɪnəns/", "pos": "n.", "meaning": "法令；條例", "phrases": ["city ordinance"], "synonyms": ["regulation", "law", "decree"], "antonyms": [], "example": "The local government passed a new ordinance to reduce noise levels in the city center."},
    "consciousness": {"phonetic": "/ˈkɑːnʃəsnəs/", "pos": "n.", "meaning": "意識；知覺", "phrases": ["environmental consciousness", "lose consciousness"], "synonyms": ["awareness"], "antonyms": ["unconsciousness"], "example": "The report aims to raise public consciousness about the importance of recycling."},
    "garment": {"phonetic": "/ˈɡɑːrmənt/", "pos": "n.", "meaning": "服裝", "phrases": ["garment industry"], "synonyms": ["clothing", "attire"], "antonyms": [], "example": "The company specializes in manufacturing high-quality garments for professional athletes."},
    "parade": {"phonetic": "/pəˈreɪd/", "pos": "n./v.", "meaning": "遊行；閱兵；展示", "phrases": ["victory parade"], "synonyms": ["procession", "display"], "antonyms": [], "example": "A large parade was held in the city center to celebrate the national holiday."},
    "spectacular": {"phonetic": "/spekˈtækjələr/", "pos": "adj./n.", "meaning": "壯觀的；極好的；精彩的演出", "phrases": ["spectacular view"], "synonyms": ["breathtaking", "amazing", "striking"], "antonyms": ["ordinary", "dull"], "example": "The new office building offers spectacular views of the mountains and the sea."},
    "light fixture": {"phonetic": "/laɪt ˈfɪkstʃər/", "pos": "n. phr.", "meaning": "燈具", "phrases": [], "synonyms": ["lamp", "luminaire"], "antonyms": [], "example": "The electrician is busy installing new energy-efficient light fixtures in the office."},
    "look through": {"phonetic": "/lʊk θruː/", "pos": "v. phr.", "meaning": "瀏覽；仔細查看", "phrases": ["look through a report"], "synonyms": ["examine", "scan", "review"], "antonyms": [], "example": "Please look through the training manual carefully before the workshop starts."},
    "make provision for": {"phonetic": "/meɪk prəˈvɪʒn fər/", "pos": "v. phr.", "meaning": "為...做準備；預留...", "phrases": [], "synonyms": ["prepare for"], "antonyms": [], "example": "The budget makes provision for any unexpected expenses that may arise."},
    "endorse": {"phonetic": "/ɪnˈdɔːrs/", "pos": "v.", "meaning": "背書；認可；代言", "phrases": ["endorse a check"], "synonyms": ["support", "approve", "sign"], "antonyms": ["oppose", "reject"], "example": "The board of directors unanimously decided to endorse the new investment plan."},
    "extinction": {"phonetic": "/ɪkˈstɪŋkʃn/", "pos": "n.", "meaning": "絕種；消滅", "phrases": ["on the verge of extinction"], "synonyms": ["destruction", "annihilation"], "antonyms": ["survival", "existence"], "example": "The organization works to protect endangered species from the threat of extinction."},
    "mandatory": {"phonetic": "/ˈmændətɔːri/", "pos": "adj.", "meaning": "強制的；義務的", "phrases": ["mandatory training"], "synonyms": ["compulsory", "required"], "antonyms": ["optional", "voluntary"], "example": "It is mandatory for all new employees to participate in the safety training session."},
    "halfway": {"phonetic": "/ˌhæfˈweɪ/", "pos": "adv./adj.", "meaning": "半途地；中途的", "phrases": ["meet halfway"], "synonyms": ["middle", "midway"], "antonyms": [], "example": "We are now halfway through the project and everything is on schedule."},
    "complex": {"phonetic": "/kəmˈpleks/ (adj.) /ˈkɑːmpleks/ (n.)", "pos": "adj./n.", "meaning": "複雜的；綜合建築物", "phrases": ["office complex", "complex issue"], "synonyms": ["complicated", "intricate", "compound"], "antonyms": ["simple"], "example": "The two companies are planning to build a large research complex in the city center."},
    "in conjunction with": {"phonetic": "/ɪn kənˈdʒʌŋkʃn wɪð/", "pos": "phr.", "meaning": "連同...；與...一起", "phrases": [], "synonyms": ["together with", "along with"], "antonyms": [], "example": "The marketing campaign was launched in conjunction with the new product release."},
    "in progress": {"phonetic": "/ɪn ˈprɑːɡres/", "pos": "phr.", "meaning": "進行中", "phrases": ["work in progress"], "synonyms": ["underway", "ongoing"], "antonyms": ["finished", "completed"], "example": "Repairs to the office building are currently in progress and should be finished by Friday."},
    "mandate": {"phonetic": "/ˈmændeɪt/", "pos": "n./v.", "meaning": "命令；授權；強制執行", "phrases": ["receive a mandate"], "synonyms": ["order", "command", "authorize"], "antonyms": [], "example": "The government has given the agency a clear mandate to improve public safety."},
    "aliment": {"phonetic": "/ˈælɪmənt/", "pos": "n./v.", "meaning": "食物；營養；給予養分", "phrases": [], "synonyms": ["food", "nourishment"], "antonyms": [], "example": "Proper aliment is essential for the health and growth of young children."},
    "detour": {"phonetic": "/ˈdiːtʊr/", "pos": "n./v.", "meaning": "繞道；迂迴路", "phrases": ["take a detour"], "synonyms": ["bypass", "deviation"], "antonyms": [], "example": "We had to take a detour because the main road was closed for roadwork."},
    "affair": {"phonetic": "/əˈfer/", "pos": "n.", "meaning": "事務；事件；私通", "phrases": ["current affairs", "foreign affairs"], "synonyms": ["matter", "event"], "antonyms": [], "example": "The minister is responsible for managing the country's domestic and foreign affairs."},
    "cinematography": {"phonetic": "/ˌsɪnəməˈtɑːɡrəfi/", "pos": "n.", "meaning": "電影製片術；攝影術", "phrases": ["best cinematography"], "synonyms": [], "antonyms": [], "example": "The film won an award for its spectacular cinematography and visual effects."},
    "honoree": {"phonetic": "/ˌɑːnəˈriː/", "pos": "n.", "meaning": "受獎者；領獎人", "phrases": [], "synonyms": ["recipient", "awardee"], "antonyms": [], "example": "The honoree gave a short speech expressing her gratitude to her colleagues."},
    "a bunch of": {"phonetic": "/ə bʌntʃ əv/", "pos": "phr.", "meaning": "一束；一群；大量", "phrases": ["a bunch of keys", "a bunch of flowers"], "synonyms": ["a lot of", "a group of"], "antonyms": [], "example": "He brought a large bunch of flowers to the office to celebrate the successful project."},
    "drop~off": {"phonetic": "/drɑːp ɔːf/", "pos": "v. phr.", "meaning": "放下(人/物)；減少；睡著", "phrases": ["drop off passengers"], "synonyms": ["deliver", "decline"], "antonyms": ["pick up"], "example": "I can drop you off at the station on my way to work tomorrow morning."},
    "brew": {"phonetic": "/bruː/", "pos": "v./n.", "meaning": "釀造；沖泡(茶/咖啡)；醞釀", "phrases": ["freshly brewed coffee"], "synonyms": ["infuse", "prepare"], "antonyms": [], "example": "The delicious aroma of freshly brewed coffee filled the entire staff room."},
    "immigration": {"phonetic": "/ˌɪmɪˈɡreɪʃn/", "pos": "n.", "meaning": "移民；入境管理", "phrases": ["immigration office", "illegal immigration"], "synonyms": ["migration"], "antonyms": ["emigration"], "example": "It took almost an hour to pass through immigration at the international airport."},
    "worked as": {"phonetic": "/wɜːrkt æz/", "pos": "v. phr.", "meaning": "擔任...職務", "phrases": [], "synonyms": ["served as"], "antonyms": [], "example": "He worked as a senior marketing manager for several years before joining our firm."},
    "docent": {"phonetic": "/ˈdoʊsnt/", "pos": "n.", "meaning": "導覽員；講師", "phrases": ["museum docent"], "synonyms": ["guide"], "antonyms": [], "example": "The docent provided an interesting tour of the art gallery for the group of students."},
    "freelancer": {"phonetic": "/ˈfriːlænsər/", "pos": "n.", "meaning": "自由職業者", "phrases": ["work as a freelancer"], "synonyms": ["independent contractor"], "antonyms": [], "example": "As a freelancer, she has the flexibility to choose her own projects and working hours."},
    "archetypal": {"phonetic": "/ˌɑːrkiˈtaɪpl/", "pos": "adj.", "meaning": "原型的；典型的", "phrases": [], "synonyms": ["typical", "classic"], "antonyms": ["unique"], "example": "The new office building is an archetypal example of modern urban architecture."},
    "reminisce": {"phonetic": "/ˌremɪˈnɪs/", "pos": "v.", "meaning": "回憶；緬懷", "phrases": ["reminisce about the past"], "synonyms": ["remember", "recall"], "antonyms": [], "example": "The former colleagues met for lunch to reminisce about their time working together."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_23:
        update_info = enriched_data_gold_23[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 1101-1150 個單字。")
