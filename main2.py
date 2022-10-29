import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

rule = requests.get(URL)
rule = rule.text

soup = BeautifulSoup(rule, "html.parser")

# Write your code below this line 👇


title = soup.find_all(name='h3', class_='title')

titles = [tittle.text for tittle in title]

titles.reverse()

with open('title.txt', 'w', encoding='utf-8') as file:
    for i in titles:
        file.write(f'{i}\n')
