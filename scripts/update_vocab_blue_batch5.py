import json

# 第 201-245 個高品質單字對應表 (藍色等級)
enriched_data_blue_5 = {
    "sporadic": {"phonetic": "/spəˈrædɪk/", "pos": "adj.", "meaning": "零星的；斷斷續續的", "phrases": ["sporadic fighting"], "synonyms": ["intermittent", "occasional"], "antonyms": ["constant", "continuous"], "example": "There has been sporadic fighting in the region despite the recent ceasefire agreement."},
    "straightforward": {"phonetic": "/ˌstreɪtˈfɔːrwərd/", "pos": "adj.", "meaning": "簡單直截的；坦率的", "phrases": ["straightforward process"], "synonyms": ["simple", "direct"], "antonyms": ["complex", "complicated"], "example": "The application process is quite straightforward and should only take a few minutes."},
    "succinct": {"phonetic": "/səkˈsɪŋkt/", "pos": "adj.", "meaning": "簡潔扼要的", "phrases": ["succinct summary"], "synonyms": ["concise", "brief"], "antonyms": ["wordy", "verbose"], "example": "The manager gave a succinct summary of the project's progress during the meeting."},
    "superb": {"phonetic": "/suːˈpɜːrb/", "pos": "adj.", "meaning": "極好的；卓越的", "phrases": ["superb service"], "synonyms": ["excellent", "outstanding"], "antonyms": ["poor", "inferior"], "example": "The restaurant is famous for its superb service and delicious international cuisine."},
    "superfluous": {"phonetic": "/suːˈpɜːrfluəs/", "pos": "adj.", "meaning": "多餘的；累贅的", "phrases": ["superfluous information"], "synonyms": ["excess", "redundant"], "antonyms": ["necessary", "essential"], "example": "Please remove any superfluous information from the report to make it more concise."},
    "susceptible": {"phonetic": "/səˈseptəbl/", "pos": "adj.", "meaning": "易受影響的；易受感染的", "phrases": ["be susceptible to"], "synonyms": ["vulnerable", "prone"], "antonyms": ["resistant", "immune"], "example": "Children and the elderly are more susceptible to certain types of respiratory diseases."},
    "suspect": {"phonetic": "/səˈspekt/", "pos": "v./n./adj.", "meaning": "懷疑；嫌疑犯", "phrases": ["prime suspect"], "synonyms": ["doubt", "distrust"], "antonyms": ["trust", "believe"], "example": "The police suspect that the fire was started deliberately by someone inside the building."},
    "swift": {"phonetic": "/swɪft/", "pos": "adj.", "meaning": "快速的；敏捷的", "phrases": ["swift action"], "synonyms": ["rapid", "fast"], "antonyms": ["slow", "sluggish"], "example": "The company took swift action to address the customer's complaints about the service."},
    "talkative": {"phonetic": "/ˈtɔːkətɪv/", "pos": "adj.", "meaning": "愛說話的", "phrases": [], "synonyms": ["chatty", "garrulous"], "antonyms": ["quiet", "reticent"], "example": "He is a very talkative person who enjoys meeting and chatting with new people."},
    "tender": {"phonetic": "/ˈtendər/", "pos": "adj./v./n.", "meaning": "溫柔的；投標；償付", "phrases": ["legal tender", "submit a tender"], "synonyms": ["gentle", "bid"], "antonyms": ["tough", "hard"], "example": "The company decided to submit a tender for the new government construction project."},
    "tantamount": {"phonetic": "/ˈtæntəmaʊnt/", "pos": "adj.", "meaning": "相當於；等於", "phrases": ["be tantamount to"], "synonyms": ["equivalent"], "antonyms": [], "example": "Her refusal to answer the question was seen as tantamount to an admission of guilt."},
    "zone": {"phonetic": "/zoʊn/", "pos": "n./v.", "meaning": "區域；地帶", "phrases": ["time zone", "pedestrian zone"], "synonyms": ["area", "region"], "antonyms": [], "example": "The city center has been designated as a pedestrian-only zone for the weekend."},
    "stopwatch": {"phonetic": "/ˈstɑːpwɑːtʃ/", "pos": "n.", "meaning": "秒錶；跑錶", "phrases": [], "synonyms": ["timer"], "antonyms": [], "example": "The coach used a stopwatch to time the runners during the training session."},
    "timepiece": {"phonetic": "/ˈtaɪmpiːs/", "pos": "n.", "meaning": "鐘；錶", "phrases": [], "synonyms": ["clock", "watch"], "antonyms": [], "example": "The antique timepiece was handed down through several generations of his family."},
    "timeless": {"phonetic": "/ˈtaɪmləs/", "pos": "adj.", "meaning": "永恆的；不受時間影響的", "phrases": ["timeless design"], "synonyms": ["eternal", "enduring"], "antonyms": ["temporary"], "example": "The design of the classic car is truly timeless and still looks modern today."},
    "chronometer": {"phonetic": "/krəˈnɑːmɪtər/", "pos": "n.", "meaning": "精密計時器", "phrases": [], "synonyms": ["chronograph"], "antonyms": [], "example": "The ship's captain used a chronometer to determine the exact time for navigation."},
    "guarantee": {"phonetic": "/ˌɡærənˈtiː/", "pos": "n./v.", "meaning": "保證；擔保", "phrases": ["money-back guarantee"], "synonyms": ["warranty", "assurance"], "antonyms": [], "example": "The new laptop comes with a two-year guarantee against any manufacturing defects."},
    "alarm clock": {"phonetic": "/əˈlɑːrm klɑːk/", "pos": "n. phr.", "meaning": "鬧鐘", "phrases": ["set an alarm clock"], "synonyms": ["alarm"], "antonyms": [], "example": "I set my alarm clock for 6 AM so that I would have enough time to get to the airport."},
    "grandfather clock": {"phonetic": "/ˈɡrænˌfɑːðər klɑːk/", "pos": "n. phr.", "meaning": "老式大擺鐘", "phrases": [], "synonyms": ["longcase clock"], "antonyms": [], "example": "The large grandfather clock in the hallway chimed every hour on the hour."},
    "announcements": {"phonetic": "/əˈnaʊnsmənts/", "pos": "n.", "meaning": "公告；宣佈(複數)", "phrases": ["public announcements"], "synonyms": ["notifications", "proclamations"], "antonyms": [], "example": "Please listen carefully to the announcements for information about your flight."},
    "notices": {"phonetic": "/ˈnoʊtɪsɪz/", "pos": "n.", "meaning": "通知；告示(複數)", "phrases": ["legal notices"], "synonyms": ["posters", "leaflets"], "antonyms": [], "example": "Several notices were posted on the bulletin board regarding the upcoming office move."},
    "cut down on": {"phonetic": "/kʌt daʊn ɑːn/", "pos": "v. phr.", "meaning": "減少；削減", "phrases": [], "synonyms": ["reduce", "decrease"], "antonyms": ["increase"], "example": "The company is trying to cut down on unnecessary expenses to improve its profits."},
    "put~into operation": {"phonetic": "/pʊt ˈɪntuː ˌɑːpəˈreɪʃn/", "pos": "v. phr.", "meaning": "實施；使運作", "phrases": [], "synonyms": ["implement", "activate"], "antonyms": ["halt", "suspend"], "example": "The new security system is expected to be put into operation early next month."},
    "call off": {"phonetic": "/kɔːl ɔːf/", "pos": "v. phr.", "meaning": "取消", "phrases": [], "synonyms": ["cancel", "abandon"], "antonyms": ["confirm", "proceed"], "example": "The meeting was called off at the last minute because the CEO was unable to attend."},
    "transportation": {"phonetic": "/ˌtrænspərˈteɪʃn/", "pos": "n.", "meaning": "運輸；交通工具", "phrases": ["public transportation"], "synonyms": ["transit", "conveyance"], "antonyms": [], "example": "Public transportation in the city is very efficient and relatively inexpensive."},
    "fill out/in a form": {"phonetic": "/fɪl aʊt ə fɔːrm/", "pos": "v. phr.", "meaning": "填寫表格", "phrases": [], "synonyms": ["complete a form"], "antonyms": [], "example": "Please fill out the application form and return it to the human resources department."},
    "admission": {"phonetic": "/ədˈmɪʃn/", "pos": "n.", "meaning": "入場費；承認", "phrases": ["admission fee"], "synonyms": ["entry", "entrance"], "antonyms": ["exit", "denial"], "example": "The cost of admission to the museum is ten dollars for adults and five dollars for children."},
    "courteous": {"phonetic": "/ˈkɜːrtiəs/", "pos": "adj.", "meaning": "彬彬有禮的", "phrases": ["courteous staff"], "synonyms": ["polite", "respectful"], "antonyms": ["rude", "impolite"], "example": "The hotel staff were very courteous and helpful during our stay."},
    "spacious": {"phonetic": "/ˈspeɪʃəs/", "pos": "adj.", "meaning": "寬敞的", "phrases": ["spacious office"], "synonyms": ["roomy", "large"], "antonyms": ["cramped", "small"], "example": "Our new office is much more spacious than the old one and has better facilities."},
    "well-equipped": {"phonetic": "/ˌwel ɪˈkwɪpt/", "pos": "adj.", "meaning": "裝備精良的", "phrases": ["well-equipped gym"], "synonyms": ["modernized"], "antonyms": ["poorly-equipped"], "example": "The new research facility is well-equipped with the latest scientific instruments."},
    "resort": {"phonetic": "/rɪˈzɔːrt/", "pos": "n./v.", "meaning": "度假勝地；訴諸", "phrases": ["summer resort", "resort to"], "synonyms": ["holiday spot"], "antonyms": [], "example": "The company is building a new luxury resort on the island to attract more tourists."},
    "canoe": {"phonetic": "/kəˈnuː/", "pos": "n./v.", "meaning": "獨木舟", "phrases": ["paddling a canoe"], "synonyms": ["boat", "kayak"], "antonyms": [], "example": "We spent the afternoon paddling a canoe along the calm waters of the river."},
    "check out": {"phonetic": "/tʃek aʊt/", "pos": "v. phr.", "meaning": "結帳退房；檢查", "phrases": ["late check-out"], "synonyms": ["leave", "inspect"], "antonyms": ["check in"], "example": "Please remember to return your room key when you check out of the hotel."},
    "speedy": {"phonetic": "/ˈspiːdi/", "pos": "adj.", "meaning": "快速的", "phrases": ["speedy recovery", "speedy response"], "synonyms": ["quick", "rapid"], "antonyms": ["slow"], "example": "We would like to thank you for your speedy response to our inquiry."},
    "receptionist": {"phonetic": "/rɪˈsepʃənɪst/", "pos": "n.", "meaning": "接待員", "phrases": [], "synonyms": ["clerk"], "antonyms": [], "example": "The receptionist will show you to the conference room when you arrive."},
    "reception": {"phonetic": "/rɪˈsepʃn/", "pos": "n.", "meaning": "接待處；歡迎會", "phrases": ["wedding reception", "reception desk"], "synonyms": ["welcome", "greeting"], "antonyms": [], "example": "The company held a special reception to welcome the new international clients."},
    "come to one's assistance": {"phonetic": "/kʌm tuː wʌnz əˈsɪstəns/", "pos": "v. phr.", "meaning": "前來援助", "phrases": [], "synonyms": ["help", "aid"], "antonyms": ["abandon"], "example": "Several colleagues came to my assistance when I was struggling with the heavy boxes."},
    "non-profit": {"phonetic": "/ˌnɑːnˈprɑːfɪt/", "pos": "adj./n.", "meaning": "非營利的；非營利組織", "phrases": ["non-profit organization"], "synonyms": ["charitable"], "antonyms": ["for-profit"], "example": "He decided to leave his corporate job to work for a non-profit organization."},
    "promising": {"phonetic": "/ˈprɑːmɪsɪŋ/", "pos": "adj.", "meaning": "有前途的；有希望的", "phrases": ["promising future"], "synonyms": ["hopeful", "encouraging"], "antonyms": ["hopeless", "discouraging"], "example": "The new marketing strategy has shown some promising results in the initial testing phase."},
    "entrepreneur": {"phonetic": "/ˌɑːntrəprəˈnɜːr/", "pos": "n.", "meaning": "企業家；創業家", "phrases": ["successful entrepreneur"], "synonyms": ["businessman", "founder"], "antonyms": [], "example": "He is a successful entrepreneur who has started several technology companies."},
    "headquarters": {"phonetic": "/ˈhedkwɔːrtərz/", "pos": "n.", "meaning": "總部", "phrases": ["corporate headquarters"], "synonyms": ["HQ", "main office"], "antonyms": [], "example": "The company's international headquarters are located in a modern building in London."},
    "finalist": {"phonetic": "/ˈfaɪnəlɪst/", "pos": "n.", "meaning": "決賽選手", "phrases": ["competition finalist"], "synonyms": ["contender"], "antonyms": [], "example": "The three finalists will be invited to give a presentation to the board of directors."},
    "seed money/capital": {"phonetic": "/siːd ˈmʌni/", "pos": "n. phr.", "meaning": "種子資金；創業資本", "phrases": ["startup seed money"], "synonyms": ["initial capital"], "antonyms": [], "example": "The entrepreneur is looking for seed money to help fund his new technology startup."},
    "application": {"phonetic": "/ˌæplɪˈkeɪʃn/", "pos": "n.", "meaning": "申請；應用", "phrases": ["job application", "application form"], "synonyms": ["petition", "request"], "antonyms": [], "example": "Please submit your job application via the company's online recruitment portal."}
}

with open('data_blue.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_blue_5:
        update_info = enriched_data_blue_5[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_blue.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修藍色等級最後一批單字 (第 201-245 個)。")
