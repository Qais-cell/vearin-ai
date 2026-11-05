import streamlit as st
import requests
import json

# إعدادات الصفحة
st.set_page_config(
    page_title="Vairen",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# مفتاح Gemini
API_KEY = "AQ.Ab8RN6Iq5EaT8cX5Sq5cxLfDHkKPcaTxITN0uJcsD_yZEleLAg"

# تصميم OLED Black والأنيميشن عبر CSS
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .oled-card {
        background: #0a0a0a;
        border: 1px solid #222222;
        border-radius: 12px;
        padding: 16px;
        transition: all 0.3s ease;
    }
    .oled-card:hover {
        border-color: #ffffff;
        transform: translateY(-2px);
    }
    /* إخفاء عناصر ستريمليت الزائدة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# إدارة حالة التطبيق (State)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "lang" not in st.session_state:
    st.session_state.lang = "العربية"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "المهن"

# ترجمة واجهة المستخدم البسيطة
translations = {
    "العربية": {
        "welcome_intro": "أهلاً، أنا فيرين",
        "start_btn": "بدء الاستخدام وتسجيل الحساب",
        "tab_prof": "المهن العالمية",
        "tab_courses": "الكورسات الاحترافية",
        "tab_ai": "الرفيق الذكي (Live)",
        "settings": "الإعدادات والذاكرة",
        "search_ph": "ابحث في المجالات...",
        "send": "إرسال",
        "input_ph": "اسأل فيرين أي شيء..."
    },
    "English": {
        "welcome_intro": "Welcome, I am Vairen",
        "start_btn": "Get Started & Sign Up",
        "tab_prof": "Global Professions",
        "tab_courses": "Elite Courses",
        "tab_ai": "AI Assistant (Live)",
        "settings": "Settings & Memory",
        "search_ph": "Search domains...",
        "send": "Send",
        "input_ph": "Ask Vairen anything..."
    }
}

t = translations[st.session_state.lang]

# 1. شاشة الانترو وتسجيل الدخول إذا لم يتم الدخول
if not st.session_state.logged_in:
    st.markdown(f"""
    <div style="text-align: center; margin-top: 10vh;">
        <h1 style="font-size: 3rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 10px;">V A I R E N</h1>
        <p style="color: #888; font-size: 1.2rem; margin-bottom: 30px;">{t['welcome_intro']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            user_name = st.text_input("اسم المستخدم / User Name", placeholder="Qais Abood")
            user_email = st.text_input("البريد الإلكتروني / Email")
            submitted = st.form_submit_button(t['start_btn'], use_container_width=True)
            if submitted and user_name:
                st.session_state.logged_in = True
                st.session_state.user_name = user_name
                st.rerun()
    st.stop()

# 2. التبويب العلوي الفخم (Settings, Memory, Language) بدون خلفية
top_col1, top_col2, top_col3 = st.columns([2, 6, 2])
with top_col1:
    st.markdown(f"**⚡ Vairen** | أهلاً، {st.session_state.get('user_name', 'قيس')}")
with top_col3:
    selected_lang = st.selectbox("Language", ["العربية", "English"], label_visibility="collapsed")
    if selected_lang != st.session_state.lang:
        st.session_state.lang = selected_lang
        st.rerun()

st.divider()

# شريط التبويبات الرئيسي
tab1, tab2, tab3 = st.tabs([t['tab_prof'], t['tab_courses'], t['tab_ai']])

# --- تبويب المهن العالمية ---
with tab1:
    st.markdown(f"### {t['tab_prof']}")
    search_query = st.text_input("Search", placeholder=t['search_ph'], label_visibility="collapsed")
    
    professions = [
        {
            "title_ar": "هندسة أنظمة الذكاء الاصطناعي", "title_en": "AI Systems Architect",
            "desc_ar": "تصميم نماذج التعلم العميق وهندسة البيانات الكبرى.", "desc_en": "Designing deep learning models and big data pipelines.",
            "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600&auto=format&fit=crop&q=60",
            "color": "#3b82f6"
        },
        {
            "title_ar": "إدارة العلامات التجارية والتصميم الرقمي", "title_en": "Digital Brand Director",
            "desc_ar": "ابتكار الهويات البصرية المتقدمة وتجربة المستخدم للمشاريع الضخمة.", "desc_en": "Creating advanced visual
