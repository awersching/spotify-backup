import spotipy.util as util
import gin


@gin.configurable
class Authorization:

    def __init__(self, scopes=None):
        self.scopes = scopes

    def authorize(self):
        username = input('Enter username: ')
        token = util.prompt_for_user_token(username, self.scopes)
