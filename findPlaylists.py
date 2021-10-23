import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import parsePlaylists
import secrets




CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "be814f3e07234414a23a0c09eb231d07"
client_credentials_manager = SpotifyClientCredentials(client_id= CLIENT_ID,
                                                           client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
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