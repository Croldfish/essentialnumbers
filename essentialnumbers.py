from bs4 import BeautifulSoup

import requests

def usdebt():
    jls_extract_var = 'http://www.pgpf.org/national-debt-clock'
    website = requests.get(jls_extract_var)

    soup = BeautifulSoup(website.content, 'html.parser')

    id = soup.find(id = 'ticker-text')

    return ("US Debt: " + id.string)

def ricekrispiesprice():
    url = 'https://www.riteaid.com/shop/kellogg-s-rice-krispies-treats-crispy-marshmallow-squares-original-value-pack-12-4oz-box?s_kwcid=AL!9320!10!76759731119795!4580359288860116&utm_source=bing&utm_medium=cpc&utm_campaign=WITHIN_4510_Evergreen_Shopping_FoodBeveragesTobacco_All_NB_Bing&utm_term=4580359288860116&utm_content=Food%20Items'
    website = requests.get(url)


    soup = BeautifulSoup(website.content, 'html.parser')
    
    
    price = soup.find(class_="price")

    return ("16ct box of Rice Krispies Treats from RiteAid: " + price.string)



