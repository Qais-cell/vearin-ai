import streamlit as st

st.set_page_config(page_title="VÆRIN Neural Canvas", page_icon="⚡", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "art_track" not in st.session_state:
    st.session_state.art_track = "الأساسيات والمنظور"

# --- تصميم نظيف ومرتب يحاكي واجهات الذكاء الاصطناعي المتقدمة (Dark Minimalist) ---
st.markdown("""
    <style>
    .stApp {
        background: #000000;
        color: #e6edf3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .main-header {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        margin-bottom: 4px;
        letter-spacing: -0.4px;
    }
    .main-sub {
        font-size: 13px;
        color: #71717a;
        text-align: center;
        margin-bottom: 24px;
    }
    .art-card {
        background: #09090b;
        border: 1px solid #1f1f23;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        transition: all 0.2s ease;
    }
    .art-card:hover {
        border-color: #3f3f46;
        background: #0f0f13;
    }
    .card-title {
        font-size: 14px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 4px;
    }
    .card-desc {
        font-size: 12px;
        color: #a1a1aa;
        line-height: 1.4;
        margin-bottom: 10px;
    }
    .badge {
        display: inline-block;
        background: #18181b;
        color: #38bdf8;
        font-size: 10px;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 10px;
        border: 1px solid #0369a1;
    }
    .stButton button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 700;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
        padding: 10px;
        font-size: 13px;
    }
    .stButton button:hover {
        background-color: #e4e4e7 !important;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #09090b !important;
        color: #ffffff !important;
        border: 1px solid #1f1f23 !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

page = st.session_state.page

if page == "home":
    col1, col2, col3 = st.columns([1, 2.5, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="main-header">VÆRIN Neural Canvas // Studio</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-sub">اختر مسار التعلم لبدء جلسة الرسم والتحليل الذكي.</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="art-card">
                <div class="card-title">✏️ الخطوط والمنظور الأولي</div>
                <div class="card-desc">بناء اليد الأساسي، التحكم بالقلم، ورسم الأشكال الهندسية عبر توجيه الكاميرا.</div>
                <div class="badge">Zero to Pro</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("بدء مسار الأساسيات", key="b1"):
            st.session_state.art_track = "الأساسيات والمنظور"
            st.session_state.page = "studio"
            st.rerun()

        st.markdown("""
            <div class="art-card">
                <div class="card-title">🎨 التظليل والواقعية المتقدمة</div>
                <div class="card-desc">توزيع الإضاءة، التباين العميق، وتقنيات كبار الرسامين العالميين.</div>
                <div class="badge">Masterclass</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("بدء مسار التظليل", key="b2"):
            st.session_state.art_track = "التظليل والإضاءة"
            st.session_state.page = "studio"
            st.rerun()

elif page == "studio":
    col1, col2, col3 = st.columns([1, 2.5, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'<div class="main-header">Art Studio // {st.session_state.art_track}</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-sub">كاميرا الذكاء الاصطناعي جاهزة لتحليل خطواتك على الورق.</div>', unsafe_allow_html=True)
        
        if st.button("← العودة للقائمة الرئيسية"):
            st.session_state.page = "home"
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        enable_camera = st.checkbox("تفعيل كاميرا التقييم والتتبع المباشر", value=True)
        if enable_camera:
            cam = st.camera_input("التقط صورة لخطواتك على الورقة:")
            if cam:
                st.success("تم تحليل الرسمة بنجاح عبر النظام الذكي!")

        st.text_area("استفسارك الفني:", placeholder="اكتب سؤالك هنا...")
        if st.button("إرسال للتحليل الفني"):
            st.success("🤖 **VÆRIN AI:** خطوطك واعدة جداً، حافظ على استقامة اليد عند التخطيط الأولي.")
