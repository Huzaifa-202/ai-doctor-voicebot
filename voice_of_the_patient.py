import logging
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
from io import BytesIO
import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Setup logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ---------- Step 1: Record Audio (Commented out since file already exists) ----------
def record_audio(file_path="patient_voice_test.mp3", duration=10, samplerate=16000):
    try:
        logging.info("🎙️ Recording started...")
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()
        logging.info("✅ Recording complete.")

        wav_buffer = BytesIO()
        sf.write(wav_buffer, audio, samplerate, format='WAV')
        wav_buffer.seek(0)

        audio_segment = AudioSegment.from_file(wav_buffer, format="wav")
        audio_segment.export(file_path, format="mp3", bitrate="128k")
        logging.info(f"💾 MP3 saved to {file_path}")

    except Exception as e:
        logging.error(f"❌ Error: {e}")

# ---------- Step 2: Transcribe Using GROQ Whisper ----------
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is missing. Make sure it's in your .env file.")

stt_model = "whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )

    print("📝 Transcription:", transcription.text)
    return transcription.text