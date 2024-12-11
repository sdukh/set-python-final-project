import os
import re
import yt_dlp


def sanitize_and_snake_case(filename):
    filename = re.sub(r'[\\/*?:"<>|\'’]', "", filename)
    filename = re.sub(r"\s+", "_", filename).lower()
    return filename


def download_audio(video_url, output_path):
    os.makedirs(output_path, exist_ok=True)

    ydl_opts_info = {
        "format": "bestaudio/best",
    }

    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        result = ydl.extract_info(video_url, download=False)
        video_title = result.get("title", "downloaded_audio")
        sanitized_title = sanitize_and_snake_case(video_title)
        audio_filename = f"{sanitized_title}.mp3"

    ydl_opts_download = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": os.path.join(output_path, f"{sanitized_title}.%(ext)s"),
    }

    with yt_dlp.YoutubeDL(ydl_opts_download) as ydl:
        ydl.download([video_url])

    full_output_path = os.path.join(output_path, audio_filename)

    if os.path.exists(full_output_path):
        print(f"File successfully downloaded and saved as: {full_output_path}")
    else:
        print(f"Failed to download file to: {full_output_path}")

    return {
        "title": video_title,
        "filename": audio_filename,
    }
