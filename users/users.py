import logging

from music import Artist
from singleton import Singleton


# class UserBuilder:
#     @staticmethod
#     def sign_up():
#         pass

class FreeUser():
    MAX_PLAYLISTS = 5

    def __init__(self):
        self.playlists = {}

    def add_playlist(self, name: str, playlist):
        if len(self.playlists) >= FreeUser.MAX_PLAYLISTS:
            logging.warning('User try to add more then %d playlist', FreeUser.MAX_PLAYLISTS)
            # TODO raise error
        elif name in self.playlists:
            logging.warning('User try to add 2 playlists with the same name')
            # TODO raise error
        else:
            self.playlists[name] = playlist


class PremiumUser(FreeUser):
    def __init__(self):
        super().__init__()

    def add_playlist(self, name: str, playlist):
        if name in self.playlists:
            logging.warning('User try to add 2 playlists with the same name')
            # TODO raise error
        else:
            self.playlists[name] = playlist


class ArtistUser(PremiumUser):
    def __init__(self, artist: Artist):
        super().__init__()
        self.artist = artist



class UserManager(metaclass=Singleton):
    def __init__(self, users: {str: FreeUser} = {}):
        self.users = users
