from singleton import Singleton


class FreeUser():
    def __init__(self, playlists={}):
        self.playlists = playlists


class PremiumUser(FreeUser):
    def __init__(self, playlists={}):
        super().__init__(playlists)


class UserManager(metaclass=Singleton):
    def __init__(self):
        self.users = {}
