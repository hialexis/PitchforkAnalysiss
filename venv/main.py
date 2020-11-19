import Spotupy
import database
import pandas as pd
import spotipy
from database import *
from spotipy.oauth2 import SpotifyClientCredentials

initial = database.run_query(sqlfile='initial_data.sql')

"""try:
"""
for x in range(0, len(initial)):
        album = initial[x][1]
        artist = initial[x][2]
        Spotupy.run_credentials()

        album_id = Spotupy.retrieve_album_id(album, artist)
        track_names = Spotupy.retireve_track_names(album_id)
        track_id = Spotupy.retrieve_track_ids(artist, track_names)
        
        audio_features = Spotupy.retrieve_audio_features(track_names, track_id)
        
"""except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}. The problem lies with the " + album + " by " + artist
    message = template.format(type(ex).__name__, ex.args)
    print(message)
"""