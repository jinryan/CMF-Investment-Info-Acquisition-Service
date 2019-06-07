holdingsData = [{'Ticker': 'BRK-B', 'Weight': '1.41%', 'Market Capitalization': '503.47B', 'Trailing PE': '18.80', 'Forward PE': '18.56', 'PEG Ratio (5 yr expected)': '0.86', 'Price/Sales (ttm)': '2.01', 'Price/Book (mrq)': '0.00', 'Enterprise Value/Revenue': '-0.05', 'Enterprise Value/EBITDA': '-0.26', 'Profit Margin': '10.70%', 'ROA (ttm)': '3.42%', 'ROE (ttm)': '7.50%', 'Quarterly Revenue Growth (yoy)': '5.50%', 'EBITDA': '49.25B', 'Quarterly Earnings Growth (yoy)': 'N/A', 'Total ESG Score': '45', 'Total ESG Percentile': '9th percentile', 'Environment Score': '41', 'Environment Percentile': '43rd percentile', 'Social Score': '49', 'Social Percentile': '0th percentile', 'Governmental Score': '44', 'Governmental Percentile': '14th percentile', 'Sector': 'Financial Services', 'Industry': 'Insurance - Diversified', 'EBITDA Margin': 'Unavailable', 'Gross Profit Margin': 'Unavailable', 'Net Profit Margin': 'Unavailable'}, {'Ticker': 'BRK-B', 'Weight': '1.41%', 'Market Capitalization': '503.47B', 'Trailing PE': '18.80', 'Forward PE': '18.56', 'PEG Ratio (5 yr expected)': '0.86', 'Price/Sales (ttm)': '2.01', 'Price/Book (mrq)': '0.00', 'Enterprise Value/Revenue': '-0.05', 'Enterprise Value/EBITDA': '-0.26', 'Profit Margin': '10.70%', 'ROA (ttm)': '3.42%', 'ROE (ttm)': '7.50%', 'Quarterly Revenue Growth (yoy)': '5.50%', 'EBITDA': '49.25B', 'Quarterly Earnings Growth (yoy)': 'N/A', 'Total ESG Score': '45', 'Total ESG Percentile': '9th percentile', 'Environment Score': '41', 'Environment Percentile': '43rd percentile', 'Social Score': '49', 'Social Percentile': '0th percentile', 'Governmental Score': '44', 'Governmental Percentile': '14th percentile', 'Sector': 'Financial Services', 'Industry': 'Insurance - Diversified', 'EBITDA Margin': 'Unavailable', 'Gross Profit Margin': 'Unavailable', 'Net Profit Margin': 'Unavailable'}, {'Ticker': 'BRK-B', 'Weight': '1.41%', 'Market Capitalization': '503.47B', 'Trailing PE': '18.80', 'Forward PE': '18.56', 'PEG Ratio (5 yr expected)': '0.86', 'Price/Sales (ttm)': '2.01', 'Price/Book (mrq)': '0.00', 'Enterprise Value/Revenue': '-0.05', 'Enterprise Value/EBITDA': '-0.26', 'Profit Margin': '10.70%', 'ROA (ttm)': '3.42%', 'ROE (ttm)': '7.50%', 'Quarterly Revenue Growth (yoy)': '5.50%', 'EBITDA': '49.25B', 'Quarterly Earnings Growth (yoy)': 'N/A', 'Total ESG Score': '45', 'Total ESG Percentile': '9th percentile', 'Environment Score': '41', 'Environment Percentile': '43rd percentile', 'Social Score': '49', 'Social Percentile': '0th percentile', 'Governmental Score': '44', 'Governmental Percentile': '14th percentile', 'Sector': 'Financial Services', 'Industry': 'Insurance - Diversified', 'EBITDA Margin': 'Unavailable', 'Gross Profit Margin': 'Unavailable', 'Net Profit Margin': 'Unavailable'}, {'Ticker': 'BRK-B', 'Weight': '1.41%', 'Market Capitalization': '503.47B', 'Trailing PE': '18.80', 'Forward PE': '18.56', 'PEG Ratio (5 yr expected)': '0.86', 'Price/Sales (ttm)': '2.01', 'Price/Book (mrq)': '0.00', 'Enterprise Value/Revenue': '-0.05', 'Enterprise Value/EBITDA': '-0.26', 'Profit Margin': '10.70%', 'ROA (ttm)': '3.42%', 'ROE (ttm)': '7.50%', 'Quarterly Revenue Growth (yoy)': '5.50%', 'EBITDA': '49.25B', 'Quarterly Earnings Growth (yoy)': 'N/A', 'Total ESG Score': '45', 'Total ESG Percentile': '9th percentile', 'Environment Score': '41', 'Environment Percentile': '43rd percentile', 'Social Score': '49', 'Social Percentile': '0th percentile', 'Governmental Score': '44', 'Governmental Percentile': '14th percentile', 'Sector': 'Financial Services', 'Industry': 'Insurance - Diversified', 'EBITDA Margin': 'Unavailable', 'Gross Profit Margin': 'Unavailable', 'Net Profit Margin': 'Unavailable'}, {'Ticker': 'BRK-B', 'Weight': '1.41%', 'Market Capitalization': '503.47B', 'Trailing PE': '18.80', 'Forward PE': '18.56', 'PEG Ratio (5 yr expected)': '0.86', 'Price/Sales (ttm)': '2.01', 'Price/Book (mrq)': '0.00', 'Enterprise Value/Revenue': '-0.05', 'Enterprise Value/EBITDA': '-0.26', 'Profit Margin': '10.70%', 'ROA (ttm)': '3.42%', 'ROE (ttm)': '7.50%', 'Quarterly Revenue Growth (yoy)': '5.50%', 'EBITDA': '49.25B', 'Quarterly Earnings Growth (yoy)': 'N/A', 'Total ESG Score': '45', 'Total ESG Percentile': '9th percentile', 'Environment Score': '41', 'Environment Percentile': '43rd percentile', 'Social Score': '49', 'Social Percentile': '0th percentile', 'Governmental Score': '44', 'Governmental Percentile': '14th percentile', 'Sector': 'Financial Services', 'Industry': 'Insurance - Diversified', 'EBITDA Margin': 'Unavailable', 'Gross Profit Margin': 'Unavailable', 'Net Profit Margin': 'Unavailable'}]


titles = list(holdingsData[0])
ultimateArray = [titles]
for eachCompany in holdingsData:
    companyInfo = []
    for eachTitle in titles:
        companyInfo.append(eachCompany[eachTitle])

    ultimateArray.append(companyInfo)

print(ultimateArray)