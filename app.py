import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN Ultimate Study AI", page_icon="🎓")

st.title("🎓 VÆRIN - معلمك الأكاديمي الخارق والمتكامل")
st.write("أهلاً بك! الإصدار النهائي المتكامل: ذاكرة حديدية، ذكاء فائق يتفوق على المدرس الخصوصي، وأداء سريع.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        # 1. تهيئة ذاكرة المحادثة المتكاملة إذا لم تكن موجودة
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system", 
                    "content": (
                        "أنت VÆRIN، المعلم الأكاديمي الخارق الذي يمتلك ذاكرة استثنائية وذكاء يفوق التدريس الخصوصي البشري بكثير. "
                        "تتذكر كل تفاصيل المحادثة الحالية وتربط المعلومات ببعضها بدقة عالية. "
                        "قدم دائماً شروحات عميقة، أمثلة واقعية، واختبر فهم الطالب بسؤال سريع أو تمرين في النهاية. "
                        "ممنوع منعاً باتاً استخدام الردود الدبلوماسية الفارغة أو المقدمات السطحية. "
                        "كن مباشراً، ذكياً، ومبدعاً باللغة العربية الفصحى الفصيحة."
                    )
                }
            ]

        # 2. عرض سجل المحادثة السابق (الذاكرة المتكاملة) على الشاشة
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        # 3. صندوق الإدخال التفاعلي للمحادثة المستمرة
        if user_query := st.chat_input("اطرح سؤالك أو تابع النقاش مع VÆRIN..."):
            # إضافة رسالة المستخدم إلى الذاكرة وعرضها فوراً
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            with st.spinner("جاري التفكير، استرجاع الذاكرة، وإعداد الشرح..."):
                # البحث الذكي والتصفية التلقائية للموديلات لمنع أخطاء 404 أو 429
                models_response = client.models.list()
                all_models = [m.id for m in models_response.data]
                
                active_models = [
                    m for m in all_models 
                    if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding', 'allam'])
                ]
                
                selected_model = active_models[0] if active_models else all_models[0]
                
                # إرسال سجل الذاكرة بالكامل إلى نموذج Groq
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model=selected_model,
                    max_tokens=1024,
                )
                
                assistant_answer = chat_completion.choices[0].message.content
                
                # إضافة رد المساعد إلى الذاكرة وعرضه في الشات
                st.session_state.messages.append({"role": "assistant", "content": assistant_answer})
                with st.chat_message("assistant"):
                    st.write(assistant_answer)

    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح Groq API الخاص بك للبدء.")
