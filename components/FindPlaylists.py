'''import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import secrets



client_credentials_manager = SpotifyClientCredentials(client_id= secrets.CLIENT_ID,
                                                           client_secret=secrets.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)'''

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import secrets
import parsePlaylists


scope = "playlist-modify-public"
SPOTIPY_REDIRECT_URI = 'http://localhost/'


token = util.prompt_for_user_token(secrets.CLIENT_USERNAME,
                                   scope,
                                   client_id=secrets.CLIENT_ID,
                                   client_secret=secrets.CLIENT_SECRET,
                                   redirect_uri=secrets.SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

def findPlaylists(query): 
    results = sp.search(q=query, limit=50, offset=0, type="playlist")

    track_Ids = []

    for track in results['playlists']['items']:
        track_Ids.append(track['id'])

    return track_Ids

x = parsePlaylists.sortTracks(findPlaylists("hype"))


for i in x:
    if i[1] > 1:
	    print(i[0] + " " + str(i[1]))

#print(sp.track(track_id = "7m9OqQk4RVRkw9JJdeAw96"))