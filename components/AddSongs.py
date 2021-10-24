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


class AddSongs:
    
    CLIENT_USERNAME = CLIENT_USERNAME

    def __init__(self):
        pass

    def addSongList(self, songList, playlist_name, length):
        # len(sp.user_playlists(self.CLIENT_USERNAME)["items"]) - 1
        playlist_id = sp.user_playlists(self.CLIENT_USERNAME)["items"][0]["id"]
        playlist_url = sp.user_playlists(self.CLIENT_USERNAME)["items"][0]["external_urls"]["spotify"]
            
        # try:
       # print(len(songList))
        #print(sp.playlist(playlist_id)["name"])
        sp.playlist_add_items(playlist_id, songList)
        # return(length + " songs added at " + urls[index])
        return(playlist_url)
        # except:
        #     return("playlist not found")
