from music_recommender.services.playlist_service_interface import playlistServiceInterface
from music_recommender.models.playlist import Playlist


class playlistService(playlistServiceInterface):
    playlistDetails = {}

    def addPlaylist(self, id, userId, name, songs):
        playlist = Playlist()
        playlist.setId(id)
        playlist.setUserId(userId)
        playlist.setName(name)
        playlist.setSongs(songs)

        self.__class__.playlistDetails[id] = playlist
        return playlist


        
        

