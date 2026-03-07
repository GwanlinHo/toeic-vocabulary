import json

# 第 51-100 個高品質單字對應表 (藍色等級)
enriched_data_blue_2 = {
    "vacillate": {"phonetic": "/ˈvæsəleɪt/", "pos": "v.", "meaning": "動搖不定；猶豫", "phrases": [], "synonyms": ["hesitate", "waver"], "antonyms": [], "example": "He tended to vacillate between the two options before making a final decision."},
    "validate": {"phonetic": "/ˈvælɪdeɪt/", "pos": "v.", "meaning": "證實；使有效", "phrases": [], "synonyms": ["verify", "confirm"], "antonyms": ["invalidate"], "example": "The data from the survey helped to validate the marketing team's initial assumptions."},
    "veil": {"phonetic": "/veɪl/", "pos": "n./v.", "meaning": "遮蓋；面紗", "phrases": ["under a veil of secrecy"], "synonyms": ["cover", "mask"], "antonyms": ["reveal"], "example": "The new product design was kept under a veil of secrecy until the official launch."},
    "verify": {"phonetic": "/ˈverɪfaɪ/", "pos": "v.", "meaning": "證實；驗證", "phrases": ["verify account"], "synonyms": ["confirm", "check"], "antonyms": [], "example": "Please verify your account details before submitting the online application form."},
    "vilify": {"phonetic": "/ˈvɪlɪfaɪ/", "pos": "v.", "meaning": "誹謗；詆毀", "phrases": [], "synonyms": ["slander", "defame"], "antonyms": ["praise", "honor"], "example": "The politician was vilified by the press for his controversial remarks."},
    "withstand": {"phonetic": "/wɪðˈstænd/", "pos": "v.", "meaning": "抵擋；經受住", "phrases": [], "synonyms": ["endure", "resist"], "antonyms": ["surrender", "yield"], "example": "The new building was designed to withstand even the most severe earthquakes."},
    "wrench": {"phonetic": "/rentʃ/", "pos": "v./n.", "meaning": "扭轉；猛扭", "phrases": [], "synonyms": ["twist", "jerk"], "antonyms": [], "example": "He managed to wrench the door open and escape from the burning building."},
    "adamant": {"phonetic": "/ˈædəmənt/", "pos": "adj.", "meaning": "堅定不移的", "phrases": [], "synonyms": ["stubborn", "unyielding"], "antonyms": ["flexible"], "example": "The manager was adamant that the project must be completed by Friday."},
    "adequate": {"phonetic": "/ˈædəkwət/", "pos": "adj.", "meaning": "足夠的；適當的", "phrases": ["adequate resources"], "synonyms": ["sufficient", "enough"], "antonyms": ["inadequate"], "example": "We need to ensure that we have adequate resources to complete the project on time."},
    "admirable": {"phonetic": "/ˈædmərəbl/", "pos": "adj.", "meaning": "令人欽佩的", "phrases": [], "synonyms": ["praiseworthy", "commendable"], "antonyms": [], "example": "Her dedication to her work is truly admirable and inspires the whole team."},
    "adroit": {"phonetic": "/əˈdrɔɪt/", "pos": "adj.", "meaning": "敏捷的；熟練的", "phrases": [], "synonyms": ["skillful", "expert"], "antonyms": ["clumsy"], "example": "The negotiator was adroit at finding common ground between the two parties."},
    "ahead": {"phonetic": "/əˈhed/", "pos": "adv./adj.", "meaning": "領先；在前面", "phrases": ["ahead of time", "straight ahead"], "synonyms": ["forward"], "antonyms": ["behind"], "example": "The company is currently ahead of its competitors in terms of technological innovation."},
    "alive": {"phonetic": "/əˈlaɪv/", "pos": "adj.", "meaning": "活著的；有活力的", "phrases": ["come alive"], "synonyms": ["living", "animated"], "antonyms": ["dead"], "example": "The city center comes alive at night with many restaurants and entertainment venues."},
    "ambiguous": {"phonetic": "/æmˈbɪɡjuəs/", "pos": "adj.", "meaning": "模稜兩可的", "phrases": ["ambiguous meaning"], "synonyms": ["unclear", "vague"], "antonyms": ["clear", "explicit"], "example": "The instructions were somewhat ambiguous, leading to confusion among the staff."},
    "ample": {"phonetic": "/ˈæmpl/", "pos": "adj.", "meaning": "豐富的；充足的", "phrases": ["ample opportunity"], "synonyms": ["abundant", "plentiful"], "antonyms": ["scant", "meager"], "example": "There will be ample opportunity for questions at the end of the presentation."},
    "annoying": {"phonetic": "/əˈnɔɪɪŋ/", "pos": "adj.", "meaning": "討厭的；惱人的", "phrases": [], "synonyms": ["irritating", "bothersome"], "antonyms": ["pleasing"], "example": "The constant noise from the construction site was extremely annoying for local residents."},
    "apart": {"phonetic": "/əˈpɑːrt/", "pos": "adv./adj.", "meaning": "分開地；除~外", "phrases": ["apart from"], "synonyms": ["separate", "aside"], "antonyms": ["together"], "example": "Apart from the minor technical issues, the product launch was a great success."},
    "apparently": {"phonetic": "/əˈpærəntli/", "pos": "adv.", "meaning": "顯然地；據說", "phrases": [], "synonyms": ["seemingly", "evidently"], "antonyms": [], "example": "Apparently, the company is planning to expand its operations into the Asian market."},
    "artificial": {"phonetic": "/ˌɑːrtɪˈfɪʃl/", "pos": "adj.", "meaning": "人工的；人造的", "phrases": ["artificial intelligence"], "synonyms": ["synthetic", "man-made"], "antonyms": ["natural"], "example": "The flowers in the lobby are artificial, but they look very realistic."},
    "becoming": {"phonetic": "/bɪˈkʌmɪŋ/", "pos": "adj.", "meaning": "合適的；相稱的", "phrases": [], "synonyms": ["fitting", "appropriate"], "antonyms": ["unbecoming"], "example": "That dark blue suit is very becoming on you and perfect for the interview."},
    "beneath": {"phonetic": "/bɪˈniːθ/", "pos": "prep./adv.", "meaning": "在...下面", "phrases": [], "synonyms": ["under", "below"], "antonyms": ["above"], "example": "The storage room is located beneath the main office on the ground floor."},
    "beneficent": {"phonetic": "/bəˈnefɪsnt/", "pos": "adj.", "meaning": "慈善的；行善的", "phrases": [], "synonyms": ["charitable", "benevolent"], "antonyms": ["malicious"], "example": "The billionaire is well-known for his beneficent contributions to various local charities."},
    "beyond": {"phonetic": "/bɪˈjɑːnd/", "pos": "prep./adv.", "meaning": "超過；在...那邊", "phrases": ["beyond doubt", "beyond reach"], "synonyms": ["outside"], "antonyms": ["within"], "example": "The success of the new product was far beyond the company's initial expectations."},
    "bothersome": {"phonetic": "/ˈbɑːðərsəm/", "pos": "adj.", "meaning": "令人煩惱的", "phrases": [], "synonyms": ["annoying", "troublesome"], "antonyms": ["convenient"], "example": "Having to fill out so much paperwork for a simple request is quite bothersome."},
    "bulk": {"phonetic": "/bʌlk/", "pos": "n./adj.", "meaning": "大量；大部份", "phrases": ["in bulk", "bulk purchase"], "synonyms": ["mass", "majority"], "antonyms": [], "example": "The bulk of the company's revenue comes from its international operations."},
    "buoyant": {"phonetic": "/ˈɔɪənt/", "pos": "adj.", "meaning": "看漲的；心情愉快的", "phrases": ["buoyant market"], "synonyms": ["cheerful", "vibrant"], "antonyms": ["depressed", "gloomy"], "example": "The stock market remained buoyant despite the recent economic uncertainty."},
    "candid": {"phonetic": "/ˈkændɪd/", "pos": "adj.", "meaning": "坦率的；誠實的", "phrases": ["candid opinion"], "synonyms": ["honest", "frank"], "antonyms": ["dishonest", "evasive"], "example": "The manager gave a candid assessment of the project's current progress and challenges."},
    "capital": {"phonetic": "/ˈkæpɪtl/", "pos": "n./adj.", "meaning": "資本；主要的", "phrases": ["venture capital", "capital city"], "synonyms": ["funds", "primary"], "antonyms": [], "example": "The company needs to raise more capital to fund its future expansion plans."},
    "circumspect": {"phonetic": "/ˈsɜːrkəmspekt/", "pos": "adj.", "meaning": "慎重的；小心的", "phrases": [], "synonyms": ["cautious", "wary"], "antonyms": ["careless", "reckless"], "example": "It is important to be circumspect when discussing confidential business information."},
    "coherent": {"phonetic": "/koʊˈhɪrənt/", "pos": "adj.", "meaning": "有條理的；連貫的", "phrases": ["coherent argument"], "synonyms": ["logical", "consistent"], "antonyms": ["incoherent", "confusing"], "example": "The presenter failed to provide a coherent explanation for the sudden drop in sales."},
    "cohesive": {"phonetic": "/koʊˈhiːsɪv/", "pos": "adj.", "meaning": "有凝聚力的", "phrases": ["cohesive team"], "synonyms": ["unified"], "antonyms": ["fragmented"], "example": "Our team is very cohesive and works well together to achieve our goals."},
    "collateral": {"phonetic": "/kəˈlætərəl/", "pos": "n./adj.", "meaning": "抵押品；附加的", "phrases": [], "synonyms": ["security", "guarantee"], "antonyms": [], "example": "He used his house as collateral to secure a loan for his new business venture."},
    "colloquial": {"phonetic": "/kəˈloʊkwiəl/", "pos": "adj.", "meaning": "口語的；通俗的", "phrases": [], "synonyms": ["informal", "conversational"], "antonyms": ["formal"], "example": "The training manual was written in a colloquial style to make it easier to understand."},
    "come across": {"phonetic": "/kʌm əˈkrɔːs/", "pos": "v. phr.", "meaning": "偶然發現；給人印象", "phrases": [], "synonyms": ["encounter", "find"], "antonyms": [], "example": "I came across some interesting data while researching for the annual report."},
    "come along": {"phonetic": "/kʌm əˈlɔːŋ/", "pos": "v. phr.", "meaning": "進展；伴隨", "phrases": [], "synonyms": ["progress", "advance"], "antonyms": [], "example": "The new project is coming along nicely and should be finished on schedule."},
    "comforting": {"phonetic": "/ˈkʌmfərtɪŋ/", "pos": "adj.", "meaning": "令人欣慰的", "phrases": [], "synonyms": ["reassuring", "soothing"], "antonyms": ["distressing"], "example": "It was comforting to know that we had the full support of the board of directors."},
    "committed": {"phonetic": "/kəˈmɪtɪd/", "pos": "adj.", "meaning": "忠誠的；堅定的", "phrases": ["be committed to"], "synonyms": ["dedicated", "loyal"], "antonyms": ["unfaithful"], "example": "The company is committed to providing its customers with the highest quality of service."},
    "complacent": {"phonetic": "/kəmˈpleɪsnt/", "pos": "adj.", "meaning": "自滿的；得意的", "phrases": [], "synonyms": ["satisfied", "smug"], "antonyms": ["humble", "modest"], "example": "We cannot afford to be complacent despite our recent success in the market."},
    "compliant": {"phonetic": "/kəmˈplaɪənt/", "pos": "adj.", "meaning": "順從的；符合規定的", "phrases": ["be compliant with"], "synonyms": ["obedient", "conforming"], "antonyms": ["defiant"], "example": "All new products must be fully compliant with the latest safety regulations."},
    "comcrete": {"word": "concrete", "phonetic": "/ˈkɑːnkriːt/", "pos": "adj./n.", "meaning": "具體的；混凝土", "phrases": ["concrete evidence", "reinforced concrete"], "synonyms": ["specific", "tangible"], "antonyms": ["abstract"], "example": "We need to see some concrete evidence before we can approve the new project proposal."},
    "confident": {"phonetic": "/ˈkɑːnfɪdənt/", "pos": "adj.", "meaning": "有信心的", "phrases": ["confident in"], "synonyms": ["certain", "assured"], "antonyms": ["doubtful", "hesitant"], "example": "The CEO is confident that the company will achieve its sales targets this year."},
    "confidential": {"phonetic": "/ˌkɑːnfɪˈdenʃl/", "pos": "adj.", "meaning": "機密的", "phrases": ["strictly confidential"], "synonyms": ["secret", "private"], "antonyms": ["public"], "example": "Please ensure that all confidential documents are kept in a secure location."},
    "congruent": {"phonetic": "/ˈkɑːŋɡruənt/", "pos": "adj.", "meaning": "一致的；合適的", "phrases": [], "synonyms": ["consistent", "harmonious"], "antonyms": ["incongruent"], "example": "The company's actions must be congruent with its stated values and mission."},
    "conscientious": {"phonetic": "/ˌkɑːnʃiˈenʃəs/", "pos": "adj.", "meaning": "認真負責的", "phrases": [], "synonyms": ["diligent", "careful"], "antonyms": ["irresponsible"], "example": "He is a very conscientious worker who always pays close attention to detail."},
    "consecutive": {"phonetic": "/kənˈsekjətɪv/", "pos": "adj.", "meaning": "連續的", "phrases": ["consecutive days"], "synonyms": ["successive", "sequential"], "antonyms": [], "example": "The company has seen an increase in profits for five consecutive quarters."},
    "contemporary": {"phonetic": "/kənˈtempəreri/", "pos": "adj./n.", "meaning": "當代的；同時代的人", "phrases": ["contemporary art"], "synonyms": ["modern", "current"], "antonyms": ["ancient", "old-fashioned"], "example": "The new office building features a contemporary design with lots of glass and steel."},
    "controlling": {"phonetic": "/kənˈtroʊlɪŋ/", "pos": "adj.", "meaning": "支配的；控制的", "phrases": ["controlling interest"], "synonyms": ["dominant"], "antonyms": [], "example": "The parent company holds a controlling interest in several smaller businesses."},
    "conventional": {"phonetic": "/kənˈvenʃənl/", "pos": "adj.", "meaning": "傳統的；慣例的", "phrases": ["conventional wisdom"], "synonyms": ["traditional", "standard"], "antonyms": ["unconventional", "innovative"], "example": "Conventional wisdom suggests that it is better to save money for a rainy day."},
    "conversant": {"phonetic": "/kənˈvɜːrsənt/", "pos": "adj.", "meaning": "熟悉的；精通的", "phrases": ["be conversant with"], "synonyms": ["familiar", "acquainted"], "antonyms": ["ignorant"], "example": "Our sales team is fully conversant with all the features of our new product line."},
    "credible": {"phonetic": "/ˈkredəbl/", "pos": "adj.", "meaning": "可信的；可靠的", "phrases": ["credible source"], "synonyms": ["believable", "trustworthy"], "antonyms": ["unreliable"], "example": "We need to find a credible source of information before we can make a decision."}
}

with open('data_blue.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_blue_2:
        update_info = enriched_data_blue_2[word].copy()
        # 如果對象本身有 'word' key，表示要更正單字拼法
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_blue.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修藍色等級第 51-100 個單字，並修正拼寫錯誤。")
