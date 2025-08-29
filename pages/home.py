import streamlit as st
from gtts import gTTS

# -----------------------
# Page Setup
# -----------------------
st.set_page_config(page_title="EchoVerse 🎧 by Team AMBUZZIN", layout="wide")

# Sidebar Info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3208/3208707.png", width=100)  # small audiobook icon
    st.title("📚 EchoVerse")
    st.markdown(
        """
        **EchoVerse** 🎧  
        An AI-powered tool that transforms your **text into natural-sounding audiobooks**.  
        
        Built with ❤️ by **Team AMBUZZIN** 🚀
        """
    )
    st.markdown("---")
    st.caption("💡 Tip: Try different tones to make your story more dramatic or inspiring!")

# -----------------------
# Title
# -----------------------
st.title("✨🎧 EchoVerse - AI Audiobook Creator")
st.markdown("Turn your words into **immersive, expressive audio** in just a few clicks. 🪄")

st.markdown("---")

# -----------------------
# Input Section
# -----------------------
st.header("📖 Enter Your Story / Text")
input_text = st.text_area("✍️ Paste your text below or upload a file", height=200)

upload_file = st.file_uploader("📂 Upload a `.txt` file", type=["txt"])
if upload_file is not None:
    input_text = upload_file.read().decode("utf-8")
    st.success("✅ File uploaded successfully!")
    with st.expander("📜 View Uploaded Content"):
        st.info(input_text)

st.markdown("---")

# -----------------------
# Options
# -----------------------
st.subheader("🎭 Narration Settings")

tone = st.radio("🎶 Choose a narration style:", 
                [" Neutral", " Suspenseful", " Inspiring"], horizontal=True)

voice = st.selectbox("🎤 Choose a voice:", ["👩 girl", "🧑 male", "👨 sigma"])

st.markdown("---")

# -----------------------
# Tone-Adaptive Rewriting
# -----------------------
st.header("📝 Adapt Your Story")
if "rewritten_text" not in st.session_state:
    st.session_state["rewritten_text"] = ""

col1, col2 = st.columns(2)

with col1:
    if st.button("✨ Rewrite & Adapt Text"):
        if input_text.strip() == "":
            st.error("⚠️ Please provide some text first!")
        else:
            st.session_state["rewritten_text"] = f"[{tone} with {voice}] {input_text}"
            st.success("✅ Text successfully adapted!")

with col2:
    if st.button("🔄 Reset"):
        st.session_state["rewritten_text"] = ""
        input_text = ""
        st.experimental_rerun()

if st.session_state["rewritten_text"]:
    st.markdown("**📜 Original Text:**")
    st.write(input_text)
    st.markdown("**📝 Adapted Text:**")
    st.success(st.session_state["rewritten_text"])

st.markdown("---")

# -----------------------
# Narration
# -----------------------
st.header("🎧 Generate Your Audiobook")

if st.button("🎙️ Create Audio"):
    if st.session_state["rewritten_text"].strip() == "":
        st.error("⚠️ Please rewrite the text first!")
    else:
        tts = gTTS(text=st.session_state["rewritten_text"], lang="en")
        audio_file = "audiobook.mp3"
        tts.save(audio_file)

        st.audio(audio_file, format="audio/mp3")

        with open(audio_file, "rb") as f:
            st.download_button(
                "⬇️ Download Audiobook",
                data=f,
                file_name="audiobook.mp3",
                mime="audio/mp3"
            )

        st.balloons()
        st.success("🎉 Your audiobook is ready! Sit back, relax & enjoy listening. 🎶")
