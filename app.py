import streamlit as st
from groq import Groq
import re
import time

st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "show_intro" not in st.session_state:
    st.session_state.show_intro = True
if "show_setup" not in st.session_state:
    st.session_state.show_setup = False
if "study_goal" not in st.session_state:
    st.session_state.study_goal = "بحث علمي متقدم وتحليل عميق"

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# --- 1. مرحلة الأنترو التحريكي المطول والأسطوري ---
if st.session_state.show_intro and not st.session_state.logged_in:
    st.markdown("""
        <style>
        @keyframes introFlow {
            0% { opacity: 0; transform: scale(0.92); filter: blur(8px); }
            40% { opacity: 1; transform: scale(1); filter: blur(0px); }
            75% { opacity: 1; transform: scale(1.02); filter: blur(0px); }
            100% { opacity: 0; transform: scale(1.08); filter: blur(10px); }
        }
        .stApp {
            background: radial-gradient(circle at center, #161b22 0%, #0d1117 100%);
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .auto-intro {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: #0d1117;
            z-index: 99999;
            animation: introFlow 3.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        .intro-logo {
            font-size: 50px;
            font-weight: 800;
            background: linear-gradient(135deg, #f0f6fc 0%, #58a6ff 50%, #1f6feb 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
            letter-spacing: -2px;
        }
        .intro-desc {
            font-size: 15px;
            color: #8b949e;
            font-weight: 400;
            letter-spacing: 1px;
        }
        </style>
        <div class="auto-intro">
            <div class="intro-logo">VÆRIN AI</div>
            <div class="intro-desc">Autonomous Academic Intelligence & Research Workspace</div>
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(3.6)
    st.session_state.show_intro = False
    st.session_state.show_setup = True
    st.rerun()

# --- 2. مرحلة تخصيص الأهداف الدراسية وأسلوب التطبيق ---
if st.session_state.show_setup and not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .setup-title {
            text-align: center;
            font-size: 24px;
            font-weight: 700;
            color: #f0f6fc;
            margin-bottom: 5px;
        }
        .setup-sub {
            text-align: center;
            font-size: 13px;
            color: #8b949e;
            margin-bottom: 20px;
        }
        .stButton button {
            background-color: #238636 !important;
            color: #ffffff !important;
            font-weight: 600;
            border-radius: 8px !important;
            border: none !important;
            width: 100%;
            margin-top: 15px;
            padding: 12px;
        }
        .stButton button:hover {
            background-color: #2ea043 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="setup-title">Configure Academic Profile</div>', unsafe_allow_html=True)
        st.markdown('<div class="setup-sub">Customize your AI tutor environment and research objectives</div>', unsafe_allow_html=True)
        
        goal_selection = st.selectbox(
            "Primary Academic Objective:",
            [
                "بحث علمي متقدم وتحليل عميق",
                "شرح المناهج الدراسية وتبسيط النظريات",
                "تلخيص المقالات والكتب الأكاديمية",
                "استشارات برمجية وهندسية بحتة"
            ]
        )
        
        academic_style = st.radio(
            "Scholarly Interaction Mode:",
            ["صارم وأكاديمي بحت (بدون حشو)", "أكاديمي توجيهي مع أمثلة تفصيلية"]
        )
        
        if st.button("Continue to Authentication"):
            st.session_state.study_goal = goal_selection
            st.session_state.academic_style = academic_style
            st.session_state.show_setup = False
            st.rerun()
    st.stop()

# --- 3. مرحلة تسجيل الدخول الحقيقي ---
if not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystem
