class Album:
    def __init__(self, name: str, songs={}):
        self.name = name
        self.songs = {}


class Artist:
    def __init__(self, name: str, album: {str, Album} = {}):
        self.name = name
        self.album = album


class ArtistManager:
    def __init__(self, artists: {str: Artist} = {}):
        self.artists = artists
