import abc


class playlistServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addPlaylist(self, id, userId, name, songs):
        pass

