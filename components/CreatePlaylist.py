import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
#import SpotifySecrets
CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "a520af0b1e0a479d965e45fd115cf1fe"
CLIENT_USERNAME = "18xwy2dfk7j0v61oyhj9b8csa"
SPOTIPY_REDIRECT_URI = "http://localhost:8080"
SCOPE = "playlist-modify-public"


token = util.prompt_for_user_token(CLIENT_USERNAME,
                                   SCOPE,
                                   client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

class CreatePlaylist:
    CLIENT_USERNAME = CLIENT_USERNAME

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
            
            sp.user_playlist_create(self.CLIENT_USERNAME, playlist_name)
            return(playlist_name + " was succesfully created as a playlist.")
        except:
            return("Playlist could not be created, try again later.")
