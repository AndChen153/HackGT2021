from heapq import nlargest
import requests
import json
from tkinter import *
from playlistcreator import *
from secrets import *
from playlistAnalyzer import * 
class popularPlaylistGenerator(object):
    def getPlaylists(self, search):
        print(search)
        query = "https://api.spotify.com/v1/search?q={}&type=playlist".format("'" + search + "'")
        response = requests.get(
            query,
            headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
         )
        response_json = response.json()
        print(response_json)
        pass;
    def getTracksFromLists(self):
        pass;
    def sortTracks(self):
        pass;
#root = Tk()
#gui = popularPlaylistGenerator()
#gui.getPlaylists("summer")
#root.mainloop()



