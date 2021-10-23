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


class AddSongs:
    
    CLIENT_USERNAME = secrets.CLIENT_USERNAME

    def __init__(self):
        pass

    def addSongList(self, songList, playlist_name, length):
        # len(sp.user_playlists(self.CLIENT_USERNAME)["items"]) - 1
        playlist_id = sp.user_playlists(self.CLIENT_USERNAME)["items"][0]["id"]
        playlist_url = sp.user_playlists(self.CLIENT_USERNAME)["items"][0]["external_urls"]["spotify"]
            
        # try:
        print(len(songList))
        print(songList)
        sp.playlist_add_items(playlist_id, songList)
        # return(length + " songs added at " + urls[index])
        return(playlist_url)
        # except:
        #     return("playlist not found")
