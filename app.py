import streamlit as st
from gtts import gTTS
import os

# Title
st.title("🌐 Text to Speech App by Raj")

# Language selection
lang_option = st.selectbox(
    "Select Language:",
    ("English", "Hindi", "Tamil")
)

# Map language names to gTTS language codes
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta"
}

# Text input
text = st.text_area("Enter text to convert into speech:")

# Button
if st.button("Speak"):
    if text.strip() != "":
        # Convert text to speech
        tts = gTTS(text=text, lang=lang_map[lang_option])
        tts.save("speech.mp3")

        # Play in browser
        audio_file = open("speech.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

        st.success(f"Speech generated successfully in {lang_option}!")
    else:
        st.warning("⚠️ Please enter some text.")
