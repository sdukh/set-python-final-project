import os
import json
import time
import whisper


def transcribe_audio(audio_path: str) -> dict[str, any]:
    start_time = time.time()
    print("--- START ---", time.ctime(start_time))

    model = whisper.load_model("base.en")

    result = model.transcribe(audio_path)
    print(f"--- TRANSCRIBED: {int(time.time() - start_time)} seconds ---")
    return result


def write_results(
    result: dict[str, any], transcripts_dir_name: str, filename_no_ext: str
) -> None:
    os.makedirs(transcripts_dir_name, exist_ok=True)

    results_path = os.path.join(transcripts_dir_name, f"{filename_no_ext}.json")
    with open(results_path, "w") as f:
        json.dump(result, f, indent=4)
        print(f"--- RESULTS SAVED: {results_path} ---")
