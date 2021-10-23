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

class FindPlaylists:
    def __init__(self):
        pass

    def findPlaylists(self,query): 
        results = sp.search(q=query, limit=50, offset=0, type="playlist")

        track_Ids = []

        for track in results['playlists']['items']:
            track_Ids.append(track['id'])


        return track_Ids

 
    # x = parser.sortTracks(findPlaylists("hype"))


    # for i in x:
    #     if i[1] > 1:
    #         print(i[0] + " " + str(i[1]))

#print(sp.track(track_id = "7m9OqQk4RVRkw9JJdeAw96"))