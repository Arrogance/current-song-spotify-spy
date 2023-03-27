import unittest
from unittest.mock import MagicMock
from twitch_spotify_spy import extract_song_artist

class TestSpotifyCurrentTrack(unittest.TestCase):

    def test_extract_song_artist(self):
        mock_current_playback = {
            "item": {
                "name": "Test Song",
                "artists": [{"name": "Test Artist"}]
            }
        }

        song, artist = extract_song_artist(mock_current_playback)
        self.assertEqual(song, "Test Song")
        self.assertEqual(artist, "Test Artist")

    def test_extract_song_artist_no_current_playback(self):
        mock_current_playback = None

        song, artist = extract_song_artist(mock_current_playback)
        self.assertIsNone(song)
        self.assertIsNone(artist)

    def test_extract_song_artist_no_item(self):
        mock_current_playback = {"item": None}

        song, artist = extract_song_artist(mock_current_playback)
        self.assertIsNone(song)
        self.assertIsNone(artist)

if __name__ == "__main__":
    unittest.main()
