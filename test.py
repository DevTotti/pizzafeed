import requests
from bs4 import BeautifulSoup
import json


url = "https://www.cicis.com/offers/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

wn = soup.title.string
#print (wn) #Site Name

results = soup.find_all("div", {"class": "vc_custom_1586183448433"})
#print(results)

for item in results:
    print(item.contents[2].text)

    print(item.contents[1].text)
    



import re 
import pprint
import requests
from bs4 import BeautifulSoup
import json
import pprint


url = "https://www.cicis.com/offers/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

wn = soup.title.string
#print (wn) #Site Name

results = soup.find_all("div", {"class": "theme-content false"})
#print(results)

for item in results:
    cp = item.find_all("div", {"class": "mk-text-block"})
    for e in cp:
        #cp = e.find_all("p", string = re.compile('^ENTER CODE.*' , re.IGNORECASE))
        cp = e.find_all(string = re.compile('^ENTER CODE.*' , re.IGNORECASE))
        pprint.pprint(cp)
    #pprint.pprint(cp)

