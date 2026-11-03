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

# --- 1. شاشة تخصيص الأهداف الدراسية ---
if st.session_state.step == "setup":
    st.markdown("""
        <style>
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .setup-title {
            text-align: center;
            font-size: 26px;
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
        st.markdown('<div class="setup-title">VÆRIN AI Workspace</div>', unsafe_allow_html=True)
        st.markdown('<div class="setup-sub">Configure your autonomous academic environment</div>', unsafe_allow_html=True)
        
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
            
    st.stop()

# --- 2. شاشة تسجيل الدخول الحقيقي ---
if st.session_state.step == "login" and not st.session_state.logged_in:
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
            background-color: #21262d !important;
            color: #c9d1d9 !important;
            font-weight: 600;
            border-radius: 8px !important;
            border: 1px solid rgba(240, 246, 252, 0.15) !important;
            width: 100%;
            margin-top: 10px;
            padding: 12px;
        }
        .stButton button:hover {
            background-color: #30363d !important;
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #f0f6fc; font-weight: 700;'>Secure Authentication</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8b949e; font-size: 13px; margin-bottom: 25px;'>Enter your verified email address to establish session</p>", unsafe_allow_html=True)
        
        email_input = st.text_input("Email Address", placeholder="name@example.com")
        
        if st.button("Authenticate & Enter"):
            if is_valid_email(email_input):
                st.session_state.logged_in = True
                st.session_state.user_email = email_input
                st.session_state.step = "chat"
                st.rerun()
            else:
                st.error("الرجاء إدخال بريد إلكتروني حقيقي وصحيح (يحتوي على @ والنطاق).")
                
    st.stop()

# --- 3. واجهة الدردشة الأساسية ---
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
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

st.title("VAERIN - Advanced Academic System")

with st.sidebar:
    st.header("Control Panel")
    st.write(f"Session: **{st.session_state.get('user_email', '')}**")
    st.write(f"Objective: **{st.session_state.get('study_goal', 'عام')}**")
    
    st.markdown("---")
    st.subheader("API Configuration")
    admin_api_key = st.text_input("Groq API Key:", type="password", value="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")
    
    st.markdown("---")
    st.subheader("Advanced Engine Settings")
    temperature = st.slider("Temperature (Creativity):", 0.0, 1.0, 0.7, 0.1)
    max_tokens_val = st.slider("Max Response Tokens:", 256, 4096, 1536, 128)
    
    st.markdown("---")
    st.subheader("System Behavior")
    scholarly_mode = st.checkbox("Strict Scholarly Tone", value=True)
    memory_persistence = st.checkbox("Active Memory Context", value=True)
    
    st.markdown("---")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("Reset Memory"):
            if "messages" in st.session_state:
                del st.session_state.messages
            st.success("Cleared.")
            st.rerun()
    with col_b:
        if st.button("Sign Out"):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            st.session_state.step = "setup"
            st.rerun()

if not admin_api_key:
    st.warning("الرجاء التأكد من إدخال مفتاح Groq API في الشريط الجانبي.")
else:
    try:
        client = Groq(api_key=admin_api_key)
        
        current_goal = st.session_
