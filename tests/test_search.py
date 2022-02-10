from unittest import TestCase

from load import LoadMusic
from music import Artist, Album, Song
from properties import Properties
from search.search import Search


class TestSearch(TestCase):
    def test_get_artists(self):
        LoadMusic.load_music("C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks")
        res = Search.get_artists()
        assert all(isinstance(x, Artist) for x in res)
        #assert len(Search.get_artists(do_limit = True)) == Search.MUX_RESULTS

    def test_get_albums(self):
        LoadMusic.load_music("C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks")
        res = Search.get_albums('2l6M7GaS9x3rZOX6nDX3CM')
        assert all(isinstance(x, Album) for x in res)

    def test_get_songs_in_album(self):
        LoadMusic.load_music("C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks")
        res = Search.get_songs_in_album('2D78QqxtzgUukykeWwntPs')
        assert list(res) == [Song('נערי שובה אלי', 39)]

    def test_get_song(self):
        LoadMusic.load_music("C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks")
        res = Search.get_song('1yjY7rpaAQvKwpdUliHx0d')
        assert res == Song('Still into You', 83)

    def test_get_beast_songs(self):
        LoadMusic.load_music("C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks")
        res = Search.get_beast_songs('2l6M7GaS9x3rZOX6nDX3CM')
        assert res == [Song('נערי שובה אלי', 39), Song('אז מה', 34)]

    def test_limit(self):
        LoadMusic.load_music("C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks")
        res = Search.limit(Search.get_artists())
        assert len(res) == Properties().properties.get('FREE_USER_LIMIT_SEARCH_RESULT')
