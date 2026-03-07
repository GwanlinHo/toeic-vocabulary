import json

# 第 601-650 個高品質單字對應表 (金色等級)
enriched_data_gold_13 = {
    "bending over": {"phonetic": "/ˈbendɪŋ ˈoʊvər/", "pos": "v. phr.", "meaning": "彎腰", "phrases": ["bending over backward"], "synonyms": [], "antonyms": [], "example": "The worker was bending over to pick up the heavy box from the floor."},
    "sweeping": {"phonetic": "/ˈswiːpɪŋ/", "pos": "v./adj.", "meaning": "打掃；徹底的；廣泛的", "phrases": ["sweeping changes"], "synonyms": ["comprehensive", "extensive"], "antonyms": ["limited"], "example": "The new manager has introduced sweeping changes to the department's operations."},
    "reaching for": {"phonetic": "/ˈriːtʃɪŋ fər/", "pos": "v. phr.", "meaning": "伸手去拿", "phrases": [], "synonyms": [], "antonyms": [], "example": "She was reaching for a file on the top shelf when the phone rang."},
    "bench": {"phonetic": "/bentʃ/", "pos": "n.", "meaning": "長凳；工作台；法官席", "phrases": ["park bench", "work bench"], "synonyms": ["seat"], "antonyms": [], "example": "The workers eat their lunch on the wooden benches outside the factory."},
    "over the phone": {"phonetic": "/ˈoʊvər ðə foʊn/", "pos": "phr.", "meaning": "透過電話", "phrases": ["discuss over the phone"], "synonyms": ["by telephone"], "antonyms": [], "example": "We can discuss the details of the contract over the phone tomorrow morning."},
    "pilot": {"phonetic": "/ˈpaɪlət/", "pos": "n./v./adj.", "meaning": "飛行員；試驗；試點的", "phrases": ["pilot project", "airline pilot"], "synonyms": ["experimental", "trial"], "antonyms": [], "example": "The company is launching a pilot project to test the new delivery system."},
    "metal gate": {"phonetic": "/ˈmetl ɡeɪt/", "pos": "n. phr.", "meaning": "金屬門；鐵門", "phrases": [], "synonyms": [], "antonyms": [], "example": "The security guard opened the heavy metal gate to let the delivery truck inside."},
    "drag": {"phonetic": "/dræɡ/", "pos": "v./n.", "meaning": "拖曳；累贅", "phrases": ["drag and drop"], "synonyms": ["pull", "haul"], "antonyms": [], "example": "They had to drag the heavy machinery across the floor to its new location."},
    "pave": {"phonetic": "/peɪv/", "pos": "v.", "meaning": "鋪設(道路)；鋪路", "phrases": ["pave the way for"], "synonyms": [], "antonyms": [], "example": "The new trade agreement will pave the way for increased cooperation between the two countries."},
    "eagerness": {"phonetic": "/ˈiːɡərnəs/", "pos": "n.", "meaning": "熱切；渴望", "phrases": ["eagerness to learn"], "synonyms": ["enthusiasm", "keenness"], "antonyms": ["indifference", "apathy"], "example": "The new employees showed great eagerness to start their first project."},
    "proposal": {"phonetic": "/prəˈpoʊzl/", "pos": "n.", "meaning": "提議；建議；求婚", "phrases": ["submit a proposal", "business proposal"], "synonyms": ["suggestion", "offer"], "antonyms": [], "example": "The board of directors is currently reviewing the proposal for the new marketing campaign."},
    "demanding": {"phonetic": "/dɪˈmændɪŋ/", "pos": "adj.", "meaning": "苛求的；耗費精力的", "phrases": ["demanding schedule"], "synonyms": ["challenging", "tough"], "antonyms": ["easy", "effortless"], "example": "Her role as a senior manager is very demanding and requires a lot of travel."},
    "strictly": {"phonetic": "/ˈstrɪktli/", "pos": "adv.", "meaning": "嚴格地；完全地", "phrases": ["strictly confidential", "strictly prohibited"], "synonyms": ["rigorously", "tightly"], "antonyms": ["leniently"], "example": "Smoking is strictly prohibited in all areas of the office building."},
    "newsletter": {"phonetic": "/ˈnjuːzletər/", "pos": "n.", "meaning": "通訊；簡報", "phrases": ["monthly newsletter"], "synonyms": ["bulletin"], "antonyms": [], "example": "The company sends out a weekly newsletter to keep its employees informed about news and events."},
    "get subsidized": {"phonetic": "/ɡet ˈsʌbsɪdaɪzd/", "pos": "v. phr.", "meaning": "獲得補助", "phrases": [], "synonyms": ["receive a grant"], "antonyms": [], "example": "Low-income families can get subsidized housing through the local government program."},
    "financially sound": {"phonetic": "/faɪˈnænʃəli saʊnd/", "pos": "adj. phr.", "meaning": "財務穩健的", "phrases": [], "synonyms": ["financially stable"], "antonyms": ["bankrupt"], "example": "The auditors confirmed that the company is financially sound and has no major debts."},
    "job opening": {"phonetic": "/dʒɑːb ˈoʊpnɪŋ/", "pos": "n. phr.", "meaning": "職缺", "phrases": [], "synonyms": ["vacancy"], "antonyms": [], "example": "There is currently a job opening for a senior accountant in our finance department."},
    "adhere to": {"phonetic": "/ədˈhɪr tuː/", "pos": "v. phr.", "meaning": "遵守；堅持；黏附", "phrases": ["adhere to regulations"], "synonyms": ["follow", "obey", "stick to"], "antonyms": ["violate", "break"], "example": "All staff members must adhere to the company's safety regulations at all times."},
    "impartially": {"phonetic": "/ɪmˈpɑːrʃəli/", "pos": "adv.", "meaning": "公正地；無私地", "phrases": [], "synonyms": ["fairly", "objectively"], "antonyms": ["unfairly", "biasedly"], "example": "The committee will review all applications impartially and select the best candidate for the job."},
    "unanimously": {"phonetic": "/juˈnænɪməsli/", "pos": "adv.", "meaning": "全體一致地", "phrases": ["vote unanimously"], "synonyms": ["consistently"], "antonyms": [], "example": "The board of directors voted unanimously to approve the new investment plan."},
    "Pick": {"word": "recruit", "phonetic": "/rɪˈkruːt/", "pos": "v./n.", "meaning": "招募；新兵", "phrases": ["recruit new talent"], "synonyms": ["enlist", "hire"], "antonyms": [], "example": "The human resources department is working hard to recruit more skilled engineers."},
    "picky": {"phonetic": "/ˈpɪki/", "pos": "adj.", "meaning": "挑剔的", "phrases": ["picky eater"], "synonyms": ["fussy", "choosy"], "antonyms": ["indiscriminate"], "example": "He is very picky about the software he uses and only wants the latest versions."},
    "morale": {"phonetic": "/məˈræl/", "pos": "n.", "meaning": "士氣", "phrases": ["boost morale", "low morale"], "synonyms": ["spirit", "confidence"], "antonyms": [], "example": "The team's morale has improved significantly since the successful launch of the product."},
    "look over": {"phonetic": "/lʊk ˈoʊvər/", "pos": "v. phr.", "meaning": "檢查；審閱", "phrases": ["look over a report"], "synonyms": ["examine", "review"], "antonyms": [], "example": "Could you please look over this document before I send it to the client?"},
    "heavy schedule": {"phonetic": "/ˈhevi ˈskedʒuːl/", "pos": "n. phr.", "meaning": "行程緊湊；忙碌的時程", "phrases": [], "synonyms": ["busy schedule"], "antonyms": ["light schedule"], "example": "The CEO has a very heavy schedule this week with many international meetings."},
    "abide by": {"phonetic": "/əˈbaɪd baɪ/", "pos": "v. phr.", "meaning": "遵守；信守", "phrases": ["abide by the rules"], "synonyms": ["comply with", "follow"], "antonyms": ["violate", "break"], "example": "All employees are expected to abide by the terms of their employment contract."},
    "be aimed at": {"phonetic": "/bi eɪmd æt/", "pos": "v. phr.", "meaning": "針對；目標是", "phrases": [], "synonyms": ["target", "focus on"], "antonyms": [], "example": "The new marketing campaign is primarily aimed at young professionals in the city."},
    "seminars": {"phonetic": "/ˈsemɪnɑːrz/", "pos": "n.", "meaning": "研討會(複數)", "phrases": ["attend a seminar"], "synonyms": ["workshops"], "antonyms": [], "example": "The company organizes monthly seminars to keep its staff updated on industry trends."},
    "take pleasure in Ving": {"phonetic": "/teɪk ˈpleʒər ɪn/", "pos": "phr.", "meaning": "樂於做某事", "phrases": [], "synonyms": ["enjoy"], "antonyms": ["dislike"], "example": "We take great pleasure in providing our customers with the highest quality of service."},
    "of use": {"phonetic": "/əv juːs/", "pos": "adj. phr.", "meaning": "有用的", "phrases": ["be of use to someone"], "synonyms": ["useful", "helpful"], "antonyms": ["useless"], "example": "I hope the information I provided will be of use to you during your research."},
    "meet the deadline": {"phonetic": "/miːt ðə ˈdedlaɪn/", "pos": "v. phr.", "meaning": "趕上截止日期", "phrases": [], "synonyms": ["finish on time"], "antonyms": ["miss the deadline"], "example": "The whole team worked late every night to ensure we would meet the deadline."},
    "displace": {"phonetic": "/dɪsˈpleɪs/", "pos": "v.", "meaning": "取代；使流離失所", "phrases": [], "synonyms": ["replace", "supplant"], "antonyms": [], "example": "New technology is expected to displace thousands of workers in the manufacturing industry."},
    "ought to do": {"phonetic": "/ˈɔːt tuː duː/", "pos": "modal v.", "meaning": "應該做", "phrases": [], "synonyms": ["should do"], "antonyms": [], "example": "We ought to review our safety procedures to prevent any future accidents."},
    "keep an eye on": {"phonetic": "/kiːp ən aɪ ɑːn/", "pos": "v. phr.", "meaning": "留意；照看", "phrases": [], "synonyms": ["watch", "monitor"], "antonyms": ["ignore"], "example": "Please keep an eye on the printer and let me know if it runs out of paper."},
    "reimbursement": {"phonetic": "/ˌriːɪmˈbɜːrsmənt/", "pos": "n.", "meaning": "核銷；補償；退款", "phrases": ["travel reimbursement"], "synonyms": ["repayment", "compensation"], "antonyms": [], "example": "You can apply for reimbursement of your travel expenses after the business trip."},
    "amenities": {"phonetic": "/əˈmenətiːz/", "pos": "n.", "meaning": "便利設施；娛樂設施(複數)", "phrases": ["hotel amenities"], "synonyms": ["facilities", "features"], "antonyms": [], "example": "The new luxury hotel offers a wide range of amenities, including a gym and a spa."},
    "limousine service": {"phonetic": "/ˈlɪməziːn ˈsɜːrvɪs/", "pos": "n. phr.", "meaning": "禮車服務", "phrases": [], "synonyms": [], "antonyms": [], "example": "The airport provides a complimentary limousine service for its first-class passengers."},
    "regular/usual/sticker price": {"phonetic": "/ˈreɡjələr praɪs/", "pos": "n. phr.", "meaning": "原價；定價", "phrases": [], "synonyms": ["list price"], "antonyms": ["discount price"], "example": "The store is offering a twenty percent discount on the regular price of all electronics."},
    "hand/turn in": {"phonetic": "/hænd ɪn/", "pos": "v. phr.", "meaning": "上交；提交", "phrases": ["hand in a report"], "synonyms": ["submit", "deliver"], "antonyms": [], "example": "Please remember to hand in your resignation letter to the HR department by Friday."},
    "readmission": {"phonetic": "/ˌriːədˈmɪʃn/", "pos": "n.", "meaning": "重新入院；重新進入", "phrases": [], "synonyms": [], "antonyms": [], "example": "The patient's readmission to the hospital was necessary due to a sudden change in his condition."},
    "silent": {"phonetic": "/ˈsaɪlənt/", "pos": "adj.", "meaning": "沉默的；無聲的", "phrases": ["silent partner"], "synonyms": ["quiet", "still"], "antonyms": ["loud", "noisy"], "example": "The board members remained silent as the CEO announced the company's financial losses."},
    "succeed in": {"phonetic": "/səkˈsiːd ɪn/", "pos": "v. phr.", "meaning": "在...方面成功", "phrases": [], "synonyms": ["achieve", "prosper"], "antonyms": ["fail in"], "example": "The company has managed to succeed in the highly competitive international market."},
    "succeed to": {"phonetic": "/səkˈsiːd tuː/", "pos": "v. phr.", "meaning": "繼承", "phrases": ["succeed to the throne"], "synonyms": ["inherit"], "antonyms": [], "example": "He is expected to succeed to the position of CEO when the current manager retires."},
    "abstain/refrain from": {"phonetic": "/əbˈsteɪn frəm/", "pos": "v. phr.", "meaning": "戒除；避開", "phrases": ["abstain from voting"], "synonyms": ["forbear", "avoid"], "antonyms": ["indulge in"], "example": "Please refrain from using your mobile phone during the presentation."},
    "object to": {"phonetic": "/əbˈdʒekt tuː/", "pos": "v. phr.", "meaning": "反對", "phrases": [], "synonyms": ["oppose", "disagree with"], "antonyms": ["agree to", "support"], "example": "Many local residents object to the construction of the new shopping center in the area."},
    "be oppose to": {"word": "be opposed to", "phonetic": "/bi əˈpoʊzd tuː/", "pos": "v. phr.", "meaning": "反對...", "phrases": [], "synonyms": ["be against"], "antonyms": ["be in favor of"], "example": "The union is strongly opposed to the management's plan to cut employee benefits."},
    "look after": {"phonetic": "/lʊk ˈæftər/", "pos": "v. phr.", "meaning": "照顧；照看", "phrases": [], "synonyms": ["care for", "take care of"], "antonyms": ["neglect"], "example": "The maintenance team is responsible for looking after the company's machinery and equipment."},
    "go through": {"phonetic": "/ɡoʊ θruː/", "pos": "v. phr.", "meaning": "經歷；仔細檢查；穿過", "phrases": ["go through documents"], "synonyms": ["experience", "examine", "undergo"], "antonyms": [], "example": "The auditors will go through all the financial records from the last fiscal year."},
    "come by": {"phonetic": "/kʌm baɪ/", "pos": "v. phr.", "meaning": "獲得；經過；順道拜訪", "phrases": [], "synonyms": ["obtain", "get", "visit"], "antonyms": [], "example": "Good jobs in this industry are hard to come by in the current economic climate."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_13:
        update_info = enriched_data_gold_13[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 601-650 個單字。")
