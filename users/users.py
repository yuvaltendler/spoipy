import logging

from exception.user_exception import PassedPlaylistsAssignment, PassSongsInPlaylistAssignment, PlaylistAlreadyExist
from music import Artist, Song
from properties import Properties
from singleton import Singleton


# class UserBuilder:
#     @staticmethod
#     def sign_up():
#         pass

class FreeUser():

    def __init__(self):
        self.playlists = {}

    def add_playlist(self, name: str, playlist: [Song]):
        if len(self.playlists) >=  Properties().properties.get('FREE_USER_LIMIT_PLAYLISTS'):
            logging.warning('User try to add more then %d playlist', Properties().properties.get('FREE_USER_LIMIT_PLAYLISTS'))
            raise PassedPlaylistsAssignment()
        elif len(playlist) > Properties().properties.get('FREE_USER_LIMIT_SONGS_IN_PLAYLIST'):
            logging.warning('User try to add playlist that bigger then %d', Properties().properties.get('FREE_USER_LIMIT_SONGS_IN_PLAYLIST'))
            raise PassSongsInPlaylistAssignment()
        elif name in self.playlists:
            logging.warning('User try to add 2 playlists with the same name')
            raise PlaylistAlreadyExist()
        else:
            self.playlists[name] = playlist

    def add_songs_to_playlist(self, playlist_name: str, songs: [Song]):
        if playlist_name not in self.playlists:
            self.add_playlist(playlist_name, songs)
            return
        playlist = self.playlists[playlist_name]
        if len(playlist) + len(songs) > Properties().properties.get('FREE_USER_LIMIT_SONGS_IN_PLAYLIST'):
            logging.warning('User try to add playlist that bigger then %d', Properties().properties.get('FREE_USER_LIMIT_SONGS_IN_PLAYLIST'))
            raise PassSongsInPlaylistAssignment()
        self.playlists[playlist_name] = playlist + songs

class PremiumUser(FreeUser):
    def __init__(self):
        super().__init__()

    def add_playlist(self, name: str, playlist):
        if name in self.playlists:
            logging.warning('User try to add 2 playlists with the same name')
            raise PlaylistAlreadyExist()
        else:
            self.playlists[name] = playlist

    def add_songs_to_playlist(self, playlist_name: str, songs: [Song]):
        if playlist_name not in self.playlists:
            self.add_playlist(playlist_name, songs)
            return
        self.playlists[playlist_name] = self.playlists[playlist_name] + songs


class ArtistUser(PremiumUser):
    def __init__(self, artist: Artist):
        super().__init__()
        self.artist = artist



class UserManager(metaclass=Singleton):
    def __init__(self, users: {str: FreeUser} = {}):
        self.users = users
