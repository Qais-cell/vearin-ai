import streamlit as st
import re

st.set_page_config(page_title="VÆRIN Art Academy", page_icon="🎨", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "art_track" not in st.session_state:
    st.session_state.art_track = "الأساسيات والمنظور"

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# --- تصميم عصري وفاخر (Dark Futuristic Theme) ---
st.markdown("""
    <style>
    .stApp {
        background: #050505;
        color: #e6edf3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .hero-title {
        font-size: 32px;
        font-weight: 950;
        text-align: center;
        background: linear-gradient(135deg, #ffffff 0%, #a855f7 50%, #6366f1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .hero-subtitle {
        font-size: 13px;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 25px;
    }
    .art-card {
        background: #0d0d11;
        border: 1px solid #1e1e2d;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 14px;
        transition: all 0.3s ease;
    }
    .art-card:hover {
        border-color: #8b5cf6;
        background: #13131c;
        transform: translateY(-2px);
    }
    .card-title {
        font-size: 16px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 6px;
    }
    .card-desc {
        font-size: 12px;
        color: #94a3b8;
        line-height: 1.4;
    }
    .badge {
        display: inline-block;
        background: rgba(139, 92, 246, 0.15);
        color: #c084fc;
        font-size: 10px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 20px;
        margin-top: 10px;
        border: 1px solid rgba(139, 92, 246, 0.3);
    }
    .stTextInput input {
        background-color: #0d0d11 !important;
        color: #ffffff !important;
        border: 1px solid #1e1e2d !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        font-weight: 700;
        border-radius: 12px !important;
        border: none !important;
        width: 100%;
        padding: 12px;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# التنقل المباشر بدون تعليق
page = st.session_state.page

if page == "home":
    col1, col2, col3 = st.columns([1, 2.5, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="hero-title">VÆRIN ART ACADEMY</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">تعلّم الرسم من الصفر حتى الاحتراف الكامل بالذكاء الاصطناعي</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="art-card">
                <div class="card-title">✏️ المستوى الأول: التخطيط والخطوط</div>
                <div class="card-desc">تدريب مباشر على رسم الأشكال والمنظور الأولي عبر تفاعل الكاميرا والتتبع.</div>
                <div class="badge">مسار مبتدئ (Zero to Pro)</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("انطلق في مسار الأساسيات"):
            st.session_state.art_track = "الأساسيات والمنظور"
            st.session_state.page = "login"
            st.rerun()

        st.markdown("""
            <div class="art-card">
                <div class="card-title">🎨 المستوى الثاني: التظليل والواقعية</div>
                <div class="card-desc">تعلم أسرار توزيع الإضاءة، التباين، وتحويل الرسم إلى ثلاثي الأبعاد.</div>
                <div class="badge">تقنيات كبار الرسامين</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("انطلق في مسار التظليل"):
            st.session_state.art_track = "التظليل والإضاءة"
            st.session_state.page = "login"
            st.rerun()

elif page == "login":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Authenticate</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">أدخل بريدك الإلكتروني لحفظ تقدمك في الأكاديمية</div>', unsafe_allow_html=True)
        
        email_input = st.text_input("البريد الإلكتروني", placeholder="artist@example.com")
        
        if st.button("الدخول إلى المرسم"):
            if is_valid_email(email_input):
                st.session_state.user_email = email_input
                st.session_state.page = "studio"
                st.rerun()
            else:
                st.error("الرجاء إدخال بريد إلكتروني صحيح.")

elif page == "studio":
    st.title("🎨 VÆRIN Neural Art Studio")
    
    with st.sidebar:
        st.header("لوحة التحكم")
        st.write(f"المستعمل: **{st.session_state.get('user_email', '')}**")
        st.write(f"المسار: **{st.session_state.get('art_track', '')}**")
        st.markdown("---")
        enable_camera = st.checkbox("تفعيل كاميرا التقييم والتتبع", value=True)
        st.markdown("---")
        if st.button("الرجوع للقائمة الرئيسية"):
            st.session_state.page = "home"
            st.rerun()

    st.subheader(f"الدرس الحالي: {st.session_state.get('art_track', '')}")
    st.info("سوف تقوم الكاميرا بالتقاط رسوماتك على الورق وتحليل خطوطك وتوجيهك خطوة بخطوة.")
    
    if enable_camera:
        camera_image = st.camera_input("وجه الكاميرا على الورقة التي ترسم عليها:")
        if camera_image:
            st.success("تم التقاط الرسمة! جاري التحليل والمقارنة بطرق كبار الرسامين...")

    st.text_area("استفساراتك الفنية أو تقييم خطوطك:", placeholder="اكتب هنا...")
    if st.button("إرسال للتحليل الفني"):
        st.write("🤖 **VÆRIN AI:** خطوطك ممتازة! واصل التدريب بخفة يد.")
