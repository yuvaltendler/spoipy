from unittest import TestCase

from exeptions.exeptions import playlistAlradyExist, passSongsInPlaylistAssignment, passedPlaylistsAssignment
from users.users import FreeUser


class TestFreeUser(TestCase):
    def test_add_playlist(self):
        user = FreeUser()
        user.playlists = {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist'}
        self.assertRaises(playlistAlradyExist, user.add_playlist, 'p3', 'playlist')
        self.assertRaises(passSongsInPlaylistAssignment, user.add_playlist, 'p8', 'playlistplaylistplaylist')
        user.add_playlist('p5', 'playlist')
        assert user.playlists == {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist', 'p5': 'playlist'}
        self.assertRaises(passedPlaylistsAssignment, user.add_playlist, 'p6', 'playlist')
