import json

# 第 451-500 個高品質單字對應表 (金色等級)
enriched_data_gold_10 = {
    "in a panic": {"phonetic": "/ɪn ə ˈpænɪk/", "pos": "phr.", "meaning": "驚慌失措地", "phrases": [], "synonyms": ["frantically"], "antonyms": ["calmly"], "example": "The crowd fled in a panic when the alarm went off."},
    "block off": {"phonetic": "/blɑːk ɔːf/", "pos": "v. phr.", "meaning": "封鎖", "phrases": ["block off the street"], "synonyms": ["close off", "seal off"], "antonyms": ["open up"], "example": "The police had to block off the road due to the accident."},
    "up to": {"phonetic": "/ʌp tuː/", "pos": "prep. phr.", "meaning": "多達；高達；取決於", "phrases": ["up to 50% off"], "synonyms": ["as many as"], "antonyms": [], "example": "The company offers discounts of up to fifty percent during the holiday season."},
    "be bound for": {"phonetic": "/bi baʊnd fər/", "pos": "v. phr.", "meaning": "前往...", "phrases": ["bound for London"], "synonyms": ["headed for"], "antonyms": [], "example": "The flight is bound for New York and is expected to depart on time."},
    "mastermind": {"phonetic": "/ˈmæstərmaɪnd/", "pos": "n./v.", "meaning": "主謀；策劃", "phrases": ["mastermind a plan"], "synonyms": ["architect", "planner"], "antonyms": [], "example": "He was identified as the mastermind behind the successful marketing campaign."},
    "devastating": {"phonetic": "/ˈdevəsteɪtɪŋ/", "pos": "adj.", "meaning": "毀滅性的；破壞力極強的", "phrases": ["devastating effect"], "synonyms": ["destructive", "catastrophic"], "antonyms": ["beneficial"], "example": "The flood had a devastating impact on the local economy."},
    "disclose": {"phonetic": "/dɪsˈkloʊz/", "pos": "v.", "meaning": "揭露；公開", "phrases": ["disclose information"], "synonyms": ["reveal", "unveil"], "antonyms": ["conceal", "hide"], "example": "The company was required to disclose its financial records to the auditors."},
    "operative": {"phonetic": "/ˈɑːpərətɪv/", "pos": "adj./n.", "meaning": "運作中的；特工", "phrases": ["intelligence operative"], "synonyms": ["functioning", "agent"], "antonyms": ["inactive"], "example": "The new security system will become fully operative next Monday."},
    "corner": {"phonetic": "/ˈkɔːrnər/", "pos": "n./v.", "meaning": "角落；壟斷；困住", "phrases": ["around the corner", "corner the market"], "synonyms": ["angle", "trap"], "antonyms": [], "example": "The company managed to corner the local market for organic products."},
    "elude": {"phonetic": "/iˈluːd/", "pos": "v.", "meaning": "逃避；躲避；使...不解", "phrases": ["elude capture"], "synonyms": ["evade", "escape"], "antonyms": ["confront", "face"], "example": "The suspect managed to elude the police for several days before being caught."},
    "outpou": {"word": "outpour", "phonetic": "/ˈaʊtpɔːr/", "pos": "n.", "meaning": "傾瀉；流露", "phrases": ["an outpour of grief"], "synonyms": ["outflow", "effusion"], "antonyms": [], "example": "There was an outpour of public support for the families affected by the disaster."},
    "the ground zero site": {"phonetic": "/ðə ɡraʊnd ˈzɪroʊ saɪt/", "pos": "n. phr.", "meaning": "事發地點；歸零地(世貿遺址)", "phrases": [], "synonyms": [], "antonyms": [], "example": "A memorial was built at the ground zero site to honor the victims of the attack."},
    "chant": {"phonetic": "/tʃænt/", "pos": "n./v.", "meaning": "喊叫；吟唱", "phrases": ["chant slogans"], "synonyms": ["shout", "sing"], "antonyms": [], "example": "The protesters began to chant slogans as they marched through the city center."},
    "vigilant": {"phonetic": "/ˈvɪdʒɪlənt/", "pos": "adj.", "meaning": "警覺的；警惕的", "phrases": ["remain vigilant"], "synonyms": ["watchful", "alert"], "antonyms": ["careless", "negligent"], "example": "Security guards must remain vigilant at all times to prevent any unauthorized entry."},
    "demise": {"phonetic": "/dɪˈmaɪz/", "pos": "n.", "meaning": "死亡；終結；垮台", "phrases": ["unexpected demise"], "synonyms": ["death", "end", "fall"], "antonyms": ["birth", "beginning"], "example": "The sudden demise of the company was a shock to its employees and shareholders."},
    "a defining moment": {"phonetic": "/ə dɪˈfaɪnɪŋ ˈmoʊmənt/", "pos": "n. phr.", "meaning": "決定性的時刻", "phrases": [], "synonyms": ["critical moment"], "antonyms": [], "example": "Winning the contract was a defining moment in the history of our small business."},
    "terrorism": {"phonetic": "/ˈterərɪzəm/", "pos": "n.", "meaning": "恐怖主義", "phrases": ["combat terrorism"], "synonyms": [], "antonyms": [], "example": "International cooperation is essential to fight the global threat of terrorism."},
    "relentlessness": {"phonetic": "/rɪˈlentləsnəs/", "pos": "n.", "meaning": "無情；持續不斷", "phrases": [], "synonyms": ["persistence", "severity"], "antonyms": [], "example": "The relentlessness of the storm caused widespread damage across the region."},
    "galvanize": {"phonetic": "/ˈɡælvənaɪz/", "pos": "v.", "meaning": "激勵；促使...採取行動", "phrases": ["galvanize support"], "synonyms": ["inspire", "stimulate"], "antonyms": ["deter", "discourage"], "example": "The speech was intended to galvanize the public into supporting the new environmental policy."},
    "martyr": {"phonetic": "/ˈmɑːrtər/", "pos": "n./v.", "meaning": "烈士；殉道者", "phrases": [], "synonyms": [], "antonyms": [], "example": "He is remembered as a martyr who gave his life for his country's freedom."},
    "impetus": {"phonetic": "/ˈɪmpɪtəs/", "pos": "n.", "meaning": "動力；推動力", "phrases": ["provide impetus"], "synonyms": ["momentum", "stimulus"], "antonyms": [], "example": "The government grant provided the necessary impetus for the research project to proceed."},
    "operationally": {"phonetic": "/ˌɑːpəˈreɪʃənəli/", "pos": "adv.", "meaning": "在運作上", "phrases": [], "synonyms": ["functionally"], "antonyms": [], "example": "The two departments are now operationally independent of each other."},
    "potent": {"phonetic": "/ˈpoʊtnt/", "pos": "adj.", "meaning": "強有力的；有效的", "phrases": ["potent medicine"], "synonyms": ["powerful", "effective"], "antonyms": ["weak", "ineffective"], "example": "The company's new advertising strategy proved to be a potent tool for increasing sales."},
    "radical": {"phonetic": "/ˈrædɪkl/", "pos": "adj./n.", "meaning": "激進的；徹底的", "phrases": ["radical change"], "synonyms": ["extreme", "fundamental"], "antonyms": ["conservative", "minor"], "example": "The company underwent a radical restructuring to improve its financial position."},
    "brace for/against": {"phonetic": "/breɪs fər/", "pos": "v. phr.", "meaning": "準備應對(困難/危險)", "phrases": ["brace for impact"], "synonyms": ["prepare for"], "antonyms": [], "example": "The city is bracing for the arrival of the hurricane later tonight."},
    "retaliation": {"phonetic": "/rɪˌtæliˈeɪʃn/", "pos": "n.", "meaning": "報復", "phrases": ["in retaliation for"], "synonyms": ["revenge", "vengeance"], "antonyms": ["forgiveness"], "example": "The company lowered its prices in retaliation for its competitor's aggressive marketing."},
    "demonstration": {"phonetic": "/ˌdemənˈstreɪʃn/", "pos": "n.", "meaning": "示範；集會遊行；證明", "phrases": ["product demonstration"], "synonyms": ["display", "protest"], "antonyms": [], "example": "The sales representative gave a live demonstration of the new kitchen appliance."},
    "a massive compound": {"phonetic": "/ə ˈmæsɪv ˈkɑːmpaʊnd/", "pos": "n. phr.", "meaning": "大型院落；大片建築群", "phrases": [], "synonyms": [], "antonyms": [], "example": "The company's headquarters are located in a massive compound on the outskirts of the city."},
    "hijack": {"phonetic": "/ˈhaɪdʒæk/", "pos": "v./n.", "meaning": "劫持；強佔", "phrases": ["hijack a plane"], "synonyms": ["seize"], "antonyms": [], "example": "The terrorists attempted to hijack the plane but were unsuccessful."},
    "militant": {"phonetic": "/ˈmɪlɪtənt/", "pos": "adj./n.", "meaning": "激進的；好戰的", "phrases": ["militant group"], "synonyms": ["aggressive", "radical"], "antonyms": ["peaceful", "moderate"], "example": "The government is negotiating with militant groups to reach a peace agreement."},
    "ally": {"phonetic": "/ˈælaɪ/", "pos": "n./v.", "meaning": "盟友；結盟", "phrases": ["close ally"], "synonyms": ["partner", "supporter"], "antonyms": ["enemy", "rival"], "example": "The two countries have been close allies for more than fifty years."},
    "touch off": {"phonetic": "/tʌtʃ ɔːf/", "pos": "v. phr.", "meaning": "引起；觸發(戰爭/爭論)", "phrases": [], "synonyms": ["spark", "trigger"], "antonyms": [], "example": "The manager's comments touched off a heated debate among the staff."},
    "to date": {"phonetic": "/tuː deɪt/", "pos": "adv. phr.", "meaning": "迄今為止", "phrases": [], "synonyms": ["so far", "until now"], "antonyms": [], "example": "This is our most successful marketing campaign to date, with millions of new customers."},
    "serve as": {"phonetic": "/sɜːrv æz/", "pos": "v. phr.", "meaning": "擔任；充當", "phrases": [], "synonyms": ["act as", "function as"], "antonyms": [], "example": "The old factory will serve as a temporary warehouse until the new one is finished."},
    "on the run": {"phonetic": "/ɑːn ðə rʌn/", "pos": "phr.", "meaning": "在逃；奔波", "phrases": ["criminal on the run"], "synonyms": ["fleeing"], "antonyms": [], "example": "The suspect has been on the run since the robbery took place last week."},
    "illegitimacy": {"phonetic": "/ˌɪlɪˈdʒɪtɪməsi/", "pos": "n.", "meaning": "私生；不合法", "phrases": [], "synonyms": ["invalidity"], "antonyms": ["legitimacy"], "example": "The court ruled on the illegitimacy of the contract due to the lack of a signature."},
    "normal": {"phonetic": "/ˈnɔːrml/", "pos": "adj./n.", "meaning": "正常的；標準", "phrases": ["back to normal"], "synonyms": ["ordinary", "regular"], "antonyms": ["abnormal", "unusual"], "example": "Business returned to normal after the new computer system was fully implemented."},
    "steadily": {"phonetic": "/ˈstedəli/", "pos": "adv.", "meaning": "穩定地；持續地", "phrases": ["increase steadily"], "synonyms": ["consistently", "gradually"], "antonyms": ["erratically"], "example": "The company's profits have increased steadily over the last five years."},
    "threshold": {"phonetic": "/ˈθreʃhoʊld/", "pos": "n.", "meaning": "門檻；開端", "phrases": ["pain threshold", "on the threshold of"], "synonyms": ["doorway", "entrance", "limit"], "antonyms": [], "example": "The company is on the threshold of a new era of growth and innovation."},
    "motherhood without marriage": {"phonetic": "/ˈmʌðərhʊd wɪˈðaʊt ˈmærɪdʒ/", "pos": "n. phr.", "meaning": "未婚生子", "phrases": [], "synonyms": [], "antonyms": [], "example": "Social attitudes toward motherhood without marriage have changed significantly in recent decades."},
    "decade": {"phonetic": "/ˈdekeɪd/", "pos": "n.", "meaning": "十年", "phrases": ["over the last decade"], "synonyms": [], "antonyms": [], "example": "The technology has seen rapid advancement over the last decade."},
    "surge": {"phonetic": "/sɜːrdʒ/", "pos": "n./v.", "meaning": "激增；澎湃", "phrases": ["power surge", "surge in demand"], "synonyms": ["increase", "rise", "swell"], "antonyms": ["decline", "fall"], "example": "There has been a sudden surge in demand for eco-friendly products this summer."},
    "birth outside marriage": {"phonetic": "/bɜːrθ ˌaʊtˈsaɪd ˈmærɪdʒ/", "pos": "n. phr.", "meaning": "婚外生育", "phrases": [], "synonyms": [], "antonyms": [], "example": "Statistics show an increase in the number of births outside marriage in many countries."},
    "transform": {"phonetic": "/trænsˈfɔːrm/", "pos": "v.", "meaning": "轉換；改變", "phrases": ["transform the business"], "synonyms": ["change", "alter", "convert"], "antonyms": ["preserve", "maintain"], "example": "Digital technology has completely transformed the way we do business today."},
    "overwhelmingly": {"phonetic": "/ˌoʊvərˈwelmɪŋli/", "pos": "adv.", "meaning": "壓倒性地；不可抵抗地", "phrases": ["overwhelmingly positive"], "synonyms": ["massively", "extremely"], "antonyms": [], "example": "The proposal was overwhelmingly supported by the members of the board."},
    "consistently": {"phonetic": "/kənˈsɪstəntli/", "pos": "adv.", "meaning": "一貫地；始終如一地", "phrases": ["consistently high quality"], "synonyms": ["steadily", "constantly"], "antonyms": ["inconsistently"], "example": "He has consistently performed well in his role as a sales manager."},
    "elevate": {"phonetic": "/ˈelɪveɪt/", "pos": "v.", "meaning": "提升；舉起", "phrases": ["elevate to a position"], "synonyms": ["raise", "lift", "promote"], "antonyms": ["lower", "demote"], "example": "The company's new marketing campaign helped to elevate its brand image."},
    "diverse": {"phonetic": "/daɪˈvɜːrs/", "pos": "adj.", "meaning": "多樣的；不同的", "phrases": ["diverse workforce"], "synonyms": ["various", "varied"], "antonyms": ["similar", "uniform"], "example": "The company has a diverse workforce with employees from many different backgrounds."},
    "shrink": {"phonetic": "/ʃrɪŋk/", "pos": "v./n.", "meaning": "縮小；收縮", "phrases": ["shrink the budget"], "synonyms": ["contract", "decrease"], "antonyms": ["expand", "grow"], "example": "The market for traditional retail stores has continued to shrink in recent years."},
    "marriageable man": {"phonetic": "/ˈmærɪdʒəbl mæn/", "pos": "n. phr.", "meaning": "適婚男子", "phrases": [], "synonyms": [], "antonyms": [], "example": "The study discussed the challenges faced by marriageable men in the current economy."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_10:
        update_info = enriched_data_gold_10[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 451-500 個單字。")
