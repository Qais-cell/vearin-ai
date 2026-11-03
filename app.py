import streamlit as st
from groq import Groq

st.set_page_config(page_title="VAERIN Ultimate Pro", page_icon=None, layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "selected_provider" not in st.session_state:
    st.session_state.selected_provider = ""

if not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        .stButton button {
            background-color: #21262d !important;
            color: #c9d1d9 !important;
            font-weight: 500;
            border-radius: 8px !important;
            border: 1px solid rgba(240, 246, 252, 0.15) !important;
            width: 100%;
            margin-bottom: 12px;
            padding: 12px;
            font-size: 14px;
        }
        .stButton button:hover {
            background-color: #30363d !important;
            border-color: #8b949e !important;
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #f0f6fc; font-weight: 600;'>VÆRIN Academic</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8b949e; font-size: 13px; margin-bottom: 30px;'>Sign in to access your professional academic workspace</p>", unsafe_allow_html=True)
        
        if st.button("Continue with Google Account"):
            st.session_state.logged_in = True
            st.session_state.selected_provider = "Google Account"
            st.rerun()
            
        if st.button("Continue with Apple ID"):
            st.session_state.logged_in = True
            st.session_state.selected_provider = "Apple ID"
            st.rerun()

        if st.button("Continue with University Email"):
            st.session_state.logged_in = True
            st.session_state.selected_provider = "University ID"
            st.rerun()
            
    st.stop()

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stChatMessage {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    h1, h2, h3 {
        color: #f0f6fc;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

st.title("VAERIN - Advanced Academic System")
st.write("System online. Direct access granted. Memory and security active.")

with st.sidebar:
    st.header("System Controls")
    st.write(f"Connected via: **{st.session_state.get('selected_provider', 'Authorized Session')}**")
    
    st.markdown("---")
    st.subheader("Admin Configuration")
    admin_api_key = st.text_input("Groq API Key:", type="password", value="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")
    
    st.markdown("---")
    st.subheader("Model Settings")
    temperature = st.slider("Temperature (Creativity):", 0.0, 1.0, 0.7, 0.1)
    max_tokens_val = st.slider("Max Tokens:", 256, 2048, 1024, 128)
    
    st.markdown("---")
    if st.button("Clear Memory & Restart"):
        if "messages" in st.session_state:
            del st.session_state.messages
        st.success("Memory cleared successfully.")
        st.rerun()
        
    if st.button("Sign out"):
        st.session_state.logged_in = False
        st.rerun()

if not admin_api_key:
    st.warning("الرجاء التأكد من إدخال مفتاح Groq API في الشريط الجانبي.")
else:
    try:
        client = Groq(api_key=admin_api_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system", 
                    "content": (
                        "You are VAERIN, an advanced academic AI tutor. "
                        "You possess a robust long-term memory connecting all conversation details accurately. "
                        "Strict rule: Never perform quizzes or assessment tests unless explicitly requested by the user. "
                        "Maintain a direct, scholarly tone without emojis or diplomatic filler phrases."
                    )
                }
            ]

        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        if user_query := st.chat_input("Type your academic query here..."):
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            with st.spinner("Analyzing and retrieving context..."):
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model="llama3-70b-8192",
                    temperature=temperature,
                    max_tokens=max_tokens_val,
                )
                
                assistant_answer = chat_completion.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": assistant_answer})
                with st.chat_message("assistant"):
                    st.write(assistant_answer)

    except Exception as e:
        st.error(f"خطأ في الاتصال أو مفتاح API غير صالح. التفاصيل: {e}")
