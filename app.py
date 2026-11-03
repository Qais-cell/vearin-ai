import streamlit as st

st.set_page_config(
    page_title="Grok",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- تصميم يطابق واجهة Grok الحقيقية 100% ---
st.markdown("""
<style>
html, body, .stApp {
    background-color: #030303 !important;
    color: #e7e9ea;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* تنسيق الهيدر واللوجو */
.grok-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0 20px 0;
    border-bottom: 1px solid #16181c;
    margin-bottom: 20px;
}
.grok-logo {
    font-size: 20px;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: -0.5px;
}

/* بطاقات الشات المطابقة لـ Grok */
.grok-bubble-ai {
    background: #0f1012;
    border: 1px solid #1f2227;
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 12px;
    font-size: 14px;
    color: #e7e9ea;
    line-height: 1.6;
}
.grok-bubble-user {
    background: #1c1f24;
    border: 1px solid #2f333a;
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 12px;
    font-size: 14px;
    color: #ffffff;
    line-height: 1.6;
}

/* الأزرار والأيقونات الدائرية المشابهة لـ Grok */
.stButton>button {
    background: #ffffff !important;
    color: #000000 !important;
    font-weight: 700 !important;
    border-radius: 20px !important;
    border: none !important;
    padding: 6px 16px !important;
    font-size: 12px !important;
}
.stButton>button:hover {
    background: #d6d6d6 !important;
}

/* حقل الكتابة السفلي */
.stTextInput input {
    background-color: #0f1012 !important;
    color: #ffffff !important;
    border: 1px solid #2f3336 !important;
    border-radius: 24px !important;
    padding: 12px 18px !important;
    font-size: 14px !important;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# إدارة حالة التطبيق (تسجيل الدخول / الشات)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- 1. واجهة تسجيل الدخول المطابقة لـ Grok ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 2.5, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 32px; font-weight: 900; color: #fff;'>Grok</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #71767b; font-size: 13px; margin-bottom: 30px;'>تسجيل الدخول للمتابعة إلى الذكاء الاصطناعي</p>", unsafe_allow_html=True)
        
        username = st.text_input("اسم المستخدم أو البريد", placeholder="أدخل اسمك...")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("تسجيل الدخول ⚡", key="login_btn"):
            if username.strip():
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.warning("يرجى إدخال الاسم للمتابعة.")

# --- 2. واجهة الشات الرئيسية بعد الدخول (تطابق grok.com) ---
else:
    # هيدر علوي مع زر الخروج وتبديل الأوضاع
    c_logo, c_tab = st.columns([3, 1])
    with c_logo:
        st.markdown(f'<div class="grok-logo">⚡ Grok <span style="font-size: 11px; color: #71767b; font-weight: 400;">// مرحباً، {st.session_state.username}</span></div>', unsafe_allow_html=True)
    with c_tab:
        if st.button("تسجيل خروج", key="logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

    # سجل المحادثة
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "ai", "content": "مرحباً! أنا Grok. كيف يمكنني مساعدتك في مهامك اليوم؟"}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "ai":
            st.markdown(f'<div class="grok-bubble-ai"><b>Grok:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="grok-bubble-user"><b>أنت:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)

    # حقل الإرسال السفلي
    user_input = st.text_input("اسأل Grok أي شيء...", placeholder="اكتب رسالتك هنا...", key="grok_input")
    if st.button("إرسال", key="send_grok"):
        if user_input.strip():
            st.session_state.messages.append({"role": "user", "content": user_input})
            reply = f"لقد استفسرت عن '{user_input}'. أنا هنا لتحليل الأفكار وتقديم الإجابات الفورية بدقة عالية."
            st.session_state.messages.append({"role": "ai", "content": reply})
            st.rerun()
