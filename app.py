import streamlit as st
from groq import Groq
import time

# إعدادات الصفحة
st.set_page_config(page_title="VÆRIN Ultimate Pro", page_icon="🎓", layout="centered")

# --- أنيميشن فتح الموقع (Intro Splash Screen) مع تسجيل الدخول واختيار طريقة الدراسة ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #000000, #111119, #1a1a2e);
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Icons", sans-serif;
        }
        .intro-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 40px 20px;
            animation: fadeInScale 1.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .main-title {
            font-size: 42px;
            font-weight: 800;
            background: linear-gradient(135deg, #0A84FF, #5E5CE6, #FF375F);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 5px;
        }
        .sub-title {
            font-size: 16px;
            color: #8E8E93;
            text-align: center;
            margin-bottom: 30px;
        }
        @keyframes fadeInScale {
            0% { opacity: 0; transform: scale(0.92); }
            100% { opacity: 1; transform: scale(1); }
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="intro-container">', unsafe_allow_html=True)
        st.markdown('<div class="main-title">VÆRIN Pro 🎓</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">المعلم الأكاديمي الأذكى والأسرع بسلاسة فائقة</div>', unsafe_allow_html=True)
        
        # خيارات تسجيل الدخول وطريقة الدراسة بالانترو
        st.markdown("### 🔐 تسجيل الدخول للبدء")
        login_method = st.radio("اختر طريقة الدخول:", ["تسجيل سريع (Google Account)", "تسجيل بالبريد الإلكتروني والرمز"])
        
        if login_method == "تسجيل بالبريد الإلكتروني والرمز":
            st.text_input("البريد الإلكتروني:")
            st.text_input("كلمة المرور:", type="password")
            
        st.markdown("### 🎯 كيف ترغب أن يدرسك VÆRIN؟")
        study_style_pref = st.selectbox("اختر أسلوبك الدراسي المفضل:", [
            "شرح عميق ومبسط مع أمثلة واقعية",
            "حل المسائل والتمارين خطوة بخطوة",
            "تلخيص المقالات والنصوص بدقة متناهية",
            "مراجعة شاملة وسريعة للمادة"
        ])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 الدخول إلى النظام وبدء الجلسة", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.study_pref = study_style_pref
            st.success("تم تسجيل الدخول بنجاح! جاري فتح الواجهة...")
            time.sleep(0.8)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- التصميم الأساسي للواجهة بسلاسة وفخامة الآيفون ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Icons", "Helvetica Neue", sans-serif;
    }
    .main {
        background-color: #000000;
        color: #F5F5F7;
    }
    .stChatMessage {
        background: rgba(28, 28, 30, 0.85);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 0.5px solid rgba(255, 255, 255, 0.15);
        border-radius: 22px;
        padding: 15px;
        margin-bottom: 14px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        animation: slideUp 0.4s ease-out;
    }
    @keyframes slideUp {
        0% { opacity: 0; transform: translateY(15px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    h1 {
        background: linear-gradient(135deg, #0A84FF, #5E5CE6, #FF375F);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 VÆRIN - المعلم الأكاديمي الخارق")
st.write(f"أهلاً بك! الأسلوب المختار: **{st.session_state.get('study_pref', 'شرح عام')}** | الذاكرة والأنظمة تعمل بكفاءة تامة.")

# --- شريط الإعدادات الجانبي ---
with st.sidebar:
    st.header("⚙️ إعدادات التحكم")
    api_key = st.text_input("🔑 مفتاح Groq API:", type="password")
    
    st.markdown("---")
    st.subheader("🎛️ تخصيص الأداء")
    temperature = st.slider("درجة الإبداع والدقة (Temperature):", 0.0, 1.0, 0.7, 0.1)
    max_tokens_val = st.slider("طول الشرح (Max Tokens):", 256, 2048, 1024, 128)
    
    st.markdown("---")
    if st.button("🗑️ مسح الذاكرة وبدء درس جديد"):
        if "messages" in st.session_state:
            del st.session_state.messages
        st.success("تم مسح الذاكرة بنجاح!")
        st.rerun()
    
    if st.button("🚪 تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()

# التحقق من مفتاح الـ API والتشغيل
if api_key:
    try:
        client = Groq(api_key=api_key)
        
        # تهيئة الذاكرة والشخصية الأكاديمية الثابتة
        if "messages" not in st.session_state:
            pref = st.session_state.get('study_pref', 'شرح عام')
            st.session_state.messages = [
                {
                    "role": "system", 
                    "content": (
                        f"أنت VÆRIN، المعلم الأكاديمي الخارق الذي يتفوق على المدرس الخصوصي. الأسلوب المفضل للطالب هو: {pref}. "
                        "تمتلك ذاكرة حديدية استثنائية وتربط تفاصيل المحادثة بدقة عالية. "
                        "قاعدة صارمة جداً: لا تقم أبداً بعمل اختبارات أو أسئلة امتحانية للطالب إلا إذا طلب منك ذلك صراحةً. "
                        "إذا طلب منك اللهجة أو أي أسلوب، نفذ طلبه فوراً بالشرح الطبيعي وبدون امتحانات عشوائية. "
                        "كن مباشراً، ذكياً، ومبدعاً."
                    )
                }
            ]

        # عرض سجل المحادثة
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        # صندوق الإدخال التفاعلي
        if user_query := st.chat_input("اطرح سؤالك أو اطلب الشرح..."):
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            with st.spinner("✨ جاري التفكير وإعداد الشرح الخارق بسلاسة..."):
                models_response = client.models.list()
                all_models = [m.id for m in models_response.data]
                
                active_models = [
                    m for m in all_models 
                    if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding', 'allam'])
                ]
                
                selected_model = active_models[0] if active_models else all_models[0]
                
                # استخدام max_tokens بالشكل الصحيح تماماً بدون أخطاء
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model=selected_model,
                    temperature=temperature,
                    max_tokens=max_tokens_val,
                )
                
                assistant_answer = chat_completion.choices[0].message.content
                
                st.session_state.messages.append({"role": "assistant", "content": assistant_answer})
                with st.chat_message("assistant"):
                    st.write(assistant_answer)

    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("👈 الرجاء إدخال مفتاح Groq API في الشريط الجانبي (Sidebar) للبدء.")
