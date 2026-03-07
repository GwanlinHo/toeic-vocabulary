import json

# 第 851-900 個高品質單字對應表 (金色等級)
enriched_data_gold_18 = {
    "bumpy": {"phonetic": "/ˈbʌmpi/", "pos": "adj.", "meaning": "崎嶇不平的；顛簸的", "phrases": ["bumpy road"], "synonyms": ["uneven", "rough"], "antonyms": ["smooth", "flat"], "example": "The economy has had a bumpy recovery over the last two years."},
    "grandiose": {"phonetic": "/ˈɡrændioʊs/", "pos": "adj.", "meaning": "宏偉的；誇大的", "phrases": ["grandiose plans"], "synonyms": ["magnificent", "ambitious"], "antonyms": ["modest", "simple"], "example": "The CEO's grandiose vision for the company's future impressed many investors."},
    "modest": {"phonetic": "/ˈmɑːdɪst/", "pos": "adj.", "meaning": "謙虛的；適度的；端莊的", "phrases": ["modest increase"], "synonyms": ["humble", "moderate"], "antonyms": ["arrogant", "extravagant"], "example": "Despite the company's huge success, the founder remains a very modest person."},
    "frantic": {"phonetic": "/ˈfræntɪk/", "pos": "adj.", "meaning": "瘋狂的；狂亂的", "phrases": ["frantic search"], "synonyms": ["frenzied", "desperate"], "antonyms": ["calm", "collected"], "example": "There was a frantic effort to finish the report before the deadline."},
    "inscribe": {"phonetic": "/ɪnˈskraɪb/", "pos": "v.", "meaning": "刻；題寫", "phrases": ["inscribe a name"], "synonyms": ["engrave", "write"], "antonyms": [], "example": "The winner's name will be inscribed on the trophy."},
    "increasingly": {"phonetic": "/ɪnˈkriːsɪŋli/", "pos": "adv.", "meaning": "漸增地；越來越多地", "phrases": ["increasingly popular"], "synonyms": ["more and more"], "antonyms": ["decreasingly"], "example": "The company is becoming increasingly dependent on international sales."},
    "in honor of": {"phonetic": "/ɪn ˈɑːnər əv/", "pos": "phr.", "meaning": "向...致敬；為了紀念", "phrases": [], "synonyms": ["to commemorate"], "antonyms": [], "example": "A special banquet was held in honor of the retiring manager."},
    "aerospace": {"phonetic": "/ˈeroʊspeɪs/", "pos": "n./adj.", "meaning": "航空航太(業)", "phrases": ["aerospace industry"], "synonyms": [], "antonyms": [], "example": "The company specializes in manufacturing high-tech components for the aerospace sector."},
    "underprivileged": {"phonetic": "/ˌʌndərˈprɪvəlɪdʒd/", "pos": "adj.", "meaning": "貧困的；弱勢的", "phrases": ["underprivileged children"], "synonyms": ["disadvantaged", "deprived"], "antonyms": ["privileged", "wealthy"], "example": "The non-profit organization provides free education to underprivileged youth in the city."},
    "discontentedly": {"phonetic": "/ˌdɪskənˈtentɪdli/", "pos": "adv.", "meaning": "不滿地", "phrases": [], "synonyms": ["unhappily"], "antonyms": ["contentedly"], "example": "The employees muttered discontentedly about the changes to the holiday schedule."},
    "attorney": {"phonetic": "/əˈtɜːrni/", "pos": "n.", "meaning": "律師", "phrases": ["defense attorney", "power of attorney"], "synonyms": ["lawyer", "counsel"], "antonyms": [], "example": "You should consult your attorney before signing any legal documents."},
    "pore over": {"phonetic": "/pɔːr ˈoʊvər/", "pos": "v. phr.", "meaning": "鑽研；詳讀", "phrases": [], "synonyms": ["examine", "scrutinize"], "antonyms": ["glance at"], "example": "The auditors spent hours poring over the company's financial records."},
    "demonstratively": {"phonetic": "/dəˈmɑːnstrətɪvli/", "pos": "adv.", "meaning": "公開地；流露感情地", "phrases": [], "synonyms": ["openly", "expressively"], "antonyms": [], "example": "She demonstratively expressed her gratitude to the team for their hard work."},
    "demonically": {"phonetic": "/dɪˈmɑːnɪkli/", "pos": "adv.", "meaning": "如魔鬼般地；瘋狂地", "phrases": [], "synonyms": ["fiendishly"], "antonyms": [], "example": "The project was demonically difficult and required everyone's full attention."},
    "tragic": {"phonetic": "/ˈtrædʒɪk/", "pos": "adj.", "meaning": "悲劇的；悲慘的", "phrases": ["tragic accident"], "synonyms": ["disastrous", "calamitous"], "antonyms": ["comic", "fortunate"], "example": "The sudden closure of the factory was a tragic event for the local community."},
    "studio": {"phonetic": "/ˈstuːdioʊ/", "pos": "n.", "meaning": "工作室；攝影棚", "phrases": ["recording studio", "art studio"], "synonyms": ["workshop"], "antonyms": [], "example": "The marketing team is using a professional studio to film the new commercial."},
    "remarkedly": {"word": "markedly", "phonetic": "/rɪˈmɑːrkɪdli/", "pos": "adv.", "meaning": "顯著地；明顯地", "phrases": ["markedly different"], "synonyms": ["significantly", "noticeably"], "antonyms": ["slightly"], "example": "Sales have improved markedly since the launch of the new website."},
    "remarkably": {"phonetic": "/rɪˈmɑːrkəbli/", "pos": "adv.", "meaning": "非凡地；顯著地", "phrases": ["remarkably successful"], "synonyms": ["extraordinarily", "strikingly"], "antonyms": ["ordinarily"], "example": "The company has remained remarkably successful despite the economic downturn."},
    "substantially": {"phonetic": "/səbˈstænʃəli/", "pos": "adv.", "meaning": "本質上；大體上；大幅地", "phrases": ["increase substantially"], "synonyms": ["significantly", "considerably"], "antonyms": ["insignificantly", "slightly"], "example": "The price of raw materials has increased substantially over the last few months."},
    "dramatically": {"phonetic": "/drəˈmætɪkli/", "pos": "adv.", "meaning": "戲劇性地；顯著地", "phrases": ["drop dramatically"], "synonyms": ["drastically", "markedly"], "antonyms": ["gradually"], "example": "The new marketing strategy has dramatically increased the company's online presence."},
    "well ahead of": {"phonetic": "/wel əˈhed əv/", "pos": "phr.", "meaning": "遠遠領先於...", "phrases": ["well ahead of schedule"], "synonyms": [], "antonyms": ["well behind"], "example": "The team finished the project well ahead of the deadline."},
    "badly": {"phonetic": "/ˈbædli/", "pos": "adv.", "meaning": "糟糕地；嚴重地；非常", "phrases": ["badly needed"], "synonyms": ["poorly", "severely"], "antonyms": ["well"], "example": "The company's image was badly damaged by the recent scandal."},
    "unbearably": {"phonetic": "/ʌnˈberəbli/", "pos": "adv.", "meaning": "不可忍受地", "phrases": ["unbearably hot"], "synonyms": ["intolerably"], "antonyms": ["tolerably"], "example": "The office was unbearably hot after the air conditioning system broke down."},
    "securely": {"phonetic": "/səˈkjʊrli/", "pos": "adv.", "meaning": "牢固地；安全地", "phrases": ["fasten securely"], "synonyms": ["firmly", "safely"], "antonyms": ["insecurely"], "example": "Please ensure that all confidential documents are stored securely in the safe."},
    "swipe": {"phonetic": "/swaɪp/", "pos": "v./n.", "meaning": "刷(卡)；滑動；揮擊", "phrases": ["swipe a card"], "synonyms": ["slide"], "antonyms": [], "example": "You need to swipe your ID card to gain access to the building."},
    "disarm": {"phonetic": "/dɪsˈɑːrm/", "pos": "v.", "meaning": "解除武裝；消除敵意", "phrases": ["disarm a security system"], "synonyms": ["deactivate", "defuse"], "antonyms": ["arm", "activate"], "example": "Please remember to disarm the alarm before entering the office in the morning."},
    "disruptive": {"phonetic": "/dɪsˈrʌptɪv/", "pos": "adj.", "meaning": "顛覆性的；引起混亂的", "phrases": ["disruptive technology"], "synonyms": ["troublesome", "unsettling"], "antonyms": ["orderly", "supportive"], "example": "The new software is expected to be a disruptive force in the industry."},
    "tap water": {"phonetic": "/tæp ˈwɔːtər/", "pos": "n. phr.", "meaning": "自來水", "phrases": ["drink tap water"], "synonyms": ["running water"], "antonyms": ["bottled water"], "example": "The city's tap water is safe to drink and meets all health standards."},
    "cloudy": {"phonetic": "/ˈklaʊdi/", "pos": "adj.", "meaning": "多雲的；陰天的；混濁的", "phrases": ["cloudy liquid"], "synonyms": ["overcast", "murky"], "antonyms": ["clear", "sunny"], "example": "The chemical solution became cloudy after the new substance was added."},
    "precipitation": {"phonetic": "/prɪˌsɪpɪˈteɪʃn/", "pos": "n.", "meaning": "降水(雨、雪等)；沈澱", "phrases": ["heavy precipitation"], "synonyms": ["rainfall"], "antonyms": [], "example": "The region has experienced unusually high levels of precipitation this winter."},
    "sediment": {"phonetic": "/ˈsedɪmənt/", "pos": "n.", "meaning": "沈澱物", "phrases": [], "synonyms": ["deposit", "dregs"], "antonyms": [], "example": "The filter is designed to remove any sediment from the water supply."},
    "maternity leave": {"phonetic": "/məˈtɜːrnəti liːv/", "pos": "n. phr.", "meaning": "產假", "phrases": ["go on maternity leave"], "synonyms": [], "antonyms": ["paternity leave"], "example": "She is currently on maternity leave and will return to work next month."},
    "be conducive to": {"phonetic": "/bi kənˈduːsɪv tuː/", "pos": "v. phr.", "meaning": "有助於...", "phrases": [], "synonyms": ["be helpful for"], "antonyms": [], "example": "A quiet working environment is conducive to concentration and productivity."},
    "arrangement": {"phonetic": "/əˈreɪndʒmənt/", "pos": "n.", "meaning": "安排；約定；佈置", "phrases": ["make arrangements", "travel arrangements"], "synonyms": ["preparation", "agreement"], "antonyms": [], "example": "We have made all the necessary travel arrangements for the business trip."},
    "arranger": {"phonetic": "/əˈreɪndʒər/", "pos": "n.", "meaning": "安排者；改編者", "phrases": [], "synonyms": ["organizer"], "antonyms": [], "example": "The event arranger is responsible for coordinating with all the suppliers."},
    "confectioner": {"phonetic": "/kənˈfekʃənər/", "pos": "n.", "meaning": "糖果店；製菓業者", "phrases": [], "synonyms": [], "antonyms": [], "example": "The local confectioner is famous for its high-quality handmade chocolates."},
    "fundraiser": {"phonetic": "/ˈfʌndreɪzər/", "pos": "n.", "meaning": "募款活動；募款人", "phrases": ["charity fundraiser"], "synonyms": [], "antonyms": [], "example": "The non-profit organization is holding a fundraiser to build a new community center."},
    "room": {"phonetic": "/ruːm/", "pos": "n./v.", "meaning": "房間；空間；餘地；居住", "phrases": ["conference room", "room for improvement"], "synonyms": ["chamber", "space", "scope"], "antonyms": [], "example": "The hotel has a large conference room that can accommodate two hundred people."},
    "venue": {"phonetic": "/ˈvenjuː/", "pos": "n.", "meaning": "場地；地點", "phrases": ["concert venue", "meeting venue"], "synonyms": ["location", "place"], "antonyms": [], "example": "The city center is a popular venue for international technology conferences."},
    "equivalent": {"phonetic": "/ɪˈkwɪvələnt/", "pos": "adj./n.", "meaning": "相等的；等價物", "phrases": ["cash equivalent"], "synonyms": ["equal", "identical"], "antonyms": ["different", "dissimilar"], "example": "The two models offer equivalent features but at very different price points."},
    "introductory": {"phonetic": "/ˌɪntrəˈdʌktəri/", "pos": "adj.", "meaning": "介紹的；入門的；優惠的", "phrases": ["introductory price", "introductory offer"], "synonyms": ["preliminary", "initial"], "antonyms": ["advanced", "final"], "example": "The company is offering an introductory price for its new software service."},
    "proficient": {"phonetic": "/prəˈfɪʃnt/", "pos": "adj.", "meaning": "精通的；熟練的", "phrases": ["proficient in English"], "synonyms": ["skilled", "expert"], "antonyms": ["incompetent", "inept"], "example": "All applicants for the position must be proficient in at least two foreign languages."},
    "vastly": {"phonetic": "/ˈvæstli/", "pos": "adv.", "meaning": "極大地；非常", "phrases": ["vastly improved"], "synonyms": ["greatly", "immensely"], "antonyms": ["slightly"], "example": "The new version of the software is vastly superior to the previous one."},
    "redeemable": {"phonetic": "/rɪˈdiːməbl/", "pos": "adj.", "meaning": "可兌換的；可贖回的", "phrases": ["redeemable voucher"], "synonyms": ["exchangeable"], "antonyms": ["irredeemable"], "example": "This coupon is redeemable for a ten percent discount at any of our stores."},
    "surveillance": {"phonetic": "/sɜːrˈveɪləns/", "pos": "n.", "meaning": "監視；監督", "phrases": ["surveillance camera", "under surveillance"], "synonyms": ["monitoring", "observation"], "antonyms": [], "example": "The building is equipped with advanced surveillance systems for security purposes."},
    "explicitly": {"phonetic": "/ɪkˈsplɪsɪtli/", "pos": "adv.", "meaning": "明確地；詳盡地", "phrases": ["explicitly state"], "synonyms": ["clearly", "plainly"], "antonyms": ["implicitly", "vaguely"], "example": "The terms of the contract were explicitly stated in the document."},
    "arguably": {"phonetic": "/ˈɑːrɡjuəbli/", "pos": "adv.", "meaning": "可以說是；有爭議地", "phrases": [], "synonyms": ["possibly", "likely"], "antonyms": [], "example": "This is arguably the most important project the company has ever undertaken."},
    "exceedingly": {"phonetic": "/ɪkˈsiːdɪŋli/", "pos": "adv.", "meaning": "極其；非常", "phrases": ["exceedingly high quality"], "synonyms": ["extremely", "exceptionally"], "antonyms": [], "example": "The manager was exceedingly happy with the team's performance this quarter."},
    "motorist": {"phonetic": "/ˈmoʊtərɪst/", "pos": "n.", "meaning": "駕車者", "phrases": [], "synonyms": ["driver"], "antonyms": ["pedestrian"], "example": "Motorists are advised to avoid the city center due to the ongoing roadwork."},
    "orderly": {"phonetic": "/ˈɔːrdərli/", "pos": "adj./n.", "meaning": "整潔的；有秩序的；勤務員", "phrases": ["orderly manner"], "synonyms": ["organized", "tidy"], "antonyms": ["disorderly", "chaotic"], "example": "The crowd filed into the building in an orderly manner once the doors opened."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_18:
        update_info = enriched_data_gold_18[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 851-900 個單字。")
