import abc


class userServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addUser(self, id, name):
        pass

    @abc.abstractmethod
    def addFriend(self, user1Id, user2Id):
        pass

    @abc.abstractmethod
    def followUser(self, user1Id, user2Id):
        pass
