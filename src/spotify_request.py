from spotipy import Spotify

from authorization import Authorization
from spotify_resource import SpotifyResource


class SpotifyRequest:

    def __init__(self):
        self.PAGE_LIMIT = 50
        self.spotify: Spotify = Authorization().authorize()

    def get_followed(self) -> SpotifyResource:
        print('Backing up followed artists...')

        current_page = self.spotify.current_user_followed_artists(limit=self.PAGE_LIMIT)
        after = current_page['artists']['cursors']['after']
        all = []

        while after:
            all += current_page['artists']['items']
            after = current_page['artists']['cursors']['after']
            current_page = self.spotify.current_user_followed_artists(limit=self.PAGE_LIMIT, after=after)
        return SpotifyResource(all, SpotifyResource.Type.ARTISTS, 'artists')

    def get_saved_songs(self) -> SpotifyResource:
        print('Backing up saved songs...')

        current_page = self.spotify.current_user_saved_tracks(limit=self.PAGE_LIMIT)
        offset = 0
        all = []

        while current_page['next']:
            all += current_page['items']
            offset += self.PAGE_LIMIT
            current_page = self.spotify.current_user_saved_tracks(limit=self.PAGE_LIMIT, offset=offset)
        return SpotifyResource(all, SpotifyResource.Type.SONGS, 'songs')

    def get_playlists(self) -> SpotifyResource:
        print('Backing up playlists...')

        current_page = self.spotify.current_user_playlists(limit=self.PAGE_LIMIT)
        offset = 0
        all = []

        while current_page['next']:
            all += current_page['items']
            offset += self.PAGE_LIMIT
            current_page = self.spotify.current_user_playlists(limit=self.PAGE_LIMIT, offset=offset)
        return SpotifyResource(all, SpotifyResource.Type.PLAYLISTS)

    def get_playlist_songs(self, playlist: SpotifyResource) -> SpotifyResource:
        print(playlist)
