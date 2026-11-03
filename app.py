import streamlit as st
from groq import Groq
import time

# إعدادات الصفحة
st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

# تهيئة حالة جلسة تسجيل الدخول
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(circle at center, #0f1117 0%, #050508 100%);
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, sans-serif;
        }
        .auth-card {
            background: rgba(22, 27, 34, 0.85);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            padding: 35px;
            max-width: 440px;
            margin: 20px auto;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
            animation: fadeInScale 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .brand-title {
            font-size: 30px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            letter-spacing: -0.5px;
            margin-bottom: 6px;
        }
        .brand-subtitle {
            font-size: 13px;
            color: #8b949e;
            text-align: center;
            margin-bottom: 20px;
        }
        .video-box {
            width: 100%;
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 20px;
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
        st.markdown('<div class="brand-subtitle">نظام المعلم الأكاديمي المتقدم</div>', unsafe_allow_html=True)
        
        # فيديو تعريفي متحرك وبدون أخطاء
        st.markdown("""
            <div class="video-box">
                <video width="100%" autoplay loop muted playsinline style="display:block;">
                    <source src="https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-and-numbers-31936-large.mp4" type="video/mp4">
                </video>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### المصادقة وتسجيل الدخول")
        auth_option = st.selectbox("طريقة الدخول:", ["تسجيل الدخول عبر Google", "تسجيل الدخول عبر GitHub", "تسجيل الدخول عبر Apple ID", "البريد الإلكتروني التقليدي"])
        
        if auth_option == "البريد الإلكتروني التقليدي":
            st.text_input("البريد الإلكتروني:")
            st.text_input("كلمة المرور:", type="password")
        
        st.markdown("---")
        st.markdown("### نمط التوجيه الدراسي")
        study_mode = st.selectbox("اختر أسلوب الدراسة:", [
            "شرح أكاديمي عميق ومفصل",
            "حل المسائل والتدريبات خطوة بخطوة",
            "تلخيص النصوص والمقالات العلمية بدقة",
            "استشارة بحثية ومراجعة شاملة"
        ])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("دخول النظام", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.study_mode = study_mode
            st.success("تم التحقق بنجاح. جاري فتح النظام...")
            time.sleep(0.5)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- واجهة الدردشة الأساسية (بدون إيموجيز وبسلاسة تامة) ---
st
