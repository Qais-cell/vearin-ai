import streamlit as st
from groq import Groq
import re
import time

st.set_page_config(page_title="VÆRIN Neural Console", page_icon=None, layout="centered")

if "app_state" not in st.session_state:
    st.session_state.app_state = "intro"
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "active_prompt" not in st.session_state:
    st.session_state.active_prompt = "بحث علمي متقدم وتحليل عميق للنظريات"

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# --- تصميم واجهة xAI / Groq Console الخرافية ---
st.markdown("""
    <style>
    @keyframes pulseGlow {
        0% { opacity: 0.3; transform: scale(0.97); filter: drop-shadow(0 0 5px rgba(255,255,255,0.2)); }
        50% { opacity: 1; transform: scale(1.02); filter: drop-shadow(0 0 25px rgba(255,255,255,0.5)); }
        100% { opacity: 0.3; transform: scale(0.97); filter: drop-shadow(0 0 5px rgba(255,255,255,0.2)); }
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stApp {
        background: #000000;
        color: #e6edf3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .intro-screen {
        text-align: center;
        padding: 130px 20px;
        animation: fadeIn 0.8s ease-out;
    }
    .intro-logo {
        font-size: 54px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 12px;
        animation: pulseGlow 3s infinite ease-in-out;
        letter-spacing: -2px;
    }
    .intro-desc {
        font-size: 15px;
        color: #848d97;
        font-weight: 400;
    }
    .console-header {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        margin-bottom: 5px;
    }
    .console-sub {
        font-size: 13px;
        color: #848d97;
        text-align: center;
        margin-bottom: 25px;
    }
    /* تصميم الكاردات بنفس نمط xAI Console */
    .xai-card {
        background: #121212;
        border: 1px solid #212121;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 14px;
        transition: all 0.25s ease;
    }
    .xai-card:hover {
        border-color: #3b3b3b;
        background: #161616;
        transform: translateY(-2px);
    }
    .card-title {
        font-size: 15px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .card-desc {
        font-size: 13px;
        color: #848d97;
        line-height: 1.4;
    }
    .badge {
        display: inline-block;
        background: #212121;
        color: #c9d1d9;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 20px;
        margin-top: 10px;
        border: 1px solid #30363d;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #121212 !important;
        color: #ffffff !important;
        border: 1px solid #262626 !important;
        border-radius: 12px !important;
        padding: 14px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #ffffff !important;
        box-shadow: 0 0 0 2px rgba(255,255,255,0.1);
    }
    .stButton button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 700;
        border-radius: 10px !important;
        border: none !important;
        width: 100%;
        padding: 12px;
        transition: all 0.2s ease;
    }
    .stButton button:hover {
        background-color: #d0d7de !important;
        transform: scale(1.01);
    }
    .stChatMessage {
        background: #121212;
        border: 1px solid #212121;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. الأنترو التلقائي النابض ---
if st.session_state.app_state == "intro":
    st.markdown("""
        <div class="intro-screen">
            <div class="intro-logo">VÆRIN // X</div>
            <div class="intro-desc">Next-Generation Autonomous Neural Console</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(3.0)
    st.session_state.app_state = "console_home"
    st.rerun()

# --- 2. واجهة الـ Console الرئيسية (بنمط كاردات xAI) ---
elif st.session_state.app_state == "console_home":
    col1, col2, col3 = st.columns([1, 2.5, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="console-header">Start a chat with examples</div>', unsafe_allow_html=True)
        st.markdown('<div class="console-sub">Pick a use case to see the exact prompt and settings, then make it your own.</div>', unsafe_allow_html=True)
        
        # كارد 1
        st.markdown("""
            <div class="xai-card">
                <div class="card-title">🔬 Advanced Scientific Research</div>
                <div class="card-desc">Deep analytical breakdown of complex academic theories and methodologies.</div>
                <div class="badge">System prompt</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Launch: Scientific Research", key="btn1"):
            st.session_state.active_prompt = "بحث علمي متقدم وتحليل عميق للنظريات"
            st.session_state.app_state = "login"
            st.rerun()

        # كارد 2
        st.markdown("""
            <div class="xai-card">
                <div class="card-title">📚 Curriculum & Theory Summarization</div>
                <div class="card-desc">Condense heavy academic textbooks and long-form papers into crisp summaries.</div>
                <div class="badge">System prompt</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Launch: Summarize & Explain", key="btn2"):
            st.session_state.active_prompt = "شرح المناهج الدراسية وتبسيط المفاهيم المعقدة"
            st.session_state.app_state = "login"
            st.rerun()

        # كارد 3
        st.markdown("""
            <div class="xai-card">
                <div class="card-title">💻 Code Architecture & Structured Data</div>
                <div class="card-desc">Extract complex logic or structural schemas from raw technical inputs.</div>
                <div class="badge">Structured outputs</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Launch: Engineering & Code", key="btn3"):
            st.session_state.active_prompt = "استشارات برمجية وهندسية وحل الخوارزميات بدقة"
            st.session_state.app_state = "login"
            st.rerun()

# --- 3. تسجيل الدخول الآمن ---
elif st.session_state.app_state == "login":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="console-header">Secure Authentication</div>', unsafe_allow_html=True)
        st.markdown('<div class="console-sub">Enter your verified email address to initialize console session</div>', unsafe_allow_html=True)
        
        email_input = st.text_input("Email Address", placeholder="name@example.com")
        
        if st.button("Authenticate & Enter Console"):
            if is_valid_email(email_input):
                st.session_state.user_email = email_input
                st.session_state.app_state = "chat"
                st.rerun()
            else:
                st.error("الرجاء إدخال بريد إلكتروني حقيقي وصحيح.")

# --- 4. واجهة الدردشة النهائية (Console Chat) ---
elif st.session_state.app_state == "chat":
    st.title("VÆRIN // Neural Console")

    with st.sidebar:
        st.header("Console Settings")
        st.write(f"User: **{st.session_state.get('user_email', '')}**")
        st.write(f"Mode: **{st.session_state.get('active_prompt', '')}**")
        
        st.markdown("---")
        admin_api_key = st.text_input("Groq API Key:", type="password", value="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")
        
        temperature = st.slider("Temperature:", 0.0, 1.0, 0.7, 0.1)
        max_tokens_val = st.slider("Max Tokens:", 256, 4096, 1536, 128)
        
        st.markdown("---")
        if st.button("Back to Console Home"):
            st.session_state.app_state = "console_home"
            st.rerun()

    if not admin_api_key:
        st.warning("الرجاء إدخال مفتاح Groq API في الشريط الجانبي للبدء.")
    else:
        try:
            client = Groq(api_key=admin_api_key)
            selected_focus = st.session_state.get("active_prompt", "بحث علمي متقدم")
            
            if "messages" not in st.session_state:
                st.session_state.messages = [
                    {
                        "role": "system", 
                        "content": (
                            f"You are VÆRIN, an advanced neural academic console focused on: '{selected_focus}'. "
                            "Maintain a strict, scholarly, direct tone without emojis or diplomatic filler."
                        )
                    }
                ]

            for message in st.session_state.messages:
                if message["role"] != "system":
                    with st.chat_message(message["role"]):
                        st.write(message["content"])

            if user_query := st.chat_input("Ask anything or send a prompt..."):
                st.session_state.messages.append({"role": "user", "content": user_query})
                with st.chat_message("user"):
                    st.write(user_query)

                with st.spinner("Synthesizing neural response..."):
                    chat_completion = client.chat.completions.create(
                        messages=st.session_state.messages,
                        model="llama3-70b-8192",
                        temperature=temperature,
                        max_tokens=max_tokens_val,
                    )
                    
                    assistant_answer = chat_completion.choices[0].message.content
                    st.session_state.messages.append({"role": "assistant", "content": assistant_answer})
                    with st.chat_message("assistant"):
                        st.write(assistant_answer)

        except Exception as e:
            st.error(f"خطأ في الاتصال: {e}")
