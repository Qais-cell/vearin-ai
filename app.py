import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي")
st.write("أهلاً بك! النظام متصل بنماذج المحادثة المباشرة حصراً.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        user_query = st.text_input("اطرح سؤالك على VÆRIN:")
        if st.button("إرسال"):
            if user_query:
                with st.spinner("جاري التفكير والرد..."):
                    models_response = client.models.list()
                    all_models = [m.id for m in models_response.data]
                    
                    # تصفية قوية جداً لاستبعاد أي موديل صوتي، أمان، أو يتطلب شروط خاصة
                    chat_models = [
                        m for m in all_models 
                        if any(x in m.lower() for x in ['llama', 'mixtral', 'gemma']) 
                        and not any(x in m.lower() for x in ['guard', 'whisper', 'vision', 'safeguard', 'orpheus', 'audio', 'prompt'])
                    ]
                    
                    # اختيار أول موديل محادثة متوافق، أو الاعتماد على اسم افتراضي مضمون
                    selected_model = chat_models[0] if chat_models else "llama3-70b-8192"
                    
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
                    st.success("الإجابة:")
                    st.write(answer)
            else:
                st.warning("الرجاء كتابة سؤال أولاً.")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح Groq API الخاص بك للبدء.")
