import abc


class songsServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addSong(self, id, name, singer, genre, tempo):
        pass

    @abc.abstractmethod
    def createUserPreference(self, userId):
        pass

    @abc.abstractmethod
    def allSongAttributes(self):
        pass

    @abc.abstractmethod
    def getRecommendations(self, userId):
        pass
