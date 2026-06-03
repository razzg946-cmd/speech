import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
from io import BytesIO

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Text to Speech & Translation",
    page_icon="🎙️",
    layout="centered"
)

# -------------------------
# Title
# -------------------------
st.title("🎙️ Text to Speech & Translation Demo by Raj")
st.write("Translate text and convert it into speech.")

# -------------------------
# Languages
# -------------------------
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Thai": "th"
    }

# -------------------------
# Language Selection
# -------------------------
input_lang = st.selectbox(
    "Select Input Language",
    list(lang_map.keys())
)

output_lang = st.selectbox(
    "Select Output Language",
    list(lang_map.keys())
)

# -------------------------
# Text Input
# -------------------------
text = st.text_area(
    "Enter Text",
    placeholder="Type something here..."
)

# -------------------------
# Translation Function
# -------------------------
def translate_text(text, src_lang, tgt_lang):
    if src_lang == tgt_lang:
        return text

    translator = GoogleTranslator(
        source=src_lang,
        target=tgt_lang
    )

    return translator.translate(text)

# -------------------------
# Text to Speech Function
# -------------------------
def text_to_speech(text, lang_code):
    audio_buffer = BytesIO()

    tts = gTTS(
        text=text,
        lang=lang_code,
        slow=False
    )

    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    return audio_buffer

# -------------------------
# Button
# -------------------------
if st.button(" Translate & Speak"):

    if not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            src_code = lang_map[input_lang]
            tgt_code = lang_map[output_lang]

            with st.spinner("Translating..."):
                translated_text = translate_text(
                    text,
                    src_code,
                    tgt_code
                )

            st.subheader("Translated Text")
            st.write(translated_text)

            with st.spinner("Generating Speech..."):
                audio_file = text_to_speech(
                    translated_text,
                    tgt_code
                )

            st.subheader("Audio")
            st.audio(audio_file, format="audio/mp3")

            audio_file.seek(0)

            st.download_button(
                label="⬇ Download MP3",
                data=audio_file,
                file_name="translated_speech.mp3",
                mime="audio/mpeg"
            )

            st.success(
                f"Speech generated successfully in {output_lang}"
            )

        except Exception as e:
            st.error(f"Error: {e}")

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.caption("Made with Streamlit + Google Translator + gTTS")
