import json

# 第 351-400 個高品質單字對應表 (金色等級)
enriched_data_gold_8 = {
    "try out sth": {"phonetic": "/traɪ aʊt/", "pos": "v. phr.", "meaning": "試驗；試用", "phrases": ["try out a new product"], "synonyms": ["test", "experiment with"], "antonyms": [], "example": "We are planning to try out the new software before we buy it."},
    "a field test": {"phonetic": "/ə fiːld test/", "pos": "n. phr.", "meaning": "實地測試", "phrases": ["conduct a field test"], "synonyms": [], "antonyms": [], "example": "The engineering team is carrying out a field test of the new solar panels."},
    "boulevard": {"phonetic": "/ˈbʊləvɑːrd/", "pos": "n.", "meaning": "大道；林蔭大道", "phrases": ["main boulevard"], "synonyms": ["avenue", "street"], "antonyms": [], "example": "The new luxury hotel is located on one of the city's most famous boulevards."},
    "To Whom It May Concern": {"phonetic": "/tuː huːm ɪt meɪ kənˈsɜːrn/", "pos": "phr.", "meaning": "敬啟者(書信用語)", "phrases": [], "synonyms": [], "antonyms": [], "example": "\"To Whom It May Concern\" is a formal way to begin a letter when you don't know the recipient's name."},
    "home delivery": {"phonetic": "/hoʊm dɪˈlɪvəri/", "pos": "n. phr.", "meaning": "送貨到府", "phrases": ["free home delivery"], "synonyms": [], "antonyms": [], "example": "The supermarket offers free home delivery for orders over fifty dollars."},
    "bedding": {"phonetic": "/ˈbedɪŋ/", "pos": "n.", "meaning": "寢具", "phrases": ["cotton bedding"], "synonyms": ["bedclothes"], "antonyms": [], "example": "The store sells a wide range of high-quality bedding and bath towels."},
    "bulky": {"phonetic": "/ˈbʌlki/", "pos": "adj.", "meaning": "笨重的；龐大的", "phrases": ["bulky items"], "synonyms": ["unwieldy", "massive"], "antonyms": ["compact", "small"], "example": "Please be careful when moving bulky items like furniture and appliances."},
    "toiletries": {"phonetic": "/ˈtɔɪlətriz/", "pos": "n.", "meaning": "盥洗用品", "phrases": ["personal toiletries"], "synonyms": [], "antonyms": [], "example": "We provide complimentary toiletries such as soap and shampoo for all our guests."},
    "feast": {"phonetic": "/fiːst/", "pos": "n./v.", "meaning": "大餐；饗宴", "phrases": ["wedding feast"], "synonyms": ["banquet", "celebration"], "antonyms": [], "example": "The company held a magnificent feast to celebrate its tenth anniversary."},
    "champagne": {"phonetic": "/ʃæmˈpeɪn/", "pos": "n.", "meaning": "香檳", "phrases": ["a bottle of champagne"], "synonyms": [], "antonyms": [], "example": "They opened a bottle of champagne to toast the success of the new project."},
    "instructive": {"phonetic": "/ɪnˈstrʌktɪv/", "pos": "adj.", "meaning": "有啟發性的；有教育意義的", "phrases": ["instructive lesson"], "synonyms": ["informative", "educational"], "antonyms": ["uninformative"], "example": "The workshop was very instructive and provided many useful tips for our work."},
    "room for improvement": {"phonetic": "/ruːm fər ɪmˈpruːvmənt/", "pos": "n. phr.", "meaning": "進步空間", "phrases": [], "synonyms": [], "antonyms": [], "example": "The report was good, but the manager noted that there was still room for improvement."},
    "disguise": {"phonetic": "/dɪsˈɡaɪz/", "pos": "v./n.", "meaning": "偽裝；掩飾", "phrases": ["in disguise"], "synonyms": ["mask", "conceal"], "antonyms": ["reveal", "expose"], "example": "He tried to disguise his disappointment when he didn't get the promotion."},
    "avenue": {"phonetic": "/ˈævənjuː/", "pos": "n.", "meaning": "大道；途徑", "phrases": ["Fifth Avenue", "explore all avenues"], "synonyms": ["boulevard", "way"], "antonyms": [], "example": "The company is exploring every avenue to find a solution to the problem."},
    "front desk": {"phonetic": "/frʌnt desk/", "pos": "n. phr.", "meaning": "櫃檯", "phrases": ["check in at the front desk"], "synonyms": ["reception desk"], "antonyms": [], "example": "Please leave your room key at the front desk when you go out for the day."},
    "get through": {"phonetic": "/ɡet θruː/", "pos": "v. phr.", "meaning": "通過；接通(電話)；完成", "phrases": ["get through to someone"], "synonyms": ["connect", "finish"], "antonyms": [], "example": "I tried to call the office several times, but I couldn't get through."},
    "look into sth": {"phonetic": "/lʊk ˈɪntuː/", "pos": "v. phr.", "meaning": "調查；研究", "phrases": [], "synonyms": ["investigate", "examine"], "antonyms": [], "example": "The management has promised to look into the complaints about the poor service."},
    "on hand": {"phonetic": "/ɑːn hænd/", "pos": "adj. phr.", "meaning": "在手邊；在場", "phrases": ["staff on hand"], "synonyms": ["available", "present"], "antonyms": [], "example": "We always have technical experts on hand to assist customers with any problems."},
    "stick": {"phonetic": "/stɪk/", "pos": "v./n.", "meaning": "黏貼；堅持；棍棒", "phrases": ["stick to the plan"], "synonyms": ["adhere", "attach"], "antonyms": [], "example": "You need to stick the label onto the package before you send it."},
    "stick in sb's mind": {"phonetic": "/stɪk ɪn wʌnz maɪnd/", "pos": "v. phr.", "meaning": "銘記在心", "phrases": [], "synonyms": ["remember"], "antonyms": ["forget"], "example": "His inspiring speech during the conference really stuck in my mind."},
    "indignant": {"phonetic": "/ɪnˈdɪɡnənt/", "pos": "adj.", "meaning": "憤慨的", "phrases": ["feel indignant"], "synonyms": ["angry", "resentful"], "antonyms": ["pleased", "contented"], "example": "She was indignant about the way she had been treated by the manager."},
    "sarcastic": {"phonetic": "/sɑːrˈkæstɪk/", "pos": "adj.", "meaning": "諷刺的；挖苦的", "phrases": ["sarcastic remark"], "synonyms": ["ironic", "mocking"], "antonyms": ["sincere"], "example": "He made a sarcastic comment about the delay, which upset several colleagues."},
    "fluffy toys": {"phonetic": "/ˈflʌfi tɔɪz/", "pos": "n. phr.", "meaning": "毛絨玩具", "phrases": [], "synonyms": ["soft toys", "plushies"], "antonyms": [], "example": "The store has a large selection of fluffy toys and games for young children."},
    "subtotal": {"phonetic": "/ˈsʌbˌtoʊtl/", "pos": "n.", "meaning": "小計", "phrases": ["calculate the subtotal"], "synonyms": [], "antonyms": [], "example": "The subtotal for the office supplies was two hundred dollars, before taxes."},
    "grand total": {"phonetic": "/ɡrænd ˈtoʊtl/", "pos": "n. phr.", "meaning": "總計", "phrases": [], "synonyms": ["total amount"], "antonyms": [], "example": "The grand total for the entire project came to over one million dollars."},
    "wrap": {"phonetic": "/ræp/", "pos": "v./n.", "meaning": "包裝；纏繞", "phrases": ["gift wrap"], "synonyms": ["cover", "envelope"], "antonyms": ["unwrap"], "example": "Would you like me to wrap the gift for you before you take it?"},
    "a variety show": {"phonetic": "/ə vəˈraɪəti ʃoʊ/", "pos": "n. phr.", "meaning": "綜藝節目", "phrases": [], "synonyms": [], "antonyms": [], "example": "The TV station is launching a new variety show featuring famous singers and comedians."},
    "flop": {"phonetic": "/flɑːp/", "pos": "n./v.", "meaning": "失敗；砸鍋", "phrases": ["total flop"], "synonyms": ["failure", "disaster"], "antonyms": ["hit", "success"], "example": "The movie was a complete flop at the box office and lost millions of dollars."},
    "a box office flop": {"phonetic": "/ə bɑːks ˈɑːfɪs flɑːp/", "pos": "n. phr.", "meaning": "票房毒藥；失敗之作", "phrases": [], "synonyms": ["commercial failure"], "antonyms": ["box office hit"], "example": "Despite the big-name stars, the film turned out to be a box office flop."},
    "a box office hit": {"phonetic": "/ə bɑːks ˈɑːfɪs hɪt/", "pos": "n. phr.", "meaning": "票房大賣之作", "phrases": [], "synonyms": ["blockbuster", "commercial success"], "antonyms": ["box office flop"], "example": "The new action movie was a major box office hit worldwide last summer."},
    "big-name": {"phonetic": "/ˈbɪɡˌneɪm/", "pos": "adj.", "meaning": "著名的；大牌的", "phrases": ["big-name actors"], "synonyms": ["famous", "renowned"], "antonyms": ["unknown"], "example": "The music festival featured several big-name artists and local bands."},
    "staging": {"phonetic": "/ˈsteɪdʒɪŋ/", "pos": "n.", "meaning": "上演；搭架；籌劃", "phrases": ["staging a play"], "synonyms": ["production", "presentation"], "antonyms": [], "example": "The staging of the new musical was absolutely spectacular and received great reviews."},
    "host": {"phonetic": "/hoʊst/", "pos": "n./v.", "meaning": "主持人；主辦", "phrases": ["host a meeting", "talk show host"], "synonyms": ["presenter", "organize"], "antonyms": ["guest"], "example": "The city is preparing to host the international technology conference next year."},
    "land": {"phonetic": "/lænd/", "pos": "n./v.", "meaning": "陸地；著陸；獲得(職位等)", "phrases": ["land a job"], "synonyms": ["earth", "obtain", "arrive"], "antonyms": ["sea"], "example": "She was very happy to land a senior position at a major marketing firm."},
    "be/get in hot water": {"phonetic": "/bi ɪn hɑːt ˈwɔːtər/", "pos": "v. phr.", "meaning": "陷入麻煩", "phrases": [], "synonyms": ["be in trouble"], "antonyms": [], "example": "The manager got in hot water after he was caught using company funds for personal expenses."},
    "take over": {"phonetic": "/teɪk ˈoʊvər/", "pos": "v. phr.", "meaning": "接管；收購", "phrases": ["hostile takeover"], "synonyms": ["acquire", "seize"], "antonyms": ["surrender"], "example": "A larger corporation is planning to take over the local telecommunications company."},
    "mock": {"phonetic": "/mɑːk/", "pos": "v./adj.", "meaning": "嘲笑；模擬的", "phrases": ["mock exam"], "synonyms": ["tease", "imitate", "simulated"], "antonyms": ["praise", "real"], "example": "The students took a mock exam to prepare for the actual test next week."},
    "disregard": {"phonetic": "/ˌdɪsrɪˈɡɑːrd/", "pos": "v./n.", "meaning": "無視；忽視", "phrases": ["disregard safety rules"], "synonyms": ["ignore", "neglect"], "antonyms": ["consider", "heed"], "example": "Please disregard the previous email as it contained some incorrect information."},
    "withdraw": {"phonetic": "/wɪðˈdrɔː/", "pos": "v.", "meaning": "提款；撤回；撤退", "phrases": ["withdraw money"], "synonyms": ["extract", "remove", "cancel"], "antonyms": ["deposit", "insert"], "example": "The company decided to withdraw its support for the project after the recent scandal."},
    "lie with sb": {"phonetic": "/laɪ wɪð/", "pos": "v. phr.", "meaning": "責任在於(某人)", "phrases": [], "synonyms": [], "antonyms": [], "example": "The final decision on the merger lies with the board of directors."},
    "lie in sth": {"phonetic": "/laɪ ɪn/", "pos": "v. phr.", "meaning": "在於", "phrases": [], "synonyms": ["consist in"], "antonyms": [], "example": "The real problem lies in the lack of communication between the two departments."},
    "beat": {"phonetic": "/biːt/", "pos": "v./n.", "meaning": "打敗；節拍", "phrases": ["beat the competition"], "synonyms": ["defeat", "overcome"], "antonyms": ["lose to"], "example": "Our new marketing strategy helped us beat our main competitors in the local market."},
    "take legal action against sb": {"phonetic": "/teɪk ˈliːɡl ˈækʃn əˈɡenst/", "pos": "v. phr.", "meaning": "對...採取法律行動", "phrases": [], "synonyms": ["sue"], "antonyms": [], "example": "The company threatened to take legal action against the competitor for trademark infringement."},
    "sue": {"phonetic": "/suː/", "pos": "v.", "meaning": "控告；起訴", "phrases": ["sue for damages"], "synonyms": ["prosecute", "litigate"], "antonyms": [], "example": "The environmental group decided to sue the factory for polluting the local river."},
    "critic": {"phonetic": "/ˈkrɪtɪk/", "pos": "n.", "meaning": "評論家；批評者", "phrases": ["food critic", "harsh critic"], "synonyms": ["reviewer"], "antonyms": ["supporter"], "example": "The new movie received mixed reviews from film critics across the country."},
    "grant": {"phonetic": "/ɡrænt/", "pos": "n./v.", "meaning": "補助金；同意；授予", "phrases": ["government grant", "grant permission"], "synonyms": ["subsidy", "award", "allow"], "antonyms": ["refuse", "deny"], "example": "The university was awarded a large grant to conduct research into renewable energy."},
    "damages": {"phonetic": "/ˈdæmɪdʒɪz/", "pos": "n.", "meaning": "賠償金", "phrases": ["seek damages", "award damages"], "synonyms": ["compensation"], "antonyms": [], "example": "The court ordered the company to pay damages to the workers who were injured."},
    "obesity": {"phonetic": "/oʊˈbiːsəti/", "pos": "n.", "meaning": "肥胖(症)", "phrases": ["childhood obesity"], "synonyms": ["fatness"], "antonyms": ["thinness"], "example": "The government is launching a new campaign to tackle the problem of childhood obesity."},
    "decline": {"phonetic": "/dɪˈklaɪn/", "pos": "v./n.", "meaning": "下降；衰退；婉拒", "phrases": ["economic decline", "decline an invitation"], "synonyms": ["decrease", "refuse"], "antonyms": ["increase", "accept"], "example": "The company has seen a decline in profits for three consecutive quarters."},
    "register": {"phonetic": "/ˈredʒɪstər/", "pos": "v./n.", "meaning": "註冊；登記", "phrases": ["register for a course", "cash register"], "synonyms": ["enroll", "record"], "antonyms": [], "example": "All participants are required to register for the conference by the end of the month."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_8:
        update_info = enriched_data_gold_8[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 351-400 個單字。")
