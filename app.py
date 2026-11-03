import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN Study AI", page_icon="🎓")

st.title("🎓 VÆRIN - معلمك الأكاديمي الخارق")
st.write("أهلاً بك! الإصدار المطور ليتفوق على التدريس الخصوصي التقليدي بالسرعة، العمق، والدقة.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        user_query = st.text_area("اطرح سؤالك أو المادة التي تريد أن أشرحها لك بتفوق:")
        if st.button("بدء الشرح المتقدم"):
            if user_query:
                with st.spinner("جاري إعداد الشرح الخارق..."):
                    models_response = client.models.list()
                    all_models = [m.id for m in models_response.data]
                    
                    active_models = [
                        m for m in all_models 
                        if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding', 'allam'])
                    ]
                    
                    selected_model = active_models[0] if active_models else all_models[0]
                    
                    # نظام تعليمي يجعله يتفوق على المعلم الخصوصي (شرح عميق، أمثلة، واختبارات فورية)
                    system_instructions = (
                        "أنت VÆRIN، المعلم الأكاديمي الخارق الذي يتفوق على أي مدرس خصوصي بشري. "
                        "مهمتك ليس فقط الإجابة، بل تقديم شرح عميق ومبسط جداً، مع ضرب أمثلة من الواقع، "
                        "وتقديم 'تمرين سريع' أو سؤال اختباري في نهاية إجابتك لتتأكد أن الطالب فهم المادة تماماً. "
                        "ممنوع الردود الدبلوماسية الفارغة. كن ذكياً، مباشراً، ومبدعاً بالشرح باللغة العربية الفصحى."
                    )
                    
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": system_instructions},
                            {"role": "user", "content": user_query}
                        ],
                        model=selected_model,
                        max_tokens=1024,
                    )
                    
                    answer = chat_completion.choices[0].message.content
                    st.success(f"شرح المعلم الخارق (عبر نموذج {selected_model}):")
                    st.write(answer)
            else:
                st.warning("الرجاء كتابة السؤال أو المادة أولاً.")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح Groq API الخاص بك للبدء.")
