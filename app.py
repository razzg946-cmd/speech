import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
from io import BytesIO

st.set_page_config(page_title="Text to Speech & Translation", layout="centered")
st.title("Text to Speech & Translation App by Raj")

# Language selection
input_lang = st.selectbox("Select Input Language:", ("English", "Hindi", "Tamil"))
output_lang = st.selectbox("Select Output Language (for speech):", ("English", "Hindi", "Tamil"))

# Map language names to codes used by translators / gTTS
lang_map = {"English": "en", "Hindi": "hi", "Tamil": "ta"}

text = st.text_area("Enter text to translate & speak:")

def translate_text(text, src_code, tgt_code):
    # use deep-translator's GoogleTranslator
    # if src_code == tgt_code we skip translation
    if src_code == tgt_code:
        return text
    # deep-translator's GoogleTranslator accepts language codes like 'en','hi','ta'
    return GoogleTranslator(source=src_code, target=tgt_code).translate(text)

def text_to_audio_bytes(text, lang_code):
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang=lang_code)
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp

if st.button("Translate & Speak"):
    if not text.strip():
        st.warning(" Please enter some text.")
    else:
        try:
            src = lang_map[input_lang]
            tgt = lang_map[output_lang]

            with st.spinner("Translating..."):
                translated = translate_text(text, src, tgt)

            st.markdown(f"**Translated Text ({output_lang}):**")
            st.write(translated)

            with st.spinner("Generating speech..."):
                audio_bytes = text_to_audio_bytes(translated, tgt)

            st.audio(audio_bytes.read(), format="audio/mp3")
            st.success(f"Speech generated successfully in {output_lang}!")
        except Exception as e:
            st.error(f" Error: {e}")
            st.caption("If you see an error, copy-paste the full error here so I can help debug.")

