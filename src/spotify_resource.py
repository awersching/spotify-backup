from enum import Enum, auto


class SpotifyResource:
    class Type(Enum):
        ARTISTS = auto()
        SONGS = auto()
        PLAYLISTS = auto()
        PLAYLIST = auto()

    def __init__(self, json, name, type: Type):
        self.json = json
        self.name = name
        self.type = type
