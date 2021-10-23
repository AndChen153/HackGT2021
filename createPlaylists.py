import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "4ed00f732cad40918222c053f68a5502"
scope = "playlist-modify-public"
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                     client_id = CLIENT_ID,
                     client_secret = CLIENT_SECRET,
                     redirect_uri = SPOTIPY_REDIRECT_URI))
print(sp.user(sp.me()['id']))
#sp.user_playlist_create(user = CLIENT_ID, name="playlist1", public = True, collaborative = False, description = "test playlist")
