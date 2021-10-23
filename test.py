import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "4ed00f732cad40918222c053f68a5502"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])