# Spotify2MP3

## Description:

Spotify2MP3 is a versatile and user-friendly application that empowers you to convert your favorite Spotify playlists and songs into MP3 format. Seamlessly transfer your music from the streaming platform to your local library, making it accessible offline and on any device. Enjoy your Spotify tracks without restrictions, anytime, anywhere, with Spotify2MP3.

## Demo

https://github.com/IgnatEduardo/Spotify2MP3/assets/81325426/714fab5e-0431-4f7f-b1b7-56ead7c3ae25

## Setup

### Prerequisites:

- Python installed on your system.
- Valid Spotify and YouTube API credentials.

___

### Steps:
1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

3. Change your working directory to the app folder:

   ```bash
   cd flaskapp
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
___
### API Credentials:

**Spotify Credentials:**
- Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to obtain your client ID and client secret.
- Configure them in the `config.json` file under the following keys:
  - `"SPOTIFY_CLIENT_ID"`
  - `"SPOTIFY_CLIENT_SECRET"`

**YouTube API Credentials:**
- Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a project to get the API key.
- Set the API key in the `config.json` file under the key:
  - `"YOUTUBE_API_KEY"`

___

## Run the App

1. Make sure you are in the virtual environment.

2. Set the Python interpreter to use the virtual environment.

3. In the terminal, run the Flask app:

   ```bash
   flask run
   ```

4. Open a web browser and navigate to [http://localhost:5000/](http://localhost:5000/) to access the app.

___

## Usage

- Enter a Spotify playlist URL and click "Convert" to convert the playlist to MP3 files sourced from YouTube.


The app assumes the following folder structure:

## Important Note

- You must have valid Spotify and YouTube API credentials. Configure them in the `config.json` file or via environment variables.
