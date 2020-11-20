import Spotupy
import database
import pandas as pd
import spotipy
from database import *
from spotipy.oauth2 import SpotifyClientCredentials

pitchfork_data =  database.run_query(sqlfile='pitchfork_data.sql')
column_names2 = ["reviewid", "album", "artist", "score", "best_new_music", "author", "pub_day", "pub_month", "pub_year", "genre", "label"]
pitchfork_data = pd.DataFrame(pitchfork_data, columns= column_names2 )

sp = Spotupy.run_credentials()
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
length_of_data = len(pitchfork_data)

for x in range(0, length_of_data):
        reviewid = pitchfork_data.iloc[x][0]
        album = pitchfork_data.iloc[x][1]
        artist = pitchfork_data.iloc[x][2]

        print(str(x)+ "/" + str(length_of_data) + " Working on Audio Features for " + album + " by " + artist)

        album_id = Spotupy.retrieve_album_id(album, artist, sp)

        if pd.isnull(album_id) == False:
            track_names = Spotupy.retireve_track_names(album_id, sp)
            track_id = Spotupy.retrieve_track_ids(artist, track_names,sp)
            audio_features = Spotupy.retrieve_audio_features(track_names, track_id, sp)
        else:
            audio_features = pd.DataFrame(columns=column_names[1:len(column_names)])
            audio_features.loc[len(audio_features)] = 0


        audio_features.insert(0, 'reviewid', reviewid)
        empty = pd.concat([empty, audio_features])

pitchfork_data = pitchfork_data.merge(empty,on='reviewid',how='left')

pitchfork_data.to_csv(r'C:/Users/18184/Documents/pitchfork_data.csv', index = False, header=True)


"""except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}. The problem lies with the " + album + " by " + artist
    message = template.format(type(ex).__name__, ex.args)
    print(message)
"""