import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import secrets
import parsePlaylists


scope = "playlist-modify-public"
SPOTIPY_REDIRECT_URI = 'http://localhost/'


token = util.prompt_for_user_token(secrets.CLIENT_USERNAME,scope,client_id=secrets.CLIENT_ID,client_secret=secrets.CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)