class Songs(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.singer = None
        self.genre = None
        self.tempo = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSinger(self, singer):
        self.singer = singer

    def getSinger(self):
        return self.singer

    def setGenre(self, genre):
        self.genre = genre

    def getGenre(self):
        return self.genre

    def setTempo(self, tempo):
        self.tempo = tempo

    def getTempo(self):
        return self.tempo
