import json

# 第 301-350 個高品質單字對應表 (金色等級)
enriched_data_gold_7 = {
    "telemarketing": {"phonetic": "/ˈtelimɑːrkɪtɪŋ/", "pos": "n.", "meaning": "電話行銷", "phrases": ["telemarketing representative"], "synonyms": [], "antonyms": [], "example": "Many consumers find telemarketing calls to be intrusive and annoying."},
    "direct mail": {"phonetic": "/dəˈrekt meɪl/", "pos": "n. phr.", "meaning": "直接郵寄廣告(DM)", "phrases": ["direct mail campaign"], "synonyms": ["junk mail"], "antonyms": [], "example": "The company sent out thousands of direct mail brochures to potential customers."},
    "point of sale": {"phonetic": "/pɔɪnt əv seɪl/", "pos": "n. phr.", "meaning": "銷售點(POS)", "phrases": ["POS system"], "synonyms": [], "antonyms": [], "example": "We need to install a new point of sale system to speed up the checkout process."},
    "markup": {"phonetic": "/ˈmɑːrkʌp/", "pos": "n.", "meaning": "漲價；毛利", "phrases": ["standard markup"], "synonyms": ["profit margin"], "antonyms": ["markdown"], "example": "The retailer adds a fifty percent markup to the wholesale price of the goods."},
    "markdown": {"phonetic": "/ˈmɑːrkdaʊn/", "pos": "n.", "meaning": "減價", "phrases": ["seasonal markdown"], "synonyms": ["discount", "reduction"], "antonyms": ["markup"], "example": "There were significant markdowns on all winter clothing during the end-of-season sale."},
    "clearance sale": {"phonetic": "/ˈklɪrəns seɪl/", "pos": "n. phr.", "meaning": "清倉大拍賣", "phrases": [], "synonyms": ["closing-down sale"], "antonyms": [], "example": "Everything must go during our annual clearance sale, with discounts of up to seventy percent."},
    "rebate": {"phonetic": "/ˈriːbeɪt/", "pos": "n./v.", "meaning": "退還款；折扣", "phrases": ["tax rebate", "mail-in rebate"], "synonyms": ["refund", "discount"], "antonyms": [], "example": "Customers can apply for a fifty-dollar mail-in rebate after purchasing the new appliance."},
    "quota": {"phonetic": "/ˈkwoʊtə/", "pos": "n.", "meaning": "配額；限額", "phrases": ["sales quota", "import quota"], "synonyms": ["allocation", "limit"], "antonyms": [], "example": "The sales team is working hard to meet its monthly quota before the end of the week."},
    "canvass": {"phonetic": "/ˈkænvəs/", "pos": "v./n.", "meaning": "遊說；調查；拉票", "phrases": ["canvass for votes"], "synonyms": ["survey", "poll"], "antonyms": [], "example": "Volunteers will canvass the local neighborhood to gather opinions on the new project."},
    "cold call": {"phonetic": "/koʊld kɔːl/", "pos": "n./v.", "meaning": "陌生電訪", "phrases": ["make cold calls"], "synonyms": [], "antonyms": [], "example": "The sales representatives spend several hours each day making cold calls to potential clients."},
    "prospect": {"phonetic": "/ˈprɑːspekt/", "pos": "n./v.", "meaning": "潛在客戶；前景；勘探", "phrases": ["business prospects", "prospective client"], "synonyms": ["possibility", "potential"], "antonyms": [], "example": "The company is identifying new prospects in the European market for its services."},
    "lead": {"phonetic": "/liːd/", "pos": "n./v.", "meaning": "銷售線索；領先", "phrases": ["generate leads", "take the lead"], "synonyms": ["clue", "guide"], "antonyms": [], "example": "Our website is a great tool for generating high-quality leads for the sales team."},
    "conversion rate": {"phonetic": "/kənˈvɜːrʒn reɪt/", "pos": "n. phr.", "meaning": "轉化率", "phrases": [], "synonyms": [], "antonyms": [], "example": "The marketing department is trying to improve the conversion rate of website visitors into customers."},
    "negotiation": {"phonetic": "/nɪˌɡoʊʃiˈeɪʃn/", "pos": "n.", "meaning": "談判", "phrases": ["contract negotiation", "under negotiation"], "synonyms": ["discussion", "bargaining"], "antonyms": [], "example": "The two companies are currently in the final stages of negotiation for the merger."},
    "deadlock": {"phonetic": "/ˈdedlɑːk/", "pos": "n./v.", "meaning": "僵局", "phrases": ["reach a deadlock"], "synonyms": ["stalemate", "impasse"], "antonyms": ["resolution"], "example": "The negotiations reached a deadlock over the issue of the purchase price."},
    "concession": {"phonetic": "/kənˈseʃn/", "pos": "n.", "meaning": "讓步；特許權", "phrases": ["make a concession"], "synonyms": ["compromise", "allowance"], "antonyms": ["refusal"], "example": "The management made several concessions to the union to avoid a strike."},
    "compromise": {"phonetic": "/ˈkɑːmprəmaɪz/", "pos": "n./v.", "meaning": "妥協", "phrases": ["reach a compromise"], "synonyms": ["settlement", "agreement"], "antonyms": ["conflict"], "example": "After hours of discussion, they finally reached a compromise that satisfied both parties."},
    "win-win": {"phonetic": "/ˈwɪnˈwɪn/", "pos": "adj.", "meaning": "雙贏的", "phrases": ["win-win situation"], "synonyms": [], "antonyms": [], "example": "The partnership is a win-win situation for both companies, as it combines their strengths."},
    "synergy": {"phonetic": "/ˈsɪnərdʒi/", "pos": "n.", "meaning": "綜效；協同作用", "phrases": ["create synergy"], "synonyms": ["cooperation", "collaboration"], "antonyms": [], "example": "The merger is expected to create significant synergy and reduce overall operational costs."},
    "logistics": {"phonetic": "/ləˈdʒɪstɪks/", "pos": "n.", "meaning": "物流；後勤", "phrases": ["logistics provider"], "synonyms": ["distribution"], "antonyms": [], "example": "Efficient logistics are essential for delivering products to customers on time."},
    "freight": {"phonetic": "/freɪt/", "pos": "n./v.", "meaning": "貨運；貨物", "phrases": ["air freight", "freight forwarder"], "synonyms": ["cargo", "shipment"], "antonyms": [], "example": "The company uses air freight to deliver urgent orders to its international clients."},
    "cargo": {"phonetic": "/ˈkɑːrɡoʊ/", "pos": "n.", "meaning": "貨物", "phrases": ["cargo ship", "precious cargo"], "synonyms": ["freight", "goods"], "antonyms": [], "example": "The ship is carrying a large cargo of electronics and machinery from Asia."},
    "shipment": {"phonetic": "/ˈʃɪpmənt/", "pos": "n.", "meaning": "裝運；貨物", "phrases": ["overseas shipment"], "synonyms": ["delivery", "consignment"], "antonyms": [], "example": "We are expecting a new shipment of raw materials to arrive at the port tomorrow."},
    "vessel": {"phonetic": "/ˈvesl/", "pos": "n.", "meaning": "船艦；容器", "phrases": ["ocean-going vessel"], "synonyms": ["ship", "boat"], "antonyms": [], "example": "The container vessel will depart for Europe as soon as the loading is finished."},
    "fleet": {"phonetic": "/fliːt/", "pos": "n.", "meaning": "艦隊；車隊", "phrases": ["delivery fleet"], "synonyms": ["group"], "antonyms": [], "example": "The company operates a large fleet of delivery trucks to serve its local customers."},
    "carrier": {"phonetic": "/ˈkeriər/", "pos": "n.", "meaning": "運送業者；航空公司", "phrases": ["national carrier", "mail carrier"], "synonyms": ["shipper"], "antonyms": [], "example": "The national carrier has announced several new international flight routes for the summer."},
    "courier": {"phonetic": "/ˈkʊriər/", "pos": "n./v.", "meaning": "快遞員；信使", "phrases": ["courier service"], "synonyms": ["messenger"], "antonyms": [], "example": "We sent the original documents to the lawyer's office by a reliable courier service."},
    "delivery": {"phonetic": "/dɪˈlɪvəri/", "pos": "n.", "meaning": "遞送；交付", "phrases": ["express delivery", "home delivery"], "synonyms": ["shipment", "distribution"], "antonyms": [], "example": "The company offers free home delivery for all orders over one hundred dollars."},
    "distribution": {"phonetic": "/ˌdɪstrɪˈbjuːʃn/", "pos": "n.", "meaning": "分配；分銷", "phrases": ["distribution network"], "synonyms": ["allocation", "delivery"], "antonyms": [], "example": "The new distribution center will help to reduce travel time for our delivery trucks."},
    "warehouse": {"phonetic": "/ˈwerhaʊs/", "pos": "n./v.", "meaning": "倉庫", "phrases": ["bonded warehouse"], "synonyms": ["depot", "storage"], "antonyms": [], "example": "The products are stored in a large climate-controlled warehouse before being shipped."},
    "storage": {"phonetic": "/ˈstɔːrɪdʒ/", "pos": "n.", "meaning": "儲存；庫存", "phrases": ["cold storage"], "synonyms": ["stocking"], "antonyms": [], "example": "We need to find additional storage space for the new shipment of equipment."},
    "stock": {"phonetic": "/stɑːk/", "pos": "n./v.", "meaning": "庫存；股票", "phrases": ["in stock", "out of stock"], "synonyms": ["inventory", "supply"], "antonyms": [], "example": "I'm sorry, but that particular model is currently out of stock in our store."},
    "out of stock": {"phonetic": "/aʊt əv stɑːk/", "pos": "adj. phr.", "meaning": "缺貨中", "phrases": [], "synonyms": ["sold out"], "antonyms": ["in stock"], "example": "Many popular electronics items were out of stock during the holiday season."},
    "backorder": {"phonetic": "/ˈbækˌɔːrdər/", "pos": "n./v.", "meaning": "延期交貨的訂單", "phrases": ["be on backorder"], "synonyms": [], "antonyms": [], "example": "The item you requested is on backorder and should be delivered in about two weeks."},
    "lead time": {"phonetic": "/liːd taɪm/", "pos": "n. phr.", "meaning": "前置時間；交貨期", "phrases": ["short lead time"], "synonyms": [], "antonyms": [], "example": "The factory has reduced its lead time from four weeks to two weeks by improving efficiency."},
    "turnaround time": {"phonetic": "/ˈtɜːrnəˌraʊnd taɪm/", "pos": "n. phr.", "meaning": "周轉時間", "phrases": [], "synonyms": [], "antonyms": [], "example": "Our standard turnaround time for processing a visa application is five working days."},
    "handling": {"phonetic": "/ˈhændlɪŋ/", "pos": "n.", "meaning": "處理；搬運", "phrases": ["shipping and handling"], "synonyms": ["processing", "management"], "antonyms": [], "example": "Please be careful during the handling of these fragile electronic components."},
    "customs": {"phonetic": "/ˈkʌstəmz/", "pos": "n.", "meaning": "海關", "phrases": ["pass through customs", "customs official"], "synonyms": [], "antonyms": [], "example": "It took almost an hour for the passengers to pass through customs at the airport."},
    "duty": {"phonetic": "/ˈduːti/", "pos": "n.", "meaning": "關稅；責任", "phrases": ["duty-free", "import duty"], "synonyms": ["tax", "obligation"], "antonyms": [], "example": "You have to pay an import duty on any electronics you bring into the country."},
    "excise": {"phonetic": "/ˈeksaɪz/", "pos": "n./v.", "meaning": "消費稅", "phrases": ["excise tax"], "synonyms": [], "antonyms": [], "example": "The government has decided to increase the excise tax on cigarettes and alcohol."},
    "levy": {"phonetic": "/ˈlevi/", "pos": "n./v.", "meaning": "徵收；徵稅", "phrases": ["levy a tax"], "synonyms": ["collect", "impose"], "antonyms": [], "example": "The local council has the power to levy a new tax on business properties."},
    "dumping": {"phonetic": "/ˈdʌmpɪŋ/", "pos": "n.", "meaning": "傾銷", "phrases": ["anti-dumping laws"], "synonyms": [], "antonyms": [], "example": "The government is investigating claims of dumping by international electronics firms."},
    "subsidy": {"phonetic": "/ˈsʌbsədi/", "pos": "n.", "meaning": "補貼；津貼", "phrases": ["export subsidy"], "synonyms": ["grant"], "antonyms": [], "example": "The agricultural industry receives a large government subsidy to keep prices stable."},
    "embargo": {"phonetic": "/ɪmˈbɑːrɡoʊ/", "pos": "n./v.", "meaning": "禁運", "phrases": ["trade embargo"], "synonyms": ["ban", "boycott"], "antonyms": [], "example": "The United Nations imposed a trade embargo on the country to pressure the government."},
    "sanction": {"phonetic": "/ˈsæŋkʃn/", "pos": "n./v.", "meaning": "制裁；核准", "phrases": ["economic sanctions"], "synonyms": ["penalty", "authorization"], "antonyms": [], "example": "Several countries have imposed economic sanctions on the region following the conflict."},
    "compliance": {"phonetic": "/kəmˈplaɪəns/", "pos": "n.", "meaning": "合規；遵守", "phrases": ["regulatory compliance"], "synonyms": ["adherence"], "antonyms": ["violation"], "example": "All businesses must ensure full compliance with the new environmental regulations."},
    "violation": {"phonetic": "/vaɪəˈleɪʃn/", "pos": "n.", "meaning": "違反；違規", "phrases": ["safety violation"], "synonyms": ["breach", "infringement"], "antonyms": ["observance"], "example": "The company was fined for multiple violations of workplace safety laws."},
    "breach": {"phonetic": "/briːtʃ/", "pos": "n./v.", "meaning": "違約；違反", "phrases": ["breach of trust"], "synonyms": ["violation", "failure"], "antonyms": ["fulfillment"], "example": "The security breach allowed hackers to gain access to customer credit card details."},
    "infringement": {"phonetic": "/ɪnˈfrɪndʒmənt/", "pos": "n.", "meaning": "侵權", "phrases": ["trademark infringement"], "synonyms": ["violation", "breach"], "antonyms": [], "example": "The artist sued the company for copyright infringement after they used her work."},
    "litigation": {"phonetic": "/ˌlɪtɪˈɡeɪʃn/", "pos": "n.", "meaning": "訴訟", "phrases": ["involved in litigation"], "synonyms": ["lawsuit"], "antonyms": [], "example": "The company spent millions of dollars on litigation related to the patent dispute."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_7:
        update_info = enriched_data_gold_7[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 301-350 個單字。")
