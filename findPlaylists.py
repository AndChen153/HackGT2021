import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import parsePlaylists
import secrets


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= secrets.CLIENT_ID,
                                                           client_secret= secrets.CLIENT_SECRET))
def findPlaylists(query): 
    results = sp.search(q=query, limit=50, offset=0, type="playlist")

    track_Ids = []

    for track in results['playlists']['items']:
        track_Ids.append(track['id'])

    return track_Ids

x = parsePlaylists.sortTracks(findPlaylists("hype"))


for i in x:
    if i[1] > 1:
	    print(i[0])

#print(sp.track(track_id = "7m9OqQk4RVRkw9JJdeAw96"))