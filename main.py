from components import addSongs, createPlaylist, findPlaylists, parsePlaylists

add = addSongs.AddSongs()
create = createPlaylist.CreatePlaylist()
find = findPlaylists.FindPlaylists()
parse = parsePlaylists.ParsePlaylists()

while (True):
    query = input("search term: ")
    playlistSize = int(input("playlist size: "))
    create.createPlaylist(query)
    songList = parse.sortTracks(find.findPlaylists(query))
    print(add.addSongList(songList, query))


