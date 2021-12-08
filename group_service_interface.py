import abc
class groupServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addGroup(self,id,name,members):
        pass
        