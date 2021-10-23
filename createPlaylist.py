import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import requests
import spotipy.util as util


CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "be814f3e07234414a23a0c09eb231d07"
scope = "playlist-modify-public"
SPOTIPY_REDIRECT_URI = 'http://localhost/'
CLIENT_USERNAME = "18xwy2dfk7j0v61oyhj9b8csa"


token = util.prompt_for_user_token(CLIENT_USERNAME,scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

def createPlaylist(playlist_name):
    try:
        sp.user_playlist_create(CLIENT_USERNAME, name=playlist_name)
        return(playlist_name + "was succesfully created as a playlist.")
    except:
        return("Playlist could not be created, try again later.")
