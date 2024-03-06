import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = "c67d684a14214d7eb458855ef6cdd3c1"
CLIENT_SECRET = "0440a8cdef934fbb96fa4f67356daa35"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get song album cover URL
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

# Function to recommend similar songs
def recommend(selected_song, music, similarity):
    index = music[music['song'] == selected_song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        # fetch the song poster
        artist = music.iloc[i[0]].artist
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names, recommended_music_posters

# Load data
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Command-line interface
print("Welcome to the Music Recommender System!")
print("Available songs:")
for song in music['song']:
    print("-", song)
selected_song = input("Type or select a song from the list: ")

recommended_music_names, recommended_music_posters = recommend(selected_song, music, similarity)

print("\nRecommended songs:")
for i, song in enumerate(recommended_music_names):
    print(f"{i+1}. {song}")
    print("   Album Cover URL:", recommended_music_posters[i])
