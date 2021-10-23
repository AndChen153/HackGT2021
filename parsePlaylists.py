import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import secrets
import parsePlaylists

scope = "playlist-modify-public"
SPOTIPY_REDIRECT_URI = 'http://localhost/'

token = util.prompt_for_user_token(secrets.CLIENT_USERNAME,scope,client_id=secrets.CLIENT_ID,client_secret=secrets.CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

def getTracks(pl_ids): 
    offset = 0
    track_dict = {}
    weightedAdd = 1
    for pl_id in pl_ids:
        follows = sp.playlist(pl_id, fields="followers")
       # print(follows['followers']['total'])
        offset = 0
        response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
        for i in response['items']:
            for item in i.values():
                 if item == None:
                    break
                 if item['id'] in track_dict.keys():
                      track_dict[item['id']] += weightedAdd
                 else:
                      track_dict[item['id']] = weightedAdd
            offset = offset + len(response['items'])
    return track_dict;

# returns sorted dictionary by frequency with key as song id and value as frequency
def sortTracks(playlists):
    tracks = getTracks(playlists)
    sortedTracks = sorted(tracks.items(), key=lambda x: x[1], reverse=True)
    return sortedTracks
