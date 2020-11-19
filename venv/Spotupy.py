import json

import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def run_credentials():
    with open("spotipy_credentials.json", "r") as file:
        creds = json.load(file)

    auth_manager = SpotifyClientCredentials(client_id=creds['SPOTIPY_CLIENT_ID'],
                                            client_secret=creds['SPOTIPY_CLIENT_SECRET'])
    sp = spotipy.Spotify(client_credentials_manager=auth_manager)

    return sp


def retrieve_album_id(album, artist):
    sp = run_credentials()
    results = sp.search(q="album:" + album, type="album", limit=1)
    album_id = results['albums']['items'][0]['uri']
    return album_id


def retireve_track_names(album_id):
    sp = run_credentials()
    track_names = []
    tracks = sp.album_tracks(album_id)
    for track in tracks['items']:
        track_names.append(track['name'])
    return track_names


def retrieve_track_ids(artist_name, track_names):
    tracks_ids = []
    sp = run_credentials()
    for i in range(0, len(track_names)):
        result = sp.search(q="artist:" + artist_name + " track:" + track_names[i], limit=1)

        if bool(result['tracks']['items']) == True:
            song_id = result['tracks']['items'][0]['uri']
        else:
            song_id = np.nan

    tracks_ids.append(song_id)

    return tracks_ids


def retrieve_audio_features(track_names, tracks_ids):
    sp = run_credentials()
    column_names = ["acousticness",
                    "danceability",
                    "duration_ms",
                    "energy",
                    "instrumentalness",
                    "key",
                    "liveness",
                    "loudness",
                    "mode",
                    "speechiness",
                    "tempo",
                    "time_signature",
                    "valence",
                    "break"
                    ]
    if pd.isnull(tracks_ids) == False:
        audio_features = sp.audio_features(tracks=tracks_ids)
        datframe = pd.DataFrame(sp.audio_features(tracks=tracks_ids))
        datframe = datframe.select_dtypes(['number'])
        datframe = pd.DataFrame(datframe.sum(axis=0) / len(track_names))

        avg_data = pd.DataFrame()
        avg_data = avg_data.append(datframe[0], ignore_index=True)
    else:
        avg_data = pd.DataFrame(columns=column_names)
        print(avg_data)
    return avg_data
