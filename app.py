# app.py
import streamlit as st
from utils.auth import validate_token

# -----------------------
# Page Setup
# -----------------------
st.set_page_config(page_title="EchoVerse Login", page_icon="🎧", layout="centered")

# -----------------------
# Custom CSS
# -----------------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1d2671, #c33764);
        font-family: 'Segoe UI', sans-serif;
    }
    /* Glassmorphism card */
    .login-box {
        background: rgba(255, 255, 255, 0.08);
        padding: 2.5rem;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        color: white;
        max-width: 420px;
        margin: auto;
    }
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #ffffffaa;
        padding: 12px;
        font-size: 16px;
        background-color: #ffffff15;
        color: white;
    }
    .stTextInput > div > div > input::placeholder {
        color: #e0e0e0;
    }
    .stButton button {
        border-radius: 12px;
        background: linear-gradient(90deg, #ff7b54, #ff5722);
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 22px;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #ff5722, #e64a19);
        transform: scale(1.05);
    }
    footer {
        color: #ddd;
        text-align: center;
        font-size: 14px;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# Login Section
# -----------------------
st.markdown("<div class='login-box'>", unsafe_allow_html=True)

st.image("https://cdn-icons-png.flaticon.com/512/3208/3208707.png", width=80)  # audiobook icon
st.title("🎧 EchoVerse")
st.subheader("Login with your Hugging Face Token")

# Token input
token = st.text_input("🔑 Enter your Hugging Face Token", type="password")

if st.button("🚀 Login"):
    is_valid, username = validate_token(token)
    if is_valid:
        st.success(f"✅ Welcome {username}!")
        st.session_state["hf_token"] = token
        st.session_state["logged_in"] = True
        st.switch_page("pages/home.py")   # redirect to home
    else:
        st.error("❌ Invalid Token. Please try again.")

# Reset session
if st.button("🔄 Clear Session"):
    for key in ["hf_token", "logged_in"]:
        if key in st.session_state:
            del st.session_state[key]
    st.info("Session cleared. You can login again.")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------
# Footer
# -----------------------
st.markdown(
    "<footer>✨ Built with ❤️ by <b>Team AMBUZZIN</b> | Powered by Hugging Face & Streamlit</footer>",
    unsafe_allow_html=True
)
