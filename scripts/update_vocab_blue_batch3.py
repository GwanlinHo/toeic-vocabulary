import json

# 第 101-150 個高品質單字對應表 (藍色等級)
enriched_data_blue_3 = {
    "curious": {"phonetic": "/ˈkjʊriəs/", "pos": "adj.", "meaning": "好奇的；奇特的", "phrases": ["curious about"], "synonyms": ["inquisitive"], "antonyms": ["indifferent"], "example": "The child was curious about how the toy car worked and tried to take it apart."},
    "curt": {"phonetic": "/kɜːrt/", "pos": "adj.", "meaning": "簡短而失禮的", "phrases": ["curt reply"], "synonyms": ["abrupt", "blunt"], "antonyms": ["polite", "courteous"], "example": "The manager's curt reply suggested that he was too busy to discuss the matter further."},
    "diligent": {"phonetic": "/ˈdɪlɪdʒənt/", "pos": "adj.", "meaning": "勤勉的；孜孜不倦的", "phrases": ["diligent worker"], "synonyms": ["hardworking", "industrious"], "antonyms": ["lazy", "negligent"], "example": "She is a diligent student who spends hours in the library every day."},
    "distinctive": {"phonetic": "/dɪˈstɪŋktɪv/", "pos": "adj.", "meaning": "獨特的；有特色的", "phrases": ["distinctive feature"], "synonyms": ["unique", "characteristic"], "antonyms": ["common", "ordinary"], "example": "The brand's distinctive logo makes its products easily recognizable."},
    "domestic affairs": {"phonetic": "/dəˈmestɪk əˈferz/", "pos": "n. phr.", "meaning": "國內事務；家務", "phrases": [], "synonyms": ["internal affairs"], "antonyms": ["foreign affairs"], "example": "The minister is responsible for managing the country's domestic affairs."},
    "drastic": {"phonetic": "/ˈdræstɪk/", "pos": "adj.", "meaning": "激烈的；嚴厲的", "phrases": ["drastic measures"], "synonyms": ["extreme", "severe"], "antonyms": ["mild", "slight"], "example": "The company had to take drastic measures to reduce costs and avoid bankruptcy."},
    "drastically": {"phonetic": "/ˈdræstɪkli/", "pos": "adv.", "meaning": "徹底地；激烈地", "phrases": ["drastically reduce"], "synonyms": ["severely", "extremely"], "antonyms": ["slightly"], "example": "The price of the product has been drastically reduced to attract more customers."},
    "dynamic": {"phonetic": "/daɪˈnæmɪk/", "pos": "adj.", "meaning": "動態的；充滿活力的", "phrases": ["dynamic market"], "synonyms": ["energetic", "vibrant"], "antonyms": ["static", "lethargic"], "example": "We are looking for a dynamic individual to lead our marketing team."},
    "earnest": {"phonetic": "/ˈɜːrnɪst/", "pos": "adj.", "meaning": "認真的；誠摯的", "phrases": ["in earnest"], "synonyms": ["serious", "sincere"], "antonyms": ["insincere", "frivolous"], "example": "He made an earnest attempt to resolve the conflict between the two departments."},
    "elect": {"phonetic": "/ɪˈlekt/", "pos": "v./adj.", "meaning": "選舉；當選的", "phrases": ["president-elect"], "synonyms": ["choose", "vote in"], "antonyms": [], "example": "The board of directors will meet next week to elect a new chairperson."},
    "elemental": {"phonetic": "/ˌelɪˈmentl/", "pos": "adj.", "meaning": "基本的；自然的", "phrases": ["elemental forces"], "synonyms": ["basic", "fundamental"], "antonyms": [], "example": "Understanding the elemental principles of economics is essential for business students."},
    "eligible": {"phonetic": "/ˈelɪdʒəbl/", "pos": "adj.", "meaning": "合格的；有資格的", "phrases": ["be eligible for"], "synonyms": ["qualified", "entitled"], "antonyms": ["ineligible"], "example": "Only employees with more than three years of service are eligible for the bonus."},
    "entitled": {"phonetic": "/ɪnˈtaɪtld/", "pos": "adj.", "meaning": "有權利的；有資格的", "phrases": ["be entitled to"], "synonyms": ["privileged", "eligible"], "antonyms": [], "example": "You are entitled to a full refund if the product is found to be defective."},
    "evasive": {"phonetic": "/ɪˈveɪsɪv/", "pos": "adj.", "meaning": "逃避的；含糊其辭的", "phrases": ["evasive answer"], "synonyms": ["ambiguous", "vague"], "antonyms": ["direct", "frank"], "example": "The manager's evasive answers during the meeting only served to increase our suspicion."},
    "extensive": {"phonetic": "/ɪkˈstensɪv/", "pos": "adj.", "meaning": "廣泛的；大規模的", "phrases": ["extensive research"], "synonyms": ["wide", "broad"], "antonyms": ["limited", "narrow"], "example": "The company carried out extensive market research before launching the new product."},
    "extraordinary": {"phonetic": "/ɪkˈstrɔːrdəneri/", "pos": "adj.", "meaning": "非凡的；特別的", "phrases": ["extraordinary talent"], "synonyms": ["exceptional", "remarkable"], "antonyms": ["ordinary", "average"], "example": "His extraordinary talent for music was recognized at a very young age."},
    "feasible": {"phonetic": "/ˈfiːzəbl/", "pos": "adj.", "meaning": "可行的；可能的", "phrases": ["financially feasible"], "synonyms": ["practicable", "viable"], "antonyms": ["impossible", "impractical"], "example": "We need to determine if the new project is financially feasible before we proceed."},
    "fall off": {"phonetic": "/fɔːl ɔːf/", "pos": "v. phr.", "meaning": "跌落；減少", "phrases": [], "synonyms": ["decrease", "decline"], "antonyms": ["increase"], "example": "Sales typically fall off during the winter months after the holiday season."},
    "fellow": {"phonetic": "/ˈfeloʊ/", "pos": "n./adj.", "meaning": "同伴；同類的", "phrases": ["fellow worker", "fellow citizen"], "synonyms": ["companion", "peer"], "antonyms": [], "example": "He is well-respected by his fellow researchers for his innovative work."},
    "firm": {"phonetic": "/fɜːrm/", "pos": "n./adj.", "meaning": "公司；穩固的", "phrases": ["law firm", "firm belief"], "synonyms": ["company", "stable"], "antonyms": ["weak", "unstable"], "example": "The law firm specializes in providing legal advice to international corporations."},
    "fleet": {"phonetic": "/fliːt/", "pos": "n./adj.", "meaning": "船隊；敏捷的", "phrases": ["vehicle fleet"], "synonyms": ["swift", "rapid"], "antonyms": ["slow"], "example": "The company operates a large fleet of delivery trucks across the country."},
    "foremost": {"phonetic": "/ˈfɔːrmoʊst/", "pos": "adj.", "meaning": "最重要的；首要的", "phrases": ["first and foremost"], "synonyms": ["leading", "primary"], "antonyms": [], "example": "He is widely recognized as one of the foremost experts in the field of medicine."},
    "formatted": {"phonetic": "/ˈfɔːrmætɪd/", "pos": "adj.", "meaning": "格式化好的", "phrases": ["properly formatted"], "synonyms": ["arranged"], "antonyms": [], "example": "Please ensure that the report is properly formatted before you submit it."},
    "forward": {"phonetic": "/ˈfɔːrwərd/", "pos": "adv./adj.", "meaning": "向前地；未來的", "phrases": ["look forward to"], "synonyms": ["ahead"], "antonyms": ["backward"], "example": "We look forward to receiving your application and meeting you for an interview."},
    "foster": {"phonetic": "/ˈfɔːstər/", "pos": "v./adj.", "meaning": "促進；領養的", "phrases": ["foster care"], "synonyms": ["promote", "encourage"], "antonyms": ["hinder", "discourage"], "example": "The workshop was designed to foster better communication between team members."},
    "fraught": {"phonetic": "/frɔːt/", "pos": "adj.", "meaning": "充滿(困難/危險)的", "phrases": ["fraught with"], "synonyms": ["filled"], "antonyms": [], "example": "The situation in the region remains fraught with tension and uncertainty."},
    "frisky": {"phonetic": "/ˈfrɪski/", "pos": "adj.", "meaning": "活潑的；愛鬧的", "phrases": [], "synonyms": ["playful", "lively"], "antonyms": ["lethargic"], "example": "The young kittens were very frisky and spent all afternoon playing together."},
    "fundamental": {"phonetic": "/ˌfʌndəˈmentl/", "pos": "adj.", "meaning": "基礎的；根本的", "phrases": ["fundamental principles"], "synonyms": ["basic", "essential"], "antonyms": ["secondary"], "example": "A fundamental understanding of mathematics is essential for this engineering course."},
    "funneled": {"phonetic": "/ˈfʌnld/", "pos": "adj.", "meaning": "匯集的；過濾的", "phrases": [], "synonyms": ["directed"], "antonyms": [], "example": "The government funds were funneled into the new education program."},
    "get through with": {"phonetic": "/ɡet θruː wɪð/", "pos": "v. phr.", "meaning": "完成；結束", "phrases": [], "synonyms": ["finish", "complete"], "antonyms": ["start", "begin"], "example": "I hope to get through with this report by the end of the day."},
    "gloosy": {"word": "glossy", "phonetic": "/ˈɡlɔːsi/", "pos": "adj.", "meaning": "光滑的；有光澤的", "phrases": ["glossy brochure"], "synonyms": ["shiny", "slick"], "antonyms": ["matte", "dull"], "example": "The company produced a glossy brochure to showcase its latest luxury products."},
    "go after": {"phonetic": "/ɡoʊ ˈæftər/", "pos": "v. phr.", "meaning": "追求；追趕", "phrases": [], "synonyms": ["pursue", "chase"], "antonyms": [], "example": "The company is planning to go after a larger share of the international market."},
    "go alone with": {"word": "go along with", "phonetic": "/ɡoʊ əˈlɔːŋ wɪð/", "pos": "v. phr.", "meaning": "贊同；伴隨", "phrases": [], "synonyms": ["agree", "comply"], "antonyms": ["oppose"], "example": "I'm happy to go along with your suggestion regarding the new marketing plan."},
    "guilty": {"phonetic": "/ˈɡɪlti/", "pos": "adj.", "meaning": "有罪的；內疚的", "phrases": ["feel guilty"], "synonyms": ["culpable"], "antonyms": ["innocent"], "example": "The jury found the defendant guilty of all charges at the end of the trial."},
    "hazardous": {"phonetic": "/ˈhæzərdəs/", "pos": "adj.", "meaning": "危險的；有害的", "phrases": ["hazardous waste"], "synonyms": ["dangerous", "risky"], "antonyms": ["safe"], "example": "All hazardous waste must be disposed of according to strict safety regulations."},
    "horrible": {"phonetic": "/ˈhɔːrəbl/", "pos": "adj.", "meaning": "可怕的；極糟的", "phrases": [], "synonyms": ["terrible", "awful"], "antonyms": ["wonderful"], "example": "The weather during our vacation was absolutely horrible with constant rain."},
    "imperative": {"phonetic": "/ɪmˈperətɪv/", "pos": "adj./n.", "meaning": "必須的；命令", "phrases": ["it is imperative that"], "synonyms": ["essential", "crucial"], "antonyms": ["optional"], "example": "It is imperative that we complete the project before the deadline."},
    "inalienable": {"phonetic": "/ɪnˈeɪliənəbl/", "pos": "adj.", "meaning": "不可剝奪的", "phrases": ["inalienable rights"], "synonyms": ["absolute"], "antonyms": [], "example": "Freedom of speech is considered an inalienable right in many democratic countries."},
    "inanimate": {"phonetic": "/ɪnˈænɪmət/", "pos": "adj.", "meaning": "無生命的；單調的", "phrases": ["inanimate object"], "synonyms": ["lifeless"], "antonyms": ["animate", "living"], "example": "The room was filled with inanimate objects that had no sentimental value to him."},
    "incumbent": {"phonetic": "/ɪnˈkʌmbənt/", "pos": "adj./n.", "meaning": "現任的；義務上的", "phrases": ["incumbent president"], "synonyms": ["current", "obligatory"], "antonyms": [], "example": "It is incumbent upon all employees to follow the company's safety regulations."},
    "infant": {"phonetic": "/ˈinfənt/", "pos": "n./adj.", "meaning": "嬰兒；初期的", "phrases": ["infant mortality"], "synonyms": ["baby", "early"], "antonyms": ["adult"], "example": "The new company is still in its infant stage and has many challenges to overcome."},
    "preterm infant": {"phonetic": "/ˈpriːtɜːrm ˈinfənt/", "pos": "n. phr.", "meaning": "早產兒", "phrases": [], "synonyms": ["premature baby"], "antonyms": [], "example": "The hospital has a special unit for providing intensive care to preterm infants."},
    "infant school": {"phonetic": "/ˈinfənt skuːl/", "pos": "n. phr.", "meaning": "幼稚園/幼兒學校", "phrases": [], "synonyms": ["nursery school", "kindergarten"], "antonyms": [], "example": "My daughter will be starting infant school in the city center next September."},
    "innocent": {"phonetic": "/ˈɪnəsnt/", "pos": "adj.", "meaning": "純真的；無罪的", "phrases": ["innocent of"], "synonyms": ["naive", "blameless"], "antonyms": ["guilty", "corrupt"], "example": "He was found to be innocent of the crime after new evidence came to light."},
    "instant": {"phonetic": "/ˈɪnstənt/", "pos": "adj./n.", "meaning": "立即的；瞬間", "phrases": ["instant coffee", "in an instant"], "synonyms": ["immediate"], "antonyms": ["delayed"], "example": "The new product was an instant success and sold out within just a few hours."},
    "instantaneously": {"phonetic": "/ˌɪnstənˈteɪniəsli/", "pos": "adv.", "meaning": "即刻地；瞬間地", "phrases": [], "synonyms": ["immediately", "instantly"], "antonyms": [], "example": "The message was delivered instantaneously to all employees via the internal network."},
    "itemize": {"phonetic": "/ˈaɪtəmaɪz/", "pos": "v.", "meaning": "詳細列舉", "phrases": ["itemized bill"], "synonyms": ["list", "detail"], "antonyms": [], "example": "Could you please itemize the expenses so that we can process your claim?"},
    "jeopardize": {"phonetic": "/ˈjepərdaɪz/", "pos": "v.", "meaning": "危及；損害", "phrases": [], "synonyms": ["endanger", "threaten"], "antonyms": ["protect", "secure"], "example": "The sudden drop in sales could jeopardize the company's future expansion plans."},
    "leverage": {"phonetic": "/ˈlevərɪdʒ/", "pos": "n./v.", "meaning": "利用；槓桿", "phrases": ["financial leverage"], "synonyms": ["influence", "exploit"], "antonyms": [], "example": "The company plans to leverage its strong brand name to enter the new market."},
    "litter": {"phonetic": "/ˈlɪtər/", "pos": "n./v.", "meaning": "垃圾；亂丟", "phrases": ["litter bin"], "synonyms": ["rubbish", "clutter"], "antonyms": ["cleanliness"], "example": "Please do not litter in the park and use the designated waste bins instead."}
}

with open('data_blue.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_blue_3:
        update_info = enriched_data_blue_3[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_blue.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修藍色等級第 101-150 個單字，並修正拼寫錯誤。")
