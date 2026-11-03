import streamlit as st
from groq import Groq
import time

# إعدادات الصفحة
st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

# --- واجهة تسجيل الدخول والانترو المتقدمة (تشبه GitHub وبدون إيموجيز) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(circle at center, #0f1117 0%, #050508 100%);
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Icons", "Segoe UI", Roboto, sans-serif;
        }
        .auth-card {
            background: rgba(22, 27, 34, 0.85);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            padding: 40px;
            max-width: 440px;
            margin: 40px auto;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
            animation: fadeInScale 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .brand-title {
            font-size: 32px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            letter-spacing: -0.5px;
            margin-bottom: 8px;
        }
        .brand-subtitle {
            font-size: 14px;
            color: #8b949e;
            text-align: center;
            margin-bottom: 30px;
        }
        .video-container {
            width: 100%;
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        @keyframes fadeInScale {
            0% { opacity: 0; transform: scale(0.95); }
            100% { opacity: 1; transform: scale(1); }
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.markdown('<div class="brand-title">VAERIN Academic AI</div>', unsafe_allow_html=True)
        st.markdown('<div class="brand-subtitle">منصة المعلم الأكاديمي الذكي المتقدمة</div>', unsafe_allow_html=True)
        
        # فيديو تعريفي قصير ومتحرك داخل الانترو
        st.markdown("""
            <div class="video-container">
                <video width="100%" autoplay loop muted playsinline style="display:block;">
                    <source src="https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-and-numbers-31936-large.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### خيارات المصادقة وتسجيل الدخول")
        auth_option = st.selectbox("اختر طريقة المصادقة:", ["تسجيل الدخول عبر Google", "تسجيل الدخول عبر GitHub", "تسجيل الدخول عبر Apple ID", "البريد الإلكتروني التقليدي"])
        
        if auth_option == "البريد الإلكتروني التقليدي":
            st.text_input("البريد الإلكتروني الأكاديمي:")
            st.text_input("كلمة المرور:", type="password")
        
        st.markdown("---")
        st.markdown("### أسلوب التوجيه الدراسي المفضل")
        study_mode = st.selectbox("حدد نمط التدريس:", [
            "شرح أكاديمي عميق ومفصل",
            "حل المسائل والتدريبات خطوة بخطوة",
            "تلخيص النصوص والمقالات العلمية بدقة",
            "استشارة بحثية ومراجعة شاملة"
        ])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("بدء الجلسة الأكاديمية", use_container_width=True):
            st.session_state.logged_in =
