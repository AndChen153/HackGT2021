import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import secrets
import math

token = util.prompt_for_user_token(secrets.CLIENT_USERNAME,
                                   secrets.SCOPE,
                                   client_id=secrets.CLIENT_ID,
                                   client_secret=secrets.CLIENT_SECRET,
                                   redirect_uri=secrets.SPOTIPY_REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)

class ParsePlaylists:

    def __init__(self):
        pass

    def getTracks(self, pl_ids): 
        offset = 0
        track_dict = {}
        weightedAdd = 1
        for pl_id in pl_ids:
            follows = sp.playlist(pl_id, fields="followers")
            #print(follows['followers']['total'])
            


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
                        track_dict[item['id']] += weightedAdd * math.log(int(follows['followers']['total']) + 10)
                    else:
                        track_dict[item['id']] = weightedAdd * math.log(int(follows['followers']['total']) + 10)
                offset = offset + len(response['items'])
        #print (track_dict)
        return track_dict

    # returns sorted dictionary by frequency with key as song id and value as frequency
    def sortTracks(self, playlists, length):
        length = int(length)
        if length < 0:
            length = 1
        elif length > 100:
            length = 100
        
        tracks = self.getTracks(playlists)
        sortedTracks = sorted(tracks.items(), key=lambda x: x[1], reverse=True)
        bestTracks = []
        # nullCase = 0
        for i in sortedTracks[0:length]:
            #print(i[0] + " " + str(i[1]))
            if i[0] != None:
                bestTracks.append(i[0])
            # elif i[0] == None:
            #     nullCase += 1
        # fixes the rare occurence that there exists a None value in the tracks
        # while nullCase > 0:
        #     newLength = length + nullCase
        #     nullCase = 0
        #     for i in sortedTracks[length: newLength]:
        #         if i[0] != None:
        #             print(i[0], length, newLength, i)
        #             bestTracks.append(i[0])
        #         elif i[0] == None:
        #             nullCase += 1
        return bestTracks
