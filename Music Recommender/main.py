
from services.user_service import userService
from services.playlist_service import playlistService
from services.songs_service import songsService
from services.exception import PlaylistNotFoundError

UserService = userService()
SongsService = songsService()
PlaylistService = playlistService()

user_1 = UserService.addUser('user1', 'hun')
user_2 = UserService.addUser('user2', 'jik')
song_1 = SongsService.addSong('song1', 'xxy', 'AB', 'Folk', 60)
song_2 = SongsService.addSong('song2', 'abc', 'DEF', 'Rock', 70)
song_3 = SongsService.addSong('song3', 'def', 'AB', 'Country', 55)
song_4 = SongsService.addSong('song4', 'ghi', 'XYZ', 'Rock', 60)
song_5 = SongsService.addSong('song5', 'klm', 'XYZ', 'Rock', 75)
song_6 = SongsService.addSong('song6', 'vgi', 'AB', 'Country', 60)
song_7 = SongsService.addSong('song7', 'lok', 'DEF', 'Indie', 55)
song_8 = SongsService.addSong('song8', 'mkl', 'AB', 'Folk', 60)
song_9 = SongsService.addSong('song9', 'lok', 'CD', 'Rock', 50)

my_playlist = PlaylistService.addPlaylist(
    'playlist1', 'user1', 'my_first', ['song1', 'song2', 'song3'])

my_playlist2 = PlaylistService.addPlaylist(
    'playlist2', 'user2', 'my_second', ['song3', 'song4', 'song7'])

PlaylistService.addSongToPlaylist('song4', 'playlist1')

print(PlaylistService.showPlaylist('playlist2'))
print(SongsService.getRecommendations('user1'))

# UserService.addFriend('user1','user2')
UserService.followUser('user1', 'user2')
print(user_1.getFollowing())
print(user_2.getFollowers())

try:
    songs = PlaylistService.showOtherPlaylist('user1', 'user2', 'playlist2')
    print(songs)
except PlaylistNotFoundError as e:
    print(e)
