import os
import unittest
from unittest.mock import MagicMock, patch
import script

class TestTwitchSpotifySpy(unittest.TestCase):

    @patch("script.load_dotenv")
    @patch("script.SpotifyOAuth")
    def test_create_spotify_client(self, mock_spotify_oauth, mock_load_dotenv):
        mock_auth_manager = MagicMock()
        mock_spotify_oauth.return_value = mock_auth_manager
        os.environ["SLEEP_DELAY"] = "20"

        sp, sleep_delay = script.create_spotify_client()

        self.assertIsNotNone(sp)
        self.assertEqual(sleep_delay, 20)
        mock_load_dotenv.assert_called_once()
        mock_spotify_oauth.assert_called_once_with(scope="user-read-playback-state")

    @patch("script.spotipy.Spotify.current_playback")
    def test_save_current_song_playing(self, mock_current_playback):
        mock_sp = MagicMock()
        mock_sp.current_playback = mock_current_playback
        track_data = {
            'item': {
                'name': 'Test Song',
                'artists': [{'name': 'Test Artist'}]
            }
        }
        mock_current_playback.return_value = track_data

        with patch("builtins.open", unittest.mock.mock_open()) as mock_file:
            script.save_current_song(mock_sp)

        mock_current_playback.assert_called_once()
        mock_file.assert_called_once_with("current_song.txt", "w")
        mock_file().write.assert_called_once_with("Test Song - Test Artist")

    @patch("script.spotipy.Spotify.current_playback")
    def test_save_current_song_not_playing(self, mock_current_playback):
        mock_sp = MagicMock()
        mock_sp.current_playback = mock_current_playback
        mock_current_playback.return_value = None

        with patch("builtins.open", unittest.mock.mock_open()) as mock_file:
            script.save_current_song(mock_sp)

        mock_current_playback.assert_called_once()
        mock_file.assert_not_called()

if __name__ == "__main__":
    unittest.main()
