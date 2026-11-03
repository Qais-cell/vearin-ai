import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي")
st.write("أهلاً بك! النظام جاهز ويعمل بكفاءة.")

# مفتاح مجاني ثابت ومضمن ليعمل التطبيق مباشرة بدون إدخال يدوي
API_KEY = "PUT_YOUR_API_KEY_HERE"

user_query = st.text_input("اطرح سؤالك على VÆRIN:")

if st.button("إرسال"):
    if user_query:
        with st.spinner("جاري التفكير..."):
            try:
                genai.configure(api_key=API_KEY)
                # استخدام الموديل المتوافق والمستقر
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(user_query)
                st.success("الإجابة:")
                st.write(response.text)
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال: {e}")
    else:
        st.warning("الرجاء كتابة سؤال أولاً.")
