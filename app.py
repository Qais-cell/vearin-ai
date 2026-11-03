import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="VÆRIN Neural Canvas",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- تصميم أسود وأبيض عائم وفخم (Monochrome Glow & Minimalist) ---
st.markdown("""
    <style>
    /* خلفية داكنة فخمة بدون أزرق أو بنفسجي */
    html, body, .stApp {
        background-color: #000000 !important;
        color: #f4f4f5;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* أنيميشن بريق أبيض وفضي عائم للعنوان */
    @keyframes floatGlow {
        0%, 100% { text-shadow: 0 0 12px rgba(255, 255, 255, 0.6), 0 0 25px rgba(161, 161, 170, 0.3); }
        50% { text-shadow: 0 0 22px rgba(255, 255, 255, 0.9), 0 0 35px rgba(255, 215, 0, 0.3); }
    }
    
    .grok-title {
        font-size: 24px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        letter-spacing: -0.5px;
        animation: floatGlow 3s infinite ease-in-out;
        margin-top: 10px;
    }
    
    .grok-sub {
        font-size: 13px;
        color: #a1a1aa;
        text-align: center;
        margin-bottom: 20px;
    }

    /* كاردات عائمة بتدرجات رمادية وأسود فخم */
    .grok-card {
        background: linear-gradient(145deg, #09090b 0%, #121215 100%);
        border: 1px solid #27272a;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.7);
    }
    
    /* أزرار باللون الأبيض والرمادي الداكن العائم */
    .stButton>button {
        background: linear-gradient(135deg, #ffffff 0%, #d4d4d8 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 10px 14px !important;
        width: 100%;
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.15);
        transition: all 0.2s ease;
    }
    
    .stButton>button:active {
        
