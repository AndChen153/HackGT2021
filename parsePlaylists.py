import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "4ed00f732cad40918222c053f68a5502"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

#pl_id = 'spotify:playlist:3rMa2dmPtINY46bimugyrO'
def getTracks(pl_ids): 
    offset = 0
    track_dict = {}
    for pl_id in pl_ids:
        offset = 0
        response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
        for i in response['items']:
            for item in i.values():
                 if item['id'] in track_dict.keys():
                      track_dict[item['id']] += 1
                 else:
                      track_dict[item['id']] = 1
            offset = offset + len(response['items'])
    return track_dict;


pl_ids = ["4EuoBAshVI1B0t5Rg6HTp7", "7DaNB3xvJ4F96C66mQgmpS", "7DaNB3xvJ4F96C66mQgmpS", "3rMa2dmPtINY46bimugyrO"]
print(getTracks(pl_ids))