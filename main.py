# main.py "insert query" "insert playlist size"
from components import AddSongs, CreatePlaylist, FindPlaylists, ParsePlaylists
import sys
import webbrowser

def createPlaylist(key, playlistSize):  
    add = AddSongs.AddSongs()
    create = CreatePlaylist.CreatePlaylist()
    find = FindPlaylists.FindPlaylists()
    parse = ParsePlaylists.ParsePlaylists()

    query = key
    # query = query.capitalize()

    create.createPlaylist(query)
    songList = parse.sortTracks(find.findPlaylists(query), playlistSize)
    webbrowser.open(add.addSongList(songList, query, playlistSize))
    return "Your content has been loaded on a new page"
  #  urllib.urlopen(add.addSongList(songList, query, playlistSize))

# createPlaylist("hype", 50)





