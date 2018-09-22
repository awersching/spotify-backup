from enum import Enum, auto


class SpotifyResource:
    class Type(Enum):
        ARTISTS = auto()
        SONGS = auto()
        PLAYLISTS = auto()
        PLAYLIST = auto()

    def __init__(self, json, type: Type, name=None):
        self.json = json
        self.type = type
        self.name = name
