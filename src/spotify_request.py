from spotipy import Spotify

from authorization import Authorization
from spotify_resource import SpotifyResource


class SpotifyRequest:

    def __init__(self):
        self.PAGE_LIMIT = 50
        self.spotify: Spotify = Authorization().authorize()

    def get_followed(self) -> SpotifyResource:
        current_page = self.spotify.current_user_followed_artists(limit=self.PAGE_LIMIT)
        after = current_page['artists']['cursors']['after']
        all = []

        while after:
            all.append(current_page['artists']['items'])
            after = current_page['artists']['cursors']['after']
            current_page = self.spotify.current_user_followed_artists(limit=self.PAGE_LIMIT, after=after)
        return SpotifyResource(all, 'artists', SpotifyResource.Type.ARTISTS)

    def get_saved_songs(self) -> SpotifyResource:
        pass

    def get_playlists(self) -> [SpotifyResource]:
        pass

    def get_playlist(self, playlist_id) -> SpotifyResource:
        pass
