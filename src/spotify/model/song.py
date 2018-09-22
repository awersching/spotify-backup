class Song:

    def __init__(self, json):
        # playlist tracks not queryable over API
        if not json:
            raise LookupError

        self.name = json['name']
        self.artists = list(map(lambda artist: artist['name'], json['artists']))
        self.album = json['album']['name']

    def __str__(self) -> str:
        return self.name + ' - ' + ', '.join(self.artists) + ' (' + self.album + ')'
