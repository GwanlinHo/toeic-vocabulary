import json

# 第 151-200 個高品質單字對應表 (金色等級)
enriched_data_gold_4 = {
    "statutory": {"phonetic": "/ˈstætʃətɔːri/", "pos": "adj.", "meaning": "法定的", "phrases": ["statutory rights"], "synonyms": ["mandatory"], "antonyms": [], "example": "Employers have a statutory obligation to provide a safe working environment."},
    "legal": {"phonetic": "/ˈliːɡl/", "pos": "adj.", "meaning": "法律的；合法的", "phrases": ["legal advice"], "synonyms": ["lawful"], "antonyms": ["illegal"], "example": "You should seek legal advice before signing the contract."},
    "lawful": {"phonetic": "/ˈliːfl/", "pos": "adj.", "meaning": "合法的；正當的", "phrases": ["lawful act"], "synonyms": ["legal", "legitimate"], "antonyms": ["unlawful"], "example": "The company's actions were found to be perfectly lawful by the court."},
    "judiciary": {"phonetic": "/dʒuːˈdɪʃieri/", "pos": "n.", "meaning": "司法部；司法系統", "phrases": ["independent judiciary"], "synonyms": [], "antonyms": [], "example": "The independence of the judiciary is essential for a fair society."},
    "litigation": {"phonetic": "/ˌlɪtɪˈɡeɪʃn/", "pos": "n.", "meaning": "訴訟", "phrases": ["pending litigation"], "synonyms": ["lawsuit"], "antonyms": [], "example": "The company is involved in a long-running litigation over a patent dispute."},
    "lawsuit": {"phonetic": "/ˈlɔːsuːt/", "pos": "n.", "meaning": "法律訴訟", "phrases": ["file a lawsuit"], "synonyms": ["case", "action"], "antonyms": [], "example": "The group filed a lawsuit against the factory for environmental damage."},
    "plaintiff": {"phonetic": "/ˈpleɪntɪf/", "pos": "n.", "meaning": "原告", "phrases": [], "synonyms": ["accuser"], "antonyms": ["defendant"], "example": "The plaintiff is seeking damages for the loss of income."},
    "defendant": {"phonetic": "/ˈdefendənt/", "pos": "n.", "meaning": "被告", "phrases": [], "synonyms": ["the accused"], "antonyms": ["plaintiff"], "example": "The defendant pleaded not guilty to all the charges."},
    "attorney": {"phonetic": "/əˈtɜːrni/", "pos": "n.", "meaning": "律師", "phrases": ["defense attorney"], "synonyms": ["lawyer", "counsel"], "antonyms": [], "example": "He hired a prominent attorney to represent him in the court case."},
    "counsel": {"phonetic": "/ˈkaʊnsl/", "pos": "n./v.", "meaning": "法律顧問；諮詢", "phrases": ["legal counsel"], "synonyms": ["advice", "consultant"], "antonyms": [], "example": "The company's legal counsel advised against the merger."},
    "testimony": {"phonetic": "/ˈtestɪmoʊni/", "pos": "n.", "meaning": "證詞", "phrases": ["expert testimony"], "synonyms": ["evidence", "witness"], "antonyms": [], "example": "Several witnesses were called to give their testimony during the trial."},
    "affidavit": {"phonetic": "/ˌæfəˈdeɪvɪt/", "pos": "n.", "meaning": "宣誓書", "phrases": ["signed affidavit"], "synonyms": [], "antonyms": [], "example": "He had to sign an affidavit stating that all the information was true."},
    "verdict": {"phonetic": "/ˈvɜːrdɪkt/", "pos": "n.", "meaning": "判決；裁決", "phrases": ["reach a verdict"], "synonyms": ["judgment", "decision"], "antonyms": [], "example": "The jury reached a verdict of guilty after several hours of deliberation."},
    "sentence": {"phonetic": "/ˈsentəns/", "pos": "n./v.", "meaning": "判刑", "phrases": ["prison sentence"], "synonyms": ["judgment"], "antonyms": [], "example": "The judge passed a severe sentence on the defendant."},
    "penalty": {"phonetic": "/ˈpenəlti/", "pos": "n.", "meaning": "處罰；罰金", "phrases": ["late penalty"], "synonyms": ["punishment", "fine"], "antonyms": ["reward"], "example": "There is a heavy penalty for late submission of the tax return."},
    "fine": {"phonetic": "/faɪn/", "pos": "n./v.", "meaning": "罰金；處以罰款", "phrases": ["pay a fine"], "synonyms": ["penalty"], "antonyms": [], "example": "The company was ordered to pay a large fine for violating regulations."},
    "damages": {"phonetic": "/ˈdæmɪdʒɪz/", "pos": "n.", "meaning": "賠償金", "phrases": ["seek damages"], "synonyms": ["compensation"], "antonyms": [], "example": "The court awarded damages to the plaintiff for his injuries."},
    "injunction": {"phonetic": "/ɪnˈdʒʌŋkʃn/", "pos": "n.", "meaning": "禁制令", "phrases": ["court injunction"], "synonyms": ["order", "command"], "antonyms": [], "example": "The company was granted an injunction to prevent its rival from using its logo."},
    "arbitration": {"phonetic": "/ˌɑːrbɪˈtreɪʃn/", "pos": "n.", "meaning": "仲裁", "phrases": ["independent arbitration"], "synonyms": ["mediation"], "antonyms": [], "example": "The dispute was settled through independent arbitration."},
    "mediation": {"phonetic": "/ˌmiːdiˈeɪʃn/", "pos": "n.", "meaning": "調解", "phrases": ["dispute mediation"], "synonyms": ["arbitration"], "antonyms": [], "example": "Mediation is often a faster way to resolve conflicts than going to court."},
    "settlement": {"phonetic": "/ˈsetlmənt/", "pos": "n.", "meaning": "和解；協議", "phrases": ["out-of-court settlement"], "synonyms": ["agreement"], "antonyms": [], "example": "The two parties reached a settlement for an undisclosed amount."},
    "agreement": {"phonetic": "/əˈɡriːmənt/", "pos": "n.", "meaning": "協議；合約", "phrases": ["sign an agreement"], "synonyms": ["contract", "deal"], "antonyms": ["disagreement"], "example": "Please read the terms of the agreement carefully before you sign."},
    "contract": {"phonetic": "/ˈkɑːntrækt/", "pos": "n./v.", "meaning": "合約；訂約", "phrases": ["sign a contract"], "synonyms": ["agreement"], "antonyms": [], "example": "The company signed a contract to provide equipment to the hospital."},
    "clause": {"phonetic": "/klɔːz/", "pos": "n.", "meaning": "條款", "phrases": ["termination clause"], "synonyms": ["provision", "article"], "antonyms": [], "example": "The termination clause allows either party to cancel the agreement."},
    "provision": {"phonetic": "/prəˈvɪʒn/", "pos": "n.", "meaning": "條款；準備", "phrases": ["statutory provision"], "synonyms": ["clause", "stipulation"], "antonyms": [], "example": "The law includes a special provision for small businesses."},
    "stipulation": {"phonetic": "/ˌstɪpjuˈleɪʃn/", "pos": "n.", "meaning": "規定；約定", "phrases": ["key stipulation"], "synonyms": ["condition", "requirement"], "antonyms": [], "example": "One of the stipulations of the grant is that the results must be made public."},
    "breach": {"phonetic": "/briːtʃ/", "pos": "n./v.", "meaning": "違約；違反", "phrases": ["breach of contract"], "synonyms": ["violation", "infringement"], "antonyms": ["observance"], "example": "The company was sued for breach of contract after failing to deliver on time."},
    "infringement": {"phonetic": "/ɪnˈfrɪndʒmənt/", "pos": "n.", "meaning": "侵權", "phrases": ["copyright infringement"], "synonyms": ["violation", "breach"], "antonyms": [], "example": "The company was accused of copyright infringement for using the music."},
    "copyright": {"phonetic": "/ˈkɑːpiraɪt/", "pos": "n./v.", "meaning": "著作權", "phrases": ["copyright owner"], "synonyms": [], "antonyms": [], "example": "You need permission from the copyright owner before using the material."},
    "trademark": {"phonetic": "/ˈtreɪdmɑːrk/", "pos": "n./v.", "meaning": "商標", "phrases": ["registered trademark"], "synonyms": ["brand", "logo"], "antonyms": [], "example": "The company's logo is a registered trademark and cannot be used by others."},
    "patent": {"phonetic": "/ˈpætnt/", "pos": "n./v.", "meaning": "專利", "phrases": ["apply for a patent"], "synonyms": ["license"], "antonyms": [], "example": "The inventor was granted a patent for his new technology."},
    "licensing": {"phonetic": "/ˈlaɪsnsɪŋ/", "pos": "n.", "meaning": "授權；許可", "phrases": ["licensing agreement"], "synonyms": ["authorization"], "antonyms": [], "example": "The licensing agreement allows the firm to manufacture our products."},
    "royalty": {"phonetic": "/ˈrɔɪəlti/", "pos": "n.", "meaning": "權利金；版稅", "phrases": ["royalty payment"], "synonyms": [], "antonyms": [], "example": "The author receives a royalty for every copy of the book sold."},
    "liability insurance": {"phonetic": "/ˌlaɪəˈbɪləti ɪnˈʃʊrəns/", "pos": "n. phr.", "meaning": "責任保險", "phrases": [], "synonyms": [], "antonyms": [], "example": "Small businesses carry liability insurance to protect against legal claims."},
    "negligence": {"phonetic": "/ˈneɡlɪdʒəns/", "pos": "n.", "meaning": "疏忽", "phrases": ["gross negligence"], "synonyms": ["carelessness"], "antonyms": ["care", "diligence"], "example": "The company was found guilty of negligence after the accident."},
    "fraud": {"phonetic": "/frɔːd/", "pos": "n.", "meaning": "詐欺", "phrases": ["credit card fraud"], "synonyms": ["deception", "scam"], "antonyms": ["honesty"], "example": "He was arrested and charged with fraud after a lengthy investigation."},
    "corruption": {"phonetic": "/kəˈrʌpʃn/", "pos": "n.", "meaning": "腐敗；貪汙", "phrases": ["political corruption"], "synonyms": ["dishonesty", "bribery"], "antonyms": ["integrity"], "example": "The government is taking steps to eliminate corruption in the public sector."},
    "bribery": {"phonetic": "/ˈbraɪbəri/", "pos": "n.", "meaning": "賄賂", "phrases": ["accept a bribery"], "synonyms": ["corruption"], "antonyms": [], "example": "The official was accused of bribery in exchange for contracts."},
    "embezzlement": {"phonetic": "/ɪmˈbezlmənt/", "pos": "n.", "meaning": "挪用；侵佔", "phrases": [], "synonyms": ["theft", "misappropriation"], "antonyms": [], "example": "The accountant was sentenced to prison for embezzlement of company funds."},
    "money laundering": {"phonetic": "/ˈmʌni ˌlɔːndərɪŋ/", "pos": "n. phr.", "meaning": "洗錢", "phrases": ["anti-money laundering"], "synonyms": [], "antonyms": [], "example": "The bank was fined for failing to follow anti-money laundering regulations."},
    "antitrust": {"phonetic": "/ˌæntiˈtrʌst/", "pos": "adj.", "meaning": "反托拉斯的；反壟斷的", "phrases": ["antitrust laws"], "synonyms": [], "antonyms": [], "example": "The merger is being investigated by antitrust authorities."},
    "taxation": {"phonetic": "/tækˈseɪʃn/", "pos": "n.", "meaning": "稅收；課稅", "phrases": ["corporate taxation"], "synonyms": ["levy", "duty"], "antonyms": [], "example": "The government plans to introduce changes to the system of corporate taxation."},
    "levy": {"phonetic": "/ˈlevi/", "pos": "n./v.", "meaning": "徵收；徵稅", "phrases": ["levy a tax"], "synonyms": ["tax", "collect"], "antonyms": [], "example": "The local government decided to levy a new tax on tourist accommodation."},
    "tariff": {"phonetic": "/ˈtærɪf/", "pos": "n.", "meaning": "關稅", "phrases": ["import tariff"], "synonyms": ["duty", "tax"], "antonyms": [], "example": "The new tariffs on imported goods are expected to increase costs."},
    "quota": {"phonetic": "/ˈkwoʊtə/", "pos": "n.", "meaning": "配額；限額", "phrases": ["export quota"], "synonyms": ["limit", "allowance"], "antonyms": [], "example": "The company has already reached its annual quota for exports."},
    "subsidy": {"phonetic": "/ˈsʌbsədi/", "pos": "n.", "meaning": "補貼；津貼", "phrases": ["government subsidy"], "synonyms": ["grant", "aid"], "antonyms": [], "example": "The government provides a subsidy to farmers during the dry season."},
    "fiscal": {"phonetic": "/ˈfɪskl/", "pos": "adj.", "meaning": "財政的；會計的", "phrases": ["fiscal year"], "synonyms": ["financial"], "antonyms": [], "example": "The company's fiscal year ends on December 31st."},
    "monetary": {"phonetic": "/ˈmɑːnɪteri/", "pos": "adj.", "meaning": "貨幣的；金融的", "phrases": ["monetary policy"], "synonyms": ["financial", "fiscal"], "antonyms": [], "example": "The central bank is planning to raise interest rates as part of its monetary policy."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_4:
        update_info = enriched_data_gold_4[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 151-200 個單字。")
