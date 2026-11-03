import streamlit as st
from groq import Groq
import re

st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

if "step" not in st.session_state:
    st.session_state.step = "setup"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "study_goal" not in st.session_state:
    st.session_state.study_goal = "بحث علمي متقدم وتحليل عميق"

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# تنسيق عام لضمان عدم حدوث أي شاشة بيضاء
st.markdown("""
    <style>
    .stApp {
        background: #0d1117;
        color: #c9d1d9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .stTextInput input {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        padding: 12px !important;
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
    .title-box {
        text-align: center;
        font-size: 26px;
        font-weight: 700;
        color: #f0f6fc;
        margin-bottom: 5px;
    }
    .sub-box {
        text-align: center;
        font-size: 13px;
        color: #8b949e;
        margin-bottom: 20px;
    }
    .stChatMessage {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 14px;
    }
    h1, h2, h3 {
        color: #f0f6fc;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# --- الخطوة 1: إعداد الأهداف الدراسية ---
if st.session_state.step == "setup":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="title-box">VÆRIN AI Workspace</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-box">Configure your autonomous academic environment</div>', unsafe_allow_html=True)
        
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
            st.session_state.step = "login"
            st.rerun()

# --- الخطوة 2: تسجيل الدخول ---
elif st.session_state.step == "login":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="title-box">Secure Authentication</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-box">Enter your verified email address to establish session</div>', unsafe_allow_html=True)
        
        email_input = st.text_input("Email Address", placeholder="name@example.com")
        
        if st.button("Authenticate & Enter"):
            if is_valid_email(email_input):
                st.session_state.logged_in = True
                st.session_state.user_email = email_input
                st.session_state.step = "chat"
                st.rerun()
            else:
                st.error("الرجاء إدخال بريد إلكتروني حقيقي وصحيح (يحتوي على @ والنطاق).")

# --- الخطوة 3: واجهة الدردشة الأساسية ---
elif st.session_state.step == "chat":
    st
