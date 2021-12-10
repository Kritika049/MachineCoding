class User(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.friends = []
        self.followers = []
        self.following = []

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setFriends(self, friends):
        self.friends = friends

    def getFriends(self):
        return self.friends

    def setFollowers(self, followers):
        self.followers = followers

    def getFollowers(self):
        return self.followers

    def setFollowing(self, following):
        self.following = following

    def getFollowing(self):
        return self.following
