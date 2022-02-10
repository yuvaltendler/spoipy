from consolemenu import *
from consolemenu.items import *

from search.search import Search
from singleton import Singleton


class Menu(metaclass=Singleton):
    def __init__(self):
        self.menu = ConsoleMenu('Spotipy', 'Welcome to spotipy')
        self.is_free_user = True
        get_artists = FunctionItem('Get all artists', Menu._get_artists, [self])
        get_albums = FunctionItem('Get artist\'s albums', Menu._get_albums, [self])

        menu_item = MenuItem("Menu Item")
        function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
        command_item = CommandItem("Run a console command", "") #"touch hello.txt"
        selection_menu = SelectionMenu(["item1", "item2", "item3"])
        submenu_item = SubmenuItem("Submenu item", selection_menu, self.menu)
        self.menu.append_item(get_artists)
        self.menu.append_item(get_albums)

        self.menu.append_item(menu_item)
        self.menu.append_item(function_item)
        self.menu.append_item(command_item)
        self.menu.append_item(submenu_item)


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
