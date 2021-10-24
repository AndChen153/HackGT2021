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

class FindPlaylists:
    def __init__(self):
        pass

    def findPlaylists(self,query): 
        results = sp.search(q=query, limit=20, offset=0, type="playlist")

        track_Ids = []

        for track in results['playlists']['items']:
            track_Ids.append(track['id'])


        return track_Ids

 
    # x = parser.sortTracks(findPlaylists("hype"))


    # for i in x:
    #     if i[1] > 1:
    #         print(i[0] + " " + str(i[1]))

#print(sp.track(track_id = "7m9OqQk4RVRkw9JJdeAw96"))