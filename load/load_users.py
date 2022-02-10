import json
import logging

from music import ArtistManager
from search.search import Search
from users import UserManager, FreeUser, ArtistUser, PremiumUser


class LoadUsers():
    @staticmethod
    def load_users(path: str):
        with open(path, 'r') as file:
            users = json.load(file)['users']
            for user in users:
                LoadUsers._parse_user(user)


    @staticmethod
    def _parse_user(user_json):
        id = user_json['id']
        logging.debug(f'parse user {id}')
        if user_json['is_free_user']:
            UserManager().users[id] = FreeUser()
        else:
            if id in ArtistManager().artists:
                UserManager().users[id] = ArtistUser(ArtistManager().artists[id])
            else:
                UserManager().users[id] = PremiumUser()
        LoadUsers._parse_playlists(user_json['playlists'], UserManager().users.get(id))


    @staticmethod
    def _parse_playlists(playlist_dict, user: FreeUser):
        for playlist_name in playlist_dict.keys():
            songs = [Search.get_song(song_id) for song_id in playlist_dict[playlist_name]]
            user.add_playlist(playlist_name, songs)
