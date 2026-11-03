import streamlit as st

st.set_page_config(page_title="VÆRIN // Grok Art Console", page_icon="⚡", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "art_track" not in st.session_state:
    st.session_state.art_track = "الأساسيات والمنظور"

# --- تصميم مطابق لواجهة Grok الأصلية بالمليم (Dark Minimalist & Neon) ---
st.markdown("""
    <style>
    .stApp {
        background: #000000;
        color: #e6edf3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .grok-header {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        margin-bottom: 4px;
        letter-spacing: -0.4px;
    }
    .grok-sub {
        font-size: 13px;
        color: #71717a;
        text-align: center;
        margin-bottom: 24px;
    }
    .grok-card {
        background: #09090b;
        border: 1px solid #1f1f23;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        transition: all 0.2s ease;
    }
    .grok-card:hover {
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
        st.markdown('<div class="grok-header">Start a drawing prompt with Grok</div>', unsafe_allow_html=True)
        st.markdown('<div class="grok-sub">Pick a training track to explore steps and AI camera feedback.</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="grok-card">
                <div class="card-title">✏️ الخطوط والمنظور الأولي</div>
                <div class="card-desc">بناء اليد الأساسي، التحكم بالقلم، ورسم الأشكال الهندسية عبر الكاميرا.</div>
                <div class="badge">Zero to Pro</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Grok: مسار الأساسيات", key="b1"):
            st.session_state.art_track = "الأساسيات والمنظور"
            st.session_state.page = "studio"
            st.rerun()

        st.markdown("""
            <div class="grok-card">
                <div class="card-title">🎨 التظليل والواقعية المتقدمة</div>
                <div class="card-desc">توزيع الإضاءة، التباين العميق، وتقنيات كبار الرسامين العالميين.</div>
                <div class="badge">Masterclass</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Grok: مسار التظليل", key="b2"):
            st.session_state.art_track = "التظليل والإضاءة"
            st.session_state.page = "studio"
            st.rerun()

elif page == "studio":
    col1, col2, col3 = st.columns([1, 2.5, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'<div class="grok-header">Grok Art Studio // {st.session_state.art_track}</div>', unsafe_allow_html=True)
        st.markdown('<div class="grok-sub">كاميرا الذكاء الاصطناعي متصلة الآن لتحليل خطوطك.</div>', unsafe_allow_html=True)
        
        if st.button("← Back to Grok Home"):
            st.session_state.page = "home"
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        enable_camera = st.checkbox("تفعيل كاميرا التقييم والتتبع المباشر", value=True)
        if enable_camera:
            cam = st.camera_input("التقط صورة لخطواتك على الورقة:")
            if cam:
                st.success("تم تحليل الرسمة بنجاح عبر Grok Vision!")

        st.text_area("اطرح سؤالك على Grok:", placeholder="اكتب استفسارك الفني هنا...")
        if st.button("Ask Grok"):
            st.success("⚡ **Grok:** خطوطك واعدة جداً، حافظ على استقامة اليد عند التخطيط الأولي.")
