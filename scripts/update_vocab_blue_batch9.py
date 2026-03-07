import json
import os

def update_vocab():
    # 第九批 20 個商務進階單字 (藍色等級)
    new_data = [
        {"word": "Prospectus", "phonetic": "/prəˈspektəs/", "pos": "n.", "meaning": "內容說明書, 招股說明書", "level": "blue", "phrases": ["company prospectus", "college prospectus"], "synonyms": ["brochure", "catalog"], "antonyms": [], "example": "Investors should carefully review the company's prospectus before making any investment decisions."},
        {"word": "Provision", "phonetic": "/prəˈvɪʒn/", "pos": "n.", "meaning": "條款, 規定, 準備金, 供應", "level": "blue", "phrases": ["contract provision", "financial provision"], "synonyms": ["stipulation", "clause"], "antonyms": [], "example": "The standard contract contains a provision for early termination under specific conditions."},
        {"word": "Proxy", "phonetic": "/ˈprɑːksi/", "pos": "n.", "meaning": "代理人, 委託書, 代理權", "level": "blue", "phrases": ["vote by proxy", "proxy server"], "synonyms": ["representative", "agent"], "antonyms": [], "example": "Shareholders who cannot attend the meeting in person may cast their votes by proxy."},
        {"word": "Prudent", "phonetic": "/ˈpruːdnt/", "pos": "adj.", "meaning": "謹慎的, 審慎的", "level": "blue", "phrases": ["prudent investment", "prudent decision"], "synonyms": ["cautious", "careful"], "antonyms": ["reckless", "imprudent"], "example": "Given the current market volatility, a prudent approach to expansion is recommended."},
        {"word": "Punctual", "phonetic": "/ˈpʌŋktʃuəl/", "pos": "adj.", "meaning": "準時的", "level": "blue", "phrases": ["punctual delivery", "be punctual"], "synonyms": ["on time", "prompt"], "antonyms": ["late", "tardy"], "example": "The manager expects all team members to be punctual for the Monday morning briefing."},
        {"word": "Purchase", "phonetic": "/ˈpɜːrtʃəs/", "pos": "v./n.", "meaning": "購買", "level": "blue", "phrases": ["purchase order", "bulk purchase"], "synonyms": ["buy", "procure"], "antonyms": ["sell"], "example": "All large equipment purchases must be approved by the regional financial director."},
        {"word": "Quote", "phonetic": "/kwoʊt/", "pos": "v./n.", "meaning": "報價, 引用", "level": "blue", "phrases": ["price quote", "request a quote"], "synonyms": ["estimate", "bid"], "antonyms": [], "example": "We requested a detailed quote from three different suppliers for the renovation project."},
        {"word": "Radical", "phonetic": "/ˈrædɪkl/", "pos": "adj.", "meaning": "激進的, 根本的, 徹底的", "level": "blue", "phrases": ["radical change", "radical reform"], "synonyms": ["extreme", "fundamental"], "antonyms": ["conservative", "moderate"], "example": "The company underwent a radical restructuring to improve its efficiency and competitiveness."},
        {"word": "Radius", "phonetic": "/ˈreɪdiəs/", "pos": "n.", "meaning": "半徑, 範圍", "level": "blue", "phrases": ["within a 10-mile radius", "search radius"], "synonyms": ["range", "scope"], "antonyms": [], "example": "The courier service guarantees same-day delivery within a 5-mile radius of the city center."},
        {"word": "Ramification", "phonetic": "/ˌræmɪfɪˈkeɪʃn/", "pos": "n.", "meaning": "後果, 影響, 衍生物", "level": "blue", "phrases": ["serious ramifications", "legal ramifications"], "synonyms": ["consequence", "implication"], "antonyms": [], "example": "The board is carefully considering the potential legal ramifications of the proposed merger."},
        {"word": "Ratify", "phonetic": "/ˈrætɪfaɪ/", "pos": "v.", "meaning": "批准, 認可", "level": "blue", "phrases": ["ratify a treaty", "ratify an agreement"], "synonyms": ["approve", "sanction"], "antonyms": ["reject", "veto"], "example": "The new trade agreement is expected to be ratified by both governments early next month."},
        {"word": "Ratio", "phonetic": "/ˈreɪʃioʊ/", "pos": "n.", "meaning": "比例, 比率", "level": "blue", "phrases": ["staff-to-student ratio", "debt-to-equity ratio"], "synonyms": ["proportion", "percentage"], "antonyms": [], "example": "The company is working to improve its debt-to-equity ratio to attract more investors."},
        {"word": "Rationalize", "phonetic": "/ˈræʃnəlaɪz/", "pos": "v.", "meaning": "使合理化, 精簡", "level": "blue", "phrases": ["rationalize operations", "rationalize the workforce"], "synonyms": ["streamline", "justify"], "antonyms": [], "example": "The organization plans to rationalize its distribution network to reduce transportation costs."},
        {"word": "Realm", "phonetic": "/relm/", "pos": "n.", "meaning": "領域, 範圍", "level": "blue", "phrases": ["realm of possibility", "digital realm"], "synonyms": ["domain", "field"], "antonyms": [], "example": "Advancements in artificial intelligence have opened up new opportunities in the realm of healthcare."},
        {"word": "Rebate", "phonetic": "/ˈriːbeɪt/", "pos": "n.", "meaning": "回扣, 退款, 折扣", "level": "blue", "phrases": ["tax rebate", "mail-in rebate"], "synonyms": ["refund", "discount"], "antonyms": [], "example": "Customers can apply for a $50 mail-in rebate after purchasing the new washing machine."},
        {"word": "Recession", "phonetic": "/rɪˈseʃn/", "pos": "n.", "meaning": "經濟衰退, 不景氣", "level": "blue", "phrases": ["economic recession", "deep recession"], "synonyms": ["downturn", "slump"], "antonyms": ["boom", "expansion"], "example": "Many small businesses struggled to survive during the global economic recession of 2008."},
        {"word": "Recipient", "phonetic": "/rɪˈsɪpiənt/", "pos": "n.", "meaning": "接受者, 收件人", "level": "blue", "phrases": ["award recipient", "intended recipient"], "synonyms": ["receiver", "beneficiary"], "antonyms": ["sender", "donor"], "example": "Please ensure that the intended recipient is available to sign for the confidential package."},
        {"word": "Reciprocal", "phonetic": "/rɪˈsɪprəkl/", "pos": "adj.", "meaning": "互惠的, 相互的", "level": "blue", "phrases": ["reciprocal agreement", "reciprocal relationship"], "synonyms": ["mutual", "joint"], "antonyms": ["one-sided", "unilateral"], "example": "The two universities signed a reciprocal agreement allowing students to participate in exchange programs."},
        {"word": "Reconcile", "phonetic": "/ˈrekənsaɪl/", "pos": "v.", "meaning": "調和, 使一致, 對帳", "level": "blue", "phrases": ["reconcile accounts", "reconcile differences"], "synonyms": ["resolve", "settle"], "antonyms": ["clash", "disagree"], "example": "The accountant spent all afternoon trying to reconcile the discrepancies in the monthly financial statements."},
        {"word": "Rectify", "phonetic": "/ˈrektɪfaɪ/", "pos": "v.", "meaning": "糾正, 改正", "level": "blue", "phrases": ["rectify the situation", "rectify an error"], "synonyms": ["correct", "remedy"], "antonyms": [], "example": "We are working closely with the supplier to rectify the shipping error as soon as possible."}
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
