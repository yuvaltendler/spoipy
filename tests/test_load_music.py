from unittest import TestCase

from load.load_music import LoadMusic
from music import ArtistManager


class TestLoadMusic(TestCase):
    def test_load_music(self):
        LoadMusic.load_music('C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks')

        artist = ArtistManager().artists['74XFHRwlV6OrjEM0A2NCMF']
        assert artist.name == 'Paramore'
        album = artist.albums['4sgYpkIASM1jVlNC8Wp9oF']
        assert album.name == 'Paramore'
        song = album.songs['1yjY7rpaAQvKwpdUliHx0d']
        assert song.name == 'Still into You'
        assert song.popularity == 83

        artist = ArtistManager().artists['2l6M7GaS9x3rZOX6nDX3CM']
        assert artist.name == 'Margalit Tzan\'ani'
        album = artist.albums['2D78QqxtzgUukykeWwntPs']
        assert album.name == 'נערי שובה אלי'
        song = album.songs['3o863oLzV4qj53EBCtEAqz']
        assert song.name == 'נערי שובה אלי'
        assert song.popularity == 39
        album = artist.albums['5DvWThv9KXSsyZPDyozM49']
        assert album.name == '\u05d2\u05dc\u05d4 \u05dc\u05d9'
        song = album.songs['03DcpryHcONqKi2uKXK5Ow']
        assert song.name == '\u05d0\u05d6 \u05de\u05d4'
        assert song.popularity == 34

    def test__load_track(self):
        path = 'C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks\\song_1yjY7rpaAQvKwpdUliHx0d.json'
        LoadMusic._load_track(path)
        artist = ArtistManager().artists['74XFHRwlV6OrjEM0A2NCMF']
        assert artist.name == 'Paramore'
        album = artist.albums['4sgYpkIASM1jVlNC8Wp9oF']
        assert album.name == 'Paramore'
        song = album.songs['1yjY7rpaAQvKwpdUliHx0d']
        assert song.name == 'Still into You'
        assert song.popularity == 83
