import abc


class songsServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addSong(self, id, name, singer, genre, tempo):
        pass