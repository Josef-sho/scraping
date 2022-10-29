from bs4 import BeautifulSoup
import requests

cot = requests.get('https://news.ycombinator.com')

cot = cot.text
soup = BeautifulSoup(cot, "html.parser")
article_text = soup.find_all(class_="titleline")

titles = []
links = []
votes = []

article_vote = soup.find_all(name="span", class_="score")

for title in article_text:
    titles.append(title.text)
    links.append(title.find(name="a").get("href"))


for article in article_vote:
    votes.append(article.text)



for i in range(len(votes)):
    print(titles[i])
    print(links[i])
    print(votes[i])





"""print(article_text.text)
article_link = soup.find(name='a')
print(article_link.get("href"))
article_vote = soup.find(name="span", class_ ="score")
print(article_vote.text)
"""




"""
with open("website.html", "r", encoding="utf8") as html:
    co = html.read()

soup = BeautifulSoup(co, "html.parser")
tags = soup.find_all(name='a')

# for tg in tags:
#     # print(tg.get("href"))
#     pass

hed = soup.find(id = "name")
print(hed)"""