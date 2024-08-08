from bs4 import BeautifulSoup
import requests
import pandas as pd
request = requests.get(url='https://news.ycombinator.com/news')


soup = BeautifulSoup(request.text, 'html.parser')

title_line = soup.find_all('span', class_='titleline')

title_list = []
title_url_list = []

for art in title_line:
    link = art.find('a')
    title_text = art.getText()
    title_list.append(title_text)
    title_url = link.get('href')
    title_url_list.append(title_url)        
 

score = soup.find_all('span', class_='score')
score_list = [int(s.getText().split()[0]) for s in score]

# print(title_list)
# print(title_url_list)
# print(score_list)

largesst_index = score_list.index(max(score_list))

dir = {
    'title' : title_list,
    'Url' : title_url_list,
    'score' : score_list,
}

