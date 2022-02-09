from music import Artist, ArtistManager, Album, Song

# def limit_search(func):
#     def get_do_limit(do_limit: bool = False):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             if do_limit:
#                 return res[:Search.MUX_RESULTS]
#             return res
#         return wrapper
#     return get_do_limit

class Search:
    MUX_RESULTS = 5

    # @limit_search
    @staticmethod
    def get_artists() -> {Artist}:
        return ArtistManager().artists.values()

    @staticmethod
    def get_albums(artist_id: str) -> {Album}:
        return ArtistManager().artists[artist_id].albums.values()

    @staticmethod
    def get_songs_in_album(album_id: str) -> {Song}:
        for artist in ArtistManager().artists.values():
            if album_id in artist.albums:
                return artist.albums[album_id].songs.values()

    @staticmethod
    def get_beast_songs(artist_id: str, num_of_results: int = 10) -> [Song]:
        songs = []
        for album in Search.get_albums(artist_id):
            songs = songs + list(album.songs.values())
        res = sorted(songs, key= lambda song: song.popularity, reverse=True)
        return res[:num_of_results]
