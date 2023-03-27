import os
import time
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load API credentials from .env file
load_dotenv()

# Authenticate with Spotify
scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Read the sleep delay from the environment
sleep_delay = int(os.getenv("SLEEP_DELAY", 10))

def get_current_playback():
    return sp.current_playback()

def extract_song_artist(current_playback):
    if not current_playback or not current_playback["item"]:
        return None, None

    song = current_playback["item"]["name"]
    artist = current_playback["item"]["artists"][0]["name"]
    return song, artist

def write_song_to_file(song, artist):
    with open("current_song.txt", "w") as file:
        file.write(f"{song} by {artist}")

def main():
    current_song = None

    while True:
        current_playback = get_current_playback()
        song, artist = extract_song_artist(current_playback)

        if not song:
            print("No song is currently playing.")
            time.sleep(sleep_delay)
            continue

        if current_song != (song, artist):
            current_song = (song, artist)
            write_song_to_file(song, artist)
            print(f"Current song written to file: {song} by {artist}")

        time.sleep(sleep_delay)

if __name__ == "__main__":
    main()
