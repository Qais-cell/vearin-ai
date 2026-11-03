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

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# --- أنترو تلقائي أسطوري (يظهر وحده بدون أزرار ثم يختفي) ---
if st.session_state.show_intro and not st.session_state.logged_in:
    st.markdown("""
        <style>
        @keyframes introAnim {
            0% { opacity: 0; transform: scale(0.95); filter: blur(5px); }
            50% { opacity: 1; transform: scale(1); filter: blur(0px); }
            100% { opacity: 0; transform: scale(1.05); filter: blur(5px); }
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
            animation: introAnim 2.8s ease-in-out forwards;
        }
        .intro-logo {
            font-size: 46px;
            font-weight: 800;
            background: linear-gradient(135deg, #f0f6fc 0%, #58a6ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            letter-spacing: -1.5px;
        }
        .intro-desc {
            font-size: 14px;
            color: #8b949e;
            font-weight: 400;
            letter-spacing: 0.5px;
        }
        </style>
        <div class="auto-intro">
            <div class="intro-logo">VÆRIN AI</div>
            <div class="intro-desc">Autonomous Academic Intelligence</div>
        </div>
    """, unsafe_allow_html=True)
    
    # انتظار لمدة 2.6 ثانية ثم الانتقال تلقائياً للواجهة التالية
    time.sleep(2.6)
    st.session_state.show_intro = False
    st.rerun()

# --- مرحلة تسجيل الدخول الحقيقي ---
if not st.session_state.logged_in:
    st.markdown("""
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            animation: fadeIn 0.5s ease-out;
        }
        .stTextInput input {
            background-color: #161b22 !important;
            color: #c9d1d9 !important;
            border: 1px solid #30363d !important;
            border-radius: 10px !important;
            padding: 14px !important;
            transition: all 0.3s ease;
        }
        .stTextInput input:focus {
            border-color: #58a6ff !important;
            box-shadow: 0 0 0 4px rgba(88, 166, 255, 0.15);
        }
        .stButton button {
            background-color: #21262d !important;
            color: #c9d1d9 !important;
            font-weight: 600;
            border-radius: 10px !important;
            border: 1px solid rgba(240, 246, 252, 0.15) !important;
            width: 100%;
            margin-top: 12px;
            padding: 14px;
            transition: all 0.25s ease;
        }
        .stButton button:hover {
            background-color: #30363d !important;
            color: #ffffff !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
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
                st.rerun()
            else:
                st.error("الرجاء إدخال بريد إلكتروني حقيقي وصحيح (يحتوي على @ والنطاق).")
                
    st.stop()

# --- واجهة الدردشة والإعدادات المتقدمة ---
st.markdown("""
    <style>
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stChatMessage {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        animation: slideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        transition: border-color 0.2s ease;
    }
    .stChatMessage:hover {
        border-color: #484f58;
    }
    h1, h2, h3 {
        color: #f0f6fc;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

st.title("VAERIN - Advanced Academic System")

# --- لوحة التحكم والإعدادات المتقدمة في الشريط الجانبي ---
with st.sidebar:
    st.header("Control Panel")
    st.write(f"Session: **{st.session_state.get('user_email', '')}**")
    
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
            st.session_state.show_intro = True
            st.rerun()

# معالجة الشات والاتصال الذكي
if not admin_api_key:
    st.warning("الرجاء التأكد من إدخال مفتاح Groq API في الشريط الجانبي.")
else:
    try:
        client = Groq(api_key=admin_api_key)
        
        tone_instruction = (
            "Maintain a strict, scholarly, direct tone without emojis or diplomatic filler phrases."
            if scholarly_mode else "Maintain an advanced professional academic style."
        )
        
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system", 
                    "content": (
                        "You are VAERIN, an advanced academic AI tutor with deep analytical capabilities. "
                        "You possess robust long-term memory connecting all conversation details accurately. "
                        "Strict rule: Never perform quizzes or assessment tests unless explicitly requested by the user. "
                        f"{tone_instruction}"
                    )
                }
            ]

        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        if user_query := st.chat_input("Type your academic query here..."):
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            with st.spinner("Executing advanced synthesis and retrieval..."):
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
        st.error(f"خطأ في الاتصال أو مفتاح API غير صالح. التفاصيل: {e}")
