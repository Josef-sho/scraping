from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "dfbe9ea8d342450299f4bf9e3c848090"
Client_Secret = "8f802bc649d749fd8391e47379c3c416"
REDIRECT_URI = "http://example.com"
scope = "user-library-read,playlist-modify-public,playlist-modify-private"
access_token = "BQCFtKbGzV9BoI78cgW6HwULoajh9TbQflCR8V9sj_ETJMB9eWcrI_NjWVsVnU2iccYdzG3pSXU3LqkIkQkGj9I3fO_UFoUPQPxlBTHZYFfXpiI4F4z8ljxHnXxbGOacFUdPMB3kaj7OC2ZsalgGPxFN-wtNqMALmOXuLXjBumKlSi4BHKebqErnStpXg3P1dyE5lSVvvZsA5zqX1u7piNZXSTLG0XnokCMY97YmrUGP0uPHHX7l1Aj8xRfXgB1A7PZWpyWhlpBzLw"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID,client_secret=Client_Secret,redirect_uri=REDIRECT_URI, scope=scope, show_dialog=True,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
response = response.text

soup = BeautifulSoup(response, "html.parser")


title = soup.select(".o-chart-results-list-row-container")

song_titles = [title.find("h3").getText().strip() for title in title]
song_artists = [artist.find_all("span")[1].getText().strip() for artist in title]

print(song_titles)