import json
from singleton import Singleton


class Properties(metaclass=Singleton):
    def __init__(self):
        self.properties = {}
        with open('C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\properties\\properties.json', 'r') as file:
            self.properties = json.load(file)
