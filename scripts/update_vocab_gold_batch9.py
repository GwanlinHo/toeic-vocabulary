import json

# 第 401-450 個高品質單字對應表 (金色等級)
enriched_data_gold_9 = {
    "commissioner": {"phonetic": "/kəˈmɪʃənər/", "pos": "n.", "meaning": "委員；專員", "phrases": ["European Commissioner"], "synonyms": ["official", "delegate"], "antonyms": [], "example": "The health commissioner is responsible for overseeing the city's vaccination program."},
    "epidemic": {"phonetic": "/ˌepɪˈdemɪk/", "pos": "n./adj.", "meaning": "流行病；傳染性的", "phrases": ["flu epidemic"], "synonyms": ["outbreak", "plague"], "antonyms": [], "example": "The government is taking urgent measures to control the spread of the epidemic."},
    "intractable": {"phonetic": "/ɪnˈtræktəbl/", "pos": "adj.", "meaning": "難以處理的；棘手的", "phrases": ["intractable problem"], "synonyms": ["stubborn", "difficult"], "antonyms": ["manageable", "docile"], "example": "The two countries have been unable to find a solution to their intractable border dispute."},
    "national conversation": {"phonetic": "/ˈnæʃnəl ˌkɑːnvərˈseɪʃn/", "pos": "n. phr.", "meaning": "全國性的討論；社會輿論", "phrases": [], "synonyms": [], "antonyms": [], "example": "The report sparked a national conversation about the need for better mental health services."},
    "aggressive": {"phonetic": "/əˈɡresɪv/", "pos": "adj.", "meaning": "積極進取的；侵略性的", "phrases": ["aggressive marketing"], "synonyms": ["assertive", "hostile"], "antonyms": ["passive", "peaceful"], "example": "The company has launched an aggressive marketing campaign to increase its market share."},
    "underscored": {"phonetic": "/ˌʌndərˈskɔːrd/", "pos": "adj./v.", "meaning": "強調的；在...下方劃線", "phrases": [], "synonyms": ["emphasized", "stressed"], "antonyms": [], "example": "The recent economic crisis has underscored the importance of financial stability."},
    "broad": {"phonetic": "/brɔːd/", "pos": "adj.", "meaning": "廣泛的；寬廣的", "phrases": ["broad experience", "broad range"], "synonyms": ["wide", "extensive"], "antonyms": ["narrow"], "example": "The manager has a broad range of experience in both marketing and finance."},
    "assault": {"phonetic": "/əˈsɔːlt/", "pos": "n./v.", "meaning": "攻擊；襲擊", "phrases": ["physical assault"], "synonyms": ["attack", "strike"], "antonyms": ["defense"], "example": "The company faces an assault from competitors who are offering lower prices."},
    "single servings": {"phonetic": "/ˈsɪŋɡl ˈsɜːrvɪŋz/", "pos": "n. phr.", "meaning": "單人份食品", "phrases": [], "synonyms": [], "antonyms": [], "example": "The store sells single servings of yogurt and other snacks for people on the go."},
    "deep fryer": {"phonetic": "/diːp ˈfraɪər/", "pos": "n. phr.", "meaning": "深層炸鍋", "phrases": [], "synonyms": [], "antonyms": [], "example": "The restaurant's kitchen is equipped with a modern deep fryer for making French fries."},
    "cafeterias": {"phonetic": "/ˌkæfəˈtɪriəz/", "pos": "n.", "meaning": "自助餐廳；員工餐廳(複數)", "phrases": ["school cafeteria"], "synonyms": ["canteen"], "antonyms": [], "example": "Most of the local office buildings have their own cafeterias for employees."},
    "whole milk": {"phonetic": "/hoʊl mɪlk/", "pos": "n. phr.", "meaning": "全脂牛奶", "phrases": [], "synonyms": [], "antonyms": ["skim milk"], "example": "Some people prefer the taste of whole milk over reduced-fat alternatives."},
    "skim milk": {"phonetic": "/skɪm mɪlk/", "pos": "n. phr.", "meaning": "脫脂牛奶", "phrases": [], "synonyms": [], "antonyms": ["whole milk"], "example": "She always buys skim milk because she is trying to reduce her calorie intake."},
    "rogue": {"phonetic": "/roʊɡ/", "pos": "adj./n.", "meaning": "不受控制的；流氓；無賴", "phrases": ["rogue state", "rogue employee"], "synonyms": ["unprincipled", "scoundrel"], "antonyms": [], "example": "The security breach was caused by a rogue employee who accessed confidential data."},
    "plug in": {"phonetic": "/plʌɡ ɪn/", "pos": "v. phr.", "meaning": "插上插頭", "phrases": [], "synonyms": ["connect"], "antonyms": ["unplug"], "example": "Make sure you plug in the printer before you try to print the documents."},
    "unplug": {"phonetic": "/ʌnˈplʌɡ/", "pos": "v. phr.", "meaning": "拔掉插頭", "phrases": [], "synonyms": ["disconnect"], "antonyms": ["plug in"], "example": "Please remember to unplug the coffee machine before you leave the office."},
    "getting through": {"phonetic": "/ˈɡetɪŋ θruː/", "pos": "v. phr.", "meaning": "度過(難關)；辦完", "phrases": [], "synonyms": ["surviving", "completing"], "antonyms": [], "example": "The company is focused on getting through the current economic downturn."},
    "acting on": {"phonetic": "/ˈæktɪŋ ɑːn/", "pos": "v. phr.", "meaning": "根據...採取行動", "phrases": [], "synonyms": ["executing", "implementing"], "antonyms": [], "example": "The management is acting on the recommendations made by the consultants."},
    "daunt": {"phonetic": "/dɔːnt/", "pos": "v.", "meaning": "使氣餒；使膽怯", "phrases": ["daunting task"], "synonyms": ["intimidate", "frighten"], "antonyms": ["encourage"], "example": "The scale of the project might daunt some people, but we are confident we can succeed."},
    "leveled off": {"phonetic": "/ˈlevld ɔːf/", "pos": "v. phr.", "meaning": "趨於平緩", "phrases": [], "synonyms": ["stabilized"], "antonyms": ["fluctuated"], "example": "After a period of rapid growth, sales have finally leveled off this quarter."},
    "at historical highs": {"phonetic": "/æt hɪˈstɔːrɪkl haɪz/", "pos": "phr.", "meaning": "處於歷史高點", "phrases": [], "synonyms": [], "antonyms": ["at historical lows"], "example": "The company's stock price is currently trading at historical highs."},
    "stroke": {"phonetic": "/stroʊk/", "pos": "n./v.", "meaning": "中風；筆劃；輕撫", "phrases": ["suffer a stroke"], "synonyms": [], "antonyms": [], "example": "He was rushed to the hospital after suffering a minor stroke at work."},
    "culprit": {"phonetic": "/ˈkʌlprɪt/", "pos": "n.", "meaning": "罪魁禍首；被告", "phrases": [], "synonyms": ["offender", "cause"], "antonyms": [], "example": "Poor communication was identified as the main culprit for the project's failure."},
    "Diabetes": {"phonetic": "/ˌdaɪəˈbiːtiːz/", "pos": "n.", "meaning": "糖尿病", "phrases": ["type 2 diabetes"], "synonyms": [], "antonyms": [], "example": "The health organization is raising awareness about the risks associated with diabetes."},
    "downturn": {"phonetic": "/ˈdaʊntɜːrn/", "pos": "n.", "meaning": "衰退；下修", "phrases": ["economic downturn"], "synonyms": ["recession", "slump"], "antonyms": ["upturn", "boom"], "example": "Many businesses have struggled during the recent downturn in the global economy."},
    "longevity": {"phonetic": "/lɔːnˈdʒevəti/", "pos": "n.", "meaning": "長壽；壽命", "phrases": ["increased longevity"], "synonyms": ["durability", "life span"], "antonyms": [], "example": "Improvements in healthcare have led to increased longevity in many developed countries."},
    "stepfather": {"phonetic": "/ˈstepfɑːðər/", "pos": "n.", "meaning": "繼父", "phrases": [], "synonyms": [], "antonyms": [], "example": "He gets along very well with his stepfather and they often go fishing together."},
    "reservist": {"phonetic": "/rɪˈzɜːrvɪst/", "pos": "n.", "meaning": "預備役軍人", "phrases": [], "synonyms": [], "antonyms": [], "example": "The company allows its employees who are reservists to take time off for military training."},
    "credit": {"phonetic": "/ˈkredɪt/", "pos": "n./v.", "meaning": "信用；學分；歸功於", "phrases": ["credit card", "tax credit"], "synonyms": ["trust", "recognition"], "antonyms": ["debt"], "example": "The manager gave her full credit for the success of the new marketing campaign."},
    "landslide": {"phonetic": "/ˈlændslaɪd/", "pos": "n.", "meaning": "山崩；壓倒性勝利", "phrases": ["landslide victory"], "synonyms": ["mudslide", "overwhelming win"], "antonyms": [], "example": "The heavy rain caused a massive landslide that blocked the main road into the city."},
    "engulf": {"phonetic": "/ɪnˈɡʌlf/", "pos": "v.", "meaning": "吞沒；包圍", "phrases": ["engulfed in flames"], "synonyms": ["swallow", "envelop"], "antonyms": [], "example": "The small coastal village was engulfed by the tsunami within minutes."},
    "overpass": {"phonetic": "/ˈoʊvərpæs/", "pos": "n.", "meaning": "陸橋；高架道路", "phrases": ["pedestrian overpass"], "synonyms": ["bridge", "flyover"], "antonyms": ["underpass"], "example": "The new overpass has helped to reduce traffic congestion at the busy intersection."},
    "collapse": {"phonetic": "/kəˈlæps/", "pos": "v./n.", "meaning": "倒塌；崩潰", "phrases": ["building collapse", "economic collapse"], "synonyms": ["fall", "breakdown"], "antonyms": ["stability", "growth"], "example": "The old bridge collapsed under the weight of the heavy delivery truck."},
    "excavator": {"phonetic": "/ˈekskəveɪtər/", "pos": "n.", "meaning": "挖掘機；怪手", "phrases": [], "synonyms": ["digger"], "antonyms": [], "example": "The construction workers used an excavator to dig the foundation for the new office building."},
    "debris": {"phonetic": "/dəˈbriː/", "pos": "n.", "meaning": "殘骸；碎片", "phrases": ["clear the debris"], "synonyms": ["rubble", "wreckage"], "antonyms": [], "example": "It took several days for the rescue teams to clear the debris from the collapsed building."},
    "inaccessible": {"phonetic": "/ˌɪnækˈsesəbl/", "pos": "adj.", "meaning": "難以接近的；達不到的", "phrases": [], "synonyms": ["unreachable", "remote"], "antonyms": ["accessible", "reachable"], "example": "The mountain village was inaccessible for several days due to the heavy snowfall."},
    "an emergency task force": {"phonetic": "/ən ɪˈmɜːrdʒənsi tæsk fɔːrs/", "pos": "n. phr.", "meaning": "緊急應變小組", "phrases": [], "synonyms": [], "antonyms": [], "example": "The government has set up an emergency task force to coordinate the rescue efforts."},
    "bulldozer": {"phonetic": "/ˈbʊldoʊzər/", "pos": "n.", "meaning": "推土機", "phrases": [], "synonyms": [], "antonyms": [], "example": "The workers used a bulldozer to clear the land before starting the construction work."},
    "detector": {"phonetic": "/dɪˈtektər/", "pos": "n.", "meaning": "探測器", "phrases": ["smoke detector", "metal detector"], "synonyms": ["sensor"], "antonyms": [], "example": "Every room in the hotel is equipped with a smoke detector for safety."},
    "detect": {"phonetic": "/dɪˈtekt/", "pos": "v.", "meaning": "偵測；察覺", "phrases": ["detect a problem"], "synonyms": ["discover", "notice"], "antonyms": ["overlook"], "example": "The new security system is designed to detect any unauthorized entry into the building."},
    "witness": {"phonetic": "/ˈwɪtnəs/", "pos": "n./v.", "meaning": "證人；目擊", "phrases": ["eye witness"], "synonyms": ["onlooker", "observe"], "antonyms": [], "example": "Several witnesses were interviewed by the police following the accident."},
    "slam": {"phonetic": "/slæm/", "pos": "v./n.", "meaning": "猛擊；砰然關上", "phrases": ["slam the door"], "synonyms": ["bang", "shut"], "antonyms": [], "example": "He was so angry that he slammed the office door as he left the meeting."},
    "sovereignty": {"phonetic": "/ˈsɑːvrənti/", "pos": "n.", "meaning": "主權；統治權", "phrases": ["national sovereignty"], "synonyms": ["autonomy", "independence"], "antonyms": ["dependency"], "example": "The country is fighting to protect its national sovereignty and territorial integrity."},
    "dispatch": {"phonetic": "/dɪˈspætʃ/", "pos": "v./n.", "meaning": "派遣；發送", "phrases": ["dispatch an order"], "synonyms": ["send", "assign"], "antonyms": [], "example": "The company will dispatch the goods as soon as the payment is received."},
    "relevant": {"phonetic": "/ˈreləvənt/", "pos": "adj.", "meaning": "相關的；切題的", "phrases": ["relevant experience"], "synonyms": ["applicable", "pertinent"], "antonyms": ["irrelevant"], "example": "Please provide any relevant information that could help us with our investigation."},
    "alternative": {"phonetic": "/ɔːlˈtɜːrnətɪv/", "pos": "n./adj.", "meaning": "替代方案；替代的", "phrases": ["alternative energy"], "synonyms": ["option", "choice"], "antonyms": [], "example": "We need to find an alternative supplier if the current one cannot deliver on time."},
    "as of": {"phonetic": "/æz əv/", "pos": "prep. phr.", "meaning": "截至...為止；自...起", "phrases": ["as of now"], "synonyms": ["starting from"], "antonyms": [], "example": "The new safety regulations will take effect as of the first of next month."},
    "cope with": {"phonetic": "/koʊp wɪð/", "pos": "v. phr.", "meaning": "處理；應對(難關)", "phrases": [], "synonyms": ["manage", "handle"], "antonyms": [], "example": "The hospital is struggling to cope with the large number of patients during the flu season."},
    "along with": {"phonetic": "/əˈlɔːŋ wɪð/", "pos": "prep. phr.", "meaning": "連同；伴隨", "phrases": [], "synonyms": ["together with"], "antonyms": [], "example": "Please send the signed contract along with a copy of your ID card."},
    "ahead of": {"phonetic": "/əˈhed əv/", "pos": "prep. phr.", "meaning": "在...之前", "phrases": ["ahead of time"], "synonyms": ["before"], "antonyms": ["behind"], "example": "The construction project was completed two weeks ahead of schedule."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_9:
        update_info = enriched_data_gold_9[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 401-450 個單字。")
