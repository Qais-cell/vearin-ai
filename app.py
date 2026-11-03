import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN Study AI", page_icon="🧠")

st.title("🧠 VÆRIN - معلمك الأكاديمي ذو الذاكرة الخارقة")
st.write("أهلاً بك! هذا الإصدار يتذكر كل تفاصيل نقاشنا وسؤالك السابق لتقديم إجابات متصلة وذكية.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        # تهيئة ذاكرة المحادثة إذا لم تكن موجودة
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system", 
                    "content": (
                        "أنت VÆRIN، المعلم الأكاديمي الخارق الذي يمتلك ذاكرة استثنائية وذكاء يفوق التدريس الخصوصي. "
                        "تتذكر كل ما قاله الطالب في المحادثة الحالية وتربط المعلومات ببعضها بدقة. "
                        "قدم دائماً شروحات عميقة، أمثلة واقعية، واختبر فهم الطالب بسؤال سريع في النهاية. "
                        "كن مباشراً، ذكياً، ومبدعاً باللغة العربية الفصحى."
                    )
                }
            ]

        # عرض سجل المحادثة السابق على الشاشة
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        # استقبال رسالة جديدة من المستخدم
        if user_query := st.chat_input("اطرح سؤالك أو تابع النقاش مع VÆRIN..."):
            # إضافة رسالة المستخدم إلى الذاكرة وعرضها
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            with st.spinner("جاري التفكير وربط الأفكار..."):
                models_response = client.models.list()
                all_models = [m.id for m in models_response.data]
                
                active_models = [
                    m for m in all_models 
                    if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding', 'allam'])
                ]
                
                selected_model = active_models[0] if active_models else all_models[0]
                
                # إرسال كامل سجل المحادثة (الذاكرة) إلى النموذج
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model=selected_model,
                    max_tokens=1024,
                )
                
                assistant_answer = chat_completion.choices[0].message.content
                
                # إضافة إجابة المساعد إلى الذاكرة وعرضها
                st.session_state.messages.append({"role": "assistant", "content": assistant_answer})
                with st.chat_message("assistant"):
                    st.write(assistant_answer)

    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح Groq API الخاص بك للبدء.")
