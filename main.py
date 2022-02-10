import logging
import os

import load
import menu
from music import Song
from properties import Properties
from users import UserManager, PremiumUser


def main():
    if os.path.exists(Properties().properties.get('LOG_FILE_PATH')):
        os.remove(Properties().properties.get('LOG_FILE_PATH'))
    logging.basicConfig(filename=Properties().properties.get('LOG_FILE_PATH'), filemode='a',
                        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.debug('start main')
    load.load_music(Properties().properties.get('TRACKS_DIRECTORY_PATH'))
    load.load_users(Properties().properties.get('USERS_PATH'))
    menu.show()
    logging.debug('stop main')


if __name__ == '__main__':
    main()
