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

# ترجمة واجهة المستخدم
translations = {
    "العربية": {
        "welcome_intro": "أهلاً، أنا فيرين",
        "start_btn": "بدء الاستخدام وتسجيل الحساب",
        "tab_prof": "المهن العالمية",
        "tab_courses": "الكورسات الاحترافية",
        "tab_ai": "الرفيق الذكي (Live)",
        "search_ph": "ابحث في المجالات...",
        "input_ph": "اسأل فيرين أي شيء..."
    },
    "English": {
        "welcome_intro": "Welcome, I am Vairen",
        "start_btn": "Get Started & Sign Up",
        "tab_prof": "Global Professions",
        "tab_courses": "Elite Courses",
        "tab_ai": "AI Assistant (Live)",
        "search_ph": "Search domains...",
        "input_ph": "Ask Vairen anything..."
    }
}

t = translations[st.session_state.lang]

# 1. شاشة الانترو وتسجيل الدخول
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

# 2. التبويب العلوي الفخم
top_col1, top_col3 = st.columns([8, 2])
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
    
    professions = [
        {
            "title_ar": "هندسة أنظمة الذكاء الاصطناعي", "title_en": "AI Systems Architect",
            "desc_ar": "تصميم نماذج التعلم العميق وهندسة البيانات الكبرى.", "desc_en": "Designing deep learning models and big data pipelines.",
            "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600&auto=format&fit=crop&q=60",
            "color": "#3b82f6"
        },
        {
            "title_ar": "إدارة العلامات التجارية والتصميم", "title_en": "Digital Brand Director",
            "desc_ar": "ابتكار الهويات البصرية المتقدمة وتجربة المستخدم.", "desc_en": "Creating advanced visual identities and enterprise UX.",
            "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&auto=format&fit=crop&q=60",
            "color": "#ec4899"
        },
        {
            "title_ar": "هندسة النمذجة السحابية والسيبرانية", "title_en": "Cloud & Cyber Security",
            "desc_ar": "حماية البنيات التحتية الرقمية وتأمين الخوادم.", "desc_en": "Securing digital infrastructures and global servers.",
            "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=60",
            "color": "#10b981"
        }
    ]

    cols = st.columns(3)
    for i, p in enumerate(professions):
        with cols[i % 3]:
            title = p['title_ar'] if st.session_state.lang == "العربية" else p['title_en']
            desc = p['desc_ar'] if st.session_state.lang == "العربية" else p['desc_en']
            st.markdown(f"""
            <div class="oled-card" style="border-top: 3px solid {p['color']};">
                <img src="{p['image']}" style="width: 100%; height: 140px; object-fit: cover; border-radius: 8px; margin-bottom: 10px;">
                <h4 style="margin: 0; color: #fff;">{title}</h4>
                <p style="color: #888; font-size: 0.85rem; margin-top: 5px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("استشر حول المهنة", key=f"prof_{i}", use_container_width=True):
                st.session_state.chat_history.append({"role": "user", "content": f"أريد خارطة طريق احترافية وشاملة للعمل في مجال: {title}"})
                st.rerun()

# --- تبويب الكورسات الاحترافية الحقيقية ---
with tab2:
    st.markdown(f"### {t['tab_courses']}")
    courses = [
        {
            "title": "Vairen Masterclass: Advanced Enterprise Architecture",
            "desc": "كورس شامل من الألف للياء لبناء أنظمة الويب الخارقة بأحدث التقنيات.",
            "modules": ["1. بنية النظريات السحابية المتقدمة", "2. الأمان وحماية البيانات", "3. تحسين الأداء وسرعة الاستجابة الخارقة"],
            "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=60"
        },
        {
            "title": "Global AI Integration & Prompt Engineering",
            "desc": "تعلم كيفية دمج نماذج اللغات الضخمة وبناء وكلاء ذكاء اصطناعي مستقلين.",
            "modules": ["1. أساسيات الهندسة العكسية للأوامر", "2. الربط المباشر مع واجهات البرمجة", "3. بناء نظام تفاعل حي (Live Assistant)"],
            "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&auto=format&fit=crop&q=60"
        }
    ]

    for c in courses:
        with st.container():
            col_img, col_txt = st.columns([1, 3])
            with col_img:
                st.image(c['image'], use_column_width=True)
            with col_txt:
                st.markdown(f"#### {c['title']}")
                st.write(c['desc'])
                with st.expander("عرض أقسام الكورس (Modules)"):
                    for m in c['modules']:
                        st.markdown(f"- {m}")
            st.divider()

# --- تبويب الرفيق الذكي (AI Assistant / Live) ---
with tab3:
    st.markdown(f"### {t['tab_ai']}")
    
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    if prompt := st.chat_input(t['input_ph']):
        st.session_state.chat_history.
