import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "18e8f7f4ba1c467e9c77afbb34645234"
CLIENT_SECRET = "4ed00f732cad40918222c053f68a5502"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

#pl_id = 'spotify:playlist:3rMa2dmPtINY46bimugyrO'
offset = 0
track_dict = {}
pl_ids = ["4EuoBAshVI1B0t5Rg6HTp7", "3rMa2dmPtINY46bimugyrO", "4ETxM0kkS3RMPveAijToRh", "3rMa2dmPtINY46bimugyrO", "37i9dQZF1DWUSyphfcc6aL", "7DaNB3xvJ4F96C66mQgmpS"]
for pl_id in pl_ids:
    while True:
        response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
    
        if len(response['items']) == 0:
            break
        for item in response['items']:
             print(item['track']['id'])
             if item['track']['id'] in track_dict:
                 track_dict[item['track']['id']] += 1
             else:
                 track_dict[item['track']['id']] = 1

        
        offset = offset + len(response['items'])
#    print(offset, "/", response['total'])
print(track_dict)