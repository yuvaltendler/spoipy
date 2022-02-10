import logging
import os

from load import LoadMusic
import menu
from properties import Properties


def main():
    if os.path.exists("log\\spotipy.log"):
        os.remove("log\\spotipy.log")
    logging.basicConfig(filename='log\\spotipy.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.debug('start main')
    properties = Properties()
    LoadMusic.load_music('C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks')
    menu.show()
    logging.debug('stop main')

if __name__ == '__main__':
    main()
