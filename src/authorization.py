import spotipy.util as util
import gin


@gin.configurable
class Authorization:

    def __init__(self, scopes=[]):
        self.scopes = scopes

    def authorize(self):
        token = util.prompt_for_user_token('6247', self.scopes)
