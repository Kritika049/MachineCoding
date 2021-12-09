import sys
sys.path.append('/Users/khush')
from music_recommender.services.songs_service import songsService
from music_recommender.services.playlist_service import playlistService
from music_recommender.services.user_service import userService

UserService = userService()
SongsService = songsService()
PlaylistService = playlistService()

user1 = UserService.addUser('user1', 'hun')
song_1 = SongsService.addSong('song1', 'xxy', 'AB', 'Folk', 60)
song_2 = SongsService.addSong('song2', 'abc', 'DEF', 'Rock', 70)
song_3 = SongsService.addSong('song3', 'def', 'AB', 'Country', 55)
song_4 = SongsService.addSong('song4', 'ghi', 'XYZ', 'Rock', 60)
song_5 = SongsService.addSong('song5', 'klm', 'XYZ', 'Rock', 75)
song_6 = SongsService.addSong('song6', 'vgi', 'AB', 'Country', 60)
song_7 = SongsService.addSong('song7', 'lok', 'DEF', 'Indie', 55)
song_8 = SongsService.addSong('song8', 'mkl', 'AB', 'Folk', 60)
my_playlist = PlaylistService.addPlaylist(
    'playlist1', 'user1', 'my_first', ['song1', 'song2', 'song3'])

PlaylistService.addSongToPlaylist('song4', 'playlist1')

# print(my_playlist.getSongs())
print(SongsService.recommend_song('user1'))
