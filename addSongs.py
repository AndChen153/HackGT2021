import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "be814f3e07234414a23a0c09eb231d07"
scope = "playlist-modify-public"
SPOTIPY_REDIRECT_URI = 'http://localhost/'
CLIENT_USERNAME = "18xwy2dfk7j0v61oyhj9b8csa"


token = util.prompt_for_user_token(CLIENT_USERNAME,scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

songs = ["0Tfxvck4aXsRXffYakDzmF","6eT7xZZlB2mwyzJ2sUKG6w","0RRm4OS5ymfZryXBuj0G2m","2hloaUoRonYssMuqLCBLTX","3UrNOHCzVxX2KZbNcKQAyu"]

ids = []
names = []
for i in range(len(sp.user_playlists(CLIENT_USERNAME)["items"])):
    ids.append(sp.user_playlists(CLIENT_USERNAME)["items"][i]["id"])
    names.append(sp.user_playlists(CLIENT_USERNAME)["items"][i]["name"])

def addSongs(songList, playlist_name):
    try:
        index = names.index(playlist_name)
        sp.playlist_add_items
    except:
        return("playlist not found")