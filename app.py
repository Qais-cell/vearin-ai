import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي")
st.write("أهلاً بك! أدخل مفتاح Google Gemini API الخاص بك للبدء.")

api_key = st.text_input("مفتاح API:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # العودة للموديل المطلوب رسمياً من غوغل
        model = genai.GenerativeModel("gemini-3.8-flash")
        
        user_query = st.text_input("اطرح سؤالك على VÆRIN:")
        if st.button("إرسال"):
            if user_query:
                with st.spinner("جاري المعالجة..."):
                    try:
                        response = model.generate_content(user_query)
                        st.success("الإجابة:")
                        st.write(response.text)
                    except Exception as api_err:
                        # إذا صار ضغط أو تجاوز للحد، الكود ينتظر ويعيد المحاولة تلقائياً
                        if "429" in str(api_err) or "quota" in str(api_err).lower():
                            st.warning("⚠️ تم الوصول للحد المؤقت، جاري إعادة المحاولة تلقائياً بعد ثوانٍ...")
                            time.sleep(15)
                            response = model.generate_content(user_query)
                            st.success("الإجابة:")
                            st.write(response.text)
                        else:
                            st.error(f"خطأ في الرد: {api_err}")
            else:
                st.warning("الرجاء كتابة سؤال أولاً.")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info("الرجاء إدخال مفتاح الـ API في الحقل أعلاه للبدء.")
