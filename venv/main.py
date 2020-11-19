import pandas as pd
import database
from database import *
import Spotupy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

initial = database.run_query(sqlfile='initial_data.sql')

album = initial[0][1]
artist = initial[0][2]

Spotupy.run_credentials()

album_id = Spotupy.retrieve_album_id(album, artist)
track_names = Spotupy.retireve_track_names(album_id)
track_id = Spotupy.retrieve_track_ids(artist,track_names)

audio_features = Spotupy.retrieve_audio_features(track_names, track_id)

print(audio_features)