import json

# 第 701-750 個高品質單字對應表 (金色等級)
enriched_data_gold_15 = {
    "stay up": {"phonetic": "/steɪ ʌp/", "pos": "v. phr.", "meaning": "熬夜；保持清醒", "phrases": ["stay up late"], "synonyms": ["remain awake"], "antonyms": ["go to bed"], "example": "I had to stay up late to finish the report before the meeting tomorrow."},
    "subordinate": {"phonetic": "/səˈbɔːrdɪnət/", "pos": "n./adj./v.", "meaning": "下屬；次要的；使從屬", "phrases": ["direct subordinate"], "synonyms": ["junior", "assistant"], "antonyms": ["superior", "boss"], "example": "A good manager should always listen to the suggestions made by their subordinates."},
    "solve": {"phonetic": "/sɑːlv/", "pos": "v.", "meaning": "解決；解答", "phrases": ["solve a problem"], "synonyms": ["resolve", "settle"], "antonyms": ["complicate"], "example": "The engineering team is working hard to solve the technical issues with the new machine."},
    "solvate": {"phonetic": "/ˈsɒlveɪt/", "pos": "v.", "meaning": "使溶劑化(化學術語)", "phrases": [], "synonyms": [], "antonyms": [], "example": "In chemistry, to solvate is to surround a solute particle with solvent molecules."},
    "solvency": {"phonetic": "/ˈsɑːlvənsi/", "pos": "n.", "meaning": "償付能力", "phrases": ["financial solvency"], "synonyms": ["stability"], "antonyms": ["insolvency", "bankruptcy"], "example": "The auditors are checking the company's solvency to ensure it can pay its debts."},
    "solvent": {"phonetic": "/ˈsɑːlvənt/", "pos": "adj./n.", "meaning": "有償付能力的；溶劑", "phrases": ["remain solvent"], "synonyms": ["financially sound"], "antonyms": ["insolvent"], "example": "The company has managed to remain solvent despite the difficult economic conditions."},
    "countersuit": {"phonetic": "/ˈkaʊntərsuːt/", "pos": "n.", "meaning": "反訴", "phrases": ["file a countersuit"], "synonyms": ["counterclaim"], "antonyms": [], "example": "The company filed a countersuit against its former partner for breach of contract."},
    "reserve the right": {"phonetic": "/rɪˈzɜːrv ðə raɪt/", "pos": "v. phr.", "meaning": "保留權利", "phrases": ["reserve the right to change prices"], "synonyms": [], "antonyms": [], "example": "The management reserves the right to refuse entry to any unauthorized persons."},
    "virus": {"phonetic": "/ˈvaɪrəs/", "pos": "n.", "meaning": "病毒", "phrases": ["computer virus", "flu virus"], "synonyms": [], "antonyms": [], "example": "The new computer virus has caused significant damage to the company's internal network."},
    "put out": {"phonetic": "/pʊt aʊt/", "pos": "v. phr.", "meaning": "熄滅；出版；生產", "phrases": ["put out a fire", "put out a fire"], "synonyms": ["extinguish", "publish"], "antonyms": [], "example": "Firefighters worked for several hours to put out the fire in the factory."},
    "janitorial staff": {"phonetic": "/ˌdʒænɪˈtɔːriəl stæf/", "pos": "n. phr.", "meaning": "清潔人員", "phrases": [], "synonyms": ["custodial staff"], "antonyms": [], "example": "The janitorial staff is responsible for cleaning and maintaining the office building."},
    "tech-oriented": {"phonetic": "/tek ˈɔːrientɪd/", "pos": "adj.", "meaning": "科技導向的", "phrases": [], "synonyms": ["technology-focused"], "antonyms": [], "example": "The city is trying to attract more tech-oriented businesses to the area."},
    "start-up": {"phonetic": "/ˈstɑːrt ʌp/", "pos": "n.", "meaning": "新創公司", "phrases": ["tech start-up"], "synonyms": ["new business"], "antonyms": ["established firm"], "example": "The technology start-up has received millions of dollars in venture capital funding."},
    "successive": {"phonetic": "/səkˈsesɪv/", "pos": "adj.", "meaning": "連續的", "phrases": ["successive quarters"], "synonyms": ["consecutive", "sequential"], "antonyms": [], "example": "The company has seen an increase in sales for four successive months."},
    "synchronize": {"phonetic": "/ˈsɪŋkrənaɪz/", "pos": "v.", "meaning": "同步", "phrases": ["synchronize data"], "synonyms": ["coordinate"], "antonyms": [], "example": "The new software allows users to synchronize their files across multiple devices."},
    "proceed with": {"phonetic": "/proʊˈsiːd wɪð/", "pos": "v. phr.", "meaning": "繼續進行；著手辦理", "phrases": [], "synonyms": ["continue with", "go ahead with"], "antonyms": ["halt", "stop"], "example": "The board of directors decided to proceed with the planned merger."},
    "cinema": {"phonetic": "/ˈsɪnəmə/", "pos": "n.", "meaning": "電影院；電影(業)", "phrases": ["go to the cinema"], "synonyms": ["movie theater"], "antonyms": [], "example": "The new shopping center will include a luxury cinema with ten screens."},
    "suspension bridge": {"phonetic": "/səˈspenʃn brɪdʒ/", "pos": "n. phr.", "meaning": "懸索橋；吊橋", "phrases": [], "synonyms": [], "antonyms": [], "example": "The Golden Gate Bridge is one of the most famous suspension bridges in the world."},
    "gymnastics": {"phonetic": "/dʒɪmˈnæstɪks/", "pos": "n.", "meaning": "體操", "phrases": ["gymnastics team"], "synonyms": [], "antonyms": [], "example": "She has been practicing gymnastics since she was five years old."},
    "medalist": {"phonetic": "/ˈmedəlɪst/", "pos": "n.", "meaning": "獎牌獲得者", "phrases": ["gold medalist"], "synonyms": ["winner"], "antonyms": [], "example": "The Olympic gold medalist was welcomed home as a national hero."},
    "tear down": {"phonetic": "/ter daʊn/", "pos": "v. phr.", "meaning": "拆毀；拆除", "phrases": [], "synonyms": ["demolish", "dismantle"], "antonyms": ["build", "construct"], "example": "The old factory was torn down to make room for a new apartment building."},
    "public servant": {"phonetic": "/ˈpʌblɪk ˈsɜːrvənt/", "pos": "n. phr.", "meaning": "公務員", "phrases": [], "synonyms": ["government official"], "antonyms": [], "example": "As a public servant, he is dedicated to improving the lives of the people in his community."},
    "mechanic": {"phonetic": "/məˈkænɪk/", "pos": "n.", "meaning": "技工；機械師", "phrases": ["car mechanic"], "synonyms": ["technician"], "antonyms": [], "example": "The mechanic checked the delivery truck's engine and found a minor problem."},
    "itching to": {"phonetic": "/ˈɪtʃɪŋ tuː/", "pos": "v. phr.", "meaning": "渴望做某事", "phrases": [], "synonyms": ["eager to", "longing to"], "antonyms": [], "example": "The sales team is itching to start the new marketing campaign next week."},
    "complimentary": {"phonetic": "/ˌkɑːmplɪˈmentəri/", "pos": "adj.", "meaning": "免費贈送的；稱讚的", "phrases": ["complimentary breakfast", "complimentary tickets"], "synonyms": ["free", "flattering"], "antonyms": ["paid", "critical"], "example": "The hotel provides complimentary bottles of water for all its guests."},
    "regardless to": {"word": "regardless of", "phonetic": "/rɪˈɡɑːrdləs əv/", "pos": "prep. phr.", "meaning": "不管...；不顧...", "phrases": [], "synonyms": ["irrespective of"], "antonyms": [], "example": "The company provides equal opportunities to all employees, regardless of their background."},
    "refer to": {"phonetic": "/rɪˈfɜːr tuː/", "pos": "v. phr.", "meaning": "提及；參考；查閱", "phrases": ["refer to a dictionary"], "synonyms": ["mention", "consult"], "antonyms": [], "example": "Please refer to the training manual if you have any questions about the new software."},
    "be responsive to": {"phonetic": "/bi rɪˈspɑːnsɪv tuː/", "pos": "v. phr.", "meaning": "對...有反應；回應", "phrases": [], "synonyms": [], "antonyms": [], "example": "The company is working hard to be more responsive to customer feedback."},
    "be accustomed to": {"phonetic": "/bi əˈkʌstəmd tuː/", "pos": "v. phr.", "meaning": "習慣於...", "phrases": [], "synonyms": ["be used to"], "antonyms": [], "example": "It took several months for him to be accustomed to the fast-paced working environment."},
    "be contingent on": {"phonetic": "/bi kənˈtɪndʒənt ɑːn/", "pos": "v. phr.", "meaning": "取決於...", "phrases": [], "synonyms": ["depend on"], "antonyms": [], "example": "The success of the project is contingent on the approval of the new budget."},
    "be founded with": {"phonetic": "/bi ˈfaʊndɪd wɪð/", "pos": "v. phr.", "meaning": "以...創立", "phrases": [], "synonyms": ["be established with"], "antonyms": [], "example": "The non-profit organization was founded with the goal of providing education to children."},
    "dealer": {"phonetic": "/ˈdiːlər/", "pos": "n.", "meaning": "商人；業者；發牌者", "phrases": ["car dealer", "authorized dealer"], "synonyms": ["trader", "merchant"], "antonyms": [], "example": "You should visit an authorized dealer to get your car serviced and repaired."},
    "amendment": {"phonetic": "/əˈmendmənt/", "pos": "n.", "meaning": "修正；改訂", "phrases": ["constitutional amendment"], "synonyms": ["correction", "alteration"], "antonyms": [], "example": "The board of directors approved several amendments to the company's bylaws."},
    "sightseeing": {"phonetic": "/ˈsaɪtsiːɪŋ/", "pos": "n.", "meaning": "觀光；遊覽", "phrases": ["go sightseeing"], "synonyms": ["touring"], "antonyms": [], "example": "We spent the whole afternoon sightseeing in the historic city center."},
    "coveted": {"phonetic": "/ˈkʌvətɪd/", "pos": "adj.", "meaning": "夢寐以求的；垂涎的", "phrases": ["coveted prize"], "synonyms": ["desired", "sought-after"], "antonyms": [], "example": "Winning the 'Best Workplace' award is a highly coveted honor in the industry."},
    "layout": {"phonetic": "/ˈleɪaʊt/", "pos": "n.", "meaning": "版面設計；佈局", "phrases": ["office layout", "website layout"], "synonyms": ["arrangement", "design"], "antonyms": [], "example": "The marketing team is working on a new layout for the company's annual report."},
    "premier": {"phonetic": "/prɪˈmɪr/ (adj.) /ˈpriːmiər/ (n.)", "pos": "adj./n.", "meaning": "首要的；首相", "phrases": ["premier league", "world's premier hotel"], "synonyms": ["leading", "prime", "prime minister"], "antonyms": [], "example": "This is widely recognized as one of the world's premier research institutions."},
    "mercury": {"phonetic": "/ˈmɜːrkjəri/", "pos": "n.", "meaning": "水銀；汞；水星", "phrases": ["mercury thermometer"], "synonyms": [], "antonyms": [], "example": "The factory was fined for failing to follow regulations regarding the disposal of mercury."},
    "overiap": {"word": "overlap", "phonetic": "/ˌoʊvərˈlæp/", "pos": "v./n.", "meaning": "重疊", "phrases": [], "synonyms": ["coincide"], "antonyms": [], "example": "The two projects overlap in several areas, so the teams need to coordinate their work."},
    "realtor": {"phonetic": "/ˈriːəltər/", "pos": "n.", "meaning": "房地產經紀人", "phrases": [], "synonyms": ["estate agent"], "antonyms": [], "example": "The realtor showed us several modern apartments in the downtown area."},
    "admit": {"phonetic": "/ədˈmɪt/", "pos": "v.", "meaning": "承認；准許進入", "phrases": ["admit defeat"], "synonyms": ["confess", "allow"], "antonyms": ["deny", "refuse"], "example": "The manager was forced to admit that the project was behind schedule."},
    "political sphere": {"phonetic": "/pəˈlɪtɪkl sfɪr/", "pos": "n. phr.", "meaning": "政界；政治圈", "phrases": [], "synonyms": [], "antonyms": [], "example": "He decided to leave his business career to enter the political sphere."},
    "political party": {"phonetic": "/pəˈlɪtɪkl ˈpɑːrti/", "pos": "n. phr.", "meaning": "政黨", "phrases": ["opposition political party"], "synonyms": [], "antonyms": [], "example": "The major political parties are currently preparing for the upcoming election."},
    "bribe": {"phonetic": "/braɪb/", "pos": "n./v.", "meaning": "賄賂", "phrases": ["accept a bribe"], "synonyms": ["kickback"], "antonyms": [], "example": "The former official was accused of accepting a bribe from a construction company."},
    "invaluable": {"phonetic": "/ɪnˈvæljuəbl/", "pos": "adj.", "meaning": "極其寶貴的；無價的", "phrases": ["invaluable advice"], "synonyms": ["priceless", "precious"], "antonyms": ["worthless"], "example": "His experience in the industry proved to be invaluable to the new start-up."},
    "discrepancy": {"phonetic": "/dɪˈskrepənsi/", "pos": "n.", "meaning": "差異；不一致", "phrases": ["financial discrepancy"], "synonyms": ["inconsistency", "difference"], "antonyms": ["agreement", "consistency"], "example": "The auditors identified a significant discrepancy in the company's financial records."},
    "symphony": {"phonetic": "/ˈsɪmfəni/", "pos": "n.", "meaning": "交響樂；交響樂團", "phrases": ["symphony orchestra"], "synonyms": [], "antonyms": [], "example": "The city's symphony orchestra will perform a series of concerts in the park this summer."},
    "struggle to do": {"phonetic": "/ˈstrʌɡl tuː duː/", "pos": "v. phr.", "meaning": "努力(做)；掙扎(做)", "phrases": [], "synonyms": ["labor", "strive"], "antonyms": [], "example": "Small businesses often struggle to survive during their first few years of operation."},
    "banking industry": {"phonetic": "/ˈbæŋkɪŋ ˈɪndəstri/", "pos": "n. phr.", "meaning": "銀行業", "phrases": [], "synonyms": [], "antonyms": [], "example": "The banking industry is facing significant challenges due to the new financial regulations."},
    "snowfall": {"phonetic": "/ˈsnoʊfɔːl/", "pos": "n.", "meaning": "降雪(量)", "phrases": ["heavy snowfall"], "synonyms": [], "antonyms": [], "example": "The heavy snowfall caused several flight delays at the international airport."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_15:
        update_info = enriched_data_gold_15[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 701-750 個單字。")
