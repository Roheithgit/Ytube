from flask import Flask, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/download/<yturl>')
def download_video(yturl):
    def download(link, download_path):
        try:
            youtube_object = YouTube(f"https://www.youtube.com/watch?v={link}")
            video_stream = youtube_object.streams.get_highest_resolution()
            video_stream.download(output_path=download_path)
            return os.path.join(download_path, youtube_object.title + ".mp4")
        except Exception as e:
            return f"An error has occurred: {str(e)}"

    download_path = "your_download_directory"  # Replace with your desired download directory
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    video_path = download(yturl, download_path)

    # Send the file as an attachment with the specified filename
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
