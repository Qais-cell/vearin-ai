import streamlit as st
import urllib.request
import urllib.parse
import json

st.set_page_config(page_title="VÆRIN AI", page_icon="🤖")

st.title("🤖 مساعد VÆRIN الذكي")
st.write("أهلاً بك! نظام حر ومجاني بالكامل.")

user_query = st.text_input("اطرح سؤالك على VÆRIN:")

if st.button("إرسال"):
    if user_query:
        with st.spinner("جاري جلب الإجابة..."):
            try:
                # استخدام رابط بديل مجاني تماماً ومستقر للدردشة
                encoded_query = urllib.parse.quote(user_query)
                url = f"https://kaiz-apis.gleeze.com/api/gpt-4o-mini?q={encoded_query}"
                
                req = urllib.request.Request(
                    url, 
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                
                with urllib.request.urlopen(req) as response:
                    data = json.loads(response.read().decode('utf-8'))
                    # استخراج النص من الاستجابة
                    if 'response' in data:
                        answer = data['response']
                    elif 'result' in data:
                        answer = data['result']
                    else:
                        answer = str(data)
                        
                    st.success("الإجابة:")
                    st.write(answer)
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال: {e}")
    else:
        st.warning("الرجاء كتابة سؤال أولاً.")
