import gin

import spotipy.util as util
from spotipy import Spotify


@gin.configurable
class Authorization:

    def __init__(self, username=None):
        self.username = username if username else input('Enter username: ')
        scopes = [
            'user-library-read',
            'playlist-read-private',
            'playlist-read-collaborative',
            'user-follow-read'
        ]
        self.scopes = ' '.join(map(str, scopes))

    def authorize(self) -> Spotify:
        print("Don't run this from IntelliJ terminal as it will mess up the link input")
        token = util.prompt_for_user_token(self.username, self.scopes)
        return Spotify(auth=token)
