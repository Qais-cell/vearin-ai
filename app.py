import streamlit as st

st.set_page_config(
    page_title="VÆRIN AI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- تصميم واجهة Grok الحقيقية (أسود داكن، رمادي، وأبيض نقي) ---
st.markdown("""
<style>
html, body, .stApp {
    background-color: #000000 !important;
    color: #e7e9ea;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
.grok-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #2f3336;
    margin-bottom: 15px;
}
.grok-logo {
    font-size: 17px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.3px;
}
.chat-bubble-ai {
    background: #16181c;
    border: 1px solid #2f3336;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 10px;
    font-size: 13px;
    color: #e7e9ea;
    line-height: 1.5;
}
.chat-bubble-user {
    background: #202327;
    border: 1px solid #3f4448;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 10px;
    font-size: 13px;
    color: #ffffff;
    line-height: 1.5;
}
.stButton>button {
    background: #ffffff !important;
    color: #000000 !important;
    font-weight: 700 !important;
    border-radius: 20px !important;
    border: none !important;
    padding: 4px 12px !important;
    font-size: 11px !important;
}
.stTextInput input {
    background-color: #16181c !important;
    color: #ffffff !important;
    border: 1px solid #2f3336 !important;
    border-radius: 20px !important;
    padding: 10px 15px !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if "mode" not in st.session_state:
    st.session_state.mode = "chat"

# --- الهيدر العلوي مطابق تماماً لواجهة Grok ---
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="grok-logo">⚡ VÆRIN</div>', unsafe_allow_html=True)
with col2:
    if st.session_state.mode == "chat":
        if st.button("الوضع الفني"):
            st.session_state.mode = "training"
            st.rerun()
    else:
        if st.button("رجوع للشات"):
            st.session_state.mode = "chat"
            st.rerun()

# --- 1. وضع التدريب أو الكاميرا (يفتح فقط عند الضغط على الزر العلوي) ---
if st.session_state.mode == "training":
    st.markdown("<p style='font-size: 12px; color: #71767b;'>وضع التدريب والتوجيه البصري</p>", unsafe_allow_html=True)
    st.markdown('<div class="chat-bubble-ai">هنا يمكنك تفعيل كاميرا التتبع أو مراجعة مسارات التدريب البصري بعيداً عن الشات الرئيسي.</div>', unsafe_allow_html=True)
    
    cam = st.camera_input("التقط صورة:")
    if cam:
        st.success("تم استقبال الصورة وتحليلها بنجاح.")

# --- 2. واجهة الشات الأساسية (مطابقة لـ Grok تماماً بدون أي دوشة) ---
else:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "ai", "content": "أهلاً بك. أنا عقل VÆRIN. كيف يمكنني مساعدتك اليوم؟"}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "ai":
            st.markdown(f'<div class="chat-bubble-ai"><b>VÆRIN:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-user"><b>أنت:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)

    user_input = st.text_input("اطرح سؤالاً أو استفساراً...", placeholder="اسأل أي شيء...", key="chat_input")
    if st.button("إرسال", key="send_btn"):
        if user_input.strip():
            st.session_state.messages.append({"role": "user", "content": user_input})
            reply = f"لقد استلمت استفسارك حول '{user_input}'. أنا جاهز للتحليل وتقديم الإجابة الفورية."
            st.session_state.messages.append({"role": "ai", "content": reply})
            st.rerun()
