import json
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def run_credentials():
    with open("spotipy_credentials.json", "r") as file:
        creds = json.load(file)

    auth_manager = SpotifyClientCredentials(client_id=creds['SPOTIPY_CLIENT_ID'],
                                        client_secret=creds['SPOTIPY_CLIENT_SECRET'])
    sp = spotipy.Spotify(client_credentials_manager=auth_manager)


def retrieve_album_id(album_name, artist_name):
    results = sp.search(q="artist:" + artist + " album:" + album, limit=1)
    album_id = results['albums']['items'][0]['uri']


def retireve_track_names(album_id):
    track_names = []
    tracks = sp.album_tracks(album_id)
    for track in tracks['items']:
        print(track['name'])
        track_names.append(track['name'])

    print(track_names)


def retrieve_track_ids(album_name, artist_name):
    album = album_name
    artist = artist_name

    album_id = retrieve_album_id(album, artist)
    track_names = retireve_track_names(album_id)

    tracks_ids = []
    for i in range(0, len(track_names)):
        print(i)
        print(track_names[i])
        result = sp.search(q="artist:" + artist + " track:" + track_names[i], limit=1)
        song_id = result['tracks']['items'][0]['uri']
        tracks_ids.append(song_id)
    print(tracks_ids)


def retrieve_audio_features(track_ids):
    audio_features = sp.audio_features(tracks=tracks_ids)
    datframe = pd.DataFrame(sp.audio_features(tracks=tracks_ids))
    datframe = datframe.select_dtypes(['number'])
    datframe = pd.DataFrame(datframe.sum(axis=0) / len(track_names))

    avg_data = pd.DataFrame()
    avg_data = avg_data.append(datframe[0], ignore_index=True)
