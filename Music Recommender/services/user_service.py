from music_recommender.services.user_service_interface import userServiceInterface
from music_recommender.models.user import User


class userService(userServiceInterface):
    userDetails = {}

    def addUser(self, id, name):
        user = User()
        user.setId(id)
        user.setName(name)

        self.__class__.userDetails[id] = user
        return user
