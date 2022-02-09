from unittest import TestCase

from load.load_music import LoadMusic
from music import ArtistManager


class TestLoadMusic(TestCase):
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
