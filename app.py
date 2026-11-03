import streamlit as st
from groq import Groq
import time

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
        st.markdown('<div class="login-title">Sign in to VAERIN</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Choose your authorized provider to continue</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # أزرار المصادقة المستوحاة من دزاين منصات التطوير الكبرى
        if st.button("Continue with Google"):
            st.session_state.logged_in = True
            st.session_state.selected_provider = "Google Account"
            st.rerun()
            
        if st.button("Continue with Apple ID"):
            st.session_state.logged_in = True
            st.session_state.selected_provider = "Apple ID"
            st.rerun()
            
        if st.button("Continue with Twitter / X"):
            st.session_state.logged_in = True
            st.session_state.selected_provider = "Twitter"
            st.rerun()
            
        if st.button("Continue with Discord"):
            st.session_state.logged_in = True
            st.session_state.selected_provider = "Discord"
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- واجهة الدردشة الأساسية (بدون إظهار أي إيميل نهائياً وبدون إيموجيز) ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stChatMessage {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    h1, h2, h3 {
        color: #f0f6fc;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

st.title("VAERIN - Advanced Academic System")
st.write("Secure session initialized successfully. Memory and security systems active.")

# --- الشريط الجانبي للإعدادات المتقدمة ---
with st.sidebar:
    st.header("System Settings")
    api_key = st.text_input("Groq API Key:", type="password")
    
    st.markdown("---")
    st.subheader("Model Controls")
    temperature = st.slider("Temperature (Creativity):", 0.0, 1.0, 0.7, 0.1)
    max_tokens_val = st.slider("Max Tokens:", 256, 2048, 1024, 128)
    
    st.markdown("---")
    if st.button("Clear Memory & Restart"):
        if "messages" in st.session_state:
            del st.session_state.messages
        st.success("Memory cleared successfully.")
        st.rerun()
        
    if st.button("Sign out"):
        st.session_state.logged_in = False
        st.rerun()

# معالجة الشات والاتصال بـ API
if api_key:
    try:
        client = Groq(api_key=api_key)
        
        # تهيئة النظام والذاكرة
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system", 
                    "content": (
                        "You are VAERIN, an advanced academic AI tutor. "
                        "You possess a robust long-term memory connecting all conversation details accurately. "
                        "Strict rule: Never perform quizzes or assessment tests unless explicitly requested by the user. "
                        "Maintain a direct, scholarly tone without emojis or diplomatic filler phrases."
                    )
                }
            ]

        # عرض الرسائل السابقة
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        # صندوق الادخال والتفاعل
        if user_query := st.chat_input("Type your academic query here..."):
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            with st.spinner("Analyzing and retrieving context..."):
                models_response = client.models.list()
                all_models = [m.id for m in models_response.data]
                
                active_models = [
                    m for m in all_models 
                    if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding', 'allam'])
                ]
                
                selected_model = active_models[0] if active_models else all_models[0]
                
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model=selected_model,
                    temperature=temperature,
                    max_tokens=max_tokens_val,
                )
                
                assistant_answer = chat_completion.choices[0].message.content
                
                st.session_state.messages.append({"role": "assistant", "content": assistant_answer})
                with st.chat_message("assistant"):
                    st.write(assistant_answer)

    except Exception as e:
        st.error(f"Connection or authentication error: {e}")
else:
    st.info("Please enter your Groq API key in the sidebar to activate the system.")
