import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN Study AI", page_icon="📚")

st.title("📚 VÆRIN - مساعدك الدراسي الأكاديمي")
st.write("أهلاً بك! الإصدار المطور للشرح الذكي والعميق.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        user_query = st.text_area("اطرح سؤالك الدراسي، المسألة، أو الموضوع:")
        if st.button("شرح بالتفصيل"):
            if user_query:
                with st.spinner("جاري التحليل والشرح..."):
                    models_response = client.models.list()
                    all_models = [m.id for m in models_response.data]
                    
                    # استبعاد نماذج علام ونماذج الأمان والتركيز على النماذج القوية
                    active_models = [
                        m for m in all_models 
                        if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding', 'allam'])
                    ]
                    
                    selected_model = active_models[0] if active_models else all_models[0]
                    
                    # تعليمات قوية وصارمة تمنع الردود الدبلوماسية الفارغة وتفرضه يكون أستاذ حقيقي
                    system_instructions = (
                        "أنت VÆRIN، أستاذ خصوصي رقمي ذكي، فائق الذكاء، ومختص أكاديمياً. "
                        "ممنوع منعاً باتاً استخدام الردود الدبلوماسية الفارغة أو المقدمات الطويلة (مثل: 'كمساعد ذكاء اصطناعي لا أمتلك تفضيلات...'). "
                        "ادخل في صلب الموضوع فوراً. قدم إجابات دقيقة، أمثلة واقعية، خطوات واضحة، وتبسيطاً كاملاً للمادة العلمية باللغة العربية الفصحى."
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
                    st.success(f"الشرح الأكاديمي (عبر نموذج {selected_model}):")
                    st.write(answer)
            else:
                st.warning("الرجاء كتابة السؤال أو المادة أولاً.")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح Groq API الخاص بك للبدء.")
