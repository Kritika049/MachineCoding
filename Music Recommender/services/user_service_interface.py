import abc


class userServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addUser(self, id, name):
        pass

    def addUser(self, userId1, userId2):
        pass
