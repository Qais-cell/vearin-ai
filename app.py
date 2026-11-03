import streamlit as st
from groq import Groq
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

# تهيئة حالة الجلسة
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

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
            text-align: center;
        }
        .login-title {
            font-size: 24px;
            font-weight: 600;
            color: #f0f6fc;
            margin-bottom: 8px;
        }
        .login-subtitle {
            font-size: 13px;
            color: #8b949e;
            margin-bottom: 25px;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">Sign in to VAERIN</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Authenticate with your Google account to start</div>', unsafe_allow_html=True)
        
        # تضمين نافذة تسجيل الدخول الحقيقية لـ Firebase باستخدام الإعدادات الخاصة بك
        firebase_auth_html = """
        <div style="text-align: center;">
            <button id="google-login-btn" style="
                background-color: #21262d;
                color: #c9d1d9;
                font-weight: 500;
                border-radius: 6px;
                border: 1px solid rgba(240, 246, 252, 0.1);
                width: 100%;
                padding: 12px;
                cursor: pointer;
                font-size: 14px;
            ">Continue with Google Account</button>
        </div>

        <script type="module">
            import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
            import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

            const firebaseConfig = {
              apiKey: "AIzaSyDyqXZtuSYBwz7oMonD0j534RhyATAQg8Q",
              authDomain: "vaerin-auth.firebaseapp.com",
              projectId: "vaerin-auth",
              storageBucket: "vaerin-auth.firebasestorage.app",
              messagingSenderId: "1014438590441",
              appId: "1:1014438590441:web:e71b89a7e236bd7364fd78",
              measurementId: "G-XMEMWSR5BC"
            };

            const app = initializeApp(firebaseConfig);
            const auth = getAuth(app);
            const provider = new GoogleAuthProvider();

            document.getElementById('google-login-btn').onclick = () => {
                signInWithPopup(auth, provider)
                  .then((result) => {
                    const user = result.user;
                    window.location.reload();
                  }).catch((error) => {
                    console.error(error);
                  });
            };
        </script>
        """
        components.html(firebase_auth_html, height=100)
        
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- واجهة الدردشة الأساسية ---
st.title("VAERIN - Advanced Academic System")
st.write("System online. Authenticated session active.")

with st.sidebar:
    st.header("System Controls")
    admin_api_key = st.text_input("Groq API Key:", type="password", value="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")
    
    if st.button("Sign out"):
        st.session_state.logged_in = False
        st.rerun()

# معالجة الشات
if admin_api_key:
    try:
        client = Groq(api_key=admin_api_key)
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system", 
                    "content": (
                        "You are VAERIN, an advanced academic AI tutor. "
                        "Strict rule: Never perform quizzes or assessment tests unless explicitly requested. "
                        "Maintain a direct, scholarly tone without emojis."
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

            with st.spinner("Analyzing..."):
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model="llama3-70b-8192",
                )
                assistant_answer = chat_completion.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": assistant_answer})
                with st.chat_message("assistant"):
                    st.write(assistant_answer)
    except Exception as e:
        st.error(f"خطأ في الاتصال: {e}")
