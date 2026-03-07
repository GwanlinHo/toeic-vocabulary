import json

# 第 1-50 個高品質單字對應表 (金色等級)
enriched_data_gold_1 = {
    "a letter of application": {"phonetic": "/ə ˈletər əv ˌæplɪˈkeɪʃn/", "pos": "n. phr.", "meaning": "求職信", "phrases": ["enclose a letter of application"], "synonyms": ["cover letter"], "antonyms": [], "example": "You should always include a letter of application when applying for a new job."},
    "specialize in": {"phonetic": "/ˈspeʃəlaɪz ɪn/", "pos": "v. phr.", "meaning": "專攻於；專門從事", "phrases": ["specialize in law"], "synonyms": ["focus on"], "antonyms": [], "example": "Our law firm specializes in providing legal advice to international technology companies."},
    "board members": {"phonetic": "/bɔːrd ˈmembərz/", "pos": "n. phr.", "meaning": "董事會成員", "phrases": ["meeting of board members"], "synonyms": [], "antonyms": [], "example": "The board members will meet tomorrow to discuss the company's financial results."},
    "the board of directors": {"phonetic": "/ðə bɔːrd əv dəˈrektərz/", "pos": "n. phr.", "meaning": "董事會", "phrases": ["chairman of the board"], "synonyms": ["the board"], "antonyms": [], "example": "The board of directors has approved the plan to expand the business into Europe."},
    "talent": {"phonetic": "/ˈtælənt/", "pos": "n.", "meaning": "天賦；人才", "phrases": ["recruit talent"], "synonyms": ["gift", "ability"], "antonyms": [], "example": "The company is always looking for new talent to join its creative marketing team."},
    "clothier": {"phonetic": "/ˈkloʊðiər/", "pos": "n.", "meaning": "服飾商；裁縫", "phrases": ["menswear clothier"], "synonyms": ["tailor", "outfitter"], "antonyms": [], "example": "The local clothier offers high-quality tailor-made suits for business professionals."},
    "discoloration": {"phonetic": "/dɪsˌkʌləˈreɪʃn/", "pos": "n.", "meaning": "褪色；變色", "phrases": ["fabric discoloration"], "synonyms": ["staining"], "antonyms": [], "example": "Please check the fabric for any signs of discoloration before you buy the clothing."},
    "defect": {"phonetic": "/ˈdiːfekt/", "pos": "n.", "meaning": "缺點；瑕疵", "phrases": ["manufacturing defect"], "synonyms": ["flaw", "imperfection"], "antonyms": ["perfection"], "example": "The customer returned the product because of a manufacturing defect in the battery."},
    "plastic surgery": {"phonetic": "/ˌplæstɪk ˈsɜːrdʒəri/", "pos": "n. phr.", "meaning": "整形手術", "phrases": ["undergo plastic surgery"], "synonyms": ["cosmetic surgery"], "antonyms": [], "example": "He decided to undergo plastic surgery to repair the damage caused by the accident."},
    "flawed": {"phonetic": "/flɔːd/", "pos": "adj.", "meaning": "有瑕疵的", "phrases": ["flawed strategy"], "synonyms": ["defective", "imperfect"], "antonyms": ["flawless"], "example": "The company's marketing strategy was flawed and failed to attract enough customers."},
    "flawless": {"phonetic": "/ˈflɔːləs/", "pos": "adj.", "meaning": "無暇的；完美的", "phrases": ["flawless performance"], "synonyms": ["perfect", "immaculate"], "antonyms": ["flawed"], "example": "The actress's performance in the new movie was flawless and received great reviews."},
    "be out on business": {"phonetic": "/bi aʊt ɑːn ˈbɪznəs/", "pos": "v. phr.", "meaning": "出差中", "phrases": [], "synonyms": ["be away on business"], "antonyms": [], "example": "The manager will be out on business for the next two weeks in the United States."},
    "set up": {"phonetic": "/set ʌp/", "pos": "v. phr.", "meaning": "建立；設置", "phrases": ["set up a business"], "synonyms": ["establish", "install"], "antonyms": ["dismantle"], "example": "The company is planning to set up a new research facility in the city center next year."},
    "look forward to +N/Ving": {"word": "look forward to", "phonetic": "/lʊk ˈfɔːrwərd tuː/", "pos": "v. phr.", "meaning": "期待", "phrases": ["look forward to meeting you"], "synonyms": ["anticipate"], "antonyms": [], "example": "We look forward to meeting you for an interview and discussing your application."},
    "hand in": {"phonetic": "/hænd ɪn/", "pos": "v. phr.", "meaning": "繳交；提交", "phrases": ["hand in a report"], "synonyms": ["submit", "deliver"], "antonyms": [], "example": "Please remember to hand in your monthly report to the manager by Friday afternoon."},
    "vacancy": {"phonetic": "/ˈveɪkənsi/", "pos": "n.", "meaning": "職缺；空房", "phrases": ["job vacancy"], "synonyms": ["opening"], "antonyms": [], "example": "There is currently a vacancy for a senior marketing manager in our overseas office."},
    "resume": {"phonetic": "/ˈrezəmeɪ/", "pos": "n.", "meaning": "履歷表", "phrases": ["submit a resume"], "synonyms": ["CV"], "antonyms": [], "example": "Please send your resume and a cover letter to our human resources department."},
    "curriculum vitae": {"phonetic": "/kəˌrɪkjələm ˈviːtaɪ/", "pos": "n. phr.", "meaning": "履歷(CV)", "phrases": ["attach a CV"], "synonyms": ["resume"], "antonyms": [], "example": "A detailed curriculum vitae should be included with your application for the position."},
    "reference": {"phonetic": "/ˈrefrəns/", "pos": "n.", "meaning": "推薦信；參考", "phrases": ["professional reference"], "synonyms": ["recommendation"], "antonyms": [], "example": "He provided several professional references from his previous employers in the industry."},
    "probation": {"phonetic": "/proʊˈbeɪʃn/", "pos": "n.", "meaning": "試用期", "phrases": ["on probation"], "synonyms": ["trial period"], "antonyms": [], "example": "New employees are required to undergo a three-month probation period before being hired."},
    "promotion": {"phonetic": "/prəˈmoʊʃn/", "pos": "n.", "meaning": "升遷；晉升", "phrases": ["get a promotion"], "synonyms": ["advancement"], "antonyms": ["demotion"], "example": "She received a promotion to department head after her successful management of the project."},
    "candidate": {"phonetic": "/ˈkændɪdət/", "pos": "n.", "meaning": "應徵者；候選人", "phrases": ["qualified candidate"], "synonyms": ["applicant"], "antonyms": [], "example": "We are currently interviewing several candidates for the position of sales director."},
    "clerk": {"phonetic": "/klɜːrk/", "pos": "n.", "meaning": "辦事員；店員", "phrases": ["shipping clerk", "desk clerk"], "synonyms": ["office worker"], "antonyms": [], "example": "The shipping clerk is responsible for processing all the orders for international delivery."},
    "permanent": {"phonetic": "/ˈpɜːrmənənt/", "pos": "adj.", "meaning": "永久的；固定的", "phrases": ["permanent job"], "synonyms": ["lasting", "stable"], "antonyms": ["temporary"], "example": "After his probation period, he was offered a permanent position in the company."},
    "temporary": {"phonetic": "/ˈtempəreri/", "pos": "adj.", "meaning": "暫時的；臨時的", "phrases": ["temporary staff"], "synonyms": ["provisional"], "antonyms": ["permanent"], "example": "The company hired several temporary workers to help during the peak holiday season."},
    "recruit": {"phonetic": "/rɪˈkruːt/", "pos": "v./n.", "meaning": "招募；新進成員", "phrases": ["new recruit"], "synonyms": ["enlist", "hire"], "antonyms": [], "example": "The human resources department is working hard to recruit more skilled engineers."},
    "qualification": {"phonetic": "/ˌkwɑːlɪfɪˈkeɪʃn/", "pos": "n.", "meaning": "資格；能力證明", "phrases": ["professional qualification"], "synonyms": ["requirement", "capability"], "antonyms": [], "example": "You need to have the right qualifications and experience to apply for this senior role."},
    "lay off": {"phonetic": "/leɪ ɔːf/", "pos": "v. phr.", "meaning": "解雇；裁員", "phrases": ["be laid off"], "synonyms": ["dismiss", "fire"], "antonyms": ["hire", "employ"], "example": "The company was forced to lay off fifty workers due to the economic downturn."},
    "pension": {"phonetic": "/ˈpenʃn/", "pos": "n.", "meaning": "退休金；養老金", "phrases": ["pension fund", "pension scheme"], "synonyms": ["retirement fund"], "antonyms": [], "example": "He is looking forward to retiring next year and receiving his monthly company pension."},
    "wages": {"phonetic": "/ˈweɪdʒɪz/", "pos": "n.", "meaning": "薪水(按時計)", "phrases": ["minimum wage"], "synonyms": ["pay", "earnings"], "antonyms": [], "example": "The workers are demanding higher wages and better working conditions in the factory."},
    "salary": {"phonetic": "/ˈæləri/", "pos": "n.", "meaning": "薪資(按月/年)", "phrases": ["monthly salary", "competitive salary"], "synonyms": ["income", "pay"], "antonyms": [], "example": "The company offers a competitive salary and a comprehensive benefits package to its staff."},
    "remuneration": {"phonetic": "/rɪˌmjuːnəˈreɪʃn/", "pos": "n.", "meaning": "報酬；酬勞", "phrases": ["financial remuneration"], "synonyms": ["payment", "compensation"], "antonyms": [], "example": "The total remuneration for the position includes a basic salary and a yearly bonus."},
    "stipend": {"phonetic": "/ˈstaɪpend/", "pos": "n.", "meaning": "補貼；獎助金", "phrases": ["monthly stipend"], "synonyms": ["allowance"], "antonyms": [], "example": "Students on the training program will receive a monthly stipend to cover their travel costs."},
    "subsidy": {"phonetic": "/ˈsʌbsədi/", "pos": "n.", "meaning": "補貼；津貼", "phrases": ["government subsidy"], "synonyms": ["grant", "aid"], "antonyms": [], "example": "The government provides a subsidy to companies that invest in renewable energy technology."},
    "allowance": {"phonetic": "/əˈlaʊəns/", "pos": "n.", "meaning": "津貼；額度", "phrases": ["housing allowance", "travel allowance"], "synonyms": ["stipend"], "antonyms": [], "example": "Employees receive a monthly housing allowance in addition to their basic salary."},
    "fringe benefits": {"phonetic": "/frɪndʒ ˈbenɪfɪts/", "pos": "n. phr.", "meaning": "附帶福利", "phrases": ["excellent fringe benefits"], "synonyms": ["perks"], "antonyms": [], "example": "The company's fringe benefits include free health insurance and a gym membership."},
    "perk": {"phonetic": "/pɜːrk/", "pos": "n.", "meaning": "額外好處；待遇", "phrases": ["job perks"], "synonyms": ["benefit", "advantage"], "antonyms": [], "example": "Having a company car is one of the many perks that come with being a senior manager."},
    "redundancy": {"phonetic": "/rɪˈdʌndənsi/", "pos": "n.", "meaning": "裁員；過剩", "phrases": ["voluntary redundancy"], "synonyms": ["layoff"], "antonyms": [], "example": "Many employees are worried about redundancy after the company's recent merger."},
    "severance pay": {"phonetic": "/ˈsevərəns peɪ/", "pos": "n. phr.", "meaning": "資遣費", "phrases": ["receive severance pay"], "synonyms": ["redundancy pay"], "antonyms": [], "example": "Workers who are laid off will receive a severance pay based on their years of service."},
    "commission": {"phonetic": "/kəˈmɪʃn/", "pos": "n./v.", "meaning": "佣金；委託", "phrases": ["earn a commission"], "synonyms": ["percentage", "fee"], "antonyms": [], "example": "Sales representatives earn a base salary plus a commission on every product they sell."},
    "bonus": {"phonetic": "/ˈboʊnəs/", "pos": "n.", "meaning": "獎金；紅利", "phrases": ["annual bonus", "performance bonus"], "synonyms": ["reward", "dividend"], "antonyms": [], "example": "All staff members received a special bonus at the end of the year for their hard work."},
    "incentive": {"phonetic": "/ɪnˈsentɪv/", "pos": "n./adj.", "meaning": "激勵；獎勵", "phrases": ["financial incentive"], "synonyms": ["motivation", "stimulus"], "antonyms": ["deterrent"], "example": "The company offers financial incentives to employees who meet their sales targets."},
    "overtime": {"phonetic": "/ˈoʊvərtaɪm/", "pos": "n./adv.", "meaning": "加班", "phrases": ["work overtime", "overtime pay"], "synonyms": ["extra hours"], "antonyms": [], "example": "Many staff members have been working a lot of overtime to finish the project on schedule."},
    "leave": {"phonetic": "/liːv/", "pos": "n.", "meaning": "休假", "phrases": ["on leave", "maternity leave"], "synonyms": ["vacation", "holiday"], "antonyms": [], "example": "She is currently on maternity leave and is expected to return to work next month."},
    "annual leave": {"phonetic": "/ˈænjuəl liːv/", "pos": "n. phr.", "meaning": "年假", "phrases": ["take annual leave"], "synonyms": ["yearly vacation"], "antonyms": [], "example": "Full-time employees are entitled to twenty days of annual leave after one year of service."},
    "sick leave": {"phonetic": "/sɪk liːv/", "pos": "n. phr.", "meaning": "病假", "phrases": ["paid sick leave"], "synonyms": [], "antonyms": [], "example": "If you are unable to come to work due to illness, you must inform the office of your sick leave."},
    "day off": {"phonetic": "/deɪ ɔːf/", "pos": "n. phr.", "meaning": "休假日", "phrases": ["take a day off"], "synonyms": ["holiday"], "antonyms": [], "example": "The manager gave him a day off as a reward for his hard work during the busy period."},
    "shift": {"phonetic": "/ʃɪft/", "pos": "n./v.", "meaning": "輪班；轉換", "phrases": ["night shift", "working in shifts"], "synonyms": ["turn", "change"], "antonyms": [], "example": "He is currently working the night shift, which starts at 10 PM and ends at 6 AM."},
    "flexible hours": {"phonetic": "/ˌfleksəbl ˈaʊərz/", "pos": "n. phr.", "meaning": "彈性工時", "phrases": ["work flexible hours"], "synonyms": ["flextime"], "antonyms": ["fixed hours"], "example": "The company offers flexible hours to help employees maintain a better work-life balance."},
    "workload": {"phonetic": "/ˈwɜːrkloʊd/", "pos": "n.", "meaning": "工作量", "phrases": ["heavy workload", "manage workload"], "synonyms": ["burden"], "antonyms": [], "example": "Many employees have complained about their heavy workload since the recent staff cuts."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_1:
        update_info = enriched_data_gold_1[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級前 50 個單字。")
