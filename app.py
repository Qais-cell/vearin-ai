import streamlit as st
import re

st.set_page_config(page_title="VÆRIN Neural Canvas // Art Academy", page_icon="🎨", layout="centered")

# إدارة حالة التطبيق للبدء فوراً وبدون أي شاشة بيضاء أو تعليق
if "app_state" not in st.session_state:
    st.session_state.app_state = "canvas_home"
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "art_track" not in st.session_state:
    st.session_state.art_track = "الأساسيات والمنظور الأولائي"

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# --- تصميم عصري وفاخر جداً مستوحى من xAI / Groq / Gemini (Dark Futuristic Theme) ---
st.markdown("""
    <style>
    @keyframes textShimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes pulseGlow {
        0% { filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.2)); }
        50% { filter: drop-shadow(0 0 20px rgba(138, 43, 226, 0.6)); }
        100% { filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.2)); }
    }
    .stApp {
        background: #050505;
        color: #e6edf3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .hero-title {
        font-size: 38px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #ffffff 0%, #a855f7 50%, #6366f1 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShimmer 4s infinite linear, pulseGlow 3s infinite ease-in-out;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        font-size: 14px;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 30px;
    }
    .art-card {
        background: #0d0d11;
        border: 1px solid #1e1e2d;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    .art-card:hover {
        border-color: #8b5cf6;
        background: #13131c;
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.2);
    }
    .card-title {
        font-size: 17px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .card-desc {
        font-size: 13px;
        color: #94a3b8;
        line-height: 1.5;
    }
    .badge {
        display: inline-block
