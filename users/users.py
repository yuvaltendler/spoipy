import logging

from exeptions.exeptions import passedPlaylistsAssignment, passSongsInPlaylistAssignment, playlistAlradyExist
from music import Artist
from singleton import Singleton


# class UserBuilder:
#     @staticmethod
#     def sign_up():
#         pass

class FreeUser():
    MAX_PLAYLISTS = 5
    MAX_SONGS_IN_PLAYLIST = 20

    def __init__(self):
        self.playlists = {}

    def add_playlist(self, name: str, playlist):
        if len(self.playlists) >= FreeUser.MAX_PLAYLISTS:
            logging.warning('User try to add more then %d playlist', FreeUser.MAX_PLAYLISTS)
            raise passedPlaylistsAssignment()
        elif len(playlist) > FreeUser.MAX_SONGS_IN_PLAYLIST:
            logging.warning('User try to add playlist that bigger then %d', FreeUser.MAX_SONGS_IN_PLAYLIST)
            raise passSongsInPlaylistAssignment()
        elif name in self.playlists:
            logging.warning('User try to add 2 playlists with the same name')
            raise playlistAlradyExist()
        else:
            self.playlists[name] = playlist


class PremiumUser(FreeUser):
    def __init__(self):
        super().__init__()

    def add_playlist(self, name: str, playlist):
        if name in self.playlists:
            logging.warning('User try to add 2 playlists with the same name')
            raise playlistAlradyExist()
        else:
            self.playlists[name] = playlist


class ArtistUser(PremiumUser):
    def __init__(self, artist: Artist):
        super().__init__()
        self.artist = artist



class UserManager(metaclass=Singleton):
    def __init__(self, users: {str: FreeUser} = {}):
        self.users = users
