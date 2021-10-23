import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "be814f3e07234414a23a0c09eb231d07"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

results = sp.search(q='ariana grande', limit=50, offset=0, type="playlist")
# print(results)

track_Ids = []

for track in results['playlists']['items']:
    print(track['id'], track['name'], track['external_urls']['spotify'])
    track_Ids.append(track['id'])

for i in track_Ids:
    if track_Ids.count(i)>1:
        print (i)

print (len(track_Ids))