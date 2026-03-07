import json

# 第 651-700 個高品質單字對應表 (金色等級)
enriched_data_gold_14 = {
    "near the curb": {"phonetic": "/nɪr ðə kɜːrb/", "pos": "phr.", "meaning": "靠近路緣", "phrases": [], "synonyms": [], "antonyms": [], "example": "Please park your car near the curb to allow other vehicles to pass."},
    "leaning against": {"phonetic": "/ˈliːnɪŋ əˈɡenst/", "pos": "v. phr.", "meaning": "靠在...上面", "phrases": [], "synonyms": [], "antonyms": [], "example": "The bicycle was leaning against the wall outside the shop."},
    "intersection": {"phonetic": "/ˌɪntərˈsekʃn/", "pos": "n.", "meaning": "交叉路口；十字路口", "phrases": ["busy intersection"], "synonyms": ["crossroads", "junction"], "antonyms": [], "example": "The new overpass has helped to reduce traffic congestion at the busy intersection."},
    "desert": {"phonetic": "/ˈdezərt/ (n.) /dɪˈzɜːrt/ (v.)", "pos": "n./v.", "meaning": "沙漠；拋棄", "phrases": ["Sahara Desert"], "synonyms": ["wasteland", "abandon"], "antonyms": ["forest"], "example": "The explorers had to carry plenty of water to survive in the hot desert."},
    "wheel": {"phonetic": "/wiːl/", "pos": "n./v.", "meaning": "輪子；方向盤；推動", "phrases": ["steering wheel", "behind the wheel"], "synonyms": [], "antonyms": [], "example": "The worker used a cart with four wheels to move the heavy boxes."},
    "porch": {"phonetic": "/pɔːrtʃ/", "pos": "n.", "meaning": "門廊；走廊", "phrases": ["front porch"], "synonyms": ["veranda", "patio"], "antonyms": [], "example": "We sat on the front porch and enjoyed the cool breeze in the evening."},
    "stir": {"phonetic": "/stɜːr/", "pos": "v./n.", "meaning": "攪拌；引起轟動", "phrases": ["stir up trouble"], "synonyms": ["mix", "agitate"], "antonyms": [], "example": "Please stir the soup constantly while it is heating on the stove."},
    "wander about": {"phonetic": "/ˈwɑːndər əˈbaʊt/", "pos": "v. phr.", "meaning": "漫步；閒逛", "phrases": [], "synonyms": ["roam", "stroll"], "antonyms": [], "example": "We spent the afternoon wandering about the historic city center."},
    "informative": {"phonetic": "/ɪnˈfɔːrmətɪv/", "pos": "adj.", "meaning": "提供資訊的；見聞廣博的", "phrases": ["informative presentation"], "synonyms": ["instructive", "educational"], "antonyms": ["uninformative"], "example": "The seminar was very informative and provided many useful insights into the market."},
    "developed nation": {"phonetic": "/dɪˈveləpt ˈneɪʃn/", "pos": "n. phr.", "meaning": "開發國家", "phrases": [], "synonyms": ["industrialized country"], "antonyms": ["developing nation"], "example": "Economic growth in developed nations has slowed down in recent years."},
    "principle": {"phonetic": "/ˈprɪnsəpl/", "pos": "n.", "meaning": "原則；原理", "phrases": ["basic principle", "in principle"], "synonyms": ["rule", "standard", "belief"], "antonyms": [], "example": "The company is based on the principles of honesty and transparency."},
    "campaign": {"phonetic": "/kæmˈpeɪn/", "pos": "n./v.", "meaning": "活動；運動；從事活動", "phrases": ["marketing campaign", "election campaign"], "synonyms": ["operation", "drive"], "antonyms": [], "example": "The company has launched a new campaign to promote its eco-friendly products."},
    "refurbish": {"phonetic": "/ˌriːˈfɜːrbɪʃ/", "pos": "v.", "meaning": "翻修；整修", "phrases": ["refurbish an office"], "synonyms": ["renovate", "remodel"], "antonyms": [], "example": "The management has decided to refurbish the old office building next month."},
    "top priority": {"phonetic": "/tɑːp praɪˈɔːrəti/", "pos": "n. phr.", "meaning": "當務之急；首要任務", "phrases": ["make something a top priority"], "synonyms": [], "antonyms": [], "example": "Improving customer service is our top priority for the coming year."},
    "get transferred to": {"phonetic": "/ɡet trænsˈfɜːrd tuː/", "pos": "v. phr.", "meaning": "被調職到...", "phrases": [], "synonyms": [], "antonyms": [], "example": "He was delighted to hear that he would get transferred to the New York office."},
    "conglomerate": {"phonetic": "/kənˈɡlɑːmərət/", "pos": "n.", "meaning": "企業集團", "phrases": ["multinational conglomerate"], "synonyms": ["group", "corporation"], "antonyms": [], "example": "The company has grown from a small family business into a massive global conglomerate."},
    "monitor": {"phonetic": "/ˈmɑːnɪtər/", "pos": "v./n.", "meaning": "監控；監視器", "phrases": ["monitor progress"], "synonyms": ["track", "observe", "screen"], "antonyms": ["ignore"], "example": "We need to monitor our competitors' marketing strategies very carefully."},
    "take advantage of": {"phonetic": "/teɪk ədˈvæntɪdʒ əv/", "pos": "v. phr.", "meaning": "利用；善用", "phrases": [], "synonyms": ["exploit", "utilize"], "antonyms": [], "example": "You should take advantage of the free training programs offered by the company."},
    "intern": {"phonetic": "/ˈɪntɜːrn/", "pos": "n./v.", "meaning": "實習生；實習", "phrases": ["unpaid intern"], "synonyms": ["apprentice", "trainee"], "antonyms": [], "example": "The marketing department is looking for an intern to help with social media."},
    "take place": {"phonetic": "/teɪk pleɪs/", "pos": "v. phr.", "meaning": "發生；舉行", "phrases": [], "synonyms": ["happen", "occur"], "antonyms": [], "example": "The annual shareholders' meeting will take place in the main conference room tomorrow."},
    "out of print": {"phonetic": "/aʊt əv prɪnt/", "pos": "adj. phr.", "meaning": "絕版", "phrases": [], "synonyms": ["unavailable"], "antonyms": ["in print"], "example": "I'm sorry, but that particular textbook is currently out of print."},
    "welfare": {"phonetic": "/ˈwelfer/", "pos": "n.", "meaning": "福利；社會救濟", "phrases": ["social welfare", "child welfare"], "synonyms": ["well-being", "benefit"], "antonyms": [], "example": "The government is increasing its spending on social welfare programs for the elderly."},
    "job fair": {"phonetic": "/dʒɑːb fer/", "pos": "n. phr.", "meaning": "就業博覽會", "phrases": ["attend a job fair"], "synonyms": ["career fair"], "antonyms": [], "example": "The university is organizing a job fair to help graduating students find employment."},
    "teleconference": {"phonetic": "/ˈtelikɑːnfərəns/", "pos": "n./v.", "meaning": "視訊會議；電話會議", "phrases": ["hold a teleconference"], "synonyms": ["video conference"], "antonyms": [], "example": "The manager held a teleconference with the international team to discuss the new project."},
    "hold off": {"phonetic": "/hoʊld ɔːf/", "pos": "v. phr.", "meaning": "延期；推遲", "phrases": ["hold off on a decision"], "synonyms": ["postpone", "delay"], "antonyms": ["proceed"], "example": "The company decided to hold off on the investment until the market stabilizes."},
    "make an offer": {"phonetic": "/meɪk ən ˈɔːfər/", "pos": "v. phr.", "meaning": "報價；出價", "phrases": [], "synonyms": ["propose", "bid"], "antonyms": [], "example": "We are planning to make an offer on the new office space later this week."},
    "hold A accountable for": {"phonetic": "/hoʊld əˈkaʊntəbl fər/", "pos": "v. phr.", "meaning": "要求 A 對...負責", "phrases": [], "synonyms": [], "antonyms": [], "example": "Shareholders will hold the board of directors accountable for the company's financial losses."},
    "by the time": {"phonetic": "/baɪ ðə taɪm/", "pos": "phr.", "meaning": "到...的時候", "phrases": [], "synonyms": [], "antonyms": [], "example": "By the time the manager arrived, the meeting had already started."},
    "be underway": {"phonetic": "/bi ˌʌndərˈweɪ/", "pos": "v. phr.", "meaning": "正在進行中", "phrases": [], "synonyms": ["in progress"], "antonyms": [], "example": "Construction of the new research facility is already underway and should be finished by next year."},
    "bankruptcy": {"phonetic": "/ˈbæŋkrʌptsi/", "pos": "n.", "meaning": "破產", "phrases": ["declare bankruptcy"], "synonyms": ["insolvency", "failure"], "antonyms": ["solvency"], "example": "Several small businesses were forced to declare bankruptcy during the economic crisis."},
    "gourmet": {"phonetic": "/ˈɡʊrmeɪ/", "pos": "n./adj.", "meaning": "美食家；美味的", "phrases": ["gourmet food", "gourmet restaurant"], "synonyms": ["epicure", "fine"], "antonyms": [], "example": "The hotel restaurant is famous for its delicious gourmet cuisine."},
    "tropical": {"phonetic": "/ˈtrɑːpɪkl/", "pos": "adj.", "meaning": "熱帶的", "phrases": ["tropical climate", "tropical fruit"], "synonyms": [], "antonyms": ["arctic", "temperate"], "example": "The island is known for its beautiful beaches and warm tropical climate."},
    "consortium": {"phonetic": "/kənˈsɔːrtiəm/", "pos": "n.", "meaning": "聯盟；財團", "phrases": ["international consortium"], "synonyms": ["syndicate", "alliance"], "antonyms": [], "example": "A consortium of international banks provided the funding for the massive construction project."},
    "on behalf of": {"phonetic": "/ɑːn bɪˈhæf əv/", "pos": "phr.", "meaning": "代表...", "phrases": [], "synonyms": ["representing"], "antonyms": [], "example": "The lawyer accepted the award on behalf of the environmental organization."},
    "call it a day": {"phonetic": "/kɔːl ɪt ə deɪ/", "pos": "v. phr.", "meaning": "收工；到此為止", "phrases": [], "synonyms": ["finish work", "stop"], "antonyms": [], "example": "It's already 7 PM, so let's call it a day and continue the discussion tomorrow morning."},
    "tremendous": {"phonetic": "/trəˈmendəs/", "pos": "adj.", "meaning": "極大的；極好的", "phrases": ["tremendous success", "tremendous pressure"], "synonyms": ["huge", "enormous", "excellent"], "antonyms": ["tiny", "slight"], "example": "The new marketing campaign has been a tremendous success, with sales doubling in just one month."},
    "session": {"phonetic": "/ˈseʃn/", "pos": "n.", "meaning": "會議；會期；學期", "phrases": ["training session", "in session"], "synonyms": ["meeting", "period"], "antonyms": [], "example": "All employees are required to participate in the upcoming safety training session."},
    "programmer": {"phonetic": "/ˈproʊɡræmər/", "pos": "n.", "meaning": "程式設計師", "phrases": ["computer programmer"], "synonyms": ["coder", "developer"], "antonyms": [], "example": "Our senior programmer is currently working on a new software update for the system."},
    "stop over": {"phonetic": "/stɑːp ˈoʊvər/", "pos": "v. phr.", "meaning": "中途停留", "phrases": [], "synonyms": ["stay over"], "antonyms": [], "example": "We decided to stop over in Tokyo for two days on our way to Europe."},
    "connecting flight": {"phonetic": "/kəˈnektɪŋ flaɪt/", "pos": "n. phr.", "meaning": "接駁班機", "phrases": ["miss a connecting flight"], "synonyms": [], "antonyms": ["direct flight"], "example": "I missed my connecting flight in London due to the delay of my first flight."},
    "garner": {"phonetic": "/ˈɡɑːrnər/", "pos": "v.", "meaning": "收集；獲得", "phrases": ["garner support"], "synonyms": ["collect", "gather", "obtain"], "antonyms": [], "example": "The new project has managed to garner a lot of interest from potential investors."},
    "resignation": {"phonetic": "/ˌrezɪɡˈneɪʃn/", "pos": "n.", "meaning": "辭職；辭呈", "phrases": ["submit a resignation"], "synonyms": [], "antonyms": [], "example": "The CEO's sudden resignation was a major shock to the entire company."},
    "on the verge of": {"phonetic": "/ɑːn ðə vɜːrdʒ əv/", "pos": "phr.", "meaning": "在...的邊緣；即將...", "phrases": ["on the verge of collapse"], "synonyms": ["on the brink of"], "antonyms": [], "example": "The company is on the verge of signing a major contract with an international client."},
    "advocate": {"phonetic": "/ˈædvəkət/ (n.) /ˈædvəkeɪt/ (v.)", "pos": "n./v.", "meaning": "擁護者；主張", "phrases": ["environmental advocate"], "synonyms": ["supporter", "promote"], "antonyms": ["opponent"], "example": "He is a strong advocate for renewable energy and has published several books on the topic."},
    "festive": {"phonetic": "/ˈfestɪv/", "pos": "adj.", "meaning": "節日的；喜慶的", "phrases": ["festive season", "festive mood"], "synonyms": ["joyful", "cheerful"], "antonyms": ["gloomy", "somber"], "example": "The city center is decorated with lights and decorations for the festive season."},
    "late fee": {"phonetic": "/leɪt fiː/", "pos": "n. phr.", "meaning": "滯納金；逾期費用", "phrases": ["charge a late fee"], "synonyms": ["penalty"], "antonyms": [], "example": "The bank charges a small late fee if you don't pay your credit card bill on time."},
    "representative": {"phonetic": "/ˌreprɪˈzentətɪv/", "pos": "n./adj.", "meaning": "代表；代理人；典型的", "phrases": ["sales representative"], "synonyms": ["agent", "delegate", "typical"], "antonyms": [], "example": "Our sales representative will visit your office tomorrow to demonstrate our new products."},
    "actively": {"phonetic": "/ˈæktɪvli/", "pos": "adv.", "meaning": "積極地；主動地", "phrases": ["actively looking for"], "synonyms": ["energetically", "vigorously"], "antonyms": ["passively", "indifferently"], "example": "The company is actively seeking new partners to expand its international operations."},
    "active": {"phonetic": "/ˈæktɪv/", "pos": "adj.", "meaning": "積極的；活躍的", "phrases": ["active member"], "synonyms": ["energetic", "busy"], "antonyms": ["inactive", "passive"], "example": "He is an active member of several professional organizations in the industry."},
    "immune": {"phonetic": "/ɪˈmjuːn/", "pos": "adj.", "meaning": "免疫的；免除的", "phrases": ["immune system"], "synonyms": ["resistant", "exempt"], "antonyms": ["susceptible"], "example": "No company is completely immune to the effects of a global economic downturn."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_14:
        update_info = enriched_data_gold_14[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 651-700 個單字。")
