from services.playlist_service_interface import playlistServiceInterface
from models.playlist import Playlist
from services.user_service import userService
from services.exception import PlaylistNotFoundError


class playlistService(playlistServiceInterface):
    playlistDetails = {}

    def addPlaylist(self, id, userId, name, songs):
        playlist = Playlist()
        playlist.setId(id)
        playlist.setUserId(userId)
        playlist.setName(name)
        playlist.setSongs(songs)

        self.__class__.playlistDetails[id] = playlist
        return playlist

    def addSongToPlaylist(self, songId, playlistId):
        playlist = self.__class__.playlistDetails[playlistId]
        playlist.getSongs().append(songId)
        return playlist

    def showPlaylist(self, playlistId):
        playlist = self.__class__.playlistDetails[playlistId]
        songs = playlist.getSongs()
        return songs

    def showOtherPlaylist(self, user1Id, user2Id, playlist2Id):
        user1 = userService.userDetails.get(user1Id)
        user2 = userService.userDetails.get(user2Id)

        if (user1Id in user2.getFriends()) or (user1Id in user2.getFollowers()):
            return self.showPlaylist(playlist2Id)

        else:
            raise PlaylistNotFoundError('error')
