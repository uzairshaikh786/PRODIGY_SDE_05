import requests
from bs4 import BeautifulSoup
import pandas as pd

Product_name = []
Prices = []
Description = []
# Reviews = []

for page in range(2, 12):
    # Construct the URL for each page
    url = "https://www.flipkart.com/search?q=mobiles+phones+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(page)

    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text, "html.parser")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    # 1) Product names
    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)

    # 2) Prices
    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)

    # 3) Descriptions
    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        name = i.text
        Description.append(name)


# Use of Pandas 
df = pd.DataFrame({"Product_name":Product_name , "Prices" : Prices, "Decription" : Description})
print(df)

df.to_csv("flipkart_mobiles_under50k.csv")

    # np = soup.find("a", class_ = "_1LKTO3").get('href')
    # # complete next page 
    # cnp = "https://www.flipkart.com" + np 
    # print(cnp)
 