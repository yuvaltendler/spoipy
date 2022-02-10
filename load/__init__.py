from load.load_music import LoadMusic
from load.load_users import LoadUsers

def load_music(folder_path: str):
    LoadMusic.load_music(folder_path)

def load_users(path: str):
    LoadUsers.load_users(path)
