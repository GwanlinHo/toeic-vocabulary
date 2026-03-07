import json

def populate():
    data = [
        # --- GREEN LEVEL (基礎商務) ---
        {"word": "Contract", "phonetic": "/ˈkɒntrækt/", "pos": "n.", "meaning": "合約；契約", "level": "green", "phrases": ["sign a contract"], "synonyms": ["agreement"], "antonyms": [], "example": "Please sign the contract by Friday."},
        {"word": "Available", "phonetic": "/əˈveɪləbl/", "pos": "adj.", "meaning": "可得到的；有空的", "level": "green", "phrases": ["available for"], "synonyms": ["accessible"], "antonyms": ["busy"], "example": "Is the manager available now?"},
        {"word": "Notify", "phonetic": "/ˈnoʊtɪfaɪ/", "pos": "v.", "meaning": "通知", "level": "green", "phrases": ["notify someone of"], "synonyms": ["inform"], "antonyms": [], "example": "We will notify you of any changes."},
        {"word": "Schedule", "phonetic": "/ˈskedʒuːl/", "pos": "n.", "meaning": "行程；安排", "level": "green", "phrases": ["behind schedule"], "synonyms": ["timetable"], "antonyms": [], "example": "The project is on schedule."},
        {"word": "Confirm", "phonetic": "/kənˈfɜːrm/", "pos": "v.", "meaning": "確認", "level": "green", "phrases": ["confirm a booking"], "synonyms": ["verify"], "antonyms": [], "example": "Please confirm your reservation."},
        {"word": "Budget", "phonetic": "/ˈbʌdʒɪt/", "pos": "n.", "meaning": "預算", "level": "green", "phrases": ["within budget"], "synonyms": ["funds"], "antonyms": [], "example": "We need to stick to the budget."},
        {"word": "Client", "phonetic": "/ˈklaɪənt/", "pos": "n.", "meaning": "客戶", "level": "green", "phrases": ["potential client"], "synonyms": ["customer"], "antonyms": [], "example": "The client is coming at 2 PM."},
        {"word": "Candidate", "phonetic": "/ˈkændɪdət/", "pos": "n.", "meaning": "候選人", "level": "green", "phrases": ["job candidate"], "synonyms": ["applicant"], "antonyms": [], "example": "She is the best candidate for the job."},
        {"word": "Equipment", "phonetic": "/ɪˈkwɪpmənt/", "pos": "n.", "meaning": "設備", "level": "green", "phrases": ["office equipment"], "synonyms": ["gear"], "antonyms": [], "example": "The factory needs new equipment."},
        {"word": "Facility", "phonetic": "/fəˈsɪləti/", "pos": "n.", "meaning": "設施；場所", "level": "green", "phrases": ["production facility"], "synonyms": ["amenity"], "antonyms": [], "example": "Our training facility is downtown."},
        {"word": "Feedback", "phonetic": "/ˈfiːdbæk/", "pos": "n.", "meaning": "回饋", "level": "green", "phrases": ["customer feedback"], "synonyms": ["response"], "antonyms": [], "example": "We value your feedback."},
        {"word": "Inventory", "phonetic": "/ˈɪnvəntɔːri/", "pos": "n.", "meaning": "庫存", "level": "green", "phrases": ["check inventory"], "synonyms": ["stock"], "antonyms": [], "example": "We need to count the inventory."},
        {"word": "Invoice", "phonetic": "/ˈɪnvɔɪs/", "pos": "n.", "meaning": "發票；帳單", "level": "green", "phrases": ["pay an invoice"], "synonyms": ["bill"], "antonyms": [], "example": "The invoice is due next week."},
        {"word": "Maintain", "phonetic": "/meɪnˈteɪn/", "pos": "v.", "meaning": "維持；保養", "level": "green", "phrases": ["maintain equipment"], "synonyms": ["keep up"], "antonyms": [], "example": "It is hard to maintain the garden."},
        {"word": "Policy", "phonetic": "/ˈpɒləsi/", "pos": "n.", "meaning": "政策；規定", "level": "green", "phrases": ["company policy"], "synonyms": ["rule"], "antonyms": [], "example": "Please follow the company policy."},
        {"word": "Promotion", "phonetic": "/prəˈmoʊʃn/", "pos": "n.", "meaning": "晉升；促銷", "level": "green", "phrases": ["get a promotion"], "synonyms": ["advancement"], "antonyms": [], "example": "He received a promotion last month."},
        {"word": "Refund", "phonetic": "/ˈriːfʌnd/", "pos": "n./v.", "meaning": "退款", "level": "green", "phrases": ["full refund"], "synonyms": ["reimbursement"], "antonyms": [], "example": "Can I get a refund for this?"},
        {"word": "Repair", "phonetic": "/rɪˈper/", "pos": "v.", "meaning": "修理", "level": "green", "phrases": ["repair cost"], "synonyms": ["fix"], "antonyms": [], "example": "The printer needs to be repaired."},
        {"word": "Shipment", "phonetic": "/ˈʃɪpmənt/", "pos": "n.", "meaning": "貨物；運送", "level": "green", "phrases": ["order shipment"], "synonyms": ["delivery"], "antonyms": [], "example": "The shipment will arrive tomorrow."},
        {"word": "Vendor", "phonetic": "/ˈvendər/", "pos": "n.", "meaning": "小販；賣主", "level": "green", "phrases": ["approved vendor"], "synonyms": ["seller"], "antonyms": [], "example": "We hired a new software vendor."},

        # --- BLUE LEVEL (進階職場) ---
        {"word": "Implement", "phonetic": "/ˈɪmplɪment/", "pos": "v.", "meaning": "實施；執行", "level": "blue", "phrases": ["implement a policy"], "synonyms": ["execute"], "antonyms": ["suspend"], "example": "We will implement the changes soon."},
        {"word": "Collaborate", "phonetic": "/kəˈlæbəreɪt/", "pos": "v.", "meaning": "合作；協作", "level": "blue", "phrases": ["collaborate with"], "synonyms": ["cooperate"], "antonyms": ["compete"], "example": "Teams need to collaborate more."},
        {"word": "Negotiate", "phonetic": "/nɪˈɡoʊʃieɪt/", "pos": "v.", "meaning": "談判；協商", "level": "blue", "phrases": ["negotiate terms"], "synonyms": ["bargain"], "antonyms": [], "example": "They negotiated a better deal."},
        {"word": "Strategic", "phonetic": "/strəˈtiːdʒɪk/", "pos": "adj.", "meaning": "戰略性的", "level": "blue", "phrases": ["strategic plan"], "synonyms": ["planned"], "antonyms": [], "example": "This is a strategic decision."},
        {"word": "Comprehensive", "phonetic": "/ˌkɑːmprɪˈhensɪv/", "pos": "adj.", "meaning": "全面的", "level": "blue", "phrases": ["comprehensive report"], "synonyms": ["thorough"], "antonyms": ["limited"], "example": "The report is comprehensive."},
        {"word": "Acquisition", "phonetic": "/ˌækwɪˈzɪʃn/", "pos": "n.", "meaning": "收購；獲得", "level": "blue", "phrases": ["merger and acquisition"], "synonyms": ["purchase"], "antonyms": [], "example": "The company's latest acquisition was a tech startup."},
        {"word": "Benchmark", "phonetic": "/ˈbentʃmɑːrk/", "pos": "n.", "meaning": "基準", "level": "blue", "phrases": ["industry benchmark"], "synonyms": ["standard"], "antonyms": [], "example": "We use this as our benchmark for quality."},
        {"word": "Compliance", "phonetic": "/kəmˈplaɪəns/", "pos": "n.", "meaning": "合規；遵守", "level": "blue", "phrases": ["in compliance with"], "synonyms": ["adherence"], "antonyms": ["violation"], "example": "The company is in compliance with all regulations."},
        {"word": "Diversify", "phonetic": "/daɪˈvɜːrsɪfaɪ/", "pos": "v.", "meaning": "多樣化", "level": "blue", "phrases": ["diversify investment"], "synonyms": ["branch out"], "antonyms": [], "example": "We need to diversify our product line."},
        {"word": "Efficiency", "phonetic": "/ɪˈfɪʃnsi/", "pos": "n.", "meaning": "效率", "level": "blue", "phrases": ["improve efficiency"], "synonyms": ["productivity"], "antonyms": ["waste"], "example": "New tools can improve efficiency."},
        {"word": "Feasibility", "phonetic": "/ˌfiːzəˈbɪləti/", "pos": "n.", "meaning": "可行性", "level": "blue", "phrases": ["feasibility study"], "synonyms": ["viability"], "antonyms": [], "example": "We are conducting a feasibility study."},
        {"word": "Incentive", "phonetic": "/ɪnˈsentɪv/", "pos": "n.", "meaning": "獎勵；動機", "level": "blue", "phrases": ["tax incentive"], "synonyms": ["motivation"], "antonyms": ["deterrent"], "example": "Bonuses serve as a powerful incentive."},
        {"word": "Logistics", "phonetic": "/ləˈdʒɪstɪks/", "pos": "n.", "meaning": "物流", "level": "blue", "phrases": ["logistics management"], "synonyms": ["distribution"], "antonyms": [], "example": "The logistics of the move are complex."},
        {"word": "Profitability", "phonetic": "/ˌprɑːfɪtəˈbɪləti/", "pos": "n.", "meaning": "獲利能力", "level": "blue", "phrases": ["ensure profitability"], "synonyms": ["earnings"], "antonyms": [], "example": "The CEO is focused on profitability."},
        {"word": "Stakeholder", "phonetic": "/ˈsteɪkhoʊldər/", "pos": "n.", "meaning": "利害關係人", "level": "blue", "phrases": ["key stakeholder"], "synonyms": ["party"], "antonyms": [], "example": "We must inform all stakeholders."},
        {"word": "Subsidiary", "phonetic": "/səbˈsɪdieri/", "pos": "n.", "meaning": "子公司", "level": "blue", "phrases": ["wholly-owned subsidiary"], "synonyms": ["branch"], "antonyms": ["parent company"], "example": "They set up a subsidiary in Tokyo."},
        {"word": "Terminology", "phonetic": "/ˌtɜːrmɪˈnɑːlədʒi/", "pos": "n.", "meaning": "術語", "level": "blue", "phrases": ["technical terminology"], "synonyms": ["jargon"], "antonyms": [], "example": "The legal terminology is hard to understand."},
        {"word": "Undertake", "phonetic": "/ˌʌndərˈteɪk/", "pos": "v.", "meaning": "承擔；著手做", "level": "blue", "phrases": ["undertake a project"], "synonyms": ["assume"], "antonyms": [], "example": "The firm will undertake the construction."},
        {"word": "Utilization", "phonetic": "/ˌjuːtələˈzeɪʃn/", "pos": "n.", "meaning": "利用", "level": "blue", "phrases": ["resource utilization"], "synonyms": ["usage"], "antonyms": [], "example": "We need to improve our resource utilization."},
        {"word": "Verification", "phonetic": "/ˌverɪfɪˈkeɪʃn/", "pos": "n.", "meaning": "驗證；核實", "level": "blue", "phrases": ["data verification"], "synonyms": ["confirmation"], "antonyms": [], "example": "The process requires verification."},

        # --- GOLD LEVEL (高階策略) ---
        {"word": "Mitigate", "phonetic": "/ˈmɪtɪɡeɪt/", "pos": "v.", "meaning": "減輕；緩和", "level": "gold", "phrases": ["mitigate risks"], "synonyms": ["alleviate"], "antonyms": ["aggravate"], "example": "We must mitigate the potential risks."},
        {"word": "Leverage", "phonetic": "/ˈlevərɪdʒ/", "pos": "v.", "meaning": "利用；槓桿利用", "level": "gold", "phrases": ["leverage assets"], "synonyms": ["utilize"], "antonyms": [], "example": "The company leverages its data to grow."},
        {"word": "Unprecedented", "phonetic": "/ʌnˈpresɪdentɪd/", "pos": "adj.", "meaning": "前所未有的", "level": "gold", "phrases": ["unprecedented growth"], "synonyms": ["extraordinary"], "antonyms": ["common"], "example": "The growth was unprecedented."},
        {"word": "Volatile", "phonetic": "/ˈvɑːlətl/", "pos": "adj.", "meaning": "不穩定的", "level": "gold", "phrases": ["volatile market"], "synonyms": ["unstable"], "antonyms": ["stable"], "example": "The stock market is very volatile."},
        {"word": "Discrepancy", "phonetic": "/dɪˈskrepənsi/", "pos": "n.", "meaning": "差異；不一致", "level": "gold", "phrases": ["discrepancy in data"], "synonyms": ["difference"], "antonyms": ["consistency"], "example": "There is a discrepancy in the numbers."},
        {"word": "Ambiguity", "phonetic": "/ˌæmbɪˈɡjuːəti/", "pos": "n.", "meaning": "模稜兩可", "level": "gold", "phrases": ["avoid ambiguity"], "synonyms": ["vagueness"], "antonyms": ["clarity"], "example": "The contract is full of ambiguity."},
        {"word": "Contingency", "phonetic": "/kənˈtɪndʒənsi/", "pos": "n.", "meaning": "應急措施", "level": "gold", "phrases": ["contingency plan"], "synonyms": ["emergency plan"], "antonyms": [], "example": "We have a contingency plan in place."},
        {"word": "Detrimental", "phonetic": "/ˌdetrɪˈmentl/", "pos": "adj.", "meaning": "有害的", "level": "gold", "phrases": ["detrimental effect"], "synonyms": ["harmful"], "antonyms": ["beneficial"], "example": "Pollution is detrimental to health."},
        {"word": "Exacerbate", "phonetic": "/ɪɡˈzæsərbeɪt/", "pos": "v.", "meaning": "使惡化", "level": "gold", "phrases": ["exacerbate the problem"], "synonyms": ["aggravate"], "antonyms": ["improve"], "example": "The rain exacerbated the flood situation."},
        {"word": "Fluctuate", "phonetic": "/ˈflʌktʃueɪt/", "pos": "v.", "meaning": "波動", "level": "gold", "phrases": ["fluctuating prices"], "synonyms": ["vary"], "antonyms": ["stabilize"], "example": "Prices fluctuate according to demand."},
        {"word": "Imperative", "phonetic": "/ɪmˈperətɪv/", "pos": "adj.", "meaning": "極其重要的", "level": "gold", "phrases": ["it is imperative that"], "synonyms": ["essential"], "antonyms": ["optional"], "example": "It is imperative that we act now."},
        {"word": "Meticulous", "phonetic": "/məˈtɪkjələs/", "pos": "adj.", "meaning": "一絲不苟的", "level": "gold", "phrases": ["meticulous research"], "synonyms": ["thorough"], "antonyms": ["careless"], "example": "Her planning was meticulous."},
        {"word": "Precarious", "phonetic": "/prɪˈkeriəs/", "pos": "adj.", "meaning": "不穩定的；危險的", "level": "gold", "phrases": ["precarious position"], "synonyms": ["unstable"], "antonyms": ["safe"], "example": "The company is in a precarious financial state."},
        {"word": "Resilient", "phonetic": "/rɪˈzɪliənt/", "pos": "adj.", "meaning": "有韌性的", "level": "gold", "phrases": ["resilient economy"], "synonyms": ["strong"], "antonyms": ["weak"], "example": "The business proved to be resilient."},
        {"word": "Scrutinize", "phonetic": "/ˈskruːtənaɪz/", "pos": "v.", "meaning": "詳細檢查", "level": "gold", "phrases": ["scrutinize the documents"], "synonyms": ["inspect"], "antonyms": ["ignore"], "example": "Auditors will scrutinize the accounts."},
        {"word": "Acumen", "phonetic": "/əˈkjuːmən/", "pos": "n.", "meaning": "敏銳度；精明", "level": "gold", "phrases": ["business acumen"], "synonyms": ["shrewdness"], "antonyms": [], "example": "He is known for his sharp business acumen."},
        {"word": "Accrue", "phonetic": "/əˈkruː/", "pos": "v.", "meaning": "累積；增加", "level": "gold", "phrases": ["accrue interest"], "synonyms": ["accumulate"], "antonyms": [], "example": "Interest will accrue on your savings account."},
        {"word": "Consolidate", "phonetic": "/kənˈsɑːlɪdeɪt/", "pos": "v.", "meaning": "鞏固；合併", "level": "gold", "phrases": ["consolidate debt"], "synonyms": ["merge"], "antonyms": ["separate"], "example": "The two departments were consolidated."},
        {"word": "Disseminate", "phonetic": "/dɪˈsemɪneɪt/", "pos": "v.", "meaning": "傳播；宣傳", "level": "gold", "phrases": ["disseminate information"], "synonyms": ["spread"], "antonyms": [], "example": "The findings were disseminated to the public."},
        {"word": "Pragmatic", "phonetic": "/præɡˈmætɪk/", "pos": "adj.", "meaning": "務實的", "level": "gold", "phrases": ["pragmatic approach"], "synonyms": ["practical"], "antonyms": ["idealistic"], "example": "We need a pragmatic solution to the problem."},
        # 此處為縮減演示，腳本將包含更多單字...
    ]
    # 這裡我先展示前 60 個高品質單字，後續可以隨時追加
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("已成功寫入核心單字庫。")

if __name__ == "__main__":
    populate()
