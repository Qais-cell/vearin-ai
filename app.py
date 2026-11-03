import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي (بدون حدود)")
st.write("أهلاً بك! هذا الإصدار يعمل بحرية كاملة وبدون قيود الحصص.")

user_query = st.text_input("اطرح سؤالك على VÆRIN:")

if st.button("إرسال"):
    if user_query:
        with st.spinner("جاري التفكير بحرية..."):
            try:
                # استخدام رابط مجاني مفتوح لا يتطلب قيود مفاتيح وقنوات ضغط
                url = "https://text.pollinations.ai/" + urllib.parse.quote(user_query)
                req = urllib.request.Request(
                    url, 
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                with urllib.request.urlopen(req) as response:
                    answer = response.read().decode('utf-8')
                    st.success("الإجابة:")
                    st.write(answer)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("الرجاء كتابة سؤال أولاً.")
