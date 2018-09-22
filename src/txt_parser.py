from spotify_resource import SpotifyResource


class TxtParser:

    def to_txt(self, resource: SpotifyResource) -> [str]:
        if resource.type is SpotifyResource.Type.ARTISTS:
            return self._to_artists_txt(resource)
        elif resource.type is SpotifyResource.Type.SONGS:
            return self._to_songs_txt(resource)
        elif resource.type is SpotifyResource.Type.PLAYLIST:
            return self._to_playlist_txt(resource)

    def _to_artists_txt(self, resource: SpotifyResource) -> [str]:
        artists = []

        for artist in resource.json:
            artists.append(artist['name'])
        return artists

    def _to_songs_txt(self, resource: SpotifyResource) -> [str]:
        songs = []

        for song in resource.json:
            song = song['track']

            name = song['name']
            artists = list(map(lambda artist: artist['name'], song['artists']))
            album = song['album']['name']
            songs.append(name + ' - ' + ", ".join(artists) + ' (' + album + ')')
        return songs

    def _to_playlist_txt(self, resource: SpotifyResource) -> [str]:
        return []
