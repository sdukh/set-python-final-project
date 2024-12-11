import os
from typing import Dict, List
from fastapi import FastAPI
from pydantic import BaseModel

from src.audio_transcriber import transcribe_audio, write_results
from src.youtube_downloader import download_audio
from utils.utils import process_whisper_segments


class YoutubeUrl(BaseModel):
    url: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/transcribe")
def transcribe(url: YoutubeUrl):
    try:
        video_url = url.url
        audio_path = "./data/audio_files"
        transcript_dir = "./data/transcripts"

        print("Downloading audio...")
        audio_filename = download_audio(video_url, audio_path)

        full_audio_path = os.path.join(audio_path, audio_filename)

        print(f"Full audio path: {full_audio_path}")
        if not os.path.isfile(full_audio_path):
            raise FileNotFoundError(f"Audio file not found at path: {full_audio_path}")

        print("Transcribing audio...")
        transcription_result = transcribe_audio(full_audio_path)

        filename_no_ext = os.path.splitext(audio_filename)[0]
        write_results(transcription_result, transcript_dir, filename_no_ext)

        segments = process_whisper_segments(transcription_result["segments"])

        combined_transcript = "\n".join(
            [f"[{item['start']}-{item['end']}] {item['text']}" for item in segments]
        )

        return {
            "message": "Transcription successful",
            "video_title": filename_no_ext,
            "segments": combined_transcript,
        }
    except BaseException as e:
        print(f"An error occurred: {str(e)}")
        return {
            "error": "An error occurred during the transcription process",
            "details": str(e),
        }
