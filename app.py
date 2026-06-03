import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="Text to Speech & Translation",
    page_icon="🎙️",
    layout="centered"
)

# App Title
st.title("🎙️ Text to Speech & Translation Demo by Raj")
st.write("Translate text between multiple languages and generate speech.")

# Supported Languages
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Thai": "th"
}

# Language Selection
input_lang = st.selectbox(
    "Select Input Language:",
    list(lang_map.keys())
)

output_lang = st.selectbox(
    "Select Output Language (for Speech):",
    list(lang_map.keys())
)

# Text Input
text = st.text_area(
    "Enter text to translate & speak:",
    height=150,
    placeholder="Type your text here..."
)


def translate_text(text, src_code, tgt_code):
    """
    Translate text using Google Translator
    """
    if src_code == tgt_code:
        return text

    return GoogleTranslator(
        source=src_code,
        target=tgt_code
    ).translate(text)


def text_to_audio_bytes(text, lang_code):
    """
    Convert text to speech and return audio bytes
    """
    mp3_fp = BytesIO()

    tts = gTTS(
        text=text,
        lang=lang_code,
        slow=False
    )

    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    return mp3_fp


# Translate & Speak Button
if st.button("🚀 Translate & Speak", use_container_width=True):

    if not text.strip():
        st.warning("⚠️ Please enter some text.")

    else:
        try:
            src = lang_map[input_lang]
            tgt = lang_map[output_lang]

            # Translation
            with st.spinner("🌍 Translating..."):
                translated_text = translate_text(
                    text,
                    src,
                    tgt
                )

            st.subheader("📄 Translated Text")
            st.success(translated_text)

            # Speech Generation
            with st.spinner("🔊 Generating Speech..."):
                audio_bytes = text_to_audio_bytes(
                    translated_text,
                    tgt
                )

            st.subheader("🎧 Audio Output")
            st.audio(
                audio_bytes.read(),
                format="audio/mp3"
            )

            # Download Button
            audio_bytes.seek(0)

            st.download_button(
                label="⬇️ Download MP3",
                data=audio_bytes,
                file_name="translated_speech.mp3",
                mime="audio/mpeg"
            )

            st.success(
                f"✅ Speech generated successfully in {output_lang}!"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.caption(
                "If you see an error, copy and paste the full error message so I can help debug it."
            )

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ using Streamlit, Google Translator, and gTTS"
)import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="Text to Speech & Translation",
    page_icon="🎙️",
    layout="centered"
)

# App Title
st.title("🎙️ Text to Speech & Translation App by Raj")
st.write("Translate text between multiple languages and generate speech.")

# Supported Languages
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Thai": "th"
}

# Language Selection
input_lang = st.selectbox(
    "Select Input Language:",
    list(lang_map.keys())
)

output_lang = st.selectbox(
    "Select Output Language (for Speech):",
    list(lang_map.keys())
)

# Text Input
text = st.text_area(
    "Enter text to translate & speak:",
    height=150,
    placeholder="Type your text here..."
)


def translate_text(text, src_code, tgt_code):
    """
    Translate text using Google Translator
    """
    if src_code == tgt_code:
        return text

    return GoogleTranslator(
        source=src_code,
        target=tgt_code
    ).translate(text)


def text_to_audio_bytes(text, lang_code):
    """
    Convert text to speech and return audio bytes
    """
    mp3_fp = BytesIO()

    tts = gTTS(
        text=text,
        lang=lang_code,
        slow=False
    )

    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    return mp3_fp


# Translate & Speak Button
if st.button("🚀 Translate & Speak", use_container_width=True):

    if not text.strip():
        st.warning("⚠️ Please enter some text.")

    else:
        try:
            src = lang_map[input_lang]
            tgt = lang_map[output_lang]

            # Translation
            with st.spinner("🌍 Translating..."):
                translated_text = translate_text(
                    text,
                    src,
                    tgt
                )

            st.subheader("📄 Translated Text")
            st.success(translated_text)

            # Speech Generation
            with st.spinner("🔊 Generating Speech..."):
                audio_bytes = text_to_audio_bytes(
                    translated_text,
                    tgt
                )

            st.subheader("🎧 Audio Output")
            st.audio(
                audio_bytes.read(),
                format="audio/mp3"
            )

            # Download Button
            audio_bytes.seek(0)

            st.download_button(
                label="⬇️ Download MP3",
                data=audio_bytes,
                file_name="translated_speech.mp3",
                mime="audio/mpeg"
            )

            st.success(
                f"✅ Speech generated successfully in {output_lang}!"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.caption(
                "If you see an error, copy and paste the full error message so I can help debug it."
            )

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ using Streamlit, Google Translator, and gTTS"
)
