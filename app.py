import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN Study AI", page_icon="📚")

st.title("📚 VÆRIN - مساعدك الدراسي الأكاديمي")
st.write("أهلاً بك! هذا الإصدار مخصص حصراً للشرح الأكاديمي، حل المسائل، وتلخيص المقالات بدقة.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        user_query = st.text_area("اطرح سؤالك الدراسي أو المادة التي تريد شرحها:")
        if st.button("بدء الشرح والتحليل"):
            if user_query:
                with st.spinner("جاري جلب نموذج المحادثة وإعداد الشرح الأكاديمي..."):
                    # جلب قائمة النماذج المتاحة فعلياً في حسابك وتجنب النماذج المعطلة أو الحماية
                    models_response = client.models.list()
                    all_models = [m.id for m in models_response.data]
                    
                    # تصفية النماذج النشطة المخصصة للشات واستبعاد الأمان والصوت
                    active_models = [
                        m for m in all_models 
                        if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding'])
                    ]
                    
                    # اختيار أول نموذج نشط حقيقي متوفر في القائمة أو أي موديل بديل يرجع من السيرفر
                    selected_model = active_models[0] if active_models else all_models[0]
                    
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system", 
                                "content": "أنت VÆRIN، مساعد أكاديمي وتعليمي خبير ومتخصص. مهمتك هي تقديم شروحات علمية دقيقة، مبسطة، ومنظمة (باستخدام النقاط والعناوين الواضحة)، ومساعدة الطالب في فهم المواد الدراسية، حل المسائل، وتقديم أمثلة تعليمية واضحة باللغة العربية الفصحى."
                            },
                            {
                                "role": "user",
                                "content": user_query,
                            }
                        ],
                        model=selected_model,
                        max_tokens=1024,
                    )
                    
                    answer = chat_completion.choices[0].message.content
                    st.success(f"النتيجة الأكاديمية (عبر نموذج {selected_model}):")
                    st.write(answer)
            else:
                st.warning("الرجاء كتابة السؤال أو المادة الدراسية أولاً.")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح Groq API الخاص بك للبدء.")
