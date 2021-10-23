import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import secrets


token = util.prompt_for_user_token(secrets.CLIENT_USERNAME,
                                   secrets.SCOPE,
                                   client_id=secrets.CLIENT_ID,
                                   client_secret=secrets.CLIENT_SECRET,
                                   redirect_uri=secrets.SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

class CreatePlaylist:
    CLIENT_USERNAME = secrets.CLIENT_USERNAME

    def __init__(self):
        pass

    def findUserPlaylists(self):
        ids = []
        names = []
        for i in range(len(sp.user_playlists(self.CLIENT_USERNAME)["items"])):
            ids.append(sp.user_playlists(self.CLIENT_USERNAME)["items"][i]["id"])
            names.append(sp.user_playlists(self.CLIENT_USERNAME)["items"][i]["name"])
        return ids, names


    def createPlaylist(self, playlist_name):
        ids, names = self.findUserPlaylists()

        try:
            playlist_name = playlist_name.lower()
            sp.user_playlist_create(self.CLIENT_USERNAME, name=playlist_name)
            return(playlist_name + " was succesfully created as a playlist.")
        except:
            return("Playlist could not be created, try again later.")
