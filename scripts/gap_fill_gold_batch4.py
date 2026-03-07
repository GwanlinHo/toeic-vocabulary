import json

# 金色等級補漏第 4 部分
gap_fill_gold_4 = {
    "tone": {"phonetic": "/toʊn/", "pos": "n.", "meaning": "語氣；音調；色調", "phrases": ["tone of voice"], "synonyms": ["inflection", "mood"], "antonyms": [], "example": "The manager's tone during the meeting was professional but firm."},
    "humorous": {"phonetic": "/ˈhjuːmərəs/", "pos": "adj.", "meaning": "幽默的；滑稽的", "phrases": ["humorous story"], "synonyms": ["funny", "amusing"], "antonyms": ["serious", "solemn"], "example": "He gave a very humorous speech that kept everyone laughing throughout the dinner."},
    "a registration form": {"phonetic": "/ə ˌredʒɪˈstreɪʃn fɔːrm/", "pos": "n. phr.", "meaning": "報名表；登記表", "phrases": ["fill out a registration form"], "synonyms": [], "antonyms": [], "example": "Please complete the registration form and return it to the front desk."},
    "deal with": {"phonetic": "/diːl wɪð/", "pos": "v. phr.", "meaning": "處理；應付；涉及", "phrases": ["deal with a customer"], "synonyms": ["handle", "manage"], "antonyms": [], "example": "Our customer service team is trained to deal with complaints efficiently."},
    "infer": {"phonetic": "/ɪnˈfɜːr/", "pos": "v.", "meaning": "推斷；暗示", "phrases": ["infer from"], "synonyms": ["deduce", "conclude"], "antonyms": [], "example": "We can infer from the data that there is a growing demand for eco-friendly products."},
    "recommend sb without reservation": {"phonetic": "/ˌrekəˈmend ˈsʌmbədi wɪˈðaʊt ˌrezərˈveɪʃn/", "pos": "v. phr.", "meaning": "毫無保留地推薦某人", "phrases": [], "synonyms": [], "antonyms": [], "example": "I can recommend her for the position without reservation based on her excellent performance."},
    "endear": {"phonetic": "/ɪnˈdɪr/", "pos": "v.", "meaning": "使受喜愛；使受愛戴", "phrases": ["endear oneself to someone"], "synonyms": [], "antonyms": [], "example": "Her helpful attitude and dedication to her work quickly endeared her to her colleagues."},
    "moderation": {"phonetic": "/ˌmɑːdəˈreɪʃn/", "pos": "n.", "meaning": "適度；節制", "phrases": ["in moderation"], "synonyms": ["temperance"], "antonyms": ["excess"], "example": "It is important to enjoy holiday treats in moderation to maintain a healthy lifestyle."},
    "psychological": {"phonetic": "/ˌsaɪkəˈlɑːdʒɪkl/", "pos": "adj.", "meaning": "心理的；心理學的", "phrases": ["psychological effect"], "synonyms": ["mental"], "antonyms": ["physical"], "example": "The researchers are studying the psychological impact of long-term unemployment."},
    "prospective": {"phonetic": "/prəˈspektɪv/", "pos": "adj.", "meaning": "預期的；潛在的", "phrases": ["prospective client", "prospective employee"], "synonyms": ["potential", "future"], "antonyms": [], "example": "The company is meeting with several prospective partners to discuss the new project."},
    "joyless": {"phonetic": "/ˈdʒɔɪləs/", "pos": "adj.", "meaning": "不快樂的；沈悶的", "phrases": [], "synonyms": ["gloomy", "miserable"], "antonyms": ["joyful", "happy"], "example": "The atmosphere in the office was joyless after the news of the budget cuts."},
    "revise": {"phonetic": "/rɪˈvaɪz/", "pos": "v.", "meaning": "修訂；修改；複習", "phrases": ["revise a report"], "synonyms": ["amend", "update"], "antonyms": [], "example": "We need to revise the marketing plan to better reflect the current market conditions."},
    "take the minutes": {"phonetic": "/teɪk ðə ˈmɪnɪts/", "pos": "v. phr.", "meaning": "記錄會議記錄", "phrases": [], "synonyms": [], "antonyms": [], "example": "The secretary is responsible for taking the minutes during the monthly board meetings."},
    "trustee": {"phonetic": "/trʌˈstiː/", "pos": "n.", "meaning": "受託人；理事", "phrases": ["board of trustees"], "synonyms": ["administrator", "guardian"], "antonyms": [], "example": "The university is managed by a board of trustees consisting of prominent community leaders."},
    "bay": {"phonetic": "/beɪ/", "pos": "n.", "meaning": "海灣；隔間；(犬)吠", "phrases": ["loading bay", "keep at bay"], "synonyms": ["gulf", "inlet"], "antonyms": [], "example": "The new warehouse has ten separate loading bays for delivery trucks."},
    "keep sb/sth at bay": {"phonetic": "/kiːp æt beɪ/", "pos": "v. phr.", "meaning": "使...無法靠近；阻止...惡化", "phrases": [], "synonyms": ["hold off", "prevent"], "antonyms": [], "example": "The new security measures are designed to keep unauthorized persons at bay."},
    "in favor of sb/sth": {"phonetic": "/ɪn ˈfeɪvər əv/", "pos": "phr.", "meaning": "贊成...；支持...", "phrases": [], "synonyms": ["supporting"], "antonyms": ["against"], "example": "The board of directors voted in favor of the proposed merger."},
    "vote against": {"phonetic": "/voʊt əˈɡenst/", "pos": "v. phr.", "meaning": "投票反對", "phrases": [], "synonyms": ["oppose"], "antonyms": ["vote for"], "example": "Several shareholders decided to vote against the new investment plan."},
    "vote for": {"phonetic": "/voʊt fər/", "pos": "v. phr.", "meaning": "投票支持", "phrases": [], "synonyms": ["support"], "antonyms": ["vote against"], "example": "I'm planning to vote for the candidate who has the most experience in the industry."},
    "curator": {"phonetic": "/ˈkjʊreɪtər/", "pos": "n.", "meaning": "館長；策展人", "phrases": ["museum curator"], "synonyms": ["manager", "keeper"], "antonyms": [], "example": "The museum curator is responsible for organizing the new modern art exhibition."},
    "cast a vote": {"phonetic": "/kæst ə voʊt/", "pos": "v. phr.", "meaning": "投票", "phrases": [], "synonyms": ["vote"], "antonyms": [], "example": "Every member of the association is entitled to cast a vote in the election."},
    "term": {"phonetic": "/tɜːrm/", "pos": "n./v.", "meaning": "術語；期限；條款；稱為", "phrases": ["long term", "in terms of", "fixed term"], "synonyms": ["period", "word", "condition"], "antonyms": [], "example": "The contract is for a fixed term of three years and can be renewed."},
    "treasure": {"phonetic": "/ˈtreʒər/", "pos": "n./v.", "meaning": "寶藏；珍品；珍惜", "phrases": ["hidden treasure"], "synonyms": ["fortune", "prize", "cherish"], "antonyms": ["trash"], "example": "The museum features many ancient treasures from various civilizations around the world."},
    "sculpture": {"phonetic": "/ˈskʌlptʃər/", "pos": "n./v.", "meaning": "雕像；雕刻", "phrases": ["modern sculpture"], "synonyms": ["statue"], "antonyms": [], "example": "A large bronze sculpture stands in the center of the office building's main lobby."},
    "custodian": {"phonetic": "/kʌˈstoʊdiən/", "pos": "n.", "meaning": "管理員；監護人", "phrases": ["legal custodian"], "synonyms": ["guardian", "caretaker"], "antonyms": [], "example": "The bank acts as a custodian for the securities held in the investment fund."},
    "custody": {"phonetic": "/ˈkʌstədi/", "pos": "n.", "meaning": "監護；拘留；保管", "phrases": ["in custody", "take into custody"], "synonyms": ["protection", "detention"], "antonyms": [], "example": "The suspect was taken into police custody for further questioning."},
    "ties": {"phonetic": "/taɪz/", "pos": "n.", "meaning": "關係；領帶(複數)", "phrases": ["family ties", "business ties"], "synonyms": ["connections", "bonds"], "antonyms": [], "example": "The two companies have maintained strong business ties for over twenty years."},
    "diplomatic ties": {"phonetic": "/ˌdɪpləˈmætɪk taɪz/", "pos": "n. phr.", "meaning": "外交關係", "phrases": ["break diplomatic ties"], "synonyms": ["diplomatic relations"], "antonyms": [], "example": "The two countries decided to restore diplomatic ties after years of conflict."},
    "fax": {"phonetic": "/fæks/", "pos": "n./v.", "meaning": "傳真", "phrases": ["send a fax"], "synonyms": ["facsimile"], "antonyms": [], "example": "Please fax a copy of the signed contract to our office by the end of the day."},
    "at length": {"phonetic": "/æt leŋkθ/", "pos": "phr.", "meaning": "詳細地；最後", "phrases": ["discuss at length"], "synonyms": ["in detail", "thoroughly"], "antonyms": ["briefly"], "example": "The manager discussed the new project at length during the morning meeting."},
    "go out": {"phonetic": "/ɡoʊ aʊt/", "pos": "v. phr.", "meaning": "出去；熄滅；(燈)停", "phrases": ["go out for dinner"], "synonyms": ["leave", "extinguish"], "antonyms": ["come in"], "example": "All the lights in the office went out during the sudden power failure."},
    "a power failure": {"phonetic": "/ə ˈpaʊər ˈfeɪljər/", "pos": "n. phr.", "meaning": "停電", "phrases": [], "synonyms": ["blackout", "power outage"], "antonyms": [], "example": "The factory had to stop production for several hours due to a power failure."},
    "the intensive care unit": {"phonetic": "/ðə ɪnˈtensɪv ker ˈjuːnɪt/", "pos": "n. phr.", "meaning": "加護病房(ICU)", "phrases": [], "synonyms": ["ICU"], "antonyms": [], "example": "The patient was moved to the intensive care unit following the major operation."},
    "hospitalization": {"phonetic": "/ˌhɑːspɪtələˈzeɪʃn/", "pos": "n.", "meaning": "住院", "phrases": ["require hospitalization"], "synonyms": [], "antonyms": [], "example": "His injuries were serious and required several weeks of hospitalization and physical therapy."},
    "electrocute": {"phonetic": "/ɪˈlektrə kjuːt/", "pos": "v.", "meaning": "觸電；電死", "phrases": [], "synonyms": [], "antonyms": [], "example": "Always turn off the power before repairing any electrical device to avoid getting electrocuted."},
    "registered mail": {"phonetic": "/ˈredʒɪstərd meɪl/", "pos": "n. phr.", "meaning": "掛號信", "phrases": ["send by registered mail"], "synonyms": [], "antonyms": [], "example": "You should send the original legal documents by registered mail to ensure they arrive safely."},
    "regular mail": {"phonetic": "/ˈreɡjələr meɪl/", "pos": "n. phr.", "meaning": "平信", "phrases": [], "synonyms": ["standard mail"], "antonyms": ["registered mail", "express mail"], "example": "The brochure was sent by regular mail and should arrive in about five working days."},
    "recreational": {"phonetic": "/ˌrekriˈeɪʃənl/", "pos": "adj.", "meaning": "娛樂的；休閒的", "phrases": ["recreational activities"], "synonyms": ["leisure"], "antonyms": ["work-related"], "example": "The company provides several recreational facilities for its employees, including a gym."},
    "babysit": {"phonetic": "/ˈbeibɪˌsɪt/", "pos": "v.", "meaning": "當臨時保姆；照看", "phrases": [], "synonyms": [], "antonyms": [], "example": "She often babysits for her neighbors' children during the weekends."},
    "frank": {"phonetic": "/fræŋk/", "pos": "adj.", "meaning": "坦白的；直率的", "phrases": ["frank discussion"], "synonyms": ["honest", "candid", "direct"], "antonyms": ["dishonest", "evasive"], "example": "The manager gave a frank assessment of the project's current progress and challenges."},
    "arrogant": {"phonetic": "/ˈærəɡənt/", "pos": "adj.", "meaning": "傲慢的；自大的", "phrases": ["arrogant behavior"], "synonyms": ["haughty", "proud", "conceited"], "antonyms": ["humble", "modest"], "example": "His arrogant attitude made it difficult for him to work effectively with the rest of the team."},
    "impersonal": {"phonetic": "/ɪmˈpɜːrsənl/", "pos": "adj.", "meaning": "不近人情的；冷淡的；客觀的", "phrases": ["impersonal service"], "synonyms": ["cold", "detached"], "antonyms": ["personal", "warm"], "example": "Large corporations can sometimes feel very impersonal to their customers and employees."},
    "take the initiative in + Ving": {"word": "take the initiative", "phonetic": "/teɪk ðə ɪˈnɪʃətɪv/", "pos": "v. phr.", "meaning": "主動(做某事)", "phrases": [], "synonyms": ["proactive"], "antonyms": [], "example": "The manager encouraged all employees to take the initiative in solving problems."},
    "interpersonal skills": {"phonetic": "/ˌɪntərˈpɜːrsənl skɪlz/", "pos": "n. phr.", "meaning": "人際關係技巧", "phrases": ["excellent interpersonal skills"], "synonyms": ["social skills"], "antonyms": [], "example": "Having excellent interpersonal skills is essential for anyone working in sales or customer service."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in gap_fill_gold_4:
        update_info = gap_fill_gold_4[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("完成金色等級補漏第 4 部分 (Tone 到 Interpersonal skills)。")
