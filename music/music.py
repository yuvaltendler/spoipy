from singleton import Singleton


class Song:
    def __init__(self, name: str, popularity: int):
        self.name = name
        self.popularity = popularity

    def __eq__(self, other):
        return self.name == other.name and \
               self.popularity == other.popularity


class Album:
    def __init__(self, name: str, songs: {str: Song} = {}):
        self.name = name
        self.songs = {}  # songs


class Artist:
    def __init__(self, name: str, albums: {str, Album} = {}):
        self.name = name
        self.albums = {}  # albums


class ArtistManager(metaclass=Singleton):
    def __init__(self, artists: {str: Artist} = {}):
        self.artists = artists
