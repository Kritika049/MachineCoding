from typing import Set
from services.songs_service_interface import songsServiceInterface
from models.songs import Songs
from services.playlist_service import playlistService


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

    # store user playlist and attributes of playlist songs to decide the order of preference

    def createUserPreference(self, userId):

        user_playlist = []
        order_attributes = {}
        preference_attributes = []

        for playlistId in playlistService.playlistDetails:
            playlist = playlistService.playlistDetails.get(playlistId)

            if userId in playlist.getUserId():
                user_songs = playlist.getSongs()
                for songId in user_songs:
                    song = self.__class__.songsDetails[songId]
                    user_playlist.append(songId)

                    if song.getGenre() not in order_attributes:
                        order_attributes[song.getGenre()] = 0
                    order_attributes[song.getGenre()] += 1

                    if song.getTempo() not in order_attributes:
                        order_attributes[song.getTempo()] = 0
                    order_attributes[song.getTempo()] += 1

                    if song.getSinger() not in order_attributes:
                        order_attributes[song.getSinger()] = 0
                    order_attributes[song.getSinger()] += 1

                    preference_attributes.append(song.getGenre())
                    preference_attributes.append(song.getTempo())
                    preference_attributes.append(song.getSinger())

        for songId in self.__class__.songsDetails:
            song = self.__class__.songsDetails[songId]
            if song.getGenre() not in order_attributes:
                order_attributes[song.getGenre()] = 0

            if song.getTempo() not in order_attributes:
                order_attributes[song.getTempo()] = 0

            if song.getSinger() not in order_attributes:
                order_attributes[song.getSinger()] = 0

        return user_playlist, order_attributes, preference_attributes

    # get details of all songs in memory

    def allSongAttributes(self):

        genreList = {}
        singerList = {}
        tempoList = {}

        for songId in self.__class__.songsDetails:
            song = self.__class__.songsDetails[songId]

            if song.getGenre() not in genreList:
                genreList[song.getGenre()] = set()
            genreList[song.getGenre()].add(songId)

            if song.getSinger() not in singerList:
                singerList[song.getSinger()] = set()
            singerList[song.getSinger()].add(songId)

            if song.getTempo() not in tempoList:
                tempoList[song.getTempo()] = set()
            tempoList[song.getTempo()].add(songId)

        return genreList, singerList, tempoList

    # get recommendations based on the playlist and order of preferences

    def getRecommendations(self, userId):

        top_recommendation = {}
        second_recommendation = {}
        third_recommendation = {}

        user_playlist, order_attributes, preference_attributes = self.createUserPreference(
            userId)
        genreList, singerList, tempoList = self.allSongAttributes()

        for songId in user_playlist:
            song = self.__class__.songsDetails[songId]

            genreSongs: Set = genreList[song.getGenre()]
            tempoSongs: Set = tempoList[song.getTempo()]
            singerSongs: Set = singerList[song.getSinger()]

            first_recommendation: Set = genreSongs.intersection(
                tempoSongs).intersection(singerSongs)

            two_recommendation: Set = (genreSongs.intersection(
                tempoSongs)).union(genreSongs.intersection(singerSongs)).union(singerSongs.intersection(tempoSongs))

            three_recommendation: Set = genreSongs.union(
                singerSongs).union(tempoSongs)

            top_recommendation.update(dict.fromkeys(first_recommendation))

            second_recommendation.update(dict.fromkeys(two_recommendation))

            third_recommendation.update(dict.fromkeys(three_recommendation))

        recommend_ids = []
        temp_sec = {}
        final_rec = []
        for id in top_recommendation.keys():
            recommend_ids.append(id)
        for id in second_recommendation.keys():
            if (id not in recommend_ids):
                song = self.__class__.songsDetails[id]
                genre = song.getGenre()
                singer = song.getSinger()
                tempo = song.getTempo()
                temp_sec[id] = [order_attributes[genre],
                                order_attributes[singer], order_attributes[tempo]]

        final_temp_sec = dict(
            sorted(temp_sec.items(), key=lambda e: (e[1][0], e[1][1], e[1][2]), reverse=True))

        for id in final_temp_sec.keys():
            recommend_ids.append(id)

        temp_third = {}
        for id in third_recommendation.keys():
            if (id not in recommend_ids):
                song = self.__class__.songsDetails[id]
                genre = song.getGenre()
                singer = song.getSinger()
                tempo = song.getTempo()
                if genre in preference_attributes:
                    temp_third[id] = [1, 0, 0]
                elif singer in preference_attributes:
                    temp_third[id] = [0, 1, 0]
                elif tempo in preference_attributes:
                    temp_third[id] = [0, 0, 1]
                else:
                    temp_third[id] = [0, 0, 0]

        final_temp_third = dict(
            sorted(temp_third.items(), key=lambda e: (e[1][0], e[1][1], e[1][2]), reverse=True))

        for id in final_temp_third.keys():
            recommend_ids.append(id)

        for id in recommend_ids:
            if id not in user_playlist:
                final_rec.append(id)

        return final_rec
