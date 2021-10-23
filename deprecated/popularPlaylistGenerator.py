import requests
import json
from secrets import *

def get_lists():
    
    query = "https://api.spotify.com/v1/search?q={}&type=playlist&market=US".format("summer")
    print(query)
    response = requests.get(         
        query,
           headers = {"Content-Type":"application/json", "Authorization":"Bearer {}".format(spotify_token)}
             )
    response_json = response.json()
    print(response_json)

def get_songs():
    pass

def get_common():
    pass

#get_lists()