from unittest import TestCase

from users.users import FreeUser


class TestFreeUser(TestCase):
    def test_add_playlist(self):
        user = FreeUser()
        user.playlists = {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist'}
        user.add_playlist('p3', 'playlist')
        assert user.playlists == {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist'}
        user.add_playlist('p8', 'playlistplaylistplaylist')
        assert user.playlists == {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist'}
        user.add_playlist('p5', 'playlist')
        assert user.playlists == {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist', 'p5': 'playlist'}
        user.add_playlist('p6', 'playlist')
        assert user.playlists == {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist', 'p5': 'playlist'}

