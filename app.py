import streamlit as st
from gtts import gTTS
from googletrans import Translator

# Title
st.title("🌐 Text to Speech & Translation App by Raj")

# Language selection for input and output
input_lang = st.selectbox(
    "Select Input Language:",
    ("English", "Hindi", "Tamil")
)

output_lang = st.selectbox(
    "Select Output Language (for speech):",
    ("English", "Hindi", "Tamil")
)

# Map language names to codes
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta"
}

# Text input
text = st.text_area("Enter text to translate & speak:")

# Button
if st.button("Translate & Speak"):
    if text.strip() != "":
        try:
            # Translate text
            translator = Translator()
            translated = translator.translate(text, 
                                              src=lang_map[input_lang], 
                                              dest=lang_map[output_lang])
            translated_text = translated.text

            st.write(f"**Translated Text ({output_lang}):** {translated_text}")

            # Convert translated text to speech
            tts = gTTS(text=translated_text, lang=lang_map[output_lang])
            tts.save("speech.mp3")

            # Play in browser
            audio_file = open("speech.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")

            st.success(f"Speech generated successfully in {output_lang}!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter some text.")
