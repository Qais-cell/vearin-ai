import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي")
st.write("أهلاً بك! أدخل مفتاح Google Gemini API وابدأ المحادثة فوراً.")

api_key = st.text_input("مفتاح API:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-3.8-flash")
        
        user_query = st.text_input("اطرح سؤالك على VÆRIN:")
        if st.button("إرسال"):
            if user_query:
                with st.spinner("جاري التفكير..."):
                    response = model.generate_content(user_query)
                    st.success("الإجابة:")
                    st.write(response.text)
            else:
                st.warning("الرجاء كتابة سؤال أولاً.")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح الـ API في الحقل أعلاه للبدء.")
