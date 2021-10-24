# main.py "insert query" "insert playlist size"
from components import AddSongs, CreatePlaylist, FindPlaylists, ParsePlaylists
import sys

def createPlaylist(key, playlistSize):  
    add = AddSongs.AddSongs()
    create = CreatePlaylist.CreatePlaylist()
    find = FindPlaylists.FindPlaylists()
    parse = ParsePlaylists.ParsePlaylists()

    query = key
    # query = query.capitalize()

    create.createPlaylist(query)
    songList = parse.sortTracks(find.findPlaylists(query), playlistSize)
    return add.addSongList(songList, query, playlistSize)
  #  urllib.urlopen(add.addSongList(songList, query, playlistSize))






