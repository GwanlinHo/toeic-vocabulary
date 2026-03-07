import json

# 第 501-550 個高品質單字對應表 (金色等級)
enriched_data_gold_11 = {
    "conservative": {"phonetic": "/kənˈsɜːrvətɪv/", "pos": "adj./n.", "meaning": "保守的；守舊的", "phrases": ["conservative estimate"], "synonyms": ["traditional", "conventional"], "antonyms": ["liberal", "radical"], "example": "The company takes a conservative approach to investing its surplus funds."},
    "incentive": {"phonetic": "/ɪnˈsentɪv/", "pos": "n./adj.", "meaning": "激勵；獎勵", "phrases": ["financial incentive", "tax incentive"], "synonyms": ["motivation", "stimulus"], "antonyms": ["deterrent"], "example": "The government offers tax incentives to companies that invest in renewable energy."},
    "safety net program": {"phonetic": "/ˈseɪfti net ˈproʊɡræm/", "pos": "n. phr.", "meaning": "社會安全網計畫", "phrases": [], "synonyms": ["social welfare program"], "antonyms": [], "example": "The government is expanding its safety net programs to help families living in poverty."},
    "steep": {"phonetic": "/stiːp/", "pos": "adj.", "meaning": "陡峭的；急劇的；過高的", "phrases": ["steep decline", "steep price"], "synonyms": ["sharp", "abrupt", "expensive"], "antonyms": ["gradual", "gentle"], "example": "The company has seen a steep decline in profits due to increased competition."},
    "on-and-off relationship": {"phonetic": "/ɑːn ænd ɔːf rɪˈleɪʃnʃɪp/", "pos": "n. phr.", "meaning": "分分合合的關係", "phrases": [], "synonyms": [], "antonyms": [], "example": "They have had an on-and-off relationship for several years before finally getting married."},
    "counterpart": {"phonetic": "/ˈkaʊntərpɑːrt/", "pos": "n.", "meaning": "對等的人或物", "phrases": ["foreign counterpart"], "synonyms": ["equivalent", "match"], "antonyms": [], "example": "The CEO met with his counterpart from the rival firm to discuss a potential merger."},
    "precipitate": {"phonetic": "/prɪˈsɪpɪteɪt/", "pos": "v./adj./n.", "meaning": "促成；加速；魯莽的", "phrases": ["precipitate a crisis"], "synonyms": ["trigger", "spark", "hasty"], "antonyms": [], "example": "The sudden increase in interest rates could precipitate an economic crisis."},
    "stigma": {"phonetic": "/ˈstɪɡmə/", "pos": "n.", "meaning": "恥辱；污名", "phrases": ["social stigma"], "synonyms": ["shame", "disgrace"], "antonyms": ["honor", "pride"], "example": "There is still a social stigma attached to mental illness in many cultures."},
    "uncommitted relationship": {"phonetic": "/ˌʌnkəˈmɪtɪd rɪˈleɪʃnʃɪp/", "pos": "n. phr.", "meaning": "不確定的關係；非承諾性關係", "phrases": [], "synonyms": [], "antonyms": ["committed relationship"], "example": "He prefers having an uncommitted relationship because he values his independence."},
    "plunge": {"phonetic": "/plʌndʒ/", "pos": "v./n.", "meaning": "驟降；猛跌；投入", "phrases": ["stock market plunge"], "synonyms": ["drop", "plummet", "dive"], "antonyms": ["rise", "soar"], "example": "The company's share price plunged following the news of the financial scandal."},
    "prompt": {"phonetic": "/prɑːmpt/", "pos": "v./adj./n.", "meaning": "促使；迅速的；提示", "phrases": ["prompt reply"], "synonyms": ["cause", "immediate"], "antonyms": ["slow", "delayed"], "example": "We would like to thank you for your prompt response to our inquiry."},
    "cognitive": {"phonetic": "/ˈkɑːɡnətɪv/", "pos": "adj.", "meaning": "認知的", "phrases": ["cognitive development"], "synonyms": ["mental", "intellectual"], "antonyms": [], "example": "The researchers are studying the cognitive effects of aging on the brain."},
    "a rotating cast": {"phonetic": "/ə roʊˈteɪtɪŋ kæst/", "pos": "n. phr.", "meaning": "輪替名單/陣容", "phrases": [], "synonyms": [], "antonyms": [], "example": "The TV show features a rotating cast of expert commentators every week."},
    "run off with": {"phonetic": "/rʌn ɔːf wɪð/", "pos": "v. phr.", "meaning": "與...私奔；偷走", "phrases": [], "synonyms": ["elope", "steal"], "antonyms": [], "example": "The former employee was accused of running off with confidential company documents."},
    "on average": {"phonetic": "/ɑːn ˈævərɪdʒ/", "pos": "adv. phr.", "meaning": "平均而言", "phrases": [], "synonyms": ["generally"], "antonyms": [], "example": "On average, the company processes five hundred orders every single day."},
    "lend a hand": {"phonetic": "/lend ə hænd/", "pos": "v. phr.", "meaning": "幫忙；協助", "phrases": [], "synonyms": ["help", "assist"], "antonyms": [], "example": "Several colleagues were happy to lend a hand when I was struggling with the project."},
    "end up": {"phonetic": "/end ʌp/", "pos": "v. phr.", "meaning": "最終；結果是", "phrases": ["end up doing something"], "synonyms": ["finish", "wind up"], "antonyms": [], "example": "We missed the last train and ended up taking a taxi all the way home."},
    "minorities": {"phonetic": "/maɪˈnɔːrətiːz/", "pos": "n.", "meaning": "少數民族；少數群體(複數)", "phrases": ["ethnic minorities"], "synonyms": [], "antonyms": ["majorities"], "example": "The government is committed to protecting the rights of ethnic minorities in the country."},
    "settled into": {"phonetic": "/ˈsetld ˈɪntuː/", "pos": "v. phr.", "meaning": "適應；習慣於", "phrases": [], "synonyms": ["adjust to"], "antonyms": [], "example": "She has finally settled into her new role as the department manager."},
    "poverty": {"phonetic": "/ˈpɑːvərti/", "pos": "n.", "meaning": "貧窮", "phrases": ["live in poverty", "poverty line"], "synonyms": ["destitution", "need"], "antonyms": ["wealth", "prosperity"], "example": "The organization works to provide education and healthcare to children living in poverty."},
    "cite": {"phonetic": "/saɪt/", "pos": "v.", "meaning": "引用；舉出", "phrases": ["cite an example"], "synonyms": ["quote", "mention"], "antonyms": [], "example": "The report cites several successful case studies to support its recommendations."},
    "honked horns": {"phonetic": "/hɑːŋkt hɔːrnz/", "pos": "v. phr.", "meaning": "按喇叭(複數)", "phrases": [], "synonyms": [], "antonyms": [], "example": "Frustrated drivers honked horns as they waited in the massive traffic jam."},
    "deep into the night": {"phonetic": "/diːp ˈɪntuː ðə naɪt/", "pos": "adv. phr.", "meaning": "深夜時分", "phrases": [], "synonyms": [], "antonyms": [], "example": "The negotiations continued deep into the night before an agreement was reached."},
    "troops": {"phonetic": "/truːps/", "pos": "n.", "meaning": "軍隊；部隊(複數)", "phrases": ["military troops"], "synonyms": ["soldiers", "forces"], "antonyms": [], "example": "The government has sent troops to the region to maintain peace and order."},
    "play down": {"phonetic": "/pleɪ daʊn/", "pos": "v. phr.", "meaning": "淡化；貶低其重要性", "phrases": [], "synonyms": ["minimize", "understate"], "antonyms": ["exaggerate", "highlight"], "example": "The company tried to play down the significance of the recent data breach."},
    "hinder": {"phonetic": "/ˈhɪndər/", "pos": "v.", "meaning": "阻礙；妨礙", "phrases": ["hinder progress"], "synonyms": ["obstruct", "impede"], "antonyms": ["help", "assist", "facilitate"], "example": "The lack of funding has continued to hinder the progress of the research project."},
    "Nonetheless": {"phonetic": "/ˌnʌnðəˈles/", "pos": "adv.", "meaning": "儘管如此", "phrases": [], "synonyms": ["nevertheless", "however"], "antonyms": [], "example": "The report was long and complex; nonetheless, it provided some very useful insights."},
    "tribal": {"phonetic": "/ˈtraɪbl/", "pos": "adj.", "meaning": "部落的", "phrases": ["tribal leader"], "synonyms": [], "antonyms": [], "example": "The researchers are studying the traditional customs of local tribal communities."},
    "any given night": {"phonetic": "/ˈeni ˈɡɪvn naɪt/", "pos": "phr.", "meaning": "在任何一個晚上", "phrases": [], "synonyms": [], "antonyms": [], "example": "On any given night, thousands of people sleep on the streets of the city center."},
    "take refuge in": {"phonetic": "/teɪk ˈrefjuːdʒ ɪn/", "pos": "v. phr.", "meaning": "避難；避入", "phrases": [], "synonyms": ["seek shelter in"], "antonyms": [], "example": "Many families were forced to take refuge in the local community center during the flood."},
    "vulnerable group": {"phonetic": "/ˈvʌlnərəbl ɡruːp/", "pos": "n. phr.", "meaning": "弱勢群體", "phrases": [], "synonyms": [], "antonyms": [], "example": "The new policy is designed to provide better support for vulnerable groups in society."},
    "prone to": {"phonetic": "/proʊn tuː/", "pos": "adj. phr.", "meaning": "易於...的；傾向於", "phrases": ["accident prone"], "synonyms": ["susceptible to", "likely to"], "antonyms": ["resistant to"], "example": "Small businesses are particularly prone to failure during their first year of operation."},
    "harassment": {"phonetic": "/həˈræsmənt/", "pos": "n.", "meaning": "騷擾", "phrases": ["sexual harassment", "workplace harassment"], "synonyms": ["bullying", "intimidation"], "antonyms": [], "example": "The company has a zero-tolerance policy regarding any form of workplace harassment."},
    "violence": {"phonetic": "/ˈvaɪələns/", "pos": "n.", "meaning": "暴力", "phrases": ["domestic violence"], "synonyms": ["force", "brutality"], "antonyms": ["peace"], "example": "The government is launching a new campaign to reduce levels of violence in the city."},
    "enduring": {"phonetic": "/ɪnˈdʊrɪŋ/", "pos": "adj.", "meaning": "持久的；長期的", "phrases": ["enduring success"], "synonyms": ["lasting", "permanent"], "antonyms": ["temporary", "brief"], "example": "The classic design of the car has an enduring appeal for many collectors."},
    "presence": {"phonetic": "/ˈprezns/", "pos": "n.", "meaning": "存在；出席；風采", "phrases": ["online presence", "strong presence"], "synonyms": ["attendance", "existence"], "antonyms": ["absence"], "example": "The company is planning to expand its online presence to reach more customers."},
    "Long-standing": {"phonetic": "/ˈlɔːŋˌstændɪŋ/", "pos": "adj.", "meaning": "長期的；存在已久的", "phrases": ["long-standing tradition"], "synonyms": ["established", "enduring"], "antonyms": ["new", "recent"], "example": "The two countries have a long-standing agreement regarding trade and security."},
    "myths": {"phonetic": "/mɪθs/", "pos": "n.", "meaning": "神話；迷思(複數)", "phrases": ["popular myths"], "synonyms": ["legends", "misconceptions"], "antonyms": ["facts"], "example": "There are many myths about the risks associated with the new technology."},
    "mythology": {"phonetic": "/mɪˈθɑːlədʒi/", "pos": "n.", "meaning": "神話學；神話(總稱)", "phrases": ["Greek mythology"], "synonyms": [], "antonyms": [], "example": "His new book explores the role of mythology in modern popular culture."},
    "reckless": {"phonetic": "/ˈrekləs/", "pos": "adj.", "meaning": "魯莽的；不計後果的", "phrases": ["reckless driving", "reckless behavior"], "synonyms": ["careless", "rash"], "antonyms": ["careful", "cautious"], "example": "The company was criticized for its reckless disregard for safety regulations."},
    "drug use": {"phonetic": "/drʌɡ juːs/", "pos": "n. phr.", "meaning": "藥物使用；吸毒", "phrases": ["illegal drug use"], "synonyms": ["substance abuse"], "antonyms": [], "example": "The health organization is raising awareness about the dangers of illegal drug use."},
    "reluctant": {"phonetic": "/rɪˈlʌktənt/", "pos": "adj.", "meaning": "不情願的；勉強的", "phrases": ["reluctant to do something"], "synonyms": ["unwilling", "hesitant"], "antonyms": ["willing", "eager"], "example": "The manager was reluctant to approve the new project without seeing more data."},
    "be fraught with": {"phonetic": "/bi frɔːt wɪð/", "pos": "v. phr.", "meaning": "充滿(危險/困難)", "phrases": ["fraught with danger"], "synonyms": ["filled with"], "antonyms": [], "example": "The project was fraught with difficulties from the very beginning."},
    "awkwardness": {"phonetic": "/ˈɔːkwərdnəs/", "pos": "n.", "meaning": "尷尬；彆扭", "phrases": ["moment of awkwardness"], "synonyms": ["embarrassment"], "antonyms": ["confidence", "grace"], "example": "There was a sense of awkwardness in the room after the two colleagues argued."},
    "pervasive": {"phonetic": "/pərˈveɪsɪv/", "pos": "adj.", "meaning": "普遍的；遍布的", "phrases": ["pervasive influence"], "synonyms": ["widespread", "prevalent"], "antonyms": ["rare", "limited"], "example": "The influence of social media is pervasive in modern society, affecting all age groups."},
    "well-intentioned": {"phonetic": "/ˌwel ɪnˈtenʃənd/", "pos": "adj.", "meaning": "出於好心的；善意的", "phrases": [], "synonyms": ["kind-hearted"], "antonyms": ["malicious"], "example": "Although the new policy was well-intentioned, it had several unexpected negative consequences."},
    "exacerbate": {"phonetic": "/ɪɡˈzæsərbeɪt/", "pos": "v.", "meaning": "使加劇；使惡化", "phrases": ["exacerbate the problem"], "synonyms": ["aggravate", "worsen"], "antonyms": ["improve", "alleviate"], "example": "The sudden drop in temperature could exacerbate the patient's respiratory condition."},
    "combat": {"phonetic": "/ˈkɑːmbæt/", "pos": "v./n.", "meaning": "打擊；戰鬥", "phrases": ["combat crime", "combat inflation"], "synonyms": ["fight", "tackle"], "antonyms": ["support", "encourage"], "example": "The government is taking new measures to combat the problem of youth unemployment."},
    "missteps": {"phonetic": "/ˌmɪsˈsteps/", "pos": "n.", "meaning": "失誤；過失(複數)", "phrases": ["political missteps"], "synonyms": ["errors", "mistakes"], "antonyms": ["successes"], "example": "The company's recent missteps have led to a significant drop in its market share."},
    "along the lines": {"phonetic": "/əˈlɔːŋ ðə laɪnz/", "pos": "phr.", "meaning": "類似於...；依照...", "phrases": ["something along the lines of"], "synonyms": ["similar to"], "antonyms": [], "example": "The new marketing strategy will be along the lines of our successful campaign last year."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_11:
        update_info = enriched_data_gold_11[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 501-550 個單字。")
