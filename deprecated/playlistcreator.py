import requests
import json
from tkinter import *
from playlistcreator import *
from secrets import *
from playlistAnalyzer import * 

class PlaylistCreator():
    def __init__(self, master):
       self.master = master
       master.title("create a playlist")
       self.label = Label(master, text="Select which genres to include", wraplength = 0)
       self.label.grid()
       self.genres = self.readGenres()
       i = 1
       self.boxList = []
       for genre in self.genres:
            self.genres[genre] = IntVar()
            Checkbutton(master, text=genre, variable = self.genres[genre]).grid(row = int((i+2)/3), column = (i-1) %3)
            i = i+1
       self.submit = Button(self.master, text="Submit", width=10, command=self.fillPlaylist)
       self.submit.grid()
       self.createEntries()
    def createEntries(self):
         self.fields = {}
         self.options = ["danceability","energy", "valence", "popularity", "mode"]
         for i in range(len(self.options)):
           print(self.options[i])
           self.fields[self.options[i]] = []
           self.label = Label(self.master, text=self.options[i])
           self.label.grid(row = i, column = 5)
           min = StringVar()
           Entry(self.master, text=self.options[i], textvariable = min).grid(row = i, column = 6)
           max = StringVar()
           Entry(self.master, text=self.options[i], textvariable = max).grid(row = i, column = 7)
           self.fields[self.options[i]].append(min)
           self.fields[self.options[i]].append(max)
         print(self.fields)
    def getSeededTracks(self):
      query = "https://api.spotify.com/v1/recommendations?{}".format(self.buildQuery())
      print(query)
      response = requests.get(
          query,
           headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
             )
      response_json = response.json()
      print(response_json)
      tracks = response_json['tracks']
      uris = []
      for item in tracks:
         uris.append(item['uri'])
      trackString = ""
      tracks = self.getSeededTracks()
      for item in tracks:
          trackString = trackString + item + "%2C"
      trackString = trackStringg[:-3]
      while len(uris) < range(100):
          query = "https://api.spotify.com/v1/recommendations?seed_tracks={}&{}".format(trackString, self.buildQuery())
          print(query)
          response = requests.get(
           query,
           headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
              )
          response_json = response.json()
          print(response_json)
          tracks = response_json['tracks']
          for item in tracks:
            uris.append(item['uri'])
      return uris
    def readGenres(self):
        file1 = open("genres.txt","r+")  
        file = file1.readlines() 
        returnval = {}
        for line in file:
            returnval[line[:-1]] =0
        return returnval
    def getSelectedGenres(self):
        string = ""
        for item in self.genres:
            if self.genres[item].get():
                string = string + str(item) + "%2C"
        print(string [:-3])
        return "seed_genres=" + string [:-3]
    def getTuneables(self):
        self.sTuneables = []
        for item in self.options:
            x = self.fields[item]
            if x[0].get() != "" and x[1].get() != "":
                self.sTuneables.append("min_" + item + "=" + x[0].get())
                self.sTuneables.append("max_" + item + "=" + x[1].get())
        return self.sTuneables
    def buildQuery(self):
        string = self.getSelectedGenres()
        x =  self.getTuneables()
        print(x)
        for item in x:
            string = string + "&" + item
        return string
    def makePlaylist(self):
        request_body = json.dumps({
            "name": "TEST",
            "description": "you tried",
            "public": False
        })
        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
        response = requests.post(
                query,
                data = request_body,
                headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
         )
        response_json = response.json()
        id = response_json["id"]    
        return id
    def fillPlaylist(self):
        uris = ""
        tracks = self.getSeededTracks()
        for item in tracks:
            uris = uris + item + "%2C"
        uris = uris[:-3]
        print(uris)
        id = "5RTA0ewYsJ7rpXKMpqQPY6"
        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(id, uris)
        response = requests.post(
                query,
                headers={"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
         )
        print(response.json())
    


#root = Tk()
#gui = PlaylistAnalyzer(root)
#gui.getPlaylists("summer")
#root.mainloop()