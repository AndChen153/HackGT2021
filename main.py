# main.py "insert query" "insert playlist size"

from components import addSongs, createPlaylist, findPlaylists, parsePlaylists
import sys

add = addSongs.AddSongs()
create = createPlaylist.CreatePlaylist()
find = findPlaylists.FindPlaylists()
parse = parsePlaylists.ParsePlaylists()

# query = input("search term: ")
query = sys.argv[1]
query = query.lower()
# playlistSize = int(input("playlist size: "))
playlistSize = sys.argv[2]


create.createPlaylist(query)
songList = parse.sortTracks(find.findPlaylists(query), playlistSize)
# print(query, playlistSize)
print(add.addSongList(songList, query, playlistSize))





