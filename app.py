import streamlit as st
from groq import Groq
import re

st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "show_intro" not in st.session_state:
    st.session_state.show_intro = True

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# --- مرحلة الأنترو الترحيبي الحركي ---
if st.session_state.show_intro and not st.session_state.logged_in:
    st.markdown("""
        <style>
        @keyframes introPulse {
            0% { opacity: 0; transform: scale(0.95); }
            50% { opacity: 1; transform: scale(1.02); }
            100% { opacity: 1; transform: scale(1); }
        }
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        .intro-box {
            text-align: center;
            padding: 80px 20px;
            animation: introPulse 1.2s cubic-bezier(0.2, 0.8, 0.2, 1);
        }
        .intro-title {
            font-size: 36px;
            font-weight: 700;
            color: #f0f6fc;
            letter-spacing: -1px;
            margin-bottom: 10px;
        }
        .intro-sub {
            font-size: 15px;
            color: #8b949e;
            margin-bottom: 30px;
        }
        .stButton button {
            background-color: #238636 !important;
            color: #ffffff !important;
            font-weight: 600;
            border-radius: 8px !important;
            border: none !important;
            padding: 12px 30px;
            font-size: 15px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #2ea043 !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(35, 134, 54, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="intro-box">
            <div class="intro-title">VÆRIN Intelligence System</div>
            <div class="intro-sub">Next-Generation Autonomous Academic Environment</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("Initialize System"):
            st.session_state.show_intro = False
            st.rerun()
    st.stop()

# --- مرحلة تسجيل الدخول بالأنميشن ---
if not st.session_state.logged_in:
    st.markdown("""
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            animation: fadeIn 0.4s ease-out;
        }
        .stTextInput input {
            background-color: #161b22 !important;
            color: #c9d1d9 !important;
            border: 1px solid #30363d !important;
            border-radius: 8px !important;
            padding: 12px !important;
            transition: all 0.3s ease;
        }
        .stTextInput input:focus {
            border-color: #58a6ff !important;
            box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.15);
        }
        .stButton button {
            background-color: #21262d !important;
            color: #c9d1d9 !important;
            font-weight: 500;
            border-radius: 8px !important;
            border: 1px solid rgba(240, 246, 252, 0.15) !important;
            width: 100%;
            margin-top: 10px;
            padding: 12px;
            font-size: 14px;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .stButton button:hover {
            background-color: #30363d !important;
            border-color: #8
