# spotify-backup

Saves followed artists, saved songs and playlists as .txt

## Build

```pipenv install```

## Run

```pipenv run python src/main.py```

Environment variables for authentication have to be set:
- `SPOTIPY_CLIENT_ID`
- `SPOTIPY_CLIENT_SECRET`
- `SPOTIPY_REDIRECT_URI`

See [https://spotipy.readthedocs.io/en/latest/#authorized-requests](https://spotipy.readthedocs.io/en/latest/#authorized-requests)