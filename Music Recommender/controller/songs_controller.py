class songsController(object):
    def __init__(self, songsService, playlistService):
        self.songsService = songsService
        self.playlistService = playlistService

    def addSong(self, id, name, singer, genre, tempo):
        return self.songsService.addSong(id, name, singer, genre, tempo)

    def recommend_songs(self, userId):
        recommendation = {}
        user_songs = []
        rec_songs = []

        for playlistId in self.playlistService.playlistDetails:
            playlist = self.playlistService.playlistDetails.get(playlistId)

            if userId in playlist.getUserId():
                songs = playlist.getSongs()
                for song in songs:
                    user_songs.append(song)

        for song in self.songsService.songsDetails:
            if song not in user_songs:
                rec_songs.append(song)

        for songrecId in rec_songs:
            for songId in user_songs:
                song = self.songsService.songsDetails.get(songId)
                songrec = self.songsService.songsDetails.get(songrecId)

                if (song.getTempo() == songrec.getTempo() and
                        song.getSinger() == songrec.getSinger() and
                        song.getGenre() == songrec.getGenre()):
                    recommendation[songrecId] = 1

                elif ((song.getTempo() == songrec.getTempo()
                       and song.getSinger() == songrec.getSinger()) or
                      (song.getTempo() == songrec.getTempo()
                       and song.getGenre() == songrec.getGenre()) or
                      (song.getSinger() == songrec.getSinger()
                       and song.getGenre() == songrec.getGenre())):
                    recommendation[songrecId] = 2

                elif (song.getTempo() == songrec.getTempo() or
                        song.getSinger() == songrec.getSinger() or
                        song.getGenre() == songrec.getGenre()):
                    if (songrecId not in recommendation):
                        recommendation[songrecId] = 3

        final_rec = dict(sorted(recommendation.items(), key=lambda x: x[1]))
        return final_rec
