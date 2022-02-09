from music import Artist, ArtistManager, Album


class Search:
    MUX_RESULTS = 5
    @staticmethod
    def limit_search(func):
        def limit_search(do_limit: bool = False, *args, **kwargs):
            res = func(*args, **kwargs)
            if do_limit:
                return res[:Search.MUX_RESULTS]
            return res
        return limit_search

    # @limit_search
    @staticmethod
    def get_artists():
        return ArtistManager().artists.values()

    @staticmethod
    def get_albums(artist_id) -> {Album}:
        return ArtistManager().artists[artist_id].albums.values()
