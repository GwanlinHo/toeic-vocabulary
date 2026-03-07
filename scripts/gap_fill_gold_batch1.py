import json

# 金色等級補漏第 1 部分
gap_fill_gold_1 = {
    "audiovisual": {"phonetic": "/ˌɔːdioʊˈvɪʒuəl/", "pos": "adj.", "meaning": "視聽的", "phrases": ["audiovisual equipment"], "synonyms": [], "antonyms": [], "example": "The conference room is equipped with the latest audiovisual technology."},
    "beyond repair": {"phonetic": "/bɪˈjɑːnd rɪˈper/", "pos": "phr.", "meaning": "無法修復", "phrases": [], "synonyms": ["irreparable"], "antonyms": [], "example": "The technician said that the old printer was damaged beyond repair."},
    "regret": {"phonetic": "/rɪˈɡret/", "pos": "v./n.", "meaning": "後悔；遺憾", "phrases": ["regret to inform you"], "synonyms": ["repent", "remorse"], "antonyms": [], "example": "We regret to inform you that your application was not successful this time."},
    "pottery": {"phonetic": "/ˈpɑːtəri/", "pos": "n.", "meaning": "陶器", "phrases": ["handmade pottery"], "synonyms": ["ceramics"], "antonyms": [], "example": "The local market is famous for its beautiful handmade pottery."},
    "porcelain": {"phonetic": "/ˈpɔːrsəlɪn/", "pos": "n.", "meaning": "瓷器", "phrases": ["fine porcelain"], "synonyms": ["china"], "antonyms": [], "example": "The museum has a large collection of ancient Chinese porcelain."},
    "aluminum": {"phonetic": "/əˈluːmɪnəm/", "pos": "n.", "meaning": "鋁", "phrases": ["aluminum foil"], "synonyms": [], "antonyms": [], "example": "Aluminum is a lightweight metal that is commonly used in aircraft construction."},
    "srainless steel": {"word": "stainless steel", "phonetic": "/ˈsteɪnləs stiːl/", "pos": "n. phr.", "meaning": "不鏽鋼", "phrases": [], "synonyms": [], "antonyms": [], "example": "Most of our kitchen appliances are made of high-quality stainless steel."},
    "preffered": {"word": "preferred", "phonetic": "/prɪˈfɜːrd/", "pos": "adj.", "meaning": "首選的；偏好的", "phrases": ["preferred candidate"], "synonyms": ["favored"], "antonyms": [], "example": "Please indicate your preferred method of payment on the form."},
    "ceramics": {"phonetic": "/səˈræmɪks/", "pos": "n.", "meaning": "陶瓷製品", "phrases": [], "synonyms": ["pottery"], "antonyms": [], "example": "She enjoys taking classes in ceramics and making her own vases."},
    "construction business": {"phonetic": "/kənˈstrʌkʃn ˈbɪznəs/", "pos": "n. phr.", "meaning": "營造業", "phrases": [], "synonyms": [], "antonyms": [], "example": "My uncle has been in the construction business for over twenty years."},
    "gardening": {"phonetic": "/ˈɡɑːrdnɪŋ/", "pos": "n.", "meaning": "園藝", "phrases": ["gardening tools"], "synonyms": [], "antonyms": [], "example": "He spends most of his weekends gardening in his backyard."},
    "cordially": {"phonetic": "/ˈkɔːrdʒəli/", "pos": "adv.", "meaning": "誠摯地", "phrases": ["cordially invited"], "synonyms": ["warmly", "sincerely"], "antonyms": [], "example": "You are cordially invited to attend the company's annual dinner party."},
    "reunion": {"phonetic": "/ˌriːˈjuːniən/", "pos": "n.", "meaning": "重聚；團圓", "phrases": ["family reunion", "class reunion"], "synonyms": ["gathering"], "antonyms": [], "example": "The university is organizing a reunion for graduates of the class of 2010."},
    "deliver a speech": {"phonetic": "/dɪˈlɪvər ə spiːtʃ/", "pos": "v. phr.", "meaning": "發表演說", "phrases": [], "synonyms": ["give a speech"], "antonyms": [], "example": "The CEO will deliver a speech at the opening ceremony of the new factory."},
    "graduate": {"phonetic": "/ˈɡrædʒuət/ (n.) /ˈɡrædʒueɪt/ (v.)", "pos": "n./v.", "meaning": "畢業生；畢業", "phrases": ["university graduate"], "synonyms": ["alumnus"], "antonyms": [], "example": "After he graduates from college, he plans to work in the finance industry."},
    "a graduate student": {"phonetic": "/ə ˈɡrædʒuət ˈstuːdnt/", "pos": "n. phr.", "meaning": "研究生", "phrases": [], "synonyms": ["postgraduate"], "antonyms": ["undergraduate"], "example": "She is currently a graduate student studying international relations."},
    "reconnect with": {"phonetic": "/ˌriːkəˈnekt wɪð/", "pos": "v. phr.", "meaning": "重新聯繫", "phrases": [], "synonyms": [], "antonyms": [], "example": "The social media platform helps people reconnect with old friends and colleagues."},
    "cabin": {"phonetic": "/ˈkæbɪn/", "pos": "n.", "meaning": "小木屋；機艙；船艙", "phrases": ["log cabin", "crew cabin"], "synonyms": ["cottage", "hut"], "antonyms": [], "example": "They decided to rent a small cabin in the mountains for their summer vacation."},
    "still": {"phonetic": "/stɪl/", "pos": "adv./adj.", "meaning": "仍然；靜止的", "phrases": ["stand still"], "synonyms": ["motionless", "yet"], "antonyms": ["moving"], "example": "The company is still waiting for the approval of its new project proposal."},
    "access": {"phonetic": "/ˈækses/", "pos": "n./v.", "meaning": "進入；取得權；存取", "phrases": ["internet access", "access data"], "synonyms": ["entry", "admission"], "antonyms": [], "example": "You need a password to access the company's confidential database."},
    "suburb": {"phonetic": "/ˈsʌbɜːrb/", "pos": "n.", "meaning": "郊區", "phrases": ["leafy suburb"], "synonyms": ["outskirts"], "antonyms": ["city center"], "example": "Many families prefer living in the suburbs where it is quieter and less polluted."},
    "major in": {"phonetic": "/ˈmeɪdʒər ɪn/", "pos": "v. phr.", "meaning": "主修", "phrases": [], "synonyms": ["specialize in"], "antonyms": ["minor in"], "example": "He decided to major in business administration at university."},
    "minor in": {"phonetic": "/ˈmaɪnər ɪn/", "pos": "v. phr.", "meaning": "副修", "phrases": [], "synonyms": [], "antonyms": ["major in"], "example": "She is majoring in economics and decided to minor in French."},
    "recommendation": {"phonetic": "/ˌrekəmenˈdeɪʃn/", "pos": "n.", "meaning": "推薦；建議", "phrases": ["letter of recommendation"], "synonyms": ["suggestion", "advice"], "antonyms": [], "example": "The report includes several recommendations for improving the production process."},
    "cover letter": {"phonetic": "/ˈkʌvər ˈletər/", "pos": "n. phr.", "meaning": "求職信", "phrases": ["attach a cover letter"], "synonyms": ["letter of application"], "antonyms": [], "example": "Please send your resume and a cover letter to the HR department."},
    "state-licensed": {"phonetic": "/steɪt ˈlaɪsnst/", "pos": "adj.", "meaning": "經州政府授權的", "phrases": [], "synonyms": ["authorized"], "antonyms": [], "example": "All of our engineers are state-licensed and have years of experience."},
    "enroll in": {"phonetic": "/ɪnˈroʊl ɪn/", "pos": "v. phr.", "meaning": "註冊(參加課程等)", "phrases": [], "synonyms": ["register for", "sign up for"], "antonyms": [], "example": "More than fifty employees have decided to enroll in the new management course."},
    "mature": {"phonetic": "/məˈtʃʊr/", "pos": "adj./v.", "meaning": "成熟的；到期", "phrases": ["mature student"], "synonyms": ["adult", "ripe"], "antonyms": ["immature"], "example": "The company's marketing strategy is aimed at a mature and sophisticated audience."},
    "a premature baby": {"phonetic": "/ə ˌpriːməˈtʃʊr ˈbeɪbi/", "pos": "n. phr.", "meaning": "早產兒", "phrases": [], "synonyms": ["preterm infant"], "antonyms": [], "example": "The hospital has a special unit for provide intensive care to premature babies."},
    "immature": {"phonetic": "/ˌɪməˈtʃʊr/", "pos": "adj.", "meaning": "不成熟的", "phrases": ["immature behavior"], "synonyms": ["childish"], "antonyms": ["mature"], "example": "His immature comments during the meeting were seen as unprofessional by the manager."},
    "pharmaceutical": {"phonetic": "/ˌfɑːrməˈsuːtɪkl/", "pos": "adj./n.", "meaning": "製藥的；藥物", "phrases": ["pharmaceutical industry"], "synonyms": ["medicinal"], "antonyms": [], "example": "The company is a major player in the global pharmaceutical industry."},
    "depressant": {"phonetic": "/dɪˈpresnt/", "pos": "n./adj.", "meaning": "抑制劑；鎮靜劑；抑鬱的", "phrases": [], "synonyms": ["sedative"], "antonyms": ["stimulant"], "example": "Alcohol is a central nervous system depressant that can affect your reaction time."},
    "anti-depressant": {"phonetic": "/ˌæntidɪˈpresnt/", "pos": "n.", "meaning": "抗抑鬱藥", "phrases": [], "synonyms": [], "antonyms": [], "example": "The doctor prescribed an anti-depressant to help the patient manage his symptoms."},
    "menstruation": {"phonetic": "/ˌmenstruˈeɪʃn/", "pos": "n.", "meaning": "月經", "phrases": [], "synonyms": ["period"], "antonyms": [], "example": "Menstruation is a natural part of the reproductive cycle for many women."},
    "menopausal": {"phonetic": "/ˌmenəˈpɔːzl/", "pos": "adj.", "meaning": "更年期的", "phrases": ["menopausal symptoms"], "synonyms": [], "antonyms": [], "example": "The clinic provides specialized healthcare services for menopausal women."},
    "stage": {"phonetic": "/steɪdʒ/", "pos": "n./v.", "meaning": "階段；舞台；上演", "phrases": ["early stage", "on stage"], "synonyms": ["phase", "platform"], "antonyms": [], "example": "The project is currently in its final stage and will be completed by next week."},
    "on the market": {"phonetic": "/ɑːn ðə ˈmɑːrkɪt/", "pos": "phr.", "meaning": "上市中；在市場上售賣", "phrases": [], "synonyms": ["available for sale"], "antonyms": [], "example": "The new model will be on the market starting from the first of next month."},
    "side effect": {"phonetic": "/saɪd ɪˈfekt/", "pos": "n. phr.", "meaning": "副作用", "phrases": ["common side effect"], "synonyms": [], "antonyms": [], "example": "Please read the label carefully to understand the potential side effects of the medication."},
    "clinical": {"phonetic": "/ˈklɪnɪkl/", "pos": "adj.", "meaning": "臨床的；門診的", "phrases": ["clinical trial", "clinical study"], "synonyms": [], "antonyms": [], "example": "The new drug has shown promising results in recent clinical trials."},
    "hypertension": {"phonetic": "/ˌhaɪpərˈtenʃn/", "pos": "n.", "meaning": "高血壓", "phrases": ["suffer from hypertension"], "synonyms": ["high blood pressure"], "antonyms": ["hypotension"], "example": "Hypertension is a serious condition that can increase the risk of heart disease."},
    "interfere with": {"phonetic": "/ˌɪntərˈfɪr wɪð/", "pos": "v. phr.", "meaning": "干擾；妨礙", "phrases": [], "synonyms": ["hinder", "obstruct"], "antonyms": ["help", "support"], "example": "The noise from the construction site is interfering with our ability to focus on work."},
    "appetite": {"phonetic": "/ˈæpɪtaɪt/", "pos": "n.", "meaning": "食慾；胃口；慾望", "phrases": ["loss of appetite"], "synonyms": ["hunger", "desire"], "antonyms": [], "example": "Stress and anxiety can often lead to a loss of appetite in some people."},
    "drowsy": {"phonetic": "/ˈdraʊzi/", "pos": "adj.", "meaning": "昏昏欲睡的", "phrases": ["feel drowsy"], "synonyms": ["sleepy"], "antonyms": ["awake", "alert"], "example": "The medication may make you feel drowsy, so do not drive after taking it."},
    "drowsiness": {"phonetic": "/ˈdraʊzinəs/", "pos": "n.", "meaning": "睏倦；睡意", "phrases": ["cause drowsiness"], "synonyms": ["sleepiness"], "antonyms": ["alertness"], "example": "One of the common symptoms of the flu is excessive drowsiness and fatigue."},
    "diarrhea": {"phonetic": "/ˌdaɪəˈriːə/", "pos": "n.", "meaning": "腹瀉", "phrases": [], "synonyms": [], "antonyms": [], "example": "He had to stay home from work today because he was suffering from diarrhea."},
    "cramp": {"phonetic": "/kræmp/", "pos": "n./v.", "meaning": "抽筋；腹痛；束縛", "phrases": ["muscle cramp", "stomach cramp"], "synonyms": ["spasm"], "antonyms": [], "example": "She had to stop running because of a sudden muscle cramp in her leg."},
    "nausea": {"phonetic": "/ˈnɔːziə/", "pos": "n.", "meaning": "噁心；反胃", "phrases": ["feel nausea"], "synonyms": ["sickness"], "antonyms": [], "example": "Motion sickness can cause symptoms such as nausea and dizziness."},
    "vomit": {"phonetic": "/ˈvɑːmɪt/", "pos": "v./n.", "meaning": "嘔吐", "phrases": [], "synonyms": ["throw up"], "antonyms": [], "example": "The child felt very sick and started to vomit after eating the spoiled food."},
    "medicine": {"phonetic": "/ˈmedɪsn/", "pos": "n.", "meaning": "藥；醫學", "phrases": ["take medicine", "modern medicine"], "synonyms": ["medication", "drug"], "antonyms": [], "example": "The doctor gave me some medicine to help with the pain in my back."},
    "medication": {"phonetic": "/ˌmedɪˈkeɪʃn/", "pos": "n.", "meaning": "藥物治療；藥劑", "phrases": ["prescribed medication"], "synonyms": ["medicine", "drug"], "antonyms": [], "example": "Please make sure you take your medication at the same time every day."},
    "physician": {"phonetic": "/fɪˈzɪʃn/", "pos": "n.", "meaning": "醫師；內科醫師", "phrases": ["family physician"], "synonyms": ["doctor", "MD"], "antonyms": [], "example": "You should consult your physician before starting any new exercise program."},
    "surgeon": {"phonetic": "/ˈsɜːrdʒən/", "pos": "n.", "meaning": "外科醫師", "phrases": ["heart surgeon"], "synonyms": [], "antonyms": [], "example": "The surgeon performed a difficult five-hour operation to repair the damage."},
    "calcium": {"phonetic": "/ˈkælsiəm/", "pos": "n.", "meaning": "鈣", "phrases": ["calcium deficiency"], "synonyms": [], "antonyms": [], "example": "Milk and cheese are excellent sources of calcium, which is essential for healthy bones."},
    "chemotherapy": {"phonetic": "/ˌkiːmoʊˈθerəpi/", "pos": "n.", "meaning": "化療", "phrases": ["undergo chemotherapy"], "synonyms": ["chemo"], "antonyms": [], "example": "The patient is currently undergoing chemotherapy to treat the cancer."},
    "dentist": {"phonetic": "/ˈdentɪst/", "pos": "n.", "meaning": "牙醫師", "phrases": ["visit the dentist"], "synonyms": [], "antonyms": [], "example": "I have an appointment with the dentist at 3 PM for a regular check-up."},
    "senior citizen": {"phonetic": "/ˈsiːniər ˈsɪtɪzn/", "pos": "n. phr.", "meaning": "銀髮族；高齡者", "phrases": ["discount for senior citizens"], "synonyms": ["elderly", "pensioner"], "antonyms": ["youth"], "example": "The museum offers a discounted admission price for senior citizens."},
    "athlete": {"phonetic": "/ˈæθliːt/", "pos": "n.", "meaning": "運動員", "phrases": ["professional athlete"], "synonyms": ["player", "competitor"], "antonyms": [], "example": "The company sponsors several young athletes to help them achieve their goals."},
    "dose": {"phonetic": "/doʊs/", "pos": "n./v.", "meaning": "劑量；一劑", "phrases": ["daily dose", "recommended dose"], "synonyms": ["amount", "portion"], "antonyms": [], "example": "The recommended dose for this medication is one tablet every eight hours."},
    "digestion": {"phonetic": "/daɪˈdʒestʃən/", "pos": "n.", "meaning": "消化", "phrases": ["poor digestion"], "synonyms": [], "antonyms": [], "example": "Eating slowly and chewing your food properly can help improve your digestion."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in gap_fill_gold_1:
        update_info = gap_fill_gold_1[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("完成金色等級補漏第 1 部分 (Audiovisual 到 Digestion)。")
