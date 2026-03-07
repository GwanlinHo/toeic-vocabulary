import json

# 第 901-950 個高品質單字對應表 (金色等級)
enriched_data_gold_19 = {
    "consignment": {"phonetic": "/kənˈsaɪnmənt/", "pos": "n.", "meaning": "寄售；委託貨物", "phrases": ["on consignment"], "synonyms": ["shipment", "delivery"], "antonyms": [], "example": "The store agreed to sell the artist's paintings on consignment."},
    "tricky": {"phonetic": "/ˈtrɪki/", "pos": "adj.", "meaning": "棘手的；狡猾的", "phrases": ["tricky situation"], "synonyms": ["difficult", "complicated"], "antonyms": ["simple", "straightforward"], "example": "Negotiating the terms of the merger proved to be a tricky process."},
    "interior decorator": {"phonetic": "/ɪnˈtɪriər ˈdekəreɪtər/", "pos": "n. phr.", "meaning": "室內設計師/裝飾師", "phrases": [], "synonyms": ["interior designer"], "antonyms": [], "example": "The company hired a professional interior decorator to redesign the main office lobby."},
    "commemorate": {"phonetic": "/kəˈmeməreɪt/", "pos": "v.", "meaning": "紀念；慶祝", "phrases": ["commemorate an anniversary"], "synonyms": ["celebrate", "honor"], "antonyms": [], "example": "A special plaque was installed to commemorate the opening of the new research facility."},
    "emit": {"phonetic": "/iˈmɪt/", "pos": "v.", "meaning": "排放；散發；發出", "phrases": ["emit greenhouse gases"], "synonyms": ["release", "discharge"], "antonyms": ["absorb"], "example": "The factory was fined for emitting excessive amounts of smoke into the atmosphere."},
    "seasoned": {"phonetic": "/ˈsiːznd/", "pos": "adj.", "meaning": "經驗豐富的；調過味的", "phrases": ["seasoned professional"], "synonyms": ["experienced", "veteran"], "antonyms": ["inexperienced"], "example": "The company is looking for a seasoned manager to lead its international sales team."},
    "amplifier": {"phonetic": "/ˈæmplɪfaɪər/", "pos": "n.", "meaning": "放大器；擴音器", "phrases": ["guitar amplifier"], "synonyms": [], "antonyms": [], "example": "The technician checked the sound system and found a problem with the amplifier."},
    "alleged": {"phonetic": "/əˈledʒd/", "pos": "adj.", "meaning": "據稱的；嫌疑的", "phrases": ["alleged crime"], "synonyms": ["supposed", "claimed"], "antonyms": ["proven", "certain"], "example": "The company is investigating the alleged misconduct of one of its senior executives."},
    "float": {"phonetic": "/floʊt/", "pos": "v./n.", "meaning": "漂浮；提出(想法)；(公司)上市；預備金", "phrases": ["float an idea", "float a company"], "synonyms": ["drift", "suggest"], "antonyms": ["sink"], "example": "The board is considering whether to float the company on the stock market next year."},
    "groom": {"phonetic": "/ɡruːm/", "pos": "v./n.", "meaning": "培訓；修飾；新郎", "phrases": ["groom for a position"], "synonyms": ["train", "prepare"], "antonyms": [], "example": "The assistant is being groomed to take over the manager's role when he retires."},
    "commencement exercise": {"phonetic": "/kəˈmensmənt ˈeksərsaɪz/", "pos": "n. phr.", "meaning": "畢業典禮", "phrases": [], "synonyms": ["graduation ceremony"], "antonyms": [], "example": "The university's commencement exercise will be held in the main stadium next Saturday."},
    "diploma": {"phonetic": "/dɪˈploʊmə/", "pos": "n.", "meaning": "文憑；畢業證書", "phrases": ["high school diploma"], "synonyms": ["certificate", "degree"], "antonyms": [], "example": "You need to provide a copy of your university diploma when you apply for the job."},
    "railing": {"phonetic": "/ˈreɪlɪŋ/", "pos": "n.", "meaning": "欄杆；扶手", "phrases": ["stair railing"], "synonyms": ["handrail"], "antonyms": [], "example": "Please hold onto the railing while walking down the steep stairs."},
    "toe": {"phonetic": "/toʊ/", "pos": "n./v.", "meaning": "腳趾；用腳尖觸碰", "phrases": ["toe the line"], "synonyms": [], "antonyms": [], "example": "Employees are expected to toe the line and follow all company policies."},
    "fireplace": {"phonetic": "/ˈfaɪərpleɪs/", "pos": "n.", "meaning": "壁爐", "phrases": ["electric fireplace"], "synonyms": ["hearth"], "antonyms": [], "example": "The hotel lobby features a large stone fireplace that creates a cozy atmosphere."},
    "span": {"phonetic": "/spæn/", "pos": "n./v.", "meaning": "跨度；期間；跨越", "phrases": ["attention span", "life span"], "synonyms": ["extent", "stretch", "bridge"], "antonyms": [], "example": "The new bridge spans the entire river and has significantly reduced travel time."},
    "shore": {"phonetic": "/ʃɔːr/", "pos": "n.", "meaning": "岸；濱", "phrases": ["on the shore"], "synonyms": ["coast", "beach"], "antonyms": [], "example": "The resort is located right on the shore of the beautiful lake."},
    "dock": {"phonetic": "/dɑːk/", "pos": "n./v.", "meaning": "碼頭；停靠；扣除(工資)", "phrases": ["loading dock", "dock a ship"], "synonyms": ["pier", "wharf", "deduct"], "antonyms": [], "example": "The shipment of raw materials is currently waiting at the loading dock."},
    "wharf": {"phonetic": "/wɔːrf/", "pos": "n.", "meaning": "碼頭", "phrases": [], "synonyms": ["pier", "dock"], "antonyms": [], "example": "The fishermen unload their catch at the wharf early every morning."},
    "discharge": {"phonetic": "/dɪsˈtʃɑːrdʒ/", "pos": "v./n.", "meaning": "排放；解雇；卸貨；履行", "phrases": ["discharge duties"], "synonyms": ["release", "emit", "dismiss"], "antonyms": ["hire", "employ", "absorb"], "example": "He has discharged his duties as project manager with great dedication and success."},
    "pride": {"phonetic": "/praɪd/", "pos": "n./v.", "meaning": "自豪；傲慢；以...自豪", "phrases": ["take pride in"], "synonyms": ["satisfaction", "arrogance"], "antonyms": ["humility", "shame"], "example": "The company takes great pride in the quality of its products and services."},
    "shut down": {"phonetic": "/ʃʌt daʊn/", "pos": "v. phr.", "meaning": "關閉；停工", "phrases": ["shut down a computer", "factory shut down"], "synonyms": ["close", "stop"], "antonyms": ["start up", "open"], "example": "The factory had to shut down for two days due to a major power failure."},
    "ballroom": {"phonetic": "/ˈbɔːlruːm/", "pos": "n.", "meaning": "宴會廳；舞廳", "phrases": ["grand ballroom"], "synonyms": [], "antonyms": [], "example": "The annual awards ceremony will be held in the hotel's grand ballroom."},
    "extent": {"phonetic": "/ɪkˈstent/", "pos": "n.", "meaning": "程度；範圍；限度", "phrases": ["to a large extent"], "synonyms": ["degree", "scope", "range"], "antonyms": [], "example": "We are currently investigating the extent of the damage caused by the fire."},
    "unanimous": {"phonetic": "/juˈnænɪməs/", "pos": "adj.", "meaning": "全體一致的", "phrases": ["unanimous decision"], "synonyms": ["consistent", "undisputed"], "antonyms": ["divided"], "example": "The proposal was approved by a unanimous vote of the board members."},
    "concise": {"phonetic": "/kənˈsaɪs/", "pos": "adj.", "meaning": "簡潔的；明了的", "phrases": ["concise report"], "synonyms": ["succinct", "brief"], "antonyms": ["wordy", "verbose"], "example": "Please provide a concise summary of the project's progress for the meeting."},
    "baseness": {"phonetic": "/ˈbeɪsnəs/", "pos": "n.", "meaning": "卑鄙；下賤", "phrases": [], "synonyms": ["meanness", "wickedness"], "antonyms": ["nobility"], "example": "The baseness of the scheme shocked everyone who heard about it."},
    "streamlined": {"phonetic": "/ˈstriːmlaɪnd/", "pos": "adj.", "meaning": "流線型的；效率化的", "phrases": ["streamlined process"], "synonyms": ["efficient", "optimized"], "antonyms": ["clunky", "inefficient"], "example": "The company has introduced a streamlined system for processing customer orders."},
    "in this regard": {"phonetic": "/ɪn ðɪs rɪˈɡɑːrd/", "pos": "phr.", "meaning": "在這一點上；關於這方面", "phrases": [], "synonyms": ["in this respect"], "antonyms": [], "example": "The new policy is very helpful; in this regard, we have seen great improvement."},
    "neurologist": {"phonetic": "/nʊˈrɑːlədʒɪst/", "pos": "n.", "meaning": "神經科醫師", "phrases": [], "synonyms": [], "antonyms": [], "example": "He had to see a neurologist after experiencing recurring headaches and dizziness."},
    "recipient": {"phonetic": "/rɪˈsɪpiənt/", "pos": "n.", "meaning": "收件人；接受者", "phrases": ["award recipient"], "synonyms": ["receiver"], "antonyms": ["sender", "giver"], "example": "The recipient of the 'Employee of the Year' award will be announced tomorrow."},
    "antique": {"phonetic": "/ænˈtiːk/", "pos": "n./adj.", "meaning": "古董；古老的", "phrases": ["antique furniture"], "synonyms": ["ancient", "vintage"], "antonyms": ["modern", "new"], "example": "The office lobby is decorated with several pieces of expensive antique furniture."},
    "proprietor": {"phonetic": "/prəˈpraɪətər/", "pos": "n.", "meaning": "所有者；經營者", "phrases": ["sole proprietor"], "synonyms": ["owner"], "antonyms": [], "example": "The proprietor of the local restaurant is planning to open a second branch."},
    "appraise": {"phonetic": "/əˈpreɪz/", "pos": "v.", "meaning": "評估；估價", "phrases": ["appraise property"], "synonyms": ["evaluate", "estimate", "assess"], "antonyms": [], "example": "The bank sent an expert to appraise the value of the building before approving the loan."},
    "extravagant": {"phonetic": "/ɪkˈstrævəɡənt/", "pos": "adj.", "meaning": "奢侈的；過度的", "phrases": ["extravagant lifestyle"], "synonyms": ["wasteful", "excessive"], "antonyms": ["economical", "thrifty", "modest"], "example": "The company's extravagant spending on the launch party was criticized by shareholders."},
    "excursion": {"phonetic": "/ɪkˈskɜːrʒn/", "pos": "n.", "meaning": "短途旅行；遠足", "phrases": ["day excursion"], "synonyms": ["trip", "outing"], "antonyms": [], "example": "The company is organizing a weekend excursion to the mountains for all staff members."},
    "cottage": {"phonetic": "/ˈkɑːtɪdʒ/", "pos": "n.", "meaning": "小屋；農舍", "phrases": ["summer cottage"], "synonyms": ["cabin", "bungalow"], "antonyms": [], "example": "They decided to rent a small cottage by the sea for their summer vacation."},
    "broker": {"phonetic": "/ˈbroʊkər/", "pos": "n./v.", "meaning": "經紀人；代理人；協商", "phrases": ["stockbroker", "insurance broker", "broker a deal"], "synonyms": ["agent", "negotiate"], "antonyms": [], "example": "The investment broker provided useful advice on diversifying the company's portfolio."},
    "rebate": {"phonetic": "/ˈriːbeɪt/", "pos": "n./v.", "meaning": "退還款；折扣", "phrases": ["tax rebate", "mail-in rebate"], "synonyms": ["refund", "discount"], "antonyms": [], "example": "You can apply for a fifty-dollar rebate after purchasing the new appliance."},
    "allot": {"phonetic": "/əˈlɑːt/", "pos": "v.", "meaning": "分配；撥給", "phrases": ["allot time", "allot funds"], "synonyms": ["allocate", "assign"], "antonyms": [], "example": "The board has decided to allot more funds to the research and development department."},
    "tentative": {"phonetic": "/ˈtentətɪv/", "pos": "adj.", "meaning": "暫時的；猶豫的", "phrases": ["tentative agreement", "tentative schedule"], "synonyms": ["provisional", "uncertain"], "antonyms": ["final", "certain", "definite"], "example": "We have reached a tentative agreement, but some details still need to be finalized."},
    "unpack": {"phonetic": "/ˌʌnˈpæk/", "pos": "v.", "meaning": "拆封；取出；分析", "phrases": ["unpack a box"], "synonyms": [], "antonyms": ["pack"], "example": "It took several hours for the workers to unpack all the new office equipment."},
    "diminutive": {"phonetic": "/dɪˈmɪnjətɪv/", "pos": "adj.", "meaning": "極小的；微小的", "phrases": [], "synonyms": ["tiny", "miniature"], "antonyms": ["huge", "enormous"], "example": "Despite its diminutive size, the new device is extremely powerful and efficient."},
    "as long as": {"phonetic": "/æz lɔːŋ æz/", "pos": "conj. phr.", "meaning": "只要", "phrases": [], "synonyms": ["provided that"], "antonyms": [], "example": "You can work from home as long as you complete all your tasks on time."},
    "intended": {"phonetic": "/ɪnˈtendɪd/", "pos": "adj.", "meaning": "預期的；擬議中的", "phrases": ["intended audience", "intended use"], "synonyms": ["planned", "proposed"], "antonyms": ["accidental"], "example": "The marketing campaign was designed to appeal to its intended audience of young professionals."},
    "vulnerable": {"phonetic": "/ˈvʌlnərəbl/", "pos": "adj.", "meaning": "易受傷的；脆弱的", "phrases": ["vulnerable group"], "synonyms": ["susceptible", "weak"], "antonyms": ["resistant", "immune", "robust"], "example": "Small businesses are particularly vulnerable to sudden changes in interest rates."},
    "burglary": {"phonetic": "/ˈbɜːrɡləri/", "pos": "n.", "meaning": "竊盜(罪)；入室盜竊", "phrases": ["commit a burglary"], "synonyms": ["theft", "break-in"], "antonyms": [], "example": "The company increased its security after a burglary took place at the warehouse last week."},
    "turn in": {"phonetic": "/tɜːrn ɪn/", "pos": "v. phr.", "meaning": "交回；上交；上床睡覺", "phrases": ["turn in a report"], "synonyms": ["submit", "hand in"], "antonyms": [], "example": "Please remember to turn in your office keys before you leave the company."},
    "savor": {"phonetic": "/ˈseɪvər/", "pos": "v./n.", "meaning": "細味；品嚐；風味", "phrases": ["savor the moment"], "synonyms": ["relish", "enjoy", "taste"], "antonyms": ["dislike"], "example": "After months of hard work, the team took some time to savor their success."},
    "lasting": {"phonetic": "/ˈlæstɪŋ/", "pos": "adj.", "meaning": "持久的；耐用的", "phrases": ["lasting impression"], "synonyms": ["enduring", "permanent", "durable"], "antonyms": ["temporary", "brief", "fleeting"], "example": "The partnership has had a lasting impact on the growth of both companies."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_19:
        update_info = enriched_data_gold_19[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 901-950 個單字。")
