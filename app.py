import streamlit as st
from datetime import datetime

# ==================== إعداد الصفحة ====================
st.set_page_config(
    page_title="Vaerin",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CSS يحاكي واجهة Grok ====================
st.markdown("""
<style>
    /* خلفية عامة */
    .stApp {
        background-color: #f8f8f7;
    }
    
    /* إخفاء عناصر Streamlit الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* السايدبار */
    section[data-testid="stSidebar"] {
        background-color: #f0f0ee;
        border-right: 1px solid #e0e0de;
    }
    
    section[data-testid="stSidebar"] .stButton > button {
        background-color: transparent;
        border: 1px solid #d0d0ce;
        border-radius: 12px;
        color: #1a1a1a;
        font-weight: 500;
        width: 100%;
        text-align: left;
        padding: 10px 16px;
        margin-bottom: 6px;
        transition: all 0.2s;
    }
    
    section[data-testid="stSidebar"] .stButton > button:hover {
        background-color: #e8e8e6;
        border-color: #c0c0be;
    }
    
    /* الرسائل */
    .user-message {
        background-color: #e8e8e6;
        border-radius: 18px;
        padding: 14px 18px;
        margin: 12px 0;
        max-width: 75%;
        margin-left: auto;
        color: #1a1a1a;
        font-size: 15.5px;
        line-height: 1.5;
    }
    
    .assistant-message {
        background-color: transparent;
        border-radius: 18px;
        padding: 14px 4px;
        margin: 12px 0;
        max-width: 85%;
        color: #1a1a1a;
        font-size: 15.5px;
        line-height: 1.55;
    }
    
    /* العنوان الكبير في الصفحة الرئيسية */
    .hero-title {
        font-size: 32px;
        font-weight: 500;
        text-align: center;
        color: #1a1a1a;
        margin-bottom: 28px;
        letter-spacing: -0.5px;
    }
    
    .model-badge {
        display: inline-block;
        background: #1a1a1a;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 500;
        margin-bottom: 8px;
    }
    
    /* منطقة الإدخال */
    .stChatInput {
        border-radius: 24px !important;
    }
    
    /* اقتراحات */
    .suggestion-chip {
        display: inline-block;
        background: white;
        border: 1px solid #e0e0de;
        border-radius: 20px;
        padding: 8px 16px;
        margin: 6px;
        font-size: 14px;
        color: #333;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .suggestion-chip:hover {
        background: #f0f0ee;
        border-color: #c0c0be;
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
    st.markdown("---")
    
    if st.button("＋  New chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("")
    st.caption("Recent")
    
    # محاكاة سجل المحادثات
    if st.session_state.chat_history:
        for i, chat in enumerate(st.session_state.chat_history[-8:]):
            if st.button(chat[:40] + "..." if len(chat) > 40 else chat, key=f"hist_{i}", use_container_width=True):
                pass
    else:
        st.caption("No previous chats")
    
    st.markdown("---")
    st.caption("Vaerin • Local Model")

# ==================== الصفحة الرئيسية / الشات ====================
if not st.session_state.messages:
    # ========== Intro Screen (مثل صفحة Grok) ==========
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2.2, 1])
    with col2:
        st.markdown('<div class="hero-title">What should we explore?</div>', unsafe_allow_html=True)
        
        # اقتراحات سريعة
        suggestions = [
            "Explain quantum computing simply",
            "Write a short story about a robot",
            "Help me plan a trip to Tokyo",
            "What is the meaning of life?"
        ]
        
        cols = st.columns(2)
        for i, suggestion in enumerate(suggestions):
            with cols[i % 2]:
                if st.button(suggestion, key=f"sug_{i}", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": suggestion})
                    st.rerun()

else:
    # ========== عرض الرسائل ==========
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message"><b>Vaerin</b><br>{msg["content"]}</div>', unsafe_allow_html=True)

# ==================== صندوق الإدخال ====================
prompt = st.chat_input("What do you want to know?")

if prompt:
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # حفظ في التاريخ
    if prompt not in st.session_state.chat_history:
        st.session_state.chat_history.append(prompt)
    
    # هنا تربط نموذجك الحقيقي (Vaerin)
    # حالياً رد وهمي فقط
    with st.spinner("Vaerin is thinking..."):
        # ==================== مكان ربط النموذج الحقيقي ====================
        # استبدل الجزء التالي بكود استدعاء نموذجك
        # مثال:
        # response = your_vaerin_model.generate(prompt)
        
        fake_response = f"""This is a placeholder response from **Vaerin**.

You said: *"{prompt}"*

Replace this section in the code with your actual model inference logic."""
        
        st.session_state.messages.append({"role": "assistant", "content": fake_response})
    
    st.rerun()
