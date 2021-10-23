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

    def findUserPlaylists(self):
        ids = []
        names = []
        urls = []

        for i in range(len(sp.user_playlists(self.CLIENT_USERNAME)["items"])):
            ids.append(sp.user_playlists(self.CLIENT_USERNAME)["items"][i]["id"])
            names.append(sp.user_playlists(self.CLIENT_USERNAME)["items"][i]["name"])
            urls.append(sp.user_playlists(self.CLIENT_USERNAME)["items"][i]["external_urls"]["spotify"])
            
        return ids, names, urls

    def addSongList(self, songList, playlist_name, length):
        ids, names, urls = self.findUserPlaylists()
        if length < 0:
            length = 1
        elif length > 100:
            length = 100
        try:
            index = names.index(playlist_name)
            sp.playlist_add_items(ids[index], songList[0:length])
            return("Songs added at " + urls[index])
        except:
            return("playlist not found")
