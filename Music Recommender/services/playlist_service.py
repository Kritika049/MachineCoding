from music_recommender.services.playlist_service_interface import playlistServiceInterface
from music_recommender.models.playlist import Playlist
from music_recommender.services.user_service import userService


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
        return print(playlist.getSongs())
    
    def showOtherPlaylist(self, user1Id, user2Id, playlist2Id):
        user1 = userService.userDetails.get(user1Id)
        user2 = userService.userDetails.get(user2Id)

        if (user1Id in user2.getFriends()) or (user1Id in user2.getFollowers()):
            playlist = self.__class__.playlistDetails[playlist2Id]
            return print(playlist.getSongs())
    

        
        
