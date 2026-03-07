import json
import os

def update_vocab():
    # 首批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Abbreviate", "phonetic": "/əˈbriːvieɪt/", "pos": "v.", "meaning": "縮寫, 縮短", "level": "blue", "phrases": ["abbreviated form", "standard abbreviation"], "synonyms": ["shorten", "curtail"], "antonyms": ["elongate", "expand"], "example": "The committee decided to abbreviate the final report for the board meeting."},
        {"word": "Abstain", "phonetic": "/əbˈsteɪn/", "pos": "v.", "meaning": "戒除, 放棄, 投棄權票", "level": "blue", "phrases": ["abstain from voting", "total abstinence"], "synonyms": ["refrain", "desist"], "antonyms": ["indulge", "participate"], "example": "Three members of the board decided to abstain from voting on the controversial proposal."},
        {"word": "Accomplice", "phonetic": "/əˈkʌmplɪs/", "pos": "n.", "meaning": "同謀, 幫兇", "level": "blue", "phrases": ["witting accomplice", "alleged accomplice"], "synonyms": ["associate", "collaborator"], "antonyms": ["opponent", "adversary"], "example": "The investigation revealed that the hacker had an accomplice within the IT department."},
        {"word": "Acquaint", "phonetic": "/əˈkweɪnt/", "pos": "v.", "meaning": "使認識, 使了解", "level": "blue", "phrases": ["acquaint oneself with", "get acquainted"], "synonyms": ["familiarize", "inform"], "antonyms": ["ignore", "unfamiliar"], "example": "New employees are required to acquaint themselves with the company's safety protocols."},
        {"word": "Adjourn", "phonetic": "/əˈdʒɜːrn/", "pos": "v.", "meaning": "休會, 延期", "level": "blue", "phrases": ["adjourn the meeting", "motion to adjourn"], "synonyms": ["suspend", "postpone"], "antonyms": ["convene", "commence"], "example": "The chairperson decided to adjourn the session until 9:00 AM the following morning."},
        {"word": "Affidavit", "phonetic": "/ˌæfəˈdeɪvɪt/", "pos": "n.", "meaning": "宣誓書", "level": "blue", "phrases": ["sign an affidavit", "sworn affidavit"], "synonyms": ["testimony", "sworn statement"], "antonyms": [], "example": "The witness provided a sworn affidavit to the court regarding the contract dispute."},
        {"word": "Aggregate", "ranking": "blue", "phonetic": "/ˈæɡrɪɡət/", "pos": "adj./n.", "meaning": "總計的, 集合體", "level": "blue", "phrases": ["aggregate demand", "in the aggregate"], "synonyms": ["total", "accumulated"], "antonyms": ["individual", "separate"], "example": "The aggregate annual revenue exceeded the initial projections by 15%."},
        {"word": "Alleviate", "phonetic": "/əˈliːvieɪt/", "pos": "v.", "meaning": "減輕, 緩和", "level": "blue", "phrases": ["alleviate poverty", "alleviate the symptoms"], "synonyms": ["relieve", "mitigate"], "antonyms": ["aggravate", "intensify"], "example": "The government introduced new tax breaks to alleviate the burden on small businesses."},
        {"word": "Amicable", "phonetic": "/ˈæmɪkəbl/", "pos": "adj.", "meaning": "友好的, 和睦的", "level": "blue", "phrases": ["amicable settlement", "amicable relationship"], "synonyms": ["friendly", "harmonious"], "antonyms": ["hostile", "antagonistic"], "example": "The two companies reached an amicable settlement after months of legal disputes."},
        {"word": "Appraisal", "phonetic": "/əˈpreɪzl/", "pos": "n.", "meaning": "評價, 估價, 考核", "level": "blue", "phrases": ["performance appraisal", "property appraisal"], "synonyms": ["assessment", "evaluation"], "antonyms": [], "example": "The annual performance appraisal is a key component of our professional development program."},
        {"word": "Arrear", "phonetic": "/əˈrɪər/", "pos": "n.", "meaning": "欠款, 拖欠", "level": "blue", "phrases": ["in arrears", "rent arrears"], "synonyms": ["debt", "deficit"], "antonyms": [], "example": "The tenant was three months in arrears with his rent payments."},
        {"word": "Asset", "phonetic": "/ˈæset/", "pos": "n.", "meaning": "資產, 優點", "level": "blue", "phrases": ["valuable asset", "fixed assets"], "synonyms": ["property", "resource"], "antonyms": ["liability"], "example": "The new marketing director has proven to be a valuable asset to the organization."},
        {"word": "Attrition", "phonetic": "/əˈtrɪʃn/", "pos": "n.", "meaning": "磨損, (人員)自然縮減", "level": "blue", "phrases": ["staff attrition", "attrition rate"], "synonyms": ["erosion", "reduction"], "antonyms": ["growth", "expansion"], "example": "The company decided not to fill the vacancies caused by natural staff attrition."},
        {"word": "Audit", "phonetic": "/ˈɔːdɪt/", "pos": "v./n.", "meaning": "審計, 查帳", "level": "blue", "phrases": ["internal audit", "financial audit"], "synonyms": ["inspection", "scrutiny"], "antonyms": [], "example": "The independent firm will conduct a thorough audit of the company's financial records."},
        {"word": "Authorize", "phonetic": "/ˈɔːθəraɪz/", "pos": "v.", "meaning": "授權, 批准", "level": "blue", "phrases": ["authorized dealer", "authorize a payment"], "synonyms": ["approve", "sanction"], "antonyms": ["forbid", "veto"], "example": "Only the department head is allowed to authorize international travel expenses."},
        {"word": "Ballot", "phonetic": "/ˈbælət/", "pos": "n./v.", "meaning": "投票, 選票", "level": "blue", "phrases": ["secret ballot", "cast a ballot"], "synonyms": ["vote", "poll"], "antonyms": [], "example": "The union members will cast their ballots to decide on the new wage agreement."},
        {"word": "Benchmark", "phonetic": "/ˈbentʃmɑːrk/", "pos": "n.", "meaning": "基準, 標竿", "level": "blue", "phrases": ["industry benchmark", "benchmark test"], "synonyms": ["standard", "criterion"], "antonyms": [], "example": "The current performance levels will serve as a benchmark for future evaluations."},
        {"word": "Beneficiary", "phonetic": "/ˌbenɪˈfɪʃieri/", "pos": "n.", "meaning": "受益人", "level": "blue", "phrases": ["sole beneficiary", "insurance beneficiary"], "synonyms": ["recipient", "heir"], "antonyms": ["donor", "benefactor"], "example": "The non-profit organization was named as the primary beneficiary of the estate."},
        {"word": "Bid", "phonetic": "/bɪd/", "pos": "v./n.", "meaning": "出價, 投標", "level": "blue", "phrases": ["takeover bid", "sealed bid"], "synonyms": ["tender", "offer"], "antonyms": [], "example": "The construction company submitted a competitive bid for the new highway project."},
        {"word": "Blueprint", "phonetic": "/ˈbluːprɪnt/", "pos": "n.", "meaning": "藍圖, 計畫", "level": "blue", "phrases": ["detailed blueprint", "blueprint for success"], "synonyms": ["plan", "design"], "antonyms": [], "example": "The CEO presented a comprehensive blueprint for the company's expansion into Asian markets."}
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
