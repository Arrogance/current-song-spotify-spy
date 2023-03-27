# Spotify Current Track Logger
This script logs the current song playing on your Spotify account to a text file called current_song.txt. It continuously checks for song changes and updates the text file accordingly.

## Requirements
- Python 3.6 or higher
- `spotipy` library
- `python-dotenv` library

## Setup
1. Clone this repository or download the files.
2. Install the required Python libraries:
```bash
pip install spotipy python-dotenv
```
3. Create a Spotify Developer account and register a new application to get your API credentials (Client ID, Client Secret, and Redirect URI).
4. Create a .env file in the same directory as your Python script and add your API credentials:
```makefile
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_uri
SLEEP_DELAY=10
```
5. Replace your_client_id, your_client_secret, and your_redirect_uri with your actual API credentials.

### Obtaining Spotify API Credentials
1. Go to the Spotify Developer Dashboard: https://developer.spotify.com/dashboard/applications
2. Log in with your Spotify account or sign up for a new account if you don't have one.
3. Click on the "Create an App" button.
4. Fill in the required information for your new app (name, description, etc.) and click "Create" at the bottom of the form.
5. Once your app is created, you'll be redirected to the app's dashboard, where you'll find your `Client ID` and `Client Secret`. Copy these values.
6. Click on the "Edit Settings" button in the app's dashboard.
7. In the "Redirect URIs" field, enter a valid redirect URI for your application. For local development, you can use http://localhost:8888/callback/. Make sure to include the trailing slash. Click "Add" and then click "Save" at the bottom of the form.
8. Copy the Redirect URI you just added.

Now you have your Spotify API credentials: Client ID, Client Secret, and Redirect URI. Add these values to your `.env` file as described above.

## Usage
Run the script by executing the following command:

```bash
python twitch_spotify_spy.py
```

The script will create or update a file named `current_song.txt` in the same directory, containing the currently playing song and artist on your Spotify account.

To stop the script, press Ctrl+C in the terminal.

## Testing
To run the tests, execute the following command:

```bash
python test_twitch_spotify_spy.py
```

This will run the test cases and report the results.
