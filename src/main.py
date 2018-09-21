import codecs
import json
from urllib import request

api_url = "https://api.spotify.com/v1/"
offset_limit_playlist = "/tracks?offset=0&limit=100"
playlist_url = "users/6247/playlists/"
auth_token = ""

zeug_url = api_url + playlist_url + \
            "6R1bBGy7EIoOSD1iffl30H" + \
            offset_limit_playlist
tarantino_url = api_url + playlist_url + \
                "0yWnlTYOMIf1bqAF4XvEow" + \
                offset_limit_playlist
gespeichert_url = api_url + "me/tracks"
folgen_url = api_url + "me/following?type=artist"

zeug_file = "/home/adrian/Backup/spotify/zeug.json"
tarantino_file = "/home/adrian/Backup/spotify/tarantino.json"
gespeichert_file = "/home/adrian/Backup/spotify/gespeichert.json"
folgen_file = "/home/adrian/Backup/spotify/folgen.json"


def rest_get(url):
    req = request.Request(url)
    req.add_header("Authorization", auth_token)
    res = request.urlopen(req)
    reader = codecs.getreader("utf-8")

    if "following" in url:
        return json.load(reader(res))["artists"]
    else:
        return json.load(reader(res))


def get_as_list(url):
    response = rest_get(url)
    items = response["items"]

    while response["next"]:
        response = rest_get(response["next"])
        items += response["items"]
    return items


def write(url, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(get_as_list(url), file)


# zeug, tarantino, gespeichert, folgen
write(zeug_url, zeug_file)
write(tarantino_url, tarantino_file)
write(gespeichert_url, gespeichert_file)
write(folgen_url, folgen_file)
