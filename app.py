import streamlit as st
from groq import Groq
import re
import time

st.set_page_config(page_title="VÆRIN AI - Neural Academic System", page_icon=None, layout="centered")

if "app_state" not in st.session_state:
    st.session_state.app_state = "intro"
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "study_goal" not in st.session_state:
    st.session_state.study_goal = "بحث علمي متقدم وتحليل عميق للنظريات"
if "scholarly_mode" not in st.session_state:
    st.session_state.scholarly_mode = "صارم وأكاديمي بحت (بدون حشو)"

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# التصميم الأسطوري والأنيميشن النابض بالحياة (Groq/Gemini Style)
st.markdown("""
    <style>
    @keyframes pulseGlow {
        0% { opacity: 0.3; transform: scale(0.97); filter: drop-shadow(0 0 5px rgba(88,166,255,0.3)); }
        50% { opacity: 1; transform: scale(1.03); filter: drop-shadow(0 0 35px rgba(88,166,255,0.8)); }
        100% { opacity: 0.3; transform: scale(0.97); filter: drop-shadow(0 0 5px rgba(88,166,255,0.3)); }
    }
    @keyframes textShimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stApp {
        background: radial-gradient(circle at center, #161b22 0%, #0d1117 100%);
        color: #c9d1d9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .intro-screen {
        text-align: center;
        padding: 120px 20px;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .intro-logo {
        font-size: 56px;
        font-weight: 900;
        background: linear-gradient(135deg, #f0f6fc 0%, #58a6ff 30%, #1f6feb 70%, #58a6ff 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 15px;
        animation: pulseGlow 3s infinite ease-in-out, textShimmer 4s infinite linear;
        letter-spacing: -2px;
    }
    .intro-desc {
        font-size: 16px;
        color: #8b949e;
        font-weight: 400;
        letter-spacing: 1px;
        animation: pulseGlow 4s infinite ease-in-out;
    }
    .pulsing-title {
        text-align: center;
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(135deg, #f0f6fc 0%, #58a6ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
        animation: pulseGlow 4s infinite ease-in-out;
    }
    .sub-title {
        text-align: center;
        font-size: 13px;
        color: #8b949e;
        margin-bottom: 25px;
    }
    .stTextInput input {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
        border-radius: 12px !important;
        padding: 14px !important;
        transition: all 0.3s ease;
    }
    .stTextInput input:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 0 4px rgba(88, 166, 255, 0.15);
    }
    .stButton button {
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important;
        color: #ffffff !important;
        font-weight: 600;
        border-radius: 12px !important;
        border: none !important;
        width: 100%;
        margin-top: 15px;
        padding: 14px;
        box-shadow: 0 8px 24px rgba(35, 134, 54, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 32px rgba(46, 160, 67, 0.6);
        filter: brightness(1.1);
    }
    .stChatMessage {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    h1, h2, h3 {
        color: #f0f6fc;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. الأنترو النابض والتلقائي (Groq/Gemini Style) ---
if st.session_state.app_state == "intro":
    st.markdown("""
        <div class="intro-screen">
            <div class="intro-logo">VÆRIN AI</div>
            <div class="intro-desc">Autonomous Academic Intelligence & Neural Workspace</div>
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(3.2)
    st.session_state.app_state = "setup"
    st.rerun()

# --- 2. إعداد الأهداف الدراسية التفاعلية ---
elif st.session_state.app_state == "setup":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="pulsing-title">Configure Academic Profile</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">Initialize your custom AI scholarly environment</div>', unsafe_allow_html=True)
        
        goal_selection = st.selectbox(
            "Primary Academic Objective:",
            [
                "🔬 بحث علمي متقدم وتحليل عميق للنظريات",
                "📚 شرح المناهج الدراسية وتبسيط المفاهيم المعقدة",
                "📝 تلخيص المقالات والكتب الأكاديمية بدقة مذهلة",
                "💻 استشارات برمجية وهندسية وحل الخوارزميات",
                "📊 تحليل البيانات وإعداد التقارير البحثية"
            ]
        )
        
        academic_style = st.radio(
            "Scholarly Interaction Mode:",
            [
                "صارم وأكاديمي بحت (بدون حشو أو عبارات دبلوماسية)",
                "أكاديمي توجيهي متقدم مع أمثلة وتطبيقات تفصيلية"
            ]
        )
        
        if st.button("Initialize Neural Workspace"):
            st.session_state.study_goal = goal_selection
            st.session_state.scholarly_mode = academic_style
            st.session_state.app_state = "login"
            st.rerun()

# --- 3. واجهة تسجيل الدخول الآمن ---
elif st.session_state.app_state == "login":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="pulsing-title">Secure Authentication</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">Enter your verified email address to establish session</div>', unsafe_allow_html=True)
        
        email_input = st.text_input("Email Address", placeholder="name@example.com")
        
        if st.button("Authenticate & Enter"):
            if is_valid_email(email_input):
                st.session_state.user_email = email_input
                st.session_state.app_state = "chat"
                st.rerun()
            else:
                st.error("الرجاء إدخال بريد إلكتروني حقيقي وصحيح (يحتوي على @ والنطاق).")

# --- 4. واجهة الدردشة والتحكم المتقدم ---
elif st.session_state.app_state == "chat":
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
        scholarly_mode_
