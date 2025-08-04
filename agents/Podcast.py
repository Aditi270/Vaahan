from gtts import gTTS
import os

def generate_audio(summary_text, filename="audio/summary.mp3"):
    # Create directory if it exists and is not empty
    dirname = os.path.dirname(filename)
    if dirname:  # Only create directory if dirname is not empty
        os.makedirs(dirname, exist_ok=True)
    tts = gTTS(summary_text)
    tts.save(filename)
    print(f"Audio saved to {filename}")