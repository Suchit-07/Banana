import requests
from bs4 import BeautifulSoup
import re

query = "banana"
search = query.replace(' ', '+')
results = 10
url = (f"https://www.google.com/search?q={search}&num={results}")

requests_results = requests.get(url)
soup_link = BeautifulSoup(requests_results.content, "html.parser")

soup_snippet = BeautifulSoup(requests_results.content, "lxml")
soup_snippet.prettify()
snippets = soup_snippet.select(".aCOpRe span:not(.f)")
print(snippets)

links = soup_link.find_all("a")

final_links = []
for link in links:
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
      title = link.find_all('h3')
      if len(title) > 0:
          curr_link = link.get('href').split("?q=")[1].split("&sa=U")[0]
          final_links.append([title[0].getText(),curr_link])
   
print(final_links)
# response = requests.get(final_links[0][1],headers={'User-Agent': 'Mozilla/5.0'})
# soup = BeautifulSoup(response.text,'lxml')

# print(soup.body.get_text(' ', strip=True))