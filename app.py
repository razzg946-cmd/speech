import streamlit as st
from deep_translator import GoogleTranslator
from io import BytesIO
import edge_tts
import asyncio
import base64

with open("Rlogo.png", "rb") as f:
    logo_data = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{logo_data}" width="140">
        <h1 style="color:#1E88E5; margin-top:10px;">
        
        </h1>
        <p style="font-size:18px;">
            Translate text and convert it into natural AI voice speech
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
# -----------------------
# Language Map (UPDATED)
# -----------------------
lang_map = {
    "English": "en",
    "Hindi": "hi",

    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",

    "Marathi": "mr",
    "Gujarati": "gu",
   

    "Bengali": "bn",
    "Odia": "or",   
    "Urdu": "ur",
  

    # 🌏 NEW ADDITIONS
    "Thai": "th",
    "Chinese (Mandarin)": "zh-CN"
}

# -----------------------
# Voice Map (UPDATED)
# -----------------------
voice_map = {
    "English": {"Male": "en-US-GuyNeural", "Female": "en-US-JennyNeural"},
    "Hindi": {"Male": "hi-IN-MadhurNeural", "Female": "hi-IN-SwaraNeural"},
    "Tamil": {"Male": "ta-IN-ValluvarNeural", "Female": "ta-IN-PallaviNeural"},
    "Telugu": {"Male": "te-IN-MohanNeural", "Female": "te-IN-ShrutiNeural"},
    "Kannada": {"Male": "kn-IN-GaganNeural", "Female": "kn-IN-SapnaNeural"},
    "Malayalam": {"Male": "ml-IN-MidhunNeural", "Female": "ml-IN-SobhanaNeural"},
    "Marathi": {"Male": "mr-IN-ManoharNeural", "Female": "mr-IN-AarohiNeural"},
    "Gujarati": {"Male": "gu-IN-NiranjanNeural", "Female": "gu-IN-DhwaniNeural"},
   
    "Bengali": {"Male": "bn-IN-BashkarNeural", "Female": "bn-IN-TanishaaNeural"},
    "Odia": {"Male": "en-US-GuyNeural", "Female": "en-US-JennyNeural"},
   
   
    "Urdu": {"Male": "ur-PK-AsadNeural", "Female": "ur-PK-UzmaNeural"},
    
    # 🌏 NEW VOICES
    "Thai": {
        "Male": "th-TH-NiwatNeural",
        "Female": "th-TH-PremwadeeNeural"
    },
    "Chinese (Mandarin)": {
        "Male": "zh-CN-YunxiNeural",
        "Female": "zh-CN-XiaoxiaoNeural"
    }
}

# -----------------------
# Safe Voice Getter
# -----------------------
def get_voice(lang, gender):
    return voice_map.get(lang, voice_map["English"]).get(gender, "en-US-GuyNeural")

# -----------------------
# Translation Function
# -----------------------
def translate_text(text, src_lang, tgt_lang):
    if src_lang == tgt_lang:
        return text

    translator = GoogleTranslator(source=src_lang, target=tgt_lang)
    return translator.translate(text)

# -----------------------
# TTS Function
# -----------------------
async def generate_audio(text, voice):
    communicate = edge_tts.Communicate(text=text, voice=voice)

    audio_data = b""

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]

    return BytesIO(audio_data)

def text_to_speech(text, voice):
    return asyncio.run(generate_audio(text, voice))

# -----------------------
# UI Inputs
# -----------------------
input_lang = st.selectbox("Input Language", list(lang_map.keys()))
output_lang = st.selectbox("Output Language", list(lang_map.keys()))
voice_gender = st.selectbox("Voice Type", ["Male", "Female"])

text = st.text_area("Enter Text", placeholder="Type something...")

# -----------------------
# Action Button
# -----------------------
if st.button("Translate & Speak"):

    if not text.strip():
        st.warning("Please enter text first!")

    else:
        try:
            src_code = lang_map[input_lang]
            tgt_code = lang_map[output_lang]

            with st.spinner("Translating..."):
                translated_text = translate_text(text, src_code, tgt_code)

            st.subheader("Translated Text")
            st.write(translated_text)

            voice = get_voice(output_lang, voice_gender)

            with st.spinner("Generating Voice..."):
                audio_file = text_to_speech(translated_text, voice)

            st.subheader("Audio Output")

            st.audio(audio_file, format="audio/mp3")

            audio_file.seek(0)

            st.download_button(
                label="⬇ Download MP3",
                data=audio_file,
                file_name="rvoice_output.mp3",
                mime="audio/mpeg"
            )

            st.success("Voice generated successfully")

        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Rvoice © Founder - Raj Gupta")
