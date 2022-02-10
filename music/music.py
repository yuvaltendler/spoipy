from singleton import Singleton


class Song:
    def __init__(self, name: str, popularity: int):
        self.name = name
        self.popularity = popularity

    def __eq__(self, other):
        return self.name == other.name and \
               self.popularity == other.popularity

    def  __repr__(self):
        return f'(name = {self.name}, popularity = {self.popularity})'


class Album:
    def __init__(self, name: str, songs=None):
        if songs is None:
            songs = {}
        self.name = name
        self.songs = songs


class Artist:
    def __init__(self, name: str, albums=None):
        if albums is None:
            albums = {}
        self.name = name
        self.albums = albums


class ArtistManager(metaclass=Singleton):
    def __init__(self, artists=None):
        if artists is None:
            artists = {}
        self.artists = artists
