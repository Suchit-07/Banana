import requests
from bs4 import BeautifulSoup
import json

query = "what does test mean"
num = 3

param = {"q": query, "num" : num}
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, likes Gecko) Version/13.0.5 Safari/605.1.15"
}

r = requests.get("https://google.com/search", params=param, headers=headers)

desc_soup = BeautifulSoup(r.content, "lxml")


search = query.replace(' ', '+')
url = (f"https://www.google.com/search?q={search}&num={num}")

requests_results = requests.get(url)
link_soup = BeautifulSoup(requests_results.content, "html.parser")

spotlight = desc_soup.select(".hgKElc") 
#print(spotlight[0].getText())

definition = desc_soup.select(".LTKOO.sY7ric") 
#print(definition[0].getText().split('Similar')[0])

description = desc_soup.select(".VwiC3b.yXK7lf")

links = link_soup.find_all("a")

final_links = []
x=0
for link in links:
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
      title = link.find_all('h3')
      if len(title) > 0:
        curr_link = link.get('href').split("?q=")[1].split("&sa=U")[0]
        try:
            final_links.append([title[0].getText(),curr_link, description[x].getText()])
        except:
            pass  
        x+=1

if definition:
    final_links.insert(0, definition[0].getText().split('Similar')[0])
if spotlight:
    final_links.insert(0, spotlight[0].getText())

print(json.dumps(final_links))