import pprint
import requests
from bs4 import BeautifulSoup
import json
import re

data = []

url = "https://www.cicis.com/offers/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

wn = soup.title.string
#print (wn) #Site Name

results = soup.find_all("div", {"class": "theme-content false"})
#print(results)

for item in results:
    
    cp = item.find_all("div", {"class": "mk-text-block"})
    #pprint.pprint(cp)

    for e in cp:
        #cp = e.find_all("p", string = re.compile('^ENTER CODE.*' , re.IGNORECASE))
        
        wn = url[:21]
        
        try:
            cp = e.contents[2].text
        except:
            pass
        
        try:
            p_typ = e.contents[1].text
        except:
            pass


        data.append({"Website Name":wn, "Pizza Summary":p_typ,   "Coupon Code":cp})
        

with open('cici.json', 'w', encoding='utf-8') as f:
	f.write(json.dumps(data, indent= 4)) 