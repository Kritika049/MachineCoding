import abc


class playlistServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addPlaylist(self, id, userId, name, songs):
        pass

    def addSongToPlaylist(self, songId, playlistId):
        pass

    def showPlaylist(self, playlistId):
        pass
    
    def showOtherPlaylist(self, user1Id, user2Id, playlist2Id):
        pass
