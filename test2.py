from bs4 import BeautifulSoup
import requests
import re

param = {"q": "can a dog eat a bananas", "num" : "4"}
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, likes Gecko) Version/13.0.5 Safari/605.1.15"
}

r = requests.get("https://google.com/search", params=param, headers=headers)

soup = BeautifulSoup(r.content, "lxml")
soup.prettify()

spotlight = soup.select(".hgKElc") 
print(spotlight)

# definition = soup.select(".LTKOO.sY7ric") 
# print(definition[0].getText().split('Similar')[0])


# title = soup.select(".VwiC3b.yXK7lf")

# for x in title:
#     print(x.getText())
#     print('---')

