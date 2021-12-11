import abc


class playlistServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addPlaylist(self, id, userId, name, songs):
        pass

    @abc.abstractmethod
    def addSongToPlaylist(self, songId, playlistId):
        pass

    @abc.abstractmethod
    def showPlaylist(self, playlistId):
        pass

    @abc.abstractmethod
    def showOtherPlaylist(self, user1Id, user2Id, playlist2Id):
        pass
