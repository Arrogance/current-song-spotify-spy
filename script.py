import os
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

def create_spotify_client():
    load_dotenv()

    scope = "user-read-playback-state"
    sleep_delay = int(os.getenv("SLEEP_DELAY", 10))
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    return sp, sleep_delay

def save_current_song(sp):
    track = sp.current_playback()
    if track:
        track_name = track['item']['name']
        track_artist = track['item']['artists'][0]['name']
        with open("current_song.txt", "w") as f:
            f.write(f"{track_name} - {track_artist}")
        print(f"Current song: {track_name} - {track_artist}")
    else:
        print("No song is currently playing.")

def main():
    sp, sleep_delay = create_spotify_client()
    while True:
        save_current_song(sp)
        time.sleep(sleep_delay)

if __name__ == "__main__":
    main()
