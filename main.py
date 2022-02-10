import logging
import os

from load import LoadMusic
import menu
from music import Song
from properties import Properties
from users import UserManager, PremiumUser


def main():
    if os.path.exists("log\\spotipy.log"):
        os.remove("log\\spotipy.log")
    logging.basicConfig(filename='log\\spotipy.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.debug('start main')
    LoadMusic.load_music(Properties().properties.get('TRACKS_DIRECTORY_PATH'))
    UserManager().users['1'] = PremiumUser()
    UserManager().users['1'].add_playlist('p1', [Song('s1', 5), Song('s2', 7)])
    menu.show()
    logging.debug('stop main')

if __name__ == '__main__':
    main()
