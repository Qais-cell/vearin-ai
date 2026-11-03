import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي")
st.write("أهلاً بك! النظام يبحث عن نموذج محادثة متاح ويتصل به تلقائياً.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        user_query = st.text_input("اطرح سؤالك على VÆRIN:")
        if st.button("إرسال"):
            if user_query:
                with st.spinner("جاري جلب نموذج المحادثة والرد..."):
                    # جلب قائمة النماذج المتوفرة في مفتاحك
                    models_response = client.models.list()
                    all_models = [m.id for m in models_response.data]
                    
                    # استبعاد نماذج الأمان والصوت وتصفية نماذج الدردشة
                    valid_models = [
                        m for m in all_models 
                        if not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'embed', 'prompt'])
                    ]
                    
                    # استخدام أول نموذج دردشة شغال أو البديل العام
                    selected_model = valid_models[0] if valid_models else "llama3-8b-8192"
                    
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": user_query,
                            }
                        ],
                        model=selected_model,
                    )
                    
                    answer = chat_completion.choices[0].message.content
                    st.success(f"الإجابة (عبر نموذج {selected_model}):")
                    st.write(answer)
            else:
                st.warning("الرجاء كتابة سؤال أولاً.")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح Groq API الخاص بك للبدء.")
