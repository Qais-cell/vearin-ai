import streamlit as st
from groq import Groq

# إعدادات الصفحة
st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

# --- مفتاح Groq المدمج والمحدث تلقائياً في الخلفية ---
MASTER_GROQ_KEY = "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"

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
        .login-card {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 35px;
            max-width: 420px;
            margin: 40px auto;
            box-shadow: 0 16px 32px rgba(1, 4, 9, 0.8);
        }
        .login-title {
            font-size: 24px;
            font-weight: 600;
            color: #f0f6fc;
            text-align: center;
            margin-bottom: 8px;
        }
        .login-subtitle {
            font-size: 13px;
            color: #8b949e;
            text-align: center;
            margin-bottom: 25px;
        }
        .stButton button {
            background-color: #21262d !important;
            color: #c9d1d9 !important;
            font-weight: 500;
            border-radius: 6px !important;
            border: 1px solid rgba(240, 246, 252, 0.1) !important;
            width: 100%;
            margin-bottom: 10px;
            padding: 10px;
            text-align: center;
        }
        .stButton button:hover {
            background-color: #30363d !important;
            border-color: #8b949e !important;
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">Sign in to VAERIN</div>
