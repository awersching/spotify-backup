import gin

from spotify.parser import Parser


@gin.configurable
class Backup:

    def __init__(self, output_directory='../'):
        self.output_directory = output_directory
        self.request = Parser()

    def backup(self):
        self.save(self.request.get_followed_artists())
        self.save(self.request.get_saved_songs())

        for playlist in self.request.get_playlists():
            try:
                self.save(self.request.get_playlist_songs(playlist))
            except LookupError:
                print('Tracks of playlist ' + playlist[0] + ' not queryable over API')

    def save(self, data: (str, [])):
        file_name = self.output_directory + data[0] + '.txt'

        with open(file_name, 'w') as file:
            for line in data[1]:
                file.write(str(line) + '\n')
