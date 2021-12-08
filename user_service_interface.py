import abc
class userServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addUser(self,id,name):
        pass