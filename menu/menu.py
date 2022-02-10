from consolemenu import *
from consolemenu.items import *

from search.search import Search
from singleton import Singleton
from users import UserManager, PremiumUser


class Menu(metaclass=Singleton):
    def __init__(self):
        self.is_free_user = True
        self.username = ''
        self.menu = ConsoleMenu('Spotipy', 'Welcome to spotipy')

        search_menu = self._get_search_menu()
        search = SubmenuItem('Search', search_menu, self.menu)
        login = FunctionItem('Login', Menu._login, [self])


        menu_item = MenuItem("Menu Item")
        function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
        command_item = CommandItem("Run a console command", "")  # "touch hello.txt"
        selection_menu = SelectionMenu(["item1", "item2", "item3"])
        submenu_item = SubmenuItem("Submenu item", selection_menu, self.menu)

        self.menu.append_item(login)
        self.menu.append_item(search)
        self.menu.append_item(menu_item)
        self.menu.append_item(function_item)
        self.menu.append_item(command_item)
        self.menu.append_item(submenu_item)

    def _get_search_menu(self):
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
            print([str(song) for song in Search.limit(Search.get_beast_songs(artist_id))])
            return
        print([str(song) for song in Search.get_beast_songs(artist_id)])

    def _login(self):
        username = input('Username: ')
        #password = getpass()
        if username in UserManager().users:
            self.username = username
            self.is_free_user = not isinstance(UserManager().users[username], PremiumUser)
