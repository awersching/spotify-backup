import gin
from spotipy import Spotify

from TxtParser import TxtParser
from authorization import Authorization


@gin.configurable
class Backup:

    def __init__(self, save_as_json=True, save_as_txt=True):
        self.PAGE_LIMIT = 50

        self.save_as_json = save_as_json
        self.save_as_txt = save_as_txt

        self.spotify: Spotify = Authorization().authorize()
        self.txt_parser = TxtParser()

    def backup(self):
        followed = self._get_followed()
        playlists = self._get_playlists()
        songs = self._get_saved_songs()

        if self.save_as_json:
            self.save_json(followed)
            self.save_json(playlists)
            self.save_json(songs)
        if self.save_as_txt:
            self.save_txt(followed)
            self.save_txt(playlists)
            self.save_txt(songs)

    def _get_followed(self) -> []:
        print('Backing up followed artists...')

        current_page = self.spotify.current_user_followed_artists(limit=self.PAGE_LIMIT)
        after = current_page['artists']['cursors']['after']
        all = []

        while after:
            all.append(current_page['artists']['items'])
            after = current_page['artists']['cursors']['after']
            current_page = self.spotify.current_user_followed_artists(limit=self.PAGE_LIMIT, after=after)
        return all

    def _get_playlists(self) -> []:
        print('Backing up playlists...')
        return []

    def _get_saved_songs(self) -> []:
        print('Backing up saved songs...')
        return []

    def save_json(self, json):
        pass

    def save_txt(self, json):
        txt = self.txt_parser.to_txt(json)
