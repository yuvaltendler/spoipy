import logging

from exception.search_exception import ArtistIdDoesNotExist, AlbumIdDoesNotExist, SongIdDoesNotExist
from music import Artist, ArtistManager, Album, Song
from properties import Properties


class Search:
    @staticmethod
    def get_artists() -> [Artist]:
        return list(ArtistManager().artists.values())

    @staticmethod
    def get_albums(artist_id: str) -> [Album]:
        if artist_id not in ArtistManager().artists:
            logging.info(f'Artist id {artist_id} does not exist')
            raise ArtistIdDoesNotExist()
        return list(ArtistManager().artists[artist_id].albums.values())

    @staticmethod
    def get_songs_in_album(album_id: str) -> [Song]:
        for artist in ArtistManager().artists.values():
            if album_id in artist.albums:
                return list(artist.albums[album_id].songs.values())
        logging.info(f'Album id {album_id} does not exist')
        raise AlbumIdDoesNotExist()

    @staticmethod
    def get_song(song_id: str) -> Song:
        for artist in ArtistManager().artists.values():
            for album in artist.albums.values():
                if song_id in album.songs:
                    return album.songs[song_id]
        logging.info(f'Song id {song_id} does not exist')
        raise SongIdDoesNotExist()

    @staticmethod
    def get_beast_songs(artist_id: str, num_of_results: int = 10) -> [Song]:
        songs = []
        for album in Search.get_albums(artist_id):
            songs = songs + list(album.songs.values())
        res = sorted(songs, key= lambda song: song.popularity, reverse=True)
        return res[:num_of_results]

    @staticmethod
    def limit(array):
        return array[:Properties().properties.get('FREE_USER_LIMIT_SEARCH_RESULT')]

