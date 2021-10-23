# Shows artist info for a URN or URL

import spotipy
from spotipy import oauth2


SPOTIPY_CLIENT_ID = '18e8f7f4ba1c467e9c77afbb34645234'
SPOTIPY_CLIENT_SECRET = '4ed00f732cad40918222c053f68a5502'
SCOPE = 'user-library-read'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'


sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE)


