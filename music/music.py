class Artist:
    def __init__(self, name: str, album = []):
        self.name = name
        self.album = album


class ArtistManager:
    def __init__(self, artists: {str: [Artist]} = {}):
        self.artists = artists
