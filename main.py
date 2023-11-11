from flask import Flask
import os

app = Flask(__name__)

""" 
This api's aim is to serve an web app to manage files on a removable mp3 drive.
The web app will be able to:
- list all files on the drive
- remove files from the drive
- add files to the drive
- play files on the drive
- use pytube to download youtube videos and save them to the drive
- manage breaking up long files into smaller files, since the mp3 doesnt allow fowarding within a file
- browse the drive by artist, album, genre, etc
- browse youtube by search query, then download and save to the drive
- download whole youtube playlists, or some subset of them
"""

@app.route('/')
def index():
    return "Api is running"

@app.route('/ext-drive/list')
def list_ext_drive():
    return "List of files on the external drive"

@app.route('/ext-drive/remove/<filename>')
def remove_from_ext_drive(filename):
    return "Removed file from external drive: " + filename

@app.route('/ext-drive/add/<filename>')
def add_to_ext_drive(filename):
    return "Added file to external drive: " + filename

@app.route('/ext-drive/play/<filename>')
def play_from_ext_drive(filename):
    return "Playing file from external drive: " + filename

@app.route('/youtube/search/<query>')
def search_youtube(query):
    return "Search youtube for: " + query

@app.route('/youtube/download/<video_id>')
def download_youtube(video_id):
    return "Download youtube video: " + video_id

@app.route('/youtube/download-playlist/<playlist_id>')
def download_youtube_playlist(playlist_id):
    return "Download youtube playlist: " + playlist_id

@app.route('/youtube/download-playlist/<playlist_id>/<start>/<end>')
def download_youtube_playlist_subset(playlist_id, start, end):
    return "Download youtube playlist: " + playlist_id + " from " + start + " to " + end


if __name__ == '__main__':
    app.run()
