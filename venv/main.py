import Spotupy
import database
import pandas as pd
import spotipy
from database import *
from spotipy.oauth2 import SpotifyClientCredentials

initial = database.run_query(sqlfile='initial_data.sql')
initial_dataframe = pd.DataFrame(initial, columns=["reviewid", "album", "artist"])

pitchfork_data = pd.DataFrame(database.run_query(sqlfile='initial_data.sql'), columns= ['reviewid', 'album', 'artist'])

"""try:
"""
column_names = ["reviewid",
                "acousticness",
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
empty = pd.DataFrame(columns=column_names)

for x in range(0, len(initial)):
        reviewid = pitchfork_data.iloc[x][0]
        album = pitchfork_data.iloc[x][1]
        artist = pitchfork_data.iloc[x][2]
        print("Working on Audio Features for " + album + " by " + artist)
        Spotupy.run_credentials()

        album_id = Spotupy.retrieve_album_id(album, artist)
        track_names = Spotupy.retireve_track_names(album_id)
        track_id = Spotupy.retrieve_track_ids(artist, track_names)
        
        audio_features = Spotupy.retrieve_audio_features(track_names, track_id)
        audio_features.insert(0, 'reviewid', reviewid)

        empty = pd.concat([empty, audio_features])

empty = empty.merge(pitchfork_data,on='reviewid',how='left')

empty.to_csv(r'C:/Users/18184/Documents/practice_pitchfork_data.csv', index = False, header=True)

"""except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}. The problem lies with the " + album + " by " + artist
    message = template.format(type(ex).__name__, ex.args)
    print(message)
"""