import abc


class userServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addUser(self, id, name):
        pass
    
    def addFriend(self, user1Id, user2Id):
        pass

    def followUser(self, user1Id, user2Id):
        pass

