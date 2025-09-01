import streamlit as st
from gtts import gTTS
import os

st.title("Text to Speech App by Raj ")

text = st.text_area("Enter text to convert into speech:")

if st.button("Speak"):
    if text.strip() != "":
        # Convert text to speech
        tts = gTTS(text=text, lang="en")
        tts.save("speech.mp3")

        # Play in browser
        audio_file = open("speech.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

        st.success("✅ Speech generated successfully!")
    else:
        st.warning("⚠️ Please enter some text.")


