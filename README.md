# 🩺 AI Doctor VoiceBot

AI Doctor VoiceBot is a multimodal application that allows users to describe symptoms through voice, upload a medical image (such as a skin condition), and receive a realistic doctor-style response both in text and voice form. It combines speech recognition, image understanding, and language generation, powered by the Groq API.

---

## ✨ Features

- 🎤 Voice input recording using `sounddevice`
- 🧠 Speech-to-text using Whisper via Groq API
- 🖼️ Medical image analysis using LLaMA Vision models
- 💬 Human-like doctor responses based on symptoms and image
- 🔊 Text-to-speech using Google TTS (`gTTS`)
- 🌐 Web interface using Gradio

---

## 🛠️ Technologies Used

| Component           | Technology              |
|---------------------|--------------------------|
| User Interface      | Gradio                   |
| Audio Input         | sounddevice, soundfile   |
| Speech-to-Text      | Whisper (Groq API)       |
| Image Reasoning     | LLaMA Vision (Groq API)  |
| Text-to-Speech      | gTTS (Google TTS)        |
| Environment Config  | dotenv (`.env`)          |
| Audio Conversion    | Pydub (optional)         |

---

## 🧠 How It Works

1. **🎤 Patient speaks** a symptom or concern using the microphone.
2. **📄 Whisper model** (via Groq API) transcribes the speech to text.
3. **🖼️ Patient uploads** an image (e.g., skin condition, rash, etc.).
4. **🧠 LLaMA Vision model** analyzes the image and combines it with the transcribed symptom.
5. **🩺 A doctor-style response** is generated using Groq’s multimodal LLM.
6. **🔊 gTTS** converts the response to speech and plays it back to the user.

This creates a smooth multimodal flow from patient input to intelligent, human-like AI response.

### 📷 Example UI

<img width="488" alt="Voicebot_UI" src="https://github.com/user-attachments/assets/f433c0dc-4bc0-4efd-b260-f476e18dcbe0" />


## 🗂️ Project Structure

ai-doctor-voicebot/
├── brain_of_the_doctor.py # Image processing and Groq Vision query
├── voice_of_the_patient.py # Audio recording and transcription logic
├── voice_of_the_doctor.py # Text-to-speech conversion using gTTS
├── voice_doctor_ui.py # Main Gradio interface
├── requirements.txt # Python dependencies
├── .env # Environment variables (not pushed to GitHub)
└── README.md # Project documentation

## ⚙️ Setup Instructions

# Project Setup Guide – AI Doctor VoiceBot

## 1. Clone the repository

git clone https://github.com/Huzaifa-202/ai-doctor-voicebot.git
cd ai-doctor-voicebot

## 2. Create and activate a virtual environment

python -m venv ai-medical-voicebot
ai-medical-voicebot\Scripts\activate

## 3. Install dependencies

pip install -r requirements.txt

## 4. Add your Groq API key

Create a `.env` file in the root directory with the following content:

GROQ_API_KEY=your_groq_api_key_here

## 5. Run the app

python voice_doctor_ui.py

Open your browser and go to:

http://localhost:7860

## 📦 Dependencies

gradio
sounddevice
soundfile
gtts
pydub
python-dotenv
groq
ffmpeg

## 🙏 Acknowledgements

Groq – for high-speed inference with Whisper and LLaMA

OpenAI Whisper – for transcription

Google TTS (gTTS) – for text-to-speech

Gradio – for the user interface

Pydub – for audio conversion


