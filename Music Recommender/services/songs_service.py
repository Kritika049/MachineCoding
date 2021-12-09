from music_recommender.services.songs_service_interface import songsServiceInterface
from music_recommender.models.songs import Songs


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
