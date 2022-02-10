import logging

from consolemenu import *
from consolemenu.items import *

from exception.search_exception import AlbumIdDoesNotExist, ArtistIdDoesNotExist, SongIdDoesNotExist
from exception.user_exception import DisconnectedUser, PlaylistAlreadyExist, PassSongsInPlaylistAssignment, \
    PassedPlaylistsAssignment, UserDoesNotExist
from search.search import Search
from singleton import Singleton
from users import UserManager, PremiumUser


class Menu(metaclass=Singleton):
    def __init__(self):
        self.is_free_user = True
        self.username = ''
        self.menu = self._build_menu()

    def _build_menu(self):
        menu = ConsoleMenu('Spotipy', 'Welcome to spotipy')

        search_menu = self._build_search_menu()
        playlist_menu = self._build_playlist_menu()
        search = SubmenuItem('Search', search_menu, menu)
        login = FunctionItem('Login', Menu._login, [self])
        playlist = SubmenuItem('Edit playlist', playlist_menu, menu)

        menu.append_item(login)
        menu.append_item(search)
        menu.append_item(playlist)

        return menu

    def _build_search_menu(self):
        search_menu = ConsoleMenu('Spotipy', 'Search menu')
        get_artists = FunctionItem('Get all artists', Menu._get_artists, [self])
        get_albums = FunctionItem('Get artist\'s albums', Menu._get_albums, [self])
        get_songs_in_album = FunctionItem('Get songs in album', Menu._get_songs_in_album, [self])
        get_beast_songs = FunctionItem('Get beast songs', Menu._get_beast_songs, [self])
        search_menu.append_item(get_artists)
        search_menu.append_item(get_albums)
        search_menu.append_item(get_songs_in_album)
        search_menu.append_item(get_beast_songs)
        return search_menu

    def _build_playlist_menu(self):
        playlist_menu = ConsoleMenu('Spotipy', 'Playlist menu')
        get_playlists = FunctionItem('Get my playlists', Menu._get_playlists, [self])
        create_playlist = FunctionItem('Create playlist', Menu._create_playlist, [self])
        add_song_to_playlist = FunctionItem('Add song to playlist', Menu._add_song_to_playlist, [self])
        playlist_menu.append_item(get_playlists)
        playlist_menu.append_item(create_playlist)
        playlist_menu.append_item(add_song_to_playlist)
        return playlist_menu

    def _get_artists(self):
        if self.is_free_user:
            print([artist.name for artist in Search.limit(Search.get_artists())])
            return
        print([artist.name for artist in Search.get_artists()])

    def _get_albums(self):
        artist_id = input('Enter artist id: ')
        try:
            if self.is_free_user:
                print([album.name for album in Search.limit(Search.get_albums(artist_id))])
                return
            print([album.name for album in Search.get_albums(artist_id)])
        except ArtistIdDoesNotExist as e:
            print(f'Exception: {type(e)} {str(e)}')

    def _get_songs_in_album(self):
        album_id = input('Enter album id: ')
        try:
            if self.is_free_user:
                print([str(song) for song in Search.limit(Search.get_songs_in_album(album_id))])
                return
            print([str(song) for song in Search.get_songs_in_album(album_id)])
        except AlbumIdDoesNotExist as e:
            print(f'Exception: {type(e)} {str(e)}')

    def _get_beast_songs(self):
        artist_id = input('Enter artist id: ')
        try:
            if self.is_free_user:
                print(Search.limit(Search.get_beast_songs(artist_id)))
                return
            print(Search.get_beast_songs(artist_id))
        except ArtistIdDoesNotExist as e:
            print(f'Exception: {type(e)} {str(e)}')

    def _login(self):
        username = input('Username: ')
        # password = getpass()
        try:
            if username not in UserManager().users:
                logging.warning('Try to connect with unknown username')
                raise UserDoesNotExist()
            self.username = username
            self.is_free_user = not isinstance(UserManager().users[username], PremiumUser)
        except UserDoesNotExist as e:
            print(f'Exception: {type(e)} {str(e)}')

    def _get_user(self):
        if self.username == '':
            logging.warning('Disconnected user try to get playlists')
            raise DisconnectedUser()
        if self.username not in UserManager().users:
            logging.warning('Try to get unknown username')
            raise UserDoesNotExist()
        return UserManager().users[self.username]

    def _get_playlists(self):
        try:
            user = self._get_user()
            print(user.playlists)
        except (DisconnectedUser, UserDoesNotExist) as e:
            print(f'Exception: {type(e)} {str(e)}')

    def _create_playlist(self):
        try:
            user = self._get_user()
            playlist_name = input('Enter playlist name: ')
            user.add_playlist(playlist_name, [])
        except (DisconnectedUser, UserDoesNotExist, PlaylistAlreadyExist, PassSongsInPlaylistAssignment) as e:
            print(f'Exception: {type(e)} {str(e)}')

    def _add_song_to_playlist(self):
        try:
            user = self._get_user()
            playlist_name = input('Enter playlist name: ')
            song_id = input('Enter song id: ')
            user.add_songs_to_playlist(playlist_name, [Search.get_song(song_id)])
        except (DisconnectedUser, UserDoesNotExist, PlaylistAlreadyExist, PassSongsInPlaylistAssignment,
                PassedPlaylistsAssignment, SongIdDoesNotExist) as e:
            print(f'Exception: {type(e)} {str(e)}')
