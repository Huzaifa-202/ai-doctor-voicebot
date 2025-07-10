# gtts_handler.py

import os
import platform
import subprocess
from gtts import gTTS
import uuid

def text_to_speech_with_gtts(input_text, output_filepath=None, play=False):
    """
    Generate TTS from text using gTTS and optionally play the file.
    
    Args:
        input_text (str): Text to convert to speech.
        output_filepath (str, optional): Output file path. Defaults to UUID-based .mp3.
        play (bool): Whether to play the audio automatically.

    Returns:
        str: Path to the generated MP3 file.
    """
    if not input_text:
        return None

    language = "en"
    if output_filepath is None:
        output_filepath = f"{uuid.uuid4()}.mp3"

    try:
        tts = gTTS(text=input_text, lang=language, slow=False)
        tts.save(output_filepath)
        print(f"✅ Audio saved to {output_filepath}")

        if play:
            os_name = platform.system()
            if os_name == "Darwin":
                subprocess.run(['afplay', output_filepath])
            elif os_name == "Windows":
                subprocess.run(['start', output_filepath], shell=True)  # Uses default player
            elif os_name == "Linux":
                subprocess.run(['mpg123', output_filepath])
            else:
                raise OSError("Unsupported OS for playback")

        return output_filepath

    except Exception as e:
        print(f"❌ Error during TTS or playback: {e}")
        return None
