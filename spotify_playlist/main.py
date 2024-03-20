import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import os

date_of_chart = "2016-07-24"
def get_hot100(date):
    billboard_top100 = f"https://www.billboard.com/charts/hot-100/{date}"

    response = requests.get(url=billboard_top100).text
    soup = BeautifulSoup(response, "html.parser")

    artist_tags = soup.find_all("span",
                                class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
    song_tags = soup.find_all("h3",
                              class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

    songs = {artist.getText().strip(): song.getText().strip() for artist, song in zip(artist_tags, song_tags)}
    return songs

try:
    with open("hot100.json", "r") as f:
        top_songs = json.load(f)
except FileNotFoundError:
    with open("hot100.json", "w") as f:
        top_songs = get_hot100(date_of_chart)
        json.dumps(top_songs)


import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIFY_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIFY_KEY")
REDIRECT_URI = "https://music.yandex.ru/"
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=
                     SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                  client_secret=SPOTIPY_CLIENT_SECRET,
                                  redirect_uri=REDIRECT_URI,
                                  scope=scope))

results = sp.current_user_saved_tracks()
print(results)