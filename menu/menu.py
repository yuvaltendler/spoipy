import logging

from consolemenu import *
from consolemenu.items import *

from exception.exception import DisconnectedUser, UserDoesNotExist
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
        search = SubmenuItem('Search', search_menu, menu)
        login = FunctionItem('Login', Menu._login, [self])
        get_playlists = FunctionItem('Get my playlists', Menu._get_playlists, [self])

        menu.append_item(login)
        menu.append_item(search)
        menu.append_item(get_playlists)
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

    def _get_artists(self):
        if self.is_free_user:
            print([artist.name for artist in Search.limit(Search.get_artists())])
            return
        print([artist.name for artist in Search.get_artists()])

    def _get_albums(self):
        artist_id = input('Enter artist id: ')
        if self.is_free_user:
            print([album.name for album in Search.limit(Search.get_albums(artist_id))])
            return
        print([album.name for album in Search.get_albums(artist_id)])

    def _get_songs_in_album(self):
        album_id = input('Enter album id: ')
        if self.is_free_user:
            print([str(song) for song in Search.limit(Search.get_songs_in_album(album_id))])
            return
        print([str(song) for song in Search.get_songs_in_album(album_id)])

    def _get_beast_songs(self):
        artist_id = input('Enter artist id: ')
        if self.is_free_user:
            print(Search.limit(Search.get_beast_songs(artist_id)))
            return
        print(Search.get_beast_songs(artist_id))

    def _login(self):
        username = input('Username: ')
        #password = getpass()
        if username not in UserManager().users:
            logging.warning('Try to connect with unknown username')
            raise UserDoesNotExist()
        self.username = username
        self.is_free_user = not isinstance(UserManager().users[username], PremiumUser)

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

