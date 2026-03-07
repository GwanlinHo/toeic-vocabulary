import json
import os

def update_vocab():
    # 第六批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Intervention", "phonetic": "/ˌɪntərˈvenʃn/", "pos": "n.", "meaning": "干預, 介入", "level": "blue", "phrases": ["government intervention", "timely intervention"], "synonyms": ["interference", "mediation"], "antonyms": [], "example": "The central bank's intervention helped to stabilize the currency exchange rate."},
        {"word": "Inventory", "phonetic": "/ˈɪnvəntɔːri/", "pos": "n.", "meaning": "庫存, 存貨盤點", "level": "blue", "phrases": ["inventory control", "take inventory"], "synonyms": ["stock", "supply"], "antonyms": [], "example": "The store will be closed on Monday so that the staff can take a full inventory of the warehouse."},
        {"word": "Invoice", "phonetic": "/ˈɪnvɔɪs/", "pos": "n./v.", "meaning": "發票, 費用清單", "level": "blue", "phrases": ["outstanding invoice", "issue an invoice"], "synonyms": ["bill", "statement"], "antonyms": [], "example": "Please ensure that the invoice is paid within 30 days of the date of issue."},
        {"word": "Irrespective", "phonetic": "/ˌɪrɪˈspektɪv/", "pos": "adj.", "meaning": "不論...的, 不考慮的", "level": "blue", "phrases": ["irrespective of age", "irrespective of cost"], "synonyms": ["regardless", "nonetheless"], "antonyms": [], "example": "The company provides equal opportunities for all applicants, irrespective of their background."},
        {"word": "Jeopardize", "phonetic": "/ˈdʒepərdaɪz/", "pos": "v.", "meaning": "使受困, 危及", "level": "blue", "phrases": ["jeopardize the project", "jeopardize safety"], "synonyms": ["endanger", "threaten"], "antonyms": ["protect", "safeguard"], "example": "The unexpected budget cuts could seriously jeopardize the future of the research program."},
        {"word": "Jurisdiction", "phonetic": "/ˌdʒʊrɪsˈdɪkʃn/", "pos": "n.", "meaning": "管轄權, 司法權", "level": "blue", "phrases": ["under the jurisdiction of", "legal jurisdiction"], "synonyms": ["authority", "control"], "antonyms": [], "example": "The matter falls under the jurisdiction of the local consumer protection agency."},
        {"word": "Justification", "phonetic": "/ˌdʒʌstɪfɪˈkeɪʃn/", "pos": "n.", "meaning": "正當理由, 辯護", "level": "blue", "phrases": ["economic justification", "no justification for"], "synonyms": ["rationale", "explanation"], "antonyms": [], "example": "The manager provided a detailed justification for the requested increase in staffing levels."},
        {"word": "Layout", "phonetic": "/ˈleɪaʊt/", "pos": "n.", "meaning": "佈局, 設計", "level": "blue", "phrases": ["office layout", "page layout"], "synonyms": ["arrangement", "design"], "antonyms": [], "example": "The new office layout is designed to encourage more collaboration among different teams."},
        {"word": "Lease", "phonetic": "/liːs/", "pos": "n./v.", "meaning": "租約, 租賃", "level": "blue", "phrases": ["lease agreement", "sign a lease"], "synonyms": ["rent", "hire"], "antonyms": [], "example": "The company decided to lease a larger office space in the city center to accommodate its growing team."},
        {"word": "Ledger", "phonetic": "/ˈledʒər/", "pos": "n.", "meaning": "分類帳, 帳簿", "level": "blue", "phrases": ["general ledger", "accounting ledger"], "synonyms": ["record book"], "antonyms": [], "example": "All financial transactions must be recorded accurately in the company's general ledger."},
        {"word": "Legacy", "phonetic": "/ˈleɡəsi/", "pos": "n.", "meaning": "遺留, 遺產", "level": "blue", "phrases": ["legacy system", "lasting legacy"], "synonyms": ["heritage", "inheritance"], "antonyms": [], "example": "The IT department is working to replace the outdated legacy system with a modern cloud-based platform."},
        {"word": "Legislation", "phonetic": "/ˌledʒɪsˈleɪʃn/", "pos": "n.", "meaning": "法律, 立法", "level": "blue", "phrases": ["labor legislation", "introduce legislation"], "synonyms": ["law", "statute"], "antonyms": [], "example": "The government is considering new legislation to protect the rights of remote workers."},
        {"word": "Legitimate", "phonetic": "/lɪˈdʒɪtɪmət/", "pos": "adj.", "meaning": "合法的, 正當的", "level": "blue", "phrases": ["legitimate business", "legitimate concern"], "synonyms": ["lawful", "valid"], "antonyms": ["illegal", "invalid"], "example": "The company has a legitimate interest in protecting its intellectual property from competitors."},
        {"word": "Leverage", "phonetic": "/ˈlevərɪdʒ/", "pos": "v./n.", "meaning": "利用, 槓桿作用", "level": "blue", "phrases": ["leverage technology", "financial leverage"], "synonyms": ["utilize", "exploit"], "antonyms": [], "example": "We plan to leverage our strong brand reputation to expand into new international markets."},
        {"word": "Liability", "phonetic": "/ˌlaɪəˈbɪləti/", "pos": "n.", "meaning": "法律責任, 債務, 累贅", "level": "blue", "phrases": ["limited liability", "total liabilities"], "synonyms": ["responsibility", "debt"], "antonyms": ["asset"], "example": "The company carries public liability insurance to protect itself against potential lawsuits from customers."},
        {"word": "Liaison", "phonetic": "/liˈeɪzɑːn/", "pos": "n.", "meaning": "聯絡, 聯絡人", "level": "blue", "phrases": ["liaison officer", "maintain liaison with"], "synonyms": ["connection", "contact"], "antonyms": [], "example": "She acts as a liaison between the marketing department and the external advertising agency."},
        {"word": "Liquidate", "phonetic": "/ˈlɪkwɪdeɪt/", "pos": "v.", "meaning": "清算, 償付, 變現", "level": "blue", "phrases": ["liquidate assets", "go into liquidation"], "synonyms": ["settle", "clear"], "antonyms": [], "example": "The court ordered the company to liquidate its assets to pay back its outstanding creditors."},
        {"word": "Litigation", "phonetic": "/ˌlɪtɪˈɡeɪʃn/", "pos": "n.", "meaning": "訴訟", "level": "blue", "phrases": ["pending litigation", "threat of litigation"], "synonyms": ["lawsuit", "legal action"], "antonyms": [], "example": "The company is currently involved in a complex litigation process regarding a patent infringement claim."},
        {"word": "Lucrative", "phonetic": "/ˈluːkrətɪv/", "pos": "adj.", "meaning": "獲利豐厚的, 有利的", "level": "blue", "phrases": ["lucrative contract", "lucrative market"], "synonyms": ["profitable", "rewarding"], "antonyms": ["unprofitable"], "example": "The new trade agreement has opened up many lucrative opportunities for local exporters."},
        {"word": "Mandatory", "phonetic": "/ˈmændətɔːri/", "pos": "adj.", "meaning": "強制性的, 義務的", "level": "blue", "phrases": ["mandatory training", "mandatory requirement"], "synonyms": ["obligatory", "compulsory"], "antonyms": ["optional", "voluntary"], "example": "It is mandatory for all new employees to attend a two-day orientation program."}
    ]
    
    file_path = "data_blue.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                current_data = json.load(f)
            except:
                current_data = []
    else:
        current_data = []

    # 避免重複 (根據 word)
    existing_words = {item['word'].lower() for item in current_data}
    added_count = 0
    for item in new_data:
        if item['word'].lower() not in existing_words:
            current_data.append(item)
            added_count += 1
            
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(current_data, f, ensure_ascii=False, indent=2)
        
    print(f"成功合併！新增了 {added_count} 個單字到 {file_path}，目前總計 {len(current_data)} 個單字。")

if __name__ == "__main__":
    update_vocab()
