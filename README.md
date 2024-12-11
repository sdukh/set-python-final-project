# YouTube Video Transcription Service

## Overview
This is a Proof of Concept (PoC) application that transcribes the audio of YouTube videos into text. It leverages the power of OpenAI's Whisper model for transcription and yt-dlp for downloading audio from YouTube videos. The service is built as a FastAPI-based API server.

## Features
- **Download YouTube video audio**: Extract and download the audio from a given YouTube video URL.
- **Transcribe audio**: Use Whisper, an advanced transcription model, to convert the downloaded audio into text.
- **Save and process transcripts**: Save transcription results in JSON format and generate structured transcripts with timestamps.

## Packages Used
- **[whisper](https://github.com/openai/whisper)**: For transcription.
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: For downloading audio from YouTube.
- **[fastapi](https://fastapi.tiangolo.com/)**: To create the API server.

## Installation

### Prerequisites
- Python 3.9 or higher
- [Poetry](https://python-poetry.org/): Dependency management tool

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/set-python-final-project.git
   cd set-python-final-project
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Usage

### Running the API Server
Start the FastAPI development server:
```bash
fastapi dev
```
The server will start at `http://127.0.0.1:8000` by default.

### Endpoints

#### 1. Root Endpoint
- **URL**: `GET /`
- **Description**: Health check endpoint to ensure the server is running.
- **Response**:
  ```json
  {
    "Hello": "World"
  }
  ```

#### 2. Transcription Endpoint
- **URL**: `POST /transcribe`
- **Description**: Takes a YouTube video URL and returns its transcription.
- **Request Body**:
  ```json
  {
    "url": "<YouTube Video URL>"
  }
  ```
- **Response**:
  - **Success**:
    ```json
    {
      "message": "Transcription successful",
      "video_title": "<Video Title>",
      "transcript": "<Transcribed Text>"
    }
    ```
  - **Error**:
    ```json
    {
      "error": "An error occurred during the transcription process",
      "details": "<Error Details>"
    }
    ```

### Testing
You can test the API using tools like Postman, Thunder Client, or curl.

#### Example Request
```http
POST http://127.0.0.1:8000/transcribe
Content-Type: application/json

{
  "url": "https://youtu.be/bzE-IMaegzQ?si=sk1NjJ4xR52ufduF"
}
```

#### Example Response
```json
{
  "message": "Transcription successful",
  "video_title": "example_video",
  "segments": "[00:00-00:10] Hello world.\n[00:10-00:20] Welcome to the transcription service."
}
```

## Project Structure
```
.
├── main.py                  # FastAPI application entry point
├── src
│   ├── audio_transcriber.py # Functions for audio transcription and saving results
│   ├── youtube_downloader.py # Functions for downloading YouTube audio
├── utils
│   └── utils.py             # Utility functions like segment processing
├── data
│   ├── audio_files          # Directory for downloaded audio files
│   └── transcripts          # Directory for saved transcription results
├── README.md                # Project documentation
└── pyproject.toml           # Poetry configuration file
```

---

Enjoy transcribing! 🎙️

