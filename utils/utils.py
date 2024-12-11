# Function to format timestamps in HH:MM:SS format
def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


# Function to process Whisper response segments
def process_whisper_segments(segments):
    processed_segments = [
        {
            "start": format_timestamp(segment["start"]),
            "end": format_timestamp(segment["end"]),
            "text": segment["text"].strip(),
        }
        for segment in segments
    ]
    return processed_segments
