class playlistController(object):
    def __init__(self, songsService, playlistService):
        self.playlistService = playlistService
        self.songsService = songsService

    def addPlaylist(self, id, userId, name, songs):
        return self.playlistService.addPlaylist(id, userId, name, songs)

    def addSongToPlaylist(self, songId, playlistId):
        playlist = self.playlistService.playlistDetails.get(playlistId)
        #song = self.songsService.songsDetails.get(songId)
        playlist.getSongs().append(songId)
        return playlist
