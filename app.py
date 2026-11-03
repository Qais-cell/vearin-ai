import streamlit as st
from groq import Groq

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي (عبر Groq)")
st.write("أهلاً بك! النظام يبحث عن أحدث نموذج متاح ويتصل به تلقائياً.")

api_key = st.text_input("أدخل مفتاح Groq API:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        user_query = st.text_input("اطرح سؤالك على VÆRIN:")
        if st.button("إرسال"):
            if user_query:
                with st.spinner("جاري جلب أحدث نموذج والرد..."):
                    # جلب قائمة النماذج المتوفرة واختيار أول نموذج شغال تلقائياً
                    models_response = client.models.list()
                    available_models = [m.id for m in models_response.data if "chat" in m.id or "llama" in m.id]
                    
                    # اختيار موديل لاما حديث متوفر في الحساب
                    selected_model = next((m for m in available_models if "llama" in m), "llama-3.1-8b-instant")
                    
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
