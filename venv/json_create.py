import json

credentials = {}
credentials['SPOTIPY_CLIENT_ID'] = "4a47495abb894ffc8cd14a355b870ccf"
credentials['SPOTIPY_CLIENT_SECRET'] = "64680462d3a443c68074f5c74643b140"
credentials['SPOTIPY_REDIRECT_URI'] = "http://localhost:1410/ "

with open("spotipy_credentials.json", "w") as file:
    json.dump(credentials, file)