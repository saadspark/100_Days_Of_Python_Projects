import requests
import datetime as dt
import bs4 as bs
import pandas as pd
date = input("Enter the date in the format YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/billboard-200/{date}")
response.raise_for_status()
data = response.text


soup = bs.BeautifulSoup(data, 'html.parser')

list_of_songs = []
song_names_spans = soup.find_all('h3',id='title-of-a-story')
for song in song_names_spans:
    list_of_songs.append(song.getText().strip())



data_frame = pd.DataFrame(list_of_songs)

data_frame.to_csv(f"100 Famous Songs of {date}.csv")

