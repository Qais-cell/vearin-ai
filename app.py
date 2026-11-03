import streamlit as st

st.set_page_config(page_title="VÆRIN Grok", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: #000000;
        color: #e6edf3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .grok-box {
        background: #09090b;
        border: 1px solid #1f1f23;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-top: 40px;
    }
    .stButton button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 700;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
        padding: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="grok-box">
        <h2 style="color: #ffffff; margin-bottom: 10px;">⚡ VÆRIN // Grok Art Studio</h2>
        <p style="color: #a1a1aa; font-size: 13px;">النظام يعمل الآن بكامل إمكانياته وبدون شاشات بيضاء.</p>
    </div>
""", unsafe_allow_html=True)

st.write("")
track = st.selectbox("اختر مسار الرسم:", ["الخطوط والمنظور الأولي", "التظليل والواقعية المتقدمة"])

if st.button("بدء جلسة الرسم عبر الكاميرا"):
    st.success(f"تم تفعيل مسار ({track}) بنجاح!")
    cam = st.camera_input("التقط صورة لورقة الرسم الخاصة بك:")
    if cam:
        st.info("⚡ Grok Vision: يتم تحليل خطوطك الآن...")
