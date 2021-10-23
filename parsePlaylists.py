from logging import NullHandler
from spotipy.oauth2 import SpotifyClientCredentials
import secrets
import spotipy
import json


CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "be814f3e07234414a23a0c09eb231d07"
client_credentials_manager = SpotifyClientCredentials(client_id= CLIENT_ID,
                                                           client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJiZcmkrIHGU'
results = sp.playlist(playlist_id)
def getTracks(pl_ids): 
    offset = 0
    track_dict = {}
    weightedAdd = 1
    for pl_id in pl_ids:
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

def sortTracks(playlists):
    tracks = getTracks(playlists)
    sortedTracks = sorted(tracks.items(), key=lambda x: x[1], reverse=True)
    return sortedTracks
