import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import secrets
import parsePlaylists


scope = "playlist-modify-public"
SPOTIPY_REDIRECT_URI = 'http://localhost/'


token = util.prompt_for_user_token(secrets.CLIENT_USERNAME,scope,client_id=secrets.CLIENT_ID,client_secret=secrets.CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

songs = ["0Tfxvck4aXsRXffYakDzmF","6eT7xZZlB2mwyzJ2sUKG6w","0RRm4OS5ymfZryXBuj0G2m","2hloaUoRonYssMuqLCBLTX","3UrNOHCzVxX2KZbNcKQAyu"]

def findUserPlaylists():
    ids = []
    names = []
    urls = []

    for i in range(len(sp.user_playlists(CLIENT_USERNAME)["items"])):
        ids.append(sp.user_playlists(CLIENT_USERNAME)["items"][i]["id"])
        names.append(sp.user_playlists(CLIENT_USERNAME)["items"][i]["name"])
        urls.append(sp.user_playlists(CLIENT_USERNAME)["items"][i]["external_urls"]["spotify"])
        
    return ids, names, urls

def addSongs(songList, playlist_name):
    ids, names, urls = findUserPlaylists()
    try:
        index = names.index(playlist_name)
        sp.playlist_add_items(ids[index], songList)

        return("Songs added at " + urls[index])
    except:
        return("playlist not found")

print(addSongs(songs, "randoPlaylist"))