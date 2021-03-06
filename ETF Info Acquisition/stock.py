#!/usr/bin/env python

import requests
import re
from bs4 import BeautifulSoup
import csv
import os
cwd = os.path.dirname(os.path.realpath(__file__))

def returnStockInfo(ticker, weight):
    ticker = ticker.replace(".", "-")
    industryAndSectorUrl = 'https://finance.yahoo.com/quote/' + ticker + '/profile?'
    statisticsurl = 'https://finance.yahoo.com/quote/' + ticker + '/key-statistics?p=' + ticker
    sustainabilityurl = 'https://finance.yahoo.com/quote/' + ticker + '/sustainability?p=' + ticker
    EBITAMarginURL = "https://csimarket.com/stocks/singleProfitabilityRatios.php?code=" + ticker + "&ebit"
    grossProfitMarginURL = "https://ycharts.com/companies/" + ticker + "/gross_profit_margin"
    netProfitMarginURL = "https://csimarket.com/stocks/singleProfitabilityRatios.php?code=" + ticker + "&net"


    industryAndSectorResponse = requests.get(industryAndSectorUrl)
    statisticsresponse = requests.get(statisticsurl)
    sustainabilityresponse = requests.get(sustainabilityurl)
    EBITAMarginURLResponse = requests.get(EBITAMarginURL)
    grossProfitMarginResponse = requests.get(grossProfitMarginURL)
    netProfitMarginResponse = requests.get(netProfitMarginURL)

    industryAndSectorSoup = BeautifulSoup(industryAndSectorResponse.text, "html.parser")
    etfdbsoup = BeautifulSoup(statisticsresponse.text, 'html.parser')
    sustainabilitysoup = BeautifulSoup(sustainabilityresponse.text, "html.parser")
    EBITAMarginSoup = BeautifulSoup(EBITAMarginURLResponse.text, "html.parser")
    grossProfitMarginSoup = BeautifulSoup(grossProfitMarginResponse.text, "html.parser")
    netProfitMarginSoup = BeautifulSoup(netProfitMarginResponse.text, "html.parser")

    usefulSustain = sustainabilitysoup.find("div", {"class": "smartphone_Mt(20px)", "data-reactid": "14"})
    usefulStats = sustainabilitysoup.find('section', attrs={'data-test': 'qsp-sustainability'})

    statistcs_name_box = etfdbsoup.find('section', attrs={'data-test': 'qsp-statistics'})
    sustainability_name_box = sustainabilitysoup.find('section', {'data-test': 'qsp-sustainability'})
    if statistcs_name_box == None or statisticsresponse.status_code != 200:
        return {"Status": "Data Unavailable. Please manually acquire it."}

    def findValueWithID(soup, type, id):
        s = soup.find(type, {"data-reactid": str(id)})
        if s != None:
            return s.getText().replace("\n", "").replace("\t", "").strip()
        else:
            return "N/A"

    def findIDFromFinanceSoup(id, altid=-1):
        if altid == -1:
            return findValueWithID(etfdbsoup, "td", id)
        else:
            value = findValueWithID(etfdbsoup, "td", id)
            if value == 'N/A':
                return findValueWithID(etfdbsoup, "td", altid)
            else:
                return value

    def findIDFromSustainabilitySoup(type, id):
        return findValueWithID(usefulSustain, type, id)

    def findIDFromIndustryAndSectorSoup():
        s = industryAndSectorSoup.find("p", {"data-reactid": "18"})
        try:
            sector = s.find("span", {"data-reactid": "21"}).getText().replace("\n", "").replace("\t", "").replace("&amp;", "&").strip()
            industry = s.find("span", {"data-reactid": "25"}).getText().replace("\n", "").replace("\t", "").replace("&amp;", "&").strip()
            return (sector, industry)
        except:
            return ("N/A", "N/A")

    # s = sustainabilitysoup.find("div", {"class": "smartphone_Mt(20px)", "data-reactid": "14"})
    # l = s.find("div", {"data-reactid": 20})
    attributesTuple = (
    "Ticker", "Market Capitalization", "Trailing PE", "Forward PE", "PEG Ratio (5 yr expected)", "Price/Sales (ttm)",
    "Price/Book (mrq)", "Enterprise Value/Revenue", "Enterprise Value/EBITDA", "Profit Margin", "ROA (ttm)",
    "ROE (ttm)", "Quarterly Revenue Growth (yoy)", "EBITDA", "Quarterly Earnings Growth (yoy)")

    valueDictionary = {"Ticker": ticker, "Weight": weight}
    valueDictionary["Market Capitalization"] = findIDFromFinanceSoup(19)
    valueDictionary["Trailing PE"] = findIDFromFinanceSoup(33)
    valueDictionary["Forward PE"] = findIDFromFinanceSoup(40)
    valueDictionary["PEG Ratio (5 yr expected)"] = findIDFromFinanceSoup(47)
    valueDictionary["Price/Sales (ttm)"] = findIDFromFinanceSoup(54)
    valueDictionary["Price/Book (mrq)"] = findIDFromFinanceSoup(61)
    valueDictionary["Enterprise Value/Revenue"] = findIDFromFinanceSoup(68, altid=69)
    valueDictionary["Enterprise Value/EBITDA"] = findIDFromFinanceSoup(75, altid=76)
    valueDictionary["Profit Margin"] = findIDFromFinanceSoup(112, altid=113)

    valueDictionary["ROA (ttm)"] = findIDFromFinanceSoup(131,altid=132)
    valueDictionary["ROE (ttm)"] = findIDFromFinanceSoup(138)

    valueDictionary["Quarterly Revenue Growth (yoy)"] = findIDFromFinanceSoup(164, altid=166)


    valueDictionary["EBITDA"] = findIDFromFinanceSoup(178, altid=173)

    valueDictionary["Quarterly Earnings Growth (yoy)"] = findIDFromFinanceSoup(199, altid=201)

    if sustainability_name_box == None or sustainabilityresponse.status_code != 200:
        valueDictionary["ESG Data"] = "Unavailable"
        attributesTuple += ("ESG Data",)
    else:
        attributesTuple += (
        "Total ESG Score", "Total ESG Percentile", "Environment Score", "Environment Percentile", "Social Score",
        "Social Percentile", "Governmental Score", "Governmental Percentile")
        valueDictionary["Total ESG Score"] = findIDFromSustainabilitySoup("div", 20)
        valueDictionary["Total ESG Percentile"] = findIDFromSustainabilitySoup("span", 23)

        valueDictionary["Environment Score"] = findIDFromSustainabilitySoup("div", 35)
        valueDictionary["Environment Percentile"] = findIDFromSustainabilitySoup("span", 38)

        valueDictionary["Social Score"] = findIDFromSustainabilitySoup("div", 45)
        valueDictionary["Social Percentile"] = findIDFromSustainabilitySoup("span", 48)

        valueDictionary["Governmental Score"] = findIDFromSustainabilitySoup("div", 55)
        valueDictionary["Governmental Percentile"] = findIDFromSustainabilitySoup("span", 58)

    if industryAndSectorResponse.status_code != 200:
        valueDictionary["Industry"] = "Unavailable"
        valueDictionary["Sector"] = "Unavailable"
    else:
        si = findIDFromIndustryAndSectorSoup()
        valueDictionary["Sector"] = si[0]
        valueDictionary["Industry"] = si[1]

    if EBITAMarginURLResponse.status_code != 200 or EBITAMarginSoup.find("td", {"class": "s9 zagqs sve_jedan_red dorubb"}) == None:
        valueDictionary["EBITDA Margin (Quarter)"] = "Unavailable"
    else:
        quarter = EBITAMarginSoup.find("td", {"class": "s9 zagqs sve_jedan_red dorubb"}).getText()
        quarter = quarter[quarter.find("(")+1:quarter.find(")")]
        valueDictionary["EBITDA Margin (Quarter)"] = EBITAMarginSoup.find("td", {"class": "debeligrub2 s"}).find("span").getText() + " For " + quarter

    if grossProfitMarginResponse.status_code != 200 or grossProfitMarginSoup.find("span", {"id": "pgNameVal"}) == None:
        valueDictionary["Gross Profit Margin"] = "Unavailable"
    else:
        valueDictionary["Gross Profit Margin"] = grossProfitMarginSoup.find("span", {"id": "pgNameVal"}).getText()

    if netProfitMarginResponse.status_code != 200 or netProfitMarginSoup.find("td", {"class": "s9 zagqs sve_jedan_red dorubb"}) == None:
        valueDictionary["Net Margin (Quarter)"] = "Unavailable"
    else:
        quarter = netProfitMarginSoup.find("td", {"class": "s9 zagqs sve_jedan_red dorubb"}).getText()
        quarter = quarter[quarter.find("(") + 1:quarter.find(")")]
        valueDictionary["Net Margin (Quarter)"] = netProfitMarginSoup.find("td", {
            "class": "debeligrub2 s"}).find("span").getText() + " For " + quarter


    return valueDictionary