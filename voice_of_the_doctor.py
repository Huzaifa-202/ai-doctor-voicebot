# Step 1: Text to Speech using gTTS
import os
import platform
import subprocess
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath="gtts_output.mp3"):
    language = "en"

    try:
        # Generate audio
        audioobj = gTTS(text=input_text, lang=language, slow=False)
        audioobj.save(output_filepath)
        print(f"✅ Audio saved to {output_filepath}")

        # Play audio based on OS
        os_name = platform.system()
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Or use mpg123, ffplay etc.
        else:
            raise OSError("Unsupported operating system")

    except Exception as e:
        print(f"❌ Error during TTS or playback: {e}")

# Example usage
input_text = "Hi! This is your AI assistant speaking using gTTS."
text_to_speech_with_gtts(input_text)
