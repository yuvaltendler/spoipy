import json

from music import ArtistManager, Song, Artist, Album


class LoadMusic:
    @staticmethod
    def load_music(folder_path: str):
        pass

    @staticmethod
    def _load_track(file_path: str):
        with open(file_path, 'r') as file:
            track = json.load(file)['track']
        song = Song(track['name'], track['popularity'])
        song_id = track['id']
        album_name = track['album']['name']
        album_id = track['album']['id']
        for artist_dict in track['artists']:
            artist_id = artist_dict['id']
            artist_name = artist_dict['name']
            if artist_id not in ArtistManager().artists:
                ArtistManager().artists[artist_id] = Artist(artist_name)
            artist = ArtistManager().artists[artist_id]
            if album_id not in ArtistManager().artists[artist_id].albums:
                artist.albums[album_id] = Album(album_name)

            artist.albums[album_id].songs[song_id] = song
