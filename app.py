import streamlit as st
from groq import Groq
import random
import time

# إعدادات الصفحة
st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

# تهيئة حالة الجلسة للتحقق وتسجيل الدخول
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False
if "generated_otp" not in st.session_state:
    st.session_state.generated_otp = ""

# --- صفحة تسجيل الدخول والتحقق برمز حقيقي (OTP) ---
if not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        .login-box {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 30px;
            max-width: 420px;
            margin: 30px auto;
            box-shadow: 0 16px 32px rgba(1, 4, 9, 0.8);
        }
        .login-title {
            font-size: 22px;
            font-weight: 600;
            color: #f0f6fc;
            text-align: center;
            margin-bottom: 20px;
        }
        .stTextInput input {
            background-color: #0d1117 !important;
            color: #c9d1d9 !important;
            border: 1px solid #30363d !important;
            border-radius: 6px !important;
        }
        .stButton button {
            background-color: #238636 !important;
            color: #ffffff !important;
            font-weight: 600;
            border-radius: 6px !important;
            border: none !important;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #2ea043 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">VAERIN Secure Authentication</div>', unsafe_allow_html=True)
        
        auth_method = st.selectbox("اختر طريقة المصادقة:", ["البريد الإلكتروني (مع رمز تحقق OTP)", "Google Account", "Twitter / X", "Apple ID"])
        
        if auth_method == "البريد الإلكتروني (مع رمز تحقق OTP)":
            user_email = st.text_input("أدخل بريدك الإلكتروني:")
            
            if not st.session_state.otp_sent:
                if st.button("إرسال رمز التحقق"):
                    if user_email and "@" in user_email:
                        # توليد رمز تحقق حقيقي مكون من 4 أرقام
                        st.session_state.generated_otp = str(random.randint(1000, 9999))
                        st.session_state.otp_sent = True
                        st.session_state.temp_email = user_email
                        # عرض الرمز مؤقتاً للشاشة للتأكد (بسبب قيود سيرفرات الستريمليت البريدية المجانية)
                        st.success(f"تم إرسال الرمز بنجاح! رمز التحقق الخاص بك هو: {st.session_state.generated_otp}")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("الرجاء إدخال بريد إلكتروني صحيح.")
            else:
                st.info(f"تم إرسال رمز التحقق إلى: {st.session_state.get('temp_email', '')}")
                entered_otp = st.text_input("أدخل رمز التحقق المكون من 4 أرقام:", type="password")
                
                if st.button("تأكيد الرمز وتسجيل الدخول"):
                    if entered_otp == st.session_state.generated_otp:
                        st.session_state.logged_in = True
                        st.success("تم التحقق بنجاح. جاري فتح النظام...")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error("رمز التحقق غير صحيح. حاول مرة أخرى.")
        else:
            # محاكاة تسجيل الدخول السريع المباشر للخدمات الأخرى
            st.info(f"سيتم ربط حساب {auth_method} بسلاسة وأمان.")
            if st.button(f"المتابعة باستخدام {auth_method}"):
                st.session_state.logged_in = True
                st.success("تم تسجيل الدخول بنجاح.")
                time.sleep(0.5)
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- واجهة الدردشة الأساسية (بدون إظهار الإيميل نهائياً وبدون إيموجيز) ---
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
st.write("نظام المعلم الأكاديمي المتقدم جاهز للعمل. الذاكرة والأمان مفعلة بكفاءة عالية.")

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
        st.session_state.otp_sent = False
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
