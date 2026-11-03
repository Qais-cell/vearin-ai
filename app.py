import streamlit as st

st.set_page_config(
    page_title="Vaerin",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS محسن يحاكي Grok ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background-color: #f7f7f5;
    }

    /* إخفاء عناصر Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* السايدبار */
    section[data-testid="stSidebar"] {
        background-color: #f0f0ee !important;
        border-right: 1px solid #e5e5e3;
    }

    section[data-testid="stSidebar"] button {
        background: transparent !important;
        border: 1px solid #dcdcd9 !important;
        border-radius: 12px !important;
        color: #1a1a1a !important;
        font-weight: 500 !important;
        padding: 10px 14px !important;
        margin-bottom: 6px !important;
        transition: 0.15s !important;
    }

    section[data-testid="stSidebar"] button:hover {
        background: #e8e8e5 !important;
    }

    /* الرسائل */
    .user-bubble {
        background: #e8e8e5;
        color: #1a1a1a;
        padding: 12px 18px;
        border-radius: 20px;
        margin: 10px 0 10px auto;
        max-width: 70%;
        width: fit-content;
        font-size: 15.5px;
        line-height: 1.5;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }

    .assistant-bubble {
        background: transparent;
        color: #1a1a1a;
        padding: 8px 4px;
        margin: 10px 0;
        max-width: 85%;
        font-size: 15.5px;
        line-height: 1.6;
    }

    .assistant-name {
        font-weight: 600;
        font-size: 14px;
        color: #555;
        margin-bottom: 4px;
    }

    /* الصفحة الرئيسية */
    .hero {
        text-align: center;
        padding-top: 18vh;
    }

    .hero h1 {
        font-size: 2.1rem;
        font-weight: 500;
        color: #1a1a1a;
        margin-bottom: 8px;
        letter-spacing: -0.6px;
    }

    .hero p {
        color: #666;
        font-size: 1rem;
        margin-bottom: 32px;
    }

    /* أزرار الاقتراحات */
    .stButton > button {
        background: white !important;
        border: 1px solid #e0e0de !important;
        border-radius: 16px !important;
        color: #333 !important;
        font-weight: 450 !important;
        padding: 12px 16px !important;
        transition: 0.15s !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }

    .stButton > button:hover {
        background: #f5f5f3 !important;
        border-color: #ccc !important;
        transform: translateY(-1px);
    }

    /* صندوق الإدخال */
    .stChatInput {
        border-radius: 24px !important;
    }

    div[data-testid="stChatInput"] {
        background: transparent !important;
    }

    /* شريط علوي بسيط */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 8px 8px 8px;
        margin-bottom: 10px;
    }

    .logo {
        font-size: 20px;
        font-weight: 600;
        color: #1a1a1a;
        letter-spacing: -0.5px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== حالة الجلسة ====================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==================== السايدبار ====================
with st.sidebar:
    st.markdown("### ✦ Vaerin")
    st.markdown("")
    
    if st.button("＋  New chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.caption("Recent chats")
    
    if st.session_state.chat_history:
        for i, chat in enumerate(reversed(st.session_state.chat_history[-10:])):
            short = chat[:38] + "..." if len(chat) > 38 else chat
            st.button(short, key=f"h_{i}", use_container_width=True)
    else:
        st.caption("No chats yet")

# ==================== المحتوى الرئيسي ====================
if not st.session_state.messages:
    # ========== الصفحة الرئيسية (مثل Grok) ==========
    st.markdown("""
    <div class="hero">
        <h1>What should we explore?</h1>
        <p>Vaerin is ready to help</p>
    </div>
    """, unsafe_allow_html=True)

    # اقتراحات
    suggestions = [
        "Explain something complex simply",
        "Write a creative short story",
        "Help me plan my next trip",
        "What is the meaning of life?"
    ]

    cols = st.columns(2)
    for i, s in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(s, key=f"s_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": s})
                st.rerun()

else:
    # ========== عرض المحادثة ==========
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'''
                <div class="assistant-bubble">
                    <div class="assistant-name">Vaerin</div>
                    {msg["content"]}
                </div>
            ''', unsafe_allow_html=True)

# ==================== الإدخال ====================
prompt = st.chat_input("What do you want to know?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    if prompt not in st.session_state.chat_history:
        st.session_state.chat_history.append(prompt)

    # ========== هنا تربط نموذجك الحقيقي ==========
    with st.spinner(""):
        # استبدل هذا الجزء بكود نموذجك
        response = f"""This is still a placeholder from **Vaerin**.

You said: "{prompt}"

Replace this section with your actual model code."""
        
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()
