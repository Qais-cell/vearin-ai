import streamlit as st

st.set_page_config(
    page_title="VÆRIN Neural Canvas",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown('<style>html, body, .stApp { background-color: #000000 !important; color: #f4f4f5; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }</style>', unsafe_allow_html=True)
st.markdown('<style>@keyframes floatGlow { 0%, 100% { text-shadow: 0 0 12px rgba(255, 255, 255, 0.6); } 50% { text-shadow: 0 0 22px rgba(255, 255, 255, 0.9); } }</style>', unsafe_allow_html=True)
st.markdown('<style>.grok-title { font-size: 18px; font-weight: 800; color: #ffffff; animation: floatGlow 3s infinite ease-in-out; }</style>', unsafe_allow_html=True)
st.markdown('<style>.grok-sub { font-size: 11px; color: #a1a1aa; margin-bottom: 12px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.grok-card { background: #09090b; border: 1px solid #27272a; border-radius: 10px; padding: 12px; margin-bottom: 10px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.stButton>button { background: #ffffff !important; color: #000000 !important; font-weight: 800 !important; border-radius: 8px !important; border: none !important; padding: 6px 12px !important; font-size: 12px !important; width: 100%; }</style>', unsafe_allow_html=True)
st.markdown('<style>.stTextInput input { background-color: #09090b !important; color: #ffffff !important; border: 1px solid #27272a !important; border-radius: 8px !important; }</style>', unsafe_allow_html=True)
st.markdown('<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>', unsafe_allow_html=True)

if "mode" not in st.session_state:
    st.session_state.mode = "chat"

# صف العرض العلوي: العنوان يساراً وتبويب التدريب أقصى اليسار فوق
top_c1, top_c2 = st.columns([2, 1])

with top_c1:
    st.markdown('<div class="grok-title">⚡ VÆRIN NEURAL</div>', unsafe_allow_html=True)

with top_c2:
    if st.session_state.mode == "chat":
        if st.button("🎯 التدريب"):
            st.session_state.mode = "training"
            st.rerun()
    else:
        if st.button("💬 المحادثة"):
            st.session_state.mode = "chat"
            st.rerun()

st.write("---")

if st.session_state.mode == "training":
    st.markdown('<div class="grok-sub">قسم تدريب المستخدم والتحليلات البصرية</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="grok-card"><h3 style="color: #ffffff; font-size: 13px;">✏️ مسار أساسيات الخطوط</h3><p style="color: #a1a1aa; font-size: 11px;">ضبط ثبات اليد وبناء الأشكال.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="grok-card"><h3 style="color: #ffffff; font-size: 13px;">📸 كاميرا التتبع الفوري</h3><p style="color: #a1a1aa; font-size: 11px;">التقط صورة لورقة الرسم لتقييم الخطوط.</p></div>', unsafe_allow_html=True)
    
    cam = st.camera_input("التقط صورة للرسمة:")
    if cam:
        st.success("⚡ تم فحص الرسمة بنجاح.")

else:
    st.markdown('<div class="grok-sub">المساعد الذكي الفني - اسأل واستشر حول الرسم</div>', unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "ai", "content": "أهلاً بك! أنا عقل VÆRIN الذكي. اطرح علي أي سؤال بخصوص تقنيات الرسم، التظليل، أو توزيع الضوء والظلال."}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "ai":
            st.markdown(f'<div class="grok-card"><span style="font-size: 10px; color: #a1a1aa;">🤖 VÆRIN AI</span><p style="font-size: 12px; margin-top: 3px; color: #f4f4f5;">{msg["content"]}</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="grok-card" style="background: #18181b;"><span style="font-size: 10px; color: #a1a1aa;">👤 أنت</span><p style="font-size: 12px; margin-top: 3px; color: #ffffff;">{msg["content"]}</p></div>', unsafe_allow_html=True)

    user_q = st.text_input("اكتب رسالتك للنموذج:", placeholder="اسأل عن أي مهارة فنية...")
    if st.button("إرسال الاستفسار"):
        if user_q.strip():
            st.session_state.messages.append({"role": "user", "content": user_q})
            reply = f"لتحسين مهارة '{user_q}'، أنصحك بالتركيز على إيقاع حركة اليد والتحكم بتدرجات الضوء."
            st.session_state.messages.append({"role": "ai", "content": reply})
            st.rerun()
