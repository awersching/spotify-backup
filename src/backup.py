import json

import gin

from spotify_request import SpotifyRequest
from spotify_resource import SpotifyResource
from txt_parser import TxtParser


@gin.configurable
class Backup:

    def __init__(self, save_as_json=True, save_as_txt=True, output_directory='../'):
        self.save_as_json = save_as_json
        self.save_as_txt = save_as_txt
        self.output_directory = output_directory

        self.request = SpotifyRequest()
        self.parser = TxtParser()

    def backup(self):
        followed = self.request.get_followed()
        songs = self.request.get_saved_songs()
        playlist_ids = self.request.get_playlists()

        if self.save_as_json:
            self.save_json(followed)
            self.save_json(songs)
            for playlist_id in playlist_ids:
                self.save_json(self.request.get_playlist(playlist_id))

        if self.save_as_txt:
            self.save_txt(followed)
            self.save_txt(songs)
            for playlist_id in playlist_ids:
                self.save_txt(self.request.get_playlist(playlist_id))

    def save_json(self, resource: SpotifyResource):
        file_name = self.output_directory + resource.name + '.json'

        with open(file_name, 'w') as file:
            json.dump(resource.json, file)

    def save_txt(self, resource: SpotifyResource):
        file_name = self.output_directory + resource.name + '.txt'
        txt = self.parser.to_txt(resource)

        with open(file_name, 'w') as file:
            for line in txt:
                file.write(line + '\n')
