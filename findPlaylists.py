import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "4ed00f732cad40918222c053f68a5502"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

results = sp.search(q='ariana grande', limit=30, offset=0, type="playlist")
# print(results)

track_Ids = []

for track in results['playlists']['items']:
    print(track['id'], track['name'], track['external_urls']['spotify'])
    track_Ids.append(track['id'])

print(track_Ids)