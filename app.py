import streamlit as st
from groq import Groq

# إعدادات الصفحة بتصميم عصري
st.set_page_config(page_title="VÆRIN Ultimate Study AI", page_icon="🎓", layout="centered")

# إضافة تأثيرات جمالية وانيميشن خفيف (CSS Styling) للواجهة
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stChatMessage:hover {
        transform: translateY(-2px);
    }
    h1 {
        background: linear-gradient(90deg, #4f46e5, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 VÆRIN - معلمك الأكاديمي الخارق")
st.write("أهلاً بك في الإصدار الفائق: واجهة حركية متطورة، تحكم كامل بالإعدادات، وذاكرة حديدية.")

# --- شريط الإعدادات الجانبي الحقيقي للطالب ---
with st.sidebar:
    st.header("⚙️ إعدادات التحكم الخارقة")
    
    api_key = st.text_input("🔑 مفتاح Groq API:", type="password")
    
    st.markdown("---")
    st.subheader("🎛️ خيارات النموذج")
    
    # خيار التحكم بدرجة الإبداع (Temperature)
    temperature = st.slider("درجة الإبداع والدقة (Temperature):", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    
    # خيار التحكم بعدد التوكنات للرد
    max_tokens_val = st.slider("طول الشرح (Max Tokens):", min_value=256, max_value=2048, value=1024, step=128)
    
    st.markdown("---")
    # زر مسح ذاكرة المحادثة لبدء درس جديد
    if st.button("🗑️ مسح الذاكرة وبدء درس جديد"):
        if "messages" in st.session_state:
            del st.session_state.messages
        st.success("تم مسح الذاكرة بنجاح!")
        st.rerun()

# التحقق من إدخال المفتاح لبدء التشغيل
if api_key:
    try:
        client = Groq(api_key=api_key)
        
        # 1. تهيئة ذاكرة المحادثة وشخصية المعلم الأكاديمي الخارق
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system", 
                    "content": (
                        "أنت VÆRIN، المعلم الأكاديمي الذكي والخارق. تمتلك ذاكرة استثنائية وتربط تفاصيل المحادثة بدقة عالية. "
                        "قاعدة صارمة جداً: لا تقم أبداً بعمل اختبارات أو أسئلة امتحانية للطالب إلا إذا طلب منك ذلك صراحةً. "
                        "إذا طلب منك التحدث باللهجة المحددة (مثل اللهجة السعودية أو غيرها) أو أي أسلوب حواري، نفذ طلبه في السوالف والشرح الطبيعي فوراً وبدون أي امتحانات. "
                        "كن مباشراً، ذكياً، ومبدعاً باللغة العربية الفصحى أو اللهجة المطلوبة."
                    )
                }
            ]

        # 2. عرض سجل المحادثة السابق مع الانيميشن والتنسيق
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        # 3. صندوق الإدخال التفاعلي المطور
        if user_query := st.chat_input("اطرح سؤالك أو اطلب شرح المادة..."):
            # إضافة رسالة المستخدم إلى الذاكرة وعرضها
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            with st.spinner("✨ جاري التفكير بعمق، استرجاع الذاكرة، وإعداد الشرح الخارق..."):
                # التصفية التلقائية الذكية للموديلات لمنع أخطاء 404 أو 429
                models_response = client.models.list()
                all_models = [m.id for m in models_response.data]
                
                active_models = [
                    m for m in all_models 
                    if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding', 'allam'])
                ]
                
                selected_model = active_models[0] if active_models else all_models[0]
                
                # إرسال الطلب مع الإعدادات المخصصة من شريط التحكم
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model=selected_model,
                    temperature=temperature,
                    max_tokens=max_tokens_val,
                )
                
                assistant_answer = chat_completion.choices[0].message.content
                
                # إضافة رد المساعد إلى الذاكرة وعرضه في الشات
                st.session_state.messages.append({"role": "assistant", "content": assistant_answer})
                with st.chat_message("assistant"):
                    st.write(assistant_answer)

    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("👈 الرجاء إدخال مفتاح Groq API في الشريط الجانبي (Sidebar) للبدء واستعراض الواجهة الخرافية.")
