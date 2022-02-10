import logging
import os

import load
import menu
from music import Song
from properties import Properties
from users import UserManager, PremiumUser


def main():
    if os.path.exists("log\\spotipy.log"):
        os.remove("log\\spotipy.log")
    logging.basicConfig(filename='log\\spotipy.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    logging.debug('start main')
    load.load_music(Properties().properties.get('TRACKS_DIRECTORY_PATH'))
    load.load_users('users_files\\users.json')
    menu.show()
    logging.debug('stop main')


if __name__ == '__main__':
    main()
