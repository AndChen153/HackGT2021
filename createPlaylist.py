import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import secrets
import parsePlaylists


scope = "playlist-modify-public"
SPOTIPY_REDIRECT_URI = 'http://localhost/'


token = util.prompt_for_user_token(secrets.CLIENT_USERNAME,scope,client_id=secrets.CLIENT_ID,client_secret=secrets.CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

def findUserPlaylists():
    ids = []
    names = []
    for i in range(len(sp.user_playlists(CLIENT_USERNAME)["items"])):
        ids.append(sp.user_playlists(CLIENT_USERNAME)["items"][i]["id"])
        names.append(sp.user_playlists(CLIENT_USERNAME)["items"][i]["name"])
    return ids, names


def createPlaylist(playlist_name):
    ids, names = findUserPlaylists()

    try:
        if playlist_name in names:
            return("Playlist name already exists.")
        else:
            sp.user_playlist_create(CLIENT_USERNAME, name=playlist_name)
            return(playlist_name + " was succesfully created as a playlist.")
    except:
        return("Playlist could not be created, try again later.")

print(createPlaylist("randoPlaylist1"))
