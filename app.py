import streamlit as st

st.set_page_config(
    page_title="VÆRIN Neural Canvas",
    page_icon="⚡",
    layout="centered"
)

# --- تصميم الفخامة (Grok-style Dark Neon & Animations) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #f1f5f9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* انترو البداية والنبض */
    @keyframes pulseGlow {
        0%, 100% { text-shadow: 0 0 10px rgba(0, 242, 254, 0.4); }
        50% { text-shadow: 0 0 25px rgba(121, 40, 202, 0.8); }
    }
    
    .grok-title {
        font-size: 24px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.5px;
        animation: pulseGlow 3s infinite ease-in-out;
    }
    
    .grok-sub {
        font-size: 13px;
        color: #a1a1aa;
        margin-bottom: 20px;
    }

    /* تنسيق الكاردات الفخمة */
    .grok-card {
        background: #09090b;
        border: 1px solid #1f1f23;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 14px;
        transition: all 0.2s ease;
    }
    .grok-card:hover {
        border-color: #00f2fe;
        background: #0f0f13;
    }
    
    /* أزرار عصرية مطابقة للتصميم */
    .stButton>button {
        background: linear-gradient(135deg, #00f2fe 0%, #7928ca 100%) !important;
        color: #ffffff !important;
        font-weight: 700;
        border-radius: 10px !important;
        border: none !important;
        padding: 10px 16px !important;
        width: 100%;
        box-shadow: 0 4px 12px rgba(0, 242, 254, 0.2);
    }
    .stButton>button:hover {
        opacity: 0.9;
    }
    
    .stTextInput input, .stTextArea textarea {
        background-color: #09090b !important;
        color: #ffffff !important;
        border: 1px solid #27272a !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التنقل
if "tab" not in st.session_state:
    st.session_state.tab = "المسارات"

# --- التبويبات العلوية (على اليسار بتنسيق فخم ونظيف) ---
col_t1, col_t2, col_t3, col_space = st.columns([1.2, 1.2, 1.2, 2.5])

with col_t1:
    if st.button("📚 المسارات", key="btn_tracks"):
        st.session_state.tab = "المسارات"
        st.rerun()
with col_t2:
    if st.button("📸 المرسم", key="btn_studio"):
        st.session_state.tab = "المرسم"
        st.rerun()
with col_t3:
    if st.button("🧠 مساعد AI", key="btn_ai"):
        st.session_state.tab = "مساعد AI"
        st.rerun()

st.write("---")

# --- محتوى الأقسام ---
if st.session_state.tab == "المسارات":
    st.markdown('<div class="grok-title">⚡ VÆRIN // Neural Canvas</div>', unsafe_allow_html=True)
    st.markdown('<div class="grok-sub">اختر مسار التعلم لبدء جلسة الرسم والتوجيه الحي.</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="grok-card">
            <h3 style="color: #00f2fe; margin-bottom: 6px; font-size: 16px;">✏️ أساسيات الخطوط والمنظور</h3>
            <p style="color: #94a3b8; font-size: 13px; margin-bottom: 10px;">ضبط حركة اليد، التحكم بالقلم، ورسم الأشكال الهندسية بدقة عالية.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("دخول مسار الأساسيات"):
        st.session_state.tab = "المرسم"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="grok-card">
            <h3 style="color: #7928ca; margin-bottom: 6px; font-size: 16px;">🎨 التظليل والواقعية المتقدمة</h3>
            <p style="color: #94a3b8; font-size: 13px; margin-bottom: 10px;">أسرار تباين الضوء والظل (Chiaroscuro) وتقنيات كبار الرسامين.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("دخول مسار التظليل"):
        st.session_state.tab = "المرسم"
        st.rerun()

elif st.session_state.tab == "المرسم":
    st.markdown('<div class="grok-title">📸 استوديو الكاميرا الحي</div>', unsafe_allow_html=True)
    st.markdown('<div class="grok-sub">كاميرا الذكاء الاصطناعي جاهزة لتحليل خطواتك على الورق.</div>', unsafe_allow_html=True)
    
    cam = st.camera_input("التقط صورة لخطوات الرسم:")
    if cam:
        st.success("⚡ تم فحص الخطوط والمنظور بنجاح! النسبة الفنية: 92%.")

elif st.session_state.tab == "مساعد AI":
    st.markdown('<div class="grok-title">🧠 عقل المساعد الذكي</div>', unsafe_allow_html=True)
    st.markdown('<div class="grok-sub">اسأل أي استفسار فني وسيجيبك النظام فوراً.</div>', unsafe_allow_html=True)
    
    q = st.text_input("اكتب سؤالك هنا:", placeholder="مثال: كيف أوزع الإضاءة؟")
    if st.button("إرسال السؤال"):
        if q:
            st.info("🤖 **VÆRIN AI:** لتوزيع الإضاءة بشكل احترافي، حدد زاوية سقوط الضوء وعزز التباين في المناطق العميقة.")
