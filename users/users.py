from singleton import Singleton


class FreeUser():
    def __init__(self, playlists = {}):
        self.playlists = playlists

class UserManager(metaclass=Singleton):
    def __init__(self):
        self.users = {}
