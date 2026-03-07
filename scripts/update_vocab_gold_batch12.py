import json

# 第 551-600 個高品質單字對應表 (金色等級)
enriched_data_gold_12 = {
    "drug addiction": {"phonetic": "/drʌɡ əˈdɪkʃn/", "pos": "n. phr.", "meaning": "藥物上癮；毒癮", "phrases": ["overcome drug addiction"], "synonyms": ["substance dependence"], "antonyms": [], "example": "The center provides support and treatment for people struggling with drug addiction."},
    "in the aggregate": {"phonetic": "/ɪn ðə ˈæɡrɪɡət/", "pos": "phr.", "meaning": "總計；合計", "phrases": [], "synonyms": ["altogether", "in total"], "antonyms": ["individually"], "example": "In the aggregate, the company's performance has been strong this year."},
    "patron": {"phonetic": "/ˈpeɪtrən/", "pos": "n.", "meaning": "贊助人；老顧客", "phrases": ["patron of the arts"], "synonyms": ["sponsor", "customer"], "antonyms": [], "example": "The museum is looking for new patrons to help fund its upcoming exhibition."},
    "patronize": {"phonetic": "/ˈpeɪtrənaɪz/", "pos": "v.", "meaning": "光顧；資助；屈尊俯就地對待", "phrases": [], "synonyms": ["frequent", "support", "condescend"], "antonyms": [], "example": "We encourage our employees to patronize local businesses in the neighborhood."},
    "A growing body of": {"phonetic": "/ə ˈɡroʊɪŋ ˈbɑːdi əv/", "pos": "phr.", "meaning": "越來越多的(證據、研究等)", "phrases": ["a growing body of evidence"], "synonyms": ["an increasing amount of"], "antonyms": [], "example": "A growing body of research suggests that a balanced diet is key to longevity."},
    "strings attached": {"phonetic": "/strɪŋz əˈtætʃt/", "pos": "phr.", "meaning": "附帶條件", "phrases": ["no strings attached"], "synonyms": ["conditions", "provisos"], "antonyms": [], "example": "The grant is offered with no strings attached, allowing the team to use it freely."},
    "mitigate": {"phonetic": "/ˈmɪtɪɡeɪt/", "pos": "v.", "meaning": "減輕；緩解", "phrases": ["mitigate risk"], "synonyms": ["alleviate", "reduce"], "antonyms": ["aggravate", "exacerbate"], "example": "The new policy is designed to mitigate the negative impact of the economic downturn."},
    "lounge around": {"phonetic": "/laʊndʒ əˈraʊnd/", "pos": "v. phr.", "meaning": "閒蕩；懶洋洋地混", "phrases": [], "synonyms": ["loiter", "relax"], "antonyms": ["work hard"], "example": "Instead of working, he spent the whole afternoon lounging around the break room."},
    "sanitation": {"phonetic": "/ˌsænɪˈteɪʃn/", "pos": "n.", "meaning": "公共衛生；衛生系統", "phrases": ["sanitation department"], "synonyms": ["hygiene"], "antonyms": [], "example": "Improvements in sanitation have significantly reduced the spread of diseases in the city."},
    "incapacitate": {"phonetic": "/ˌɪnkəˈpæsɪteɪt/", "pos": "v.", "meaning": "使失去能力；使殘廢", "phrases": [], "synonyms": ["disable", "cripple"], "antonyms": ["enable"], "example": "A serious injury could incapacitate a worker for several months."},
    "mental": {"phonetic": "/ˈmentl/", "pos": "adj.", "meaning": "心理的；精神的", "phrases": ["mental health"], "synonyms": ["psychological", "cognitive"], "antonyms": ["physical"], "example": "Stress at work can have a significant impact on an employee's mental well-being."},
    "ground": {"phonetic": "/ɡraʊnd/", "pos": "n./v.", "meaning": "地面；理由；磨碎(grind過去式)", "phrases": ["on the grounds of", "common ground"], "synonyms": ["earth", "basis", "reason"], "antonyms": ["sky"], "example": "The company was sued on the grounds of unfair dismissal by its former employee."},
    "perceive as": {"phonetic": "/pərˈsiːv æz/", "pos": "v. phr.", "meaning": "視為；感知為", "phrases": [], "synonyms": ["regard as", "view as"], "antonyms": [], "example": "The new CEO is perceived as a strong and decisive leader by the staff."},
    "subtler": {"phonetic": "/ˈsʌtlər/", "pos": "adj. (comparative)", "meaning": "更細微的；更巧妙的", "phrases": [], "synonyms": ["finer", "more delicate"], "antonyms": ["obvious"], "example": "There are subtler differences between the two product models that only experts can notice."},
    "ascertain": {"phonetic": "/ˌæsərˈteɪn/", "pos": "v.", "meaning": "查明；弄清", "phrases": ["ascertain the facts"], "synonyms": ["determine", "discover"], "antonyms": [], "example": "The investigators are working to ascertain the cause of the fire in the warehouse."},
    "compound": {"phonetic": "/ˈkɑːmpaʊnd/", "pos": "n./v./adj.", "meaning": "複合物；合成；惡化", "phrases": ["chemical compound", "compound interest"], "synonyms": ["mixture", "worsen"], "antonyms": ["simple"], "example": "High interest rates will compound the company's existing financial problems."},
    "alienation": {"phonetic": "/ˌeɪliəˈneɪʃn/", "pos": "n.", "meaning": "疏離；疏遠", "phrases": ["social alienation"], "synonyms": ["estrangement", "isolation"], "antonyms": ["connection", "inclusion"], "example": "Long working hours can lead to a sense of alienation from family and friends."},
    "precarious": {"phonetic": "/prɪˈkeriəs/", "pos": "adj.", "meaning": "不穩定的；危險的", "phrases": ["precarious position"], "synonyms": ["unstable", "risky"], "antonyms": ["stable", "secure"], "example": "The company's financial situation remains precarious due to the ongoing trade war."},
    "discretion": {"phonetic": "/dɪˈskreʃn/", "pos": "n.", "meaning": "謹慎；裁量權", "phrases": ["at one's discretion", "viewer discretion"], "synonyms": ["caution", "judgment"], "antonyms": ["recklessness", "imprudence"], "example": "The manager has the discretion to approve small expenses without consulting the board."},
    "keep track of": {"phonetic": "/kiːp træk əv/", "pos": "v. phr.", "meaning": "記錄；追蹤", "phrases": [], "synonyms": ["monitor", "record"], "antonyms": ["lose track of"], "example": "It is important to keep track of all your business expenses for tax purposes."},
    "A vast majority of": {"phonetic": "/ə væst məˈdʒɔːrəti əv/", "pos": "phr.", "meaning": "絕大多數的", "phrases": [], "synonyms": ["most", "the bulk of"], "antonyms": ["a tiny minority of"], "example": "A vast majority of employees expressed their satisfaction with the new health benefits."},
    "Nonintrusive": {"phonetic": "/ˌnɑːnɪnˈtruːsɪv/", "pos": "adj.", "meaning": "非侵入性的；不擾人的", "phrases": ["nonintrusive testing"], "synonyms": ["unobtrusive"], "antonyms": ["intrusive"], "example": "The new security cameras are designed to be nonintrusive and blend into the environment."},
    "intrude": {"phonetic": "/ɪnˈtruːd/", "pos": "v.", "meaning": "侵入；闖入", "phrases": ["intrude on privacy"], "synonyms": ["encroach", "invade"], "antonyms": ["withdraw"], "example": "I'm sorry to intrude, but there is an urgent phone call for the manager."},
    "assemble": {"phonetic": "/əˈsembl/", "pos": "v.", "meaning": "組裝；集合", "phrases": ["assemble a team"], "synonyms": ["gather", "collect", "build"], "antonyms": ["disassemble", "disperse"], "example": "The workers will assemble the new machinery in the factory tomorrow morning."},
    "fronts": {"phonetic": "/frʌnts/", "pos": "n.", "meaning": "方面；前線(複數)", "phrases": ["on all fronts"], "synonyms": ["aspects"], "antonyms": [], "example": "The company is making progress on all fronts, including sales and research."},
    "millennium": {"phonetic": "/mɪˈleniəm/", "pos": "n.", "meaning": "千年；千禧年", "phrases": ["new millennium"], "synonyms": [], "antonyms": [], "example": "The turn of the millennium saw a significant increase in the use of digital technology."},
    "pad": {"phonetic": "/pæd/", "pos": "n./v.", "meaning": "墊子；便箋本；虛報", "phrases": ["pad an expense account", "launch pad"], "synonyms": ["cushion", "notebook"], "antonyms": [], "example": "The employee was fired after he was caught padding his monthly expense account."},
    "tempt": {"phonetic": "/tempt/", "pos": "v.", "meaning": "誘惑；吸引", "phrases": ["tempted to"], "synonyms": ["allure", "entice"], "antonyms": ["deter", "repel"], "example": "The low prices might tempt customers to buy things they don't really need."},
    "postpone": {"phonetic": "/poʊˈspoʊn/", "pos": "v.", "meaning": "延期", "phrases": ["postpone a meeting"], "synonyms": ["delay", "defer"], "antonyms": ["advance", "bring forward"], "example": "The meeting has been postponed until next week due to the manager's illness."},
    "simultaneously": {"phonetic": "/ˌsaɪmlˈteɪniəsli/", "pos": "adv.", "meaning": "同時地", "phrases": [], "synonyms": ["at the same time", "concurrently"], "antonyms": ["sequentially"], "example": "The data was updated simultaneously on all the company's servers around the world."},
    "commerce": {"phonetic": "/ˈkɑːmɜːrs/", "pos": "n.", "meaning": "商業；貿易", "phrases": ["e-commerce", "chamber of commerce"], "synonyms": ["trade", "business"], "antonyms": [], "example": "The city has long been a major center of international commerce and finance."},
    "migration": {"phonetic": "/maɪˈɡreɪʃn/", "pos": "n.", "meaning": "遷移；移居", "phrases": ["data migration"], "synonyms": ["movement", "relocation"], "antonyms": [], "example": "The migration of the company's database to the new cloud system will take several hours."},
    "Tariffs": {"phonetic": "/ˈtærɪfs/", "pos": "n.", "meaning": "關稅(複數)", "phrases": ["impose tariffs"], "synonyms": ["duties", "taxes"], "antonyms": [], "example": "The government has decided to impose new tariffs on imported steel and aluminum."},
    "tread": {"phonetic": "/tred/", "pos": "v./n.", "meaning": "踏；步履", "phrases": ["tread carefully"], "synonyms": ["step", "walk"], "antonyms": [], "example": "The company needs to tread carefully when negotiating with its international partners."},
    "well-trodden territory": {"phonetic": "/ˌwel ˈtrɑːdn ˈterətɔːri/", "pos": "phr.", "meaning": "熟悉的領域；老生常談", "phrases": [], "synonyms": [], "antonyms": ["uncharted territory"], "example": "This marketing strategy is well-trodden territory for our experienced sales team."},
    "The chief executive": {"phonetic": "/ðə tʃiːf ɪɡˈzekjətɪv/", "pos": "n. phr.", "meaning": "執行長；最高負責人", "phrases": [], "synonyms": ["CEO"], "antonyms": [], "example": "The chief executive announced a new plan to expand the company's operations."},
    "dying industry": {"phonetic": "/ˈdaɪɪŋ ˈɪndəstri/", "pos": "n. phr.", "meaning": "夕陽產業", "phrases": [], "synonyms": ["declining industry"], "antonyms": ["growth industry"], "example": "Coal mining is often considered a dying industry in many developed countries."},
    "weighs": {"phonetic": "/weɪz/", "pos": "v.", "meaning": "稱重；權衡(第三人稱單數)", "phrases": ["weigh the options"], "synonyms": ["consider", "evaluate"], "antonyms": [], "example": "The manager carefully weighs all the pros and cons before making a decision."},
    "all the rage": {"phonetic": "/ɔːl ðə reɪdʒ/", "pos": "phr.", "meaning": "風行一時；非常流行", "phrases": [], "synonyms": ["very popular", "trendy"], "antonyms": ["outdated"], "example": "Eco-friendly products are all the rage among young consumers this summer."},
    "electrical hybrids": {"phonetic": "/ɪˈlektrɪkl ˈhaɪbrɪdz/", "pos": "n. phr.", "meaning": "油電混合車(複數)", "phrases": [], "synonyms": [], "antonyms": [], "example": "The demand for electrical hybrids has increased due to rising fuel costs."},
    "fuel cells": {"phonetic": "/ˈfjuːəl selz/", "pos": "n. phr.", "meaning": "燃料電池(複數)", "phrases": [], "synonyms": [], "antonyms": [], "example": "Researchers are looking for ways to make fuel cells more efficient and affordable."},
    "the ground-level": {"phonetic": "/ðə ɡraʊnd ˈlevl/", "pos": "n./adj.", "meaning": "地面層；基層", "phrases": ["ground-level entrance"], "synonyms": ["ground floor"], "antonyms": [], "example": "The shop is located on the ground-level of the new office building."},
    "platform": {"phonetic": "/ˈplæt fɔːrm/", "pos": "n.", "meaning": "平台；月台；政綱", "phrases": ["online platform", "social media platform"], "synonyms": ["stage", "basis"], "antonyms": [], "example": "The company has launched a new online platform for its customers to buy products."},
    "intellectual property": {"phonetic": "/ˌɪntəˈlektʃuəl ˈprɑːpərti/", "pos": "n. phr.", "meaning": "智慧財產權(IP)", "phrases": ["IP rights"], "synonyms": ["IP"], "antonyms": [], "example": "Protecting intellectual property is essential for companies in the technology sector."},
    "battlefield": {"phonetic": "/ˈbætlfiːld/", "pos": "n.", "meaning": "戰場", "phrases": ["corporate battlefield"], "synonyms": [], "antonyms": [], "example": "The smartphone market has become a major battlefield for global technology firms."},
    "sluggish": {"phonetic": "/ˈslʌɡɪʃ/", "pos": "adj.", "meaning": "蕭條的；緩慢的；懶散的", "phrases": ["sluggish economy", "sluggish sales"], "synonyms": ["slow", "inactive", "lethargic"], "antonyms": ["brisk", "active", "rapid"], "example": "Sales have remained sluggish this quarter despite the new marketing campaign."},
    "delicate": {"phonetic": "/ˈdelɪkət/", "pos": "adj.", "meaning": "脆弱的；精緻的；棘手的", "phrases": ["delicate situation", "delicate fabric"], "synonyms": ["fragile", "fine", "sensitive"], "antonyms": ["robust", "rough"], "example": "The negotiations are in a delicate stage and could fail if we are not careful."},
    "stake": {"phonetic": "/steɪk/", "pos": "n./v.", "meaning": "股份；利害關係；賭注", "phrases": ["stakeholder", "controlling stake"], "synonyms": ["share", "interest"], "antonyms": [], "example": "The parent company holds a forty percent stake in its international subsidiary."},
    "curtain": {"phonetic": "/ˈkɜːrtn/", "pos": "n.", "meaning": "窗簾；幕", "phrases": ["iron curtain", "curtain call"], "synonyms": ["drape"], "antonyms": [], "example": "Please close the curtains to block out the bright sunlight in the office."},
    "carton": {"phonetic": "/ˈkɑːrtn/", "pos": "n.", "meaning": "紙盒；紙板箱", "phrases": ["a milk carton"], "synonyms": ["box", "case"], "antonyms": [], "example": "The order was delivered in three large cartons, which were clearly labeled."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_12:
        update_info = enriched_data_gold_12[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 551-600 個單字。")
