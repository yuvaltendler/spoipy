import logging
import os

from load import LoadMusic
from properties import Properties


def main():
    if os.path.exists("log\\spotipy.log"):
        os.remove("log\\spotipy.log")
    logging.basicConfig(filename='log\\spotipy.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.debug('start main')
    properties = Properties()
    LoadMusic.load_music('C:\\Users\\user\\Documents\\Army\\codes\\spotipy\\tracks')
    logging.debug('stop main')

if __name__ == '__main__':
    main()
