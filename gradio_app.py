from dotenv import load_dotenv
load_dotenv()

# Step 1: Imports
import os
import gradio as gr

# ✅ Use your existing logic
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts  # ← import from your own module

# Step 2: System prompt
system_prompt = """You have to act as a professional doctor, I know you are not but this is for learning purpose. 
What's in this image? Do you find anything wrong with it medically? If you make a differential, suggest some remedies for them. 
Do not add any numbers or special characters in your response. Your response should be in one long paragraph. 
Also always answer as if you are answering to a real person. Do not say 'In the image I see' but say 
'With what I see, I think you have ....' Do not respond as an AI model in markdown, your answer should mimic 
that of an actual doctor not an AI bot. Keep your answer concise (max 2 sentences). 
No preamble, start your answer right away please."""

# Step 3: Main processing function
def process_inputs(audio_filepath, image_filepath):
    # 1. STT
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    # 2. LLM + image
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    # 3. TTS with gTTS
    gtts_path = "final.mp3"
    text_to_speech_with_gtts(input_text=doctor_response, output_filepath=gtts_path)

    return speech_to_text_output, doctor_response, gtts_path

# Step 4: Gradio UI
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Patient's Voice"),
        gr.Image(type="filepath", label="Image of Skin / Body")
    ],
    outputs=[
        gr.Textbox(label="Transcribed Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice (TTS)")
    ],
    title="🩺 AI Doctor with Vision and Voice (gTTS only)"
)

iface.launch(server_name="0.0.0.0", server_port=7860, debug=True)

