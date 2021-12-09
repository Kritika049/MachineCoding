import sys
sys.path.append('/Users/khush')
from music_recommender.controllers.user_controller import userController
from music_recommender.controllers.playlist_controller import playlistController
from music_recommender.controllers.songs_controller import songsController
from music_recommender.services.user_service import userService
from music_recommender.services.playlist_service import playlistService
from music_recommender.services.songs_service import songsService

UserController = userController(userService())
PlaylistController = playlistController(songsService(), playlistService())
SongsController = songsController(songsService(), playlistService())

user1 = UserController.addUser('user1', 'hun')
song_1 = SongsController.addSong('song1', 'xxy', 'AB', 'Folk', 60)
song_2 = SongsController.addSong('song2', 'abc', 'DEF', 'Rock', 70)
song_3 = SongsController.addSong('song3', 'def', 'AB', 'Country', 55)
song_4 = SongsController.addSong('song4', 'ghi', 'XYZ', 'Rock', 60)
song_5 = SongsController.addSong('song5', 'klm', 'XYZ', 'Rock', 75)
song_6 = SongsController.addSong('song6', 'vgi', 'AB', 'Country', 60)
song_7 = SongsController.addSong('song7', 'lok', 'DEF', 'Indie', 55)
song_8 = SongsController.addSong('song8', 'mkl', 'AB', 'Folk', 60)

my_playlist = PlaylistController.addPlaylist(
    'playlist1', 'user1', 'my_first', ['song1', 'song2', 'song3'])

PlaylistController.addSongToPlaylist('song4', 'playlist1')

# print(my_playlist.getSongs())
print(SongsController.recommend_songs('user1'))
