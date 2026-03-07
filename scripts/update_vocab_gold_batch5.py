import json

# 第 201-250 個高品質單字對應表 (金色等級)
enriched_data_gold_5 = {
    "revenue": {"phonetic": "/ˈrevənjuː/", "pos": "n.", "meaning": "營收；稅收", "phrases": ["generate revenue"], "synonyms": ["income", "earnings"], "antonyms": ["expenditure"], "example": "The company's annual revenue increased by fifteen percent last year."},
    "expenditure": {"phonetic": "/ɪkˈspendɪtʃər/", "pos": "n.", "meaning": "支出；開支", "phrases": ["capital expenditure"], "synonyms": ["spending", "outlay"], "antonyms": ["revenue"], "example": "We need to reduce our monthly expenditure on office supplies."},
    "budget": {"phonetic": "/ˈbʌdʒɪt/", "pos": "n./v.", "meaning": "預算", "phrases": ["within budget", "over budget"], "synonyms": ["allocation"], "antonyms": [], "example": "The project must be completed within the original budget."},
    "surplus": {"phonetic": "/ˈsɜːrpləs/", "pos": "n./adj.", "meaning": "盈餘；過剩", "phrases": ["budget surplus"], "synonyms": ["excess", "extra"], "antonyms": ["deficit"], "example": "The company reported a significant surplus at the end of the fiscal year."},
    "deficit": {"phonetic": "/ˈdefɪsɪt/", "pos": "n.", "meaning": "赤字；虧損", "phrases": ["trade deficit"], "synonyms": ["shortfall", "loss"], "antonyms": ["surplus"], "example": "The government is taking steps to reduce the national budget deficit."},
    "asset": {"phonetic": "/ˈæset/", "pos": "n.", "meaning": "資產", "phrases": ["fixed assets", "valuable asset"], "synonyms": ["property", "resource"], "antonyms": ["liability"], "example": "The company's total assets are valued at over ten million dollars."},
    "liability": {"phonetic": "/ˌlaɪəˈbɪləti/", "pos": "n.", "meaning": "負債；責任", "phrases": ["total liabilities"], "synonyms": ["debt", "obligation"], "antonyms": ["asset"], "example": "The business has many liabilities that need to be paid off soon."},
    "ledger": {"phonetic": "/ˈledʒər/", "pos": "n.", "meaning": "分類帳；總帳", "phrases": ["general ledger"], "synonyms": ["account book"], "antonyms": [], "example": "The accountant recorded all the transactions in the company's ledger."},
    "balance sheet": {"phonetic": "/ˈbæləns ʃiːt/", "pos": "n. phr.", "meaning": "資產負債表", "phrases": [], "synonyms": ["financial statement"], "antonyms": [], "example": "The balance sheet shows the company's financial position at a specific point in time."},
    "audit": {"phonetic": "/ˈɔːdɪt/", "pos": "n./v.", "meaning": "審計；查帳", "phrases": ["internal audit"], "synonyms": ["inspection", "examination"], "antonyms": [], "example": "An independent firm was hired to audit the company's financial records."},
    "auditor": {"phonetic": "/ˈɔːdɪtər/", "pos": "n.", "meaning": "審計師", "phrases": ["external auditor"], "synonyms": ["inspector"], "antonyms": [], "example": "The auditor identified several errors in the annual tax return."},
    "accountant": {"phonetic": "/əˈkaʊntənt/", "pos": "n.", "meaning": "會計師", "phrases": ["certified public accountant"], "synonyms": ["bookkeeper"], "antonyms": [], "example": "Our company accountant is responsible for managing all financial transactions."},
    "bookkeeping": {"phonetic": "/ˈbʊkˌkiːpɪŋ/", "pos": "n.", "meaning": "簿記", "phrases": [], "synonyms": ["accounting"], "antonyms": [], "example": "Good bookkeeping is essential for any successful small business."},
    "depreciation": {"phonetic": "/dɪˌpriːʃiˈeɪʃn/", "pos": "n.", "meaning": "折舊；貶值", "phrases": ["asset depreciation"], "synonyms": ["devaluation"], "antonyms": ["appreciation"], "example": "The value of the machinery has decreased due to annual depreciation."},
    "appreciation": {"phonetic": "/əˌpriːʃiˈeɪʃn/", "pos": "n.", "meaning": "增值；感謝", "phrases": ["capital appreciation"], "synonyms": ["increase", "gratitude"], "antonyms": ["depreciation"], "example": "The value of the property has seen significant appreciation over the last five years."},
    "amortization": {"phonetic": "/ˌæmərtɪˈzeɪʃn/", "pos": "n.", "meaning": "攤銷；分期償還", "phrases": [], "synonyms": [], "antonyms": [], "example": "The loan will be repaid through a process of monthly amortization."},
    "liquidity": {"phonetic": "/lɪˈkwɪdəti/", "pos": "n.", "meaning": "流動性(資金)", "phrases": ["cash liquidity"], "synonyms": ["availability"], "antonyms": [], "example": "The company needs to maintain enough liquidity to meet its short-term obligations."},
    "solvency": {"phonetic": "/sɔːlˈvənsi/", "pos": "n.", "meaning": "償付能力", "phrases": ["financial solvency"], "synonyms": [], "antonyms": ["insolvency"], "example": "The bank is investigating the company's solvency before approving the loan."},
    "insolvency": {"phonetic": "/ɪnˈsɑːlvənsi/", "pos": "n.", "meaning": "無力償還；破產", "phrases": ["corporate insolvency"], "synonyms": ["bankruptcy"], "antonyms": ["solvency"], "example": "The firm was forced into insolvency due to its massive debts."},
    "bankruptcy": {"phonetic": "/ˈbæŋkrʌptsi/", "pos": "n.", "meaning": "破產", "phrases": ["file for bankruptcy"], "synonyms": ["insolvency", "failure"], "antonyms": ["solvency"], "example": "Several small businesses declared bankruptcy during the economic crisis."},
    "collateral": {"phonetic": "/kəˈlætərəl/", "pos": "n./adj.", "meaning": "抵押品；附加的", "phrases": ["loan collateral"], "synonyms": ["security", "guarantee"], "antonyms": [], "example": "He used his house as collateral to secure a business loan."},
    "mortgage": {"phonetic": "/ˈmɔːrɡɪdʒ/", "pos": "n./v.", "meaning": "抵押貸款(房屋)", "phrases": ["pay off a mortgage"], "synonyms": ["loan"], "antonyms": [], "example": "They took out a thirty-year mortgage to buy their first home."},
    "interest rate": {"phonetic": "/ˈɪntrəst reɪt/", "pos": "n. phr.", "meaning": "利率", "phrases": ["fixed interest rate"], "synonyms": [], "antonyms": [], "example": "The central bank decided to lower interest rates to encourage borrowing."},
    "prime rate": {"phonetic": "/praɪm reɪt/", "pos": "n. phr.", "meaning": "優惠利率", "phrases": [], "synonyms": ["base rate"], "antonyms": [], "example": "Most commercial banks adjust their lending rates based on the prime rate."},
    "inflation": {"phonetic": "/ɪnˈfleɪʃn/", "pos": "n.", "meaning": "通貨膨脹", "phrases": ["high inflation"], "synonyms": [], "antonyms": ["deflation"], "example": "Rising food prices are a clear sign of increasing inflation in the country."},
    "deflation": {"phonetic": "/dɪˈfleɪʃn/", "pos": "n.", "meaning": "通貨緊縮", "phrases": [], "synonyms": [], "antonyms": ["inflation"], "example": "The government is worried about the impact of deflation on the national economy."},
    "recession": {"phonetic": "/rɪˈseʃn/", "pos": "n.", "meaning": "經濟衰退", "phrases": ["economic recession"], "synonyms": ["downturn", "slump"], "antonyms": ["boom", "expansion"], "example": "The country is currently in a deep recession with high unemployment rates."},
    "depression": {"phonetic": "/rɪˈseʃn/", "pos": "n.", "meaning": "經濟衰退", "phrases": ["economic recession"], "synonyms": ["downturn", "slump"], "antonyms": ["boom", "expansion"], "example": "The country is currently in a deep recession with high unemployment rates."},
    "depression": {"phonetic": "/dɪˈpreʃn/", "pos": "n.", "meaning": "經濟大蕭條；憂鬱", "phrases": ["Great Depression"], "synonyms": ["slump", "despair"], "antonyms": ["prosperity"], "example": "The Great Depression of the 1930s had a devastating impact on global trade."},
    "boom": {"phonetic": "/buːm/", "pos": "n./v.", "meaning": "繁榮；激增", "phrases": ["economic boom"], "synonyms": ["prosperity", "growth"], "antonyms": ["slump", "recession"], "example": "The local tourism industry is experiencing a massive boom this summer."},
    "capitalism": {"phonetic": "/ˈkæpɪtəlɪzəm/", "pos": "n.", "meaning": "資本主義", "phrases": [], "synonyms": ["free enterprise"], "antonyms": ["socialism"], "example": "The country's economy is based on the principles of free-market capitalism."},
    "investment": {"phonetic": "/ɪnˈvestmənt/", "pos": "n.", "meaning": "投資", "phrases": ["foreign investment", "capital investment"], "synonyms": ["venture", "stake"], "antonyms": [], "example": "The company is looking for new investment to fund its expansion plans."},
    "investor": {"phonetic": "/ɪnˈvestər/", "pos": "n.", "meaning": "投資者", "phrases": ["private investor", "institutional investor"], "synonyms": ["backer", "shareholder"], "antonyms": [], "example": "Most investors were happy with the company's strong annual results."},
    "portfolio": {"phonetic": "/pɔːrtˈfoʊlioʊ/", "pos": "n.", "meaning": "投資組合；作品集", "phrases": ["investment portfolio"], "synonyms": [], "antonyms": [], "example": "You should diversify your investment portfolio to reduce risk."},
    "stock market": {"phonetic": "/stɑːk ˈmɑːrkɪt/", "pos": "n. phr.", "meaning": "股市", "phrases": ["stock market crash"], "synonyms": ["equity market"], "antonyms": [], "example": "The stock market remained volatile throughout the day due to political news."},
    "share price": {"phonetic": "/ʃer praɪs/", "pos": "n. phr.", "meaning": "股價", "phrases": [], "synonyms": ["stock price"], "antonyms": [], "example": "The company's share price dropped after the news of the CEO's resignation."},
    "broker": {"phonetic": "/ˈbroʊkər/", "pos": "n.", "meaning": "經紀人；代理人", "phrases": ["stockbroker", "insurance broker"], "synonyms": ["agent", "dealer"], "antonyms": [], "example": "The broker charged a small commission for processing the stock transaction."},
    "dividend": {"phonetic": "/ˈdɪvɪdend/", "pos": "n.", "meaning": "股利；紅利", "phrases": ["annual dividend"], "synonyms": ["share", "bonus"], "antonyms": [], "example": "The board has recommended a dividend of fifty cents per share."},
    "bond": {"phonetic": "/bɑːnd/", "pos": "n./v.", "meaning": "債券；聯結", "phrases": ["government bond", "corporate bond"], "synonyms": ["security", "debenture"], "antonyms": [], "example": "Investing in government bonds is generally seen as a low-risk strategy."},
    "commodity": {"phonetic": "/kəˈmɑːdəti/", "pos": "n.", "meaning": "商品；日用品", "phrases": ["commodity market"], "synonyms": ["good", "product"], "antonyms": [], "example": "Gold and oil are two of the most actively traded commodities in the world."},
    "derivative": {"phonetic": "/dɪˈrɪvətɪv/", "pos": "n./adj.", "meaning": "衍生性金融商品；衍生的", "phrases": ["financial derivatives"], "synonyms": [], "antonyms": [], "example": "The bank uses complex derivatives to hedge against financial risk."},
    "speculation": {"phonetic": "/ˌspekjuˈleɪʃn/", "pos": "n.", "meaning": "投機；推測", "phrases": ["market speculation"], "synonyms": ["guess", "gamble"], "antonyms": [], "example": "There has been a lot of speculation about the future of the technology firm."},
    "hedging": {"phonetic": "/ˈhedʒɪŋ/", "pos": "n.", "meaning": "避險", "phrases": ["hedging strategy"], "synonyms": [], "antonyms": [], "example": "Hedging is a way for companies to protect themselves against price fluctuations."},
    "leverage": {"phonetic": "/ˈlevərɪdʒ/", "pos": "n./v.", "meaning": "槓桿作用；利用", "phrases": ["financial leverage"], "synonyms": ["influence", "exploit"], "antonyms": [], "example": "The company used financial leverage to increase its return on investment."},
    "margin": {"phonetic": "/ˈmɑːrdʒɪn/", "pos": "n.", "meaning": "利潤率；邊緣；保證金", "phrases": ["profit margin", "safety margin"], "synonyms": ["edge", "border"], "antonyms": [], "example": "The company's profit margin has increased significantly over the last year."},
    "arbitrage": {"phonetic": "/ˈɑːrbɪtrɑːʒ/", "pos": "n.", "meaning": "套利", "phrases": [], "synonyms": [], "antonyms": [], "example": "Arbitrage involves buying and selling the same asset in different markets to profit from price differences."},
    "offshore": {"phonetic": "/ˌɔːfˈʃɔːr/", "pos": "adj./adv.", "meaning": "離岸的；海外的", "phrases": ["offshore bank account"], "synonyms": ["overseas"], "antonyms": ["onshore"], "example": "The company has several offshore accounts to manage its international revenue."},
    "tax haven": {"phonetic": "/tæks ˈheɪvn/", "pos": "n. phr.", "meaning": "避稅天堂", "phrases": [], "synonyms": [], "antonyms": [], "example": "Some small island nations are well-known tax havens for multinational corporations."},
    "remittance": {"phonetic": "/rɪˈmɪtns/", "pos": "n.", "meaning": "匯款", "phrases": ["electronic remittance"], "synonyms": ["payment", "transfer"], "antonyms": [], "example": "The migrant worker sends a monthly remittance to his family in his home country."},
    "exchange rate": {"phonetic": "/ˈeksˈtʃeɪndʒ reɪt/", "pos": "n. phr.", "meaning": "匯率", "phrases": ["fixed exchange rate"], "synonyms": [], "antonyms": [], "example": "The current exchange rate makes it very expensive for us to import goods from Europe."}
}

with open('data_gold.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    word = item['word']
    if word in enriched_data_gold_5:
        update_info = enriched_data_gold_5[word].copy()
        if 'word' in update_info:
            item['word'] = update_info.pop('word')
        item.update(update_info)

with open('data_gold.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("成功精修金色等級第 201-250 個單字。")
