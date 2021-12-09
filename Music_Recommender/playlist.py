class Playlist(object):
    def __init__(self):
        self.id = None
        self.UserId = None
        self.name = None
        self.songs = []

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setUserId(self, UserId):
        self.UserId = UserId

    def getUserId(self):
        return self.UserId

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSongs(self, songs):
        self.songs = songs

    def getSongs(self):
        return self.songs
