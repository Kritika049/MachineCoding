from music_recommender.services.songs_service_interface import songsServiceInterface
from music_recommender.models.songs import Songs
from music_recommender.services.playlist_service import playlistService


class songsService(songsServiceInterface):
    songsDetails = {}

    def addSong(self, id, name, singer, genre, tempo):
        song = Songs()
        song.setId(id)
        song.setName(name)
        song.setSinger(singer)
        song.setGenre(genre)
        song.setTempo(tempo)

        self.__class__.songsDetails[id] = song
        return song

    def recommend_songs(self, userId):
        recommendation = {}
        user_songs = []
        rec_songs = []

        for playlistId in playlistService.playlistDetails:
            playlist = playlistService.playlistDetails.get(playlistId)

            if userId in playlist.getUserId():
                songs = playlist.getSongs()
                for song in songs:
                    user_songs.append(song)

        for song in self.__class__.songsDetails:
            if song not in user_songs:
                rec_songs.append(song)

        for songrecId in rec_songs:
            for songId in user_songs:
                song = self.__class__.songsDetails[songId]
                songrec = self.__class__.songsDetails[songrecId]

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
