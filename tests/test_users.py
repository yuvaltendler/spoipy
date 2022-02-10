from unittest import TestCase

from exception.exception import PlaylistAlreadyExist, PassSongsInPlaylistAssignment, PassedPlaylistsAssignment
from users.users import FreeUser


class TestFreeUser(TestCase):
    def test_add_playlist(self):
        user = FreeUser()
        user.playlists = {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist'}
        self.assertRaises(PlaylistAlreadyExist, user.add_playlist, 'p3', 'playlist')
        self.assertRaises(PassSongsInPlaylistAssignment, user.add_playlist, 'p8', 'playlistplaylistplaylist')
        user.add_playlist('p5', 'playlist')
        assert user.playlists == {'p1': 'playlist', 'p2': 'playlist', 'p3': 'playlist', 'p4': 'playlist', 'p5': 'playlist'}
        self.assertRaises(PassedPlaylistsAssignment, user.add_playlist, 'p6', 'playlist')

    def test_add_songs_to_playlist(self):
        user = FreeUser()
        user.add_playlist('p1', [])
        self.assertRaises(PassSongsInPlaylistAssignment, user.add_playlist, 'p1', 'playlistplaylistplaylist')

