import streamlit as st
from groq import Groq

# إعدادات الصفحة
st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

# تهيئة حالة جلسة تسجيل الدخول
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "selected_provider" not in st.session_state:
    st.session_state.selected_provider = ""

if not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        .login-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 75vh;
        }
        .login-card {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 40px 30px;
            width: 100%;
            max-width: 440px;
            box-shadow: 0 20px 40px rgba(1, 4, 9, 0.9);
            text-align: center;
        }
        .login-logo {
            font-size: 26px;
            font-weight: 700;
            color: #f0f6fc;
            margin-bottom: 8px;
            letter-spacing: -0.5px;
        }
        .login-subtitle {
            font-size: 14px;
            color: #8b949e;
            margin-bottom: 30px;
        }
        .stButton button {
            background-color: #21262d !important;
            color: #c9d1d9 !important;
            font-weight: 500;
            border-radius: 8px !important;
            border: 1px solid rgba(240, 246, 252, 0.15) !important;
            width: 100%;
            margin-bottom: 12px;
            padding: 12px;
            font-size: 14px;
        }
        .stButton button:hover {
            background-color: #30363d !important;
            border-color: #8b949e !important;
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-container"><div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="login-logo">VÆRIN Academic</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">Sign in to
