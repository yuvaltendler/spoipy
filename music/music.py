from singleton import Singleton


class Song:
    def __init__(self, name: str, popularity: int):
        self.name = name
        self.popularity = popularity


class Album:
    def __init__(self, name: str, songs: {str: Song} = {}):
        self.name = name
        self.songs = songs


class Artist:
    def __init__(self, name: str, album: {str, Album} = {}):
        self.name = name
        self.album = album


class ArtistManager(metaclass=Singleton):
    def __init__(self, artists: {str: Artist} = {}):
        self.artists = artists
