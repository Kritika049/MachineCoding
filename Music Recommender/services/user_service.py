from services.user_service_interface import userServiceInterface
from models.user import User


class userService(userServiceInterface):
    userDetails = {}

    def addUser(self, id, name):
        user = User()
        user.setId(id)
        user.setName(name)

        self.__class__.userDetails[id] = user
        return user

    def addFriend(self, user1Id, user2Id):
        user1 = self.__class__.userDetails[user1Id]
        user2 = self.__class__.userDetails[user2Id]
        user1.getFriends().append(user2Id)
        user2.getFriends().append(user1Id)
        return user1, user2

    def followUser(self, user1Id, user2Id):
        user1 = self.__class__.userDetails[user1Id]
        user2 = self.__class__.userDetails[user2Id]
        user1.getFollowing().append(user2Id)
        user2.getFollowers().append(user1Id)
        return user1, user2
