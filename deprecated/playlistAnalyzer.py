
import requests
import json
from tkinter import *
from playlistcreator import *
from secrets import *
class PlaylistAnalyzer():
    def __init__(self, master):
        self.master = master
        self.master.title("Spotify Analyzer")
        self.playlists = []
        self.userEntry = Entry(self.master, width=50)
        self.userEntry.grid()
        self.login = Button(self.master, text="Login", width=10, command=self.getUser)
        self.login.grid()
        self.v = StringVar()
        Label(master, textvariable=self.v).grid()
        self.v.set("Please Log In")
        self.playlistEntry = Entry(self.master, width=50)
        self.playlistEntry.grid()
        self.select = Button(self.master, text="Select", width=10, command=self.getSelectedPlaylist)
        self.select.grid()
        self.x = StringVar()
        Label(self.master, textvariable=self.x).grid()
        self.x.set(" ")
    def getPlaylists(self, user):
     query = "https://api.spotify.com/v1/users/{}/playlists".format(user)
     response = requests.get(
         query,
          headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
            )
     response_json = response.json()
     items = response_json['items']
     i = 0
     playlistids = {}
     for item in items:
          curList = items[i]
          playlistid = curList['id']
          playlistname = curList['name']
          playlistids[playlistname] = playlistid
          i += 1
     return playlistids
    def getTopListens(self, user):
      query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
      response = requests.get(
          query,
          headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
            )
      response_json = response.json()
      items = response_json['items']
      trackids = []
      for item in items:
           track = item
           trackid = track['uri']
           trackids.append(trackid)
      return trackids
    def getTrackIds(self, playlistId):
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlistId)
        response = requests.get(
          query,
          headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
            )
        response_json = response.json()
        items = response_json['items']
        i = 0
        trackids = []
        for item in items:
            track = item
            trackinfo = track['track']
            trackid = trackinfo['id']
            trackids.append(trackid)
        return trackids
    def trackInfo(self, trackId):
        query = "https://api.spotify.com/v1/audio-features/{}".format(trackId)
        response = requests.get(
           query,
           headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
             )
        response_json = response.json()
        results = []
        results.append(response_json['energy'])
        results.append(response_json['danceability'])
        results.append(response_json['valence'])
        query = "https://api.spotify.com/v1/tracks/{}".format(trackId)
        response = requests.get(
           query,
           headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
             )
        response_json = response.json()
        results.append(response_json['popularity'])
        return results
    def analyzePlaylist(self, playlistId):
        tracks = self.getTrackIds(playlistId)
        print("thinking...")
        numTracks = 0
        energy = 0 
        danceability = 0
        valence = 0
        popularity = 0
        for track in tracks:
            numTracks += 1
            x = self.trackInfo(track)
            energy += x[0]
            danceability += x[1]
            valence += x[2]
            popularity += x[3]
        results = {}
        results['valence'] = valence/numTracks
        results['energy'] = energy/numTracks
        results['danceability'] = danceability/numTracks
        results['popularity'] = popularity/numTracks
        print(results)
        return results
    def getUser(self):
        global playlists 
        playlists = self.getPlaylists(self.userEntry.get())
        string = ""
        i = 0
        for item in playlists:
            string = string + str(i) + ": " + item + "\n"
            i += 1
        print(string)
        self.v.set(string)
    def getSelectedPlaylist(self):
        selection = list(playlists)[0]
        results = self.analyzePlaylist(playlists[selection])
        string =  "Valence (happiness) factor (0 - 100): " + str(results['valence'] * 100)
        string = string + "\nEnergy factor (0 - 100):" + str(results['energy']  * 100)
        string = string + "\nDanceability factor (0 - 100): " + str(results['danceability']  * 100)
        string = string + "\nPopularity factor (0 - 100): " + str(results['popularity'])
        self.x.set(string)

root = Tk()
my_gui = PlaylistAnalyzer(root)
root.mainloop()
