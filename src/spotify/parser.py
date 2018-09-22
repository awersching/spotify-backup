from spotipy import Spotify

from spotify.authorization import Authorization
from spotify.model.song import Song


class Parser:

    def __init__(self):
        self.PAGE_LIMIT = 50

        self.auth = Authorization()
        self.spotify: Spotify = self.auth.authorize()

    def get_followed_artists(self) -> (str, []):
        print('Backing up followed artists...')

        all = []
        after = None
        while True:
            current_page = self.spotify.current_user_followed_artists(limit=self.PAGE_LIMIT, after=after)
            artists = current_page['artists']['items']
            all += (artist['name'] for artist in artists)

            after = current_page['artists']['cursors']['after']
            if not after:
                break
        return 'artists', all

    def get_saved_songs(self) -> (str, []):
        print('Backing up saved songs...')

        all = []
        offset = 0
        while True:
            current_page = self.spotify.current_user_saved_tracks(limit=self.PAGE_LIMIT, offset=offset)
            songs = current_page['items']
            all += (Song(song['track']) for song in songs)

            next = current_page['next']
            offset += self.PAGE_LIMIT
            if not next:
                break
        return 'songs', all

    def get_playlists(self) -> [(str, str)]:
        print('Backing up playlists...')

        all = []
        offset = 0
        while True:
            current_page = self.spotify.current_user_playlists(limit=self.PAGE_LIMIT, offset=offset)
            playlists = current_page['items']
            all += ((playlist['name'], playlist['id']) for playlist in playlists)

            next = current_page['next']
            offset += self.PAGE_LIMIT
            if not next:
                break
        return all

    def get_playlist_songs(self, playlist: (str, str)) -> (str, []):
        all = []
        offset = 0
        while True:
            current_page = self.spotify.user_playlist_tracks(self.auth.username, playlist_id=playlist[1], offset=offset)
            songs = current_page['items']
            all += (Song(song['track']) for song in songs)

            next = current_page['next']
            offset += self.PAGE_LIMIT
            if not next:
                break
        return playlist[0], all
