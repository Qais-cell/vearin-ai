import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي")
st.write("أهلاً بك! النظام متصل ومستعد للمحادثة.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        user_query = st.text_input("اطرح سؤالك على VÆRIN:")
        if st.button("إرسال"):
            if user_query:
                with st.spinner("جاري التفكير والرد..."):
                    models_response = client.models.list()
                    # استخراج جميع النماذج المتاحة فعلياً في حسابك وتجنب النماذج المعطلة أو الحماية
                    active_models = [
                        m.id for m in models_response.data 
                        if not any(x in m.id.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt', 'embedding'])
                    ]
                    
                    # اختيار أول نموذج نشط وحقيقي متوفر في القائمة
                    selected_model = active_models[0] if active_models else "llama-3.3-70b-versatile"
                    
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
