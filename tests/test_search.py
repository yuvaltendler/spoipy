from unittest import TestCase

from load import LoadMusic
from music import Artist, Album
from search.search import Search


class TestSearch(TestCase):
    def test_get_artists(self):
        LoadMusic.load_music("C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks")
        res = Search.get_artists()
        assert all(isinstance(x, Artist) for x in res)
        # assert len(Search.get_artists(do_limit = True)) == Search.MUX_RESULTS

    def test_get_albums(self):
        LoadMusic.load_music("C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks")
        res = Search.get_albums('2l6M7GaS9x3rZOX6nDX3CM')
        assert all(isinstance(x, Album) for x in res)
