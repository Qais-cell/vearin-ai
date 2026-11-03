import streamlit as st

st.set_page_config(
    page_title="VÆRIN Neural Canvas",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
html, body, .stApp {
    background-color: #000000 !important;
    color: #f4f4f5;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
@keyframes floatGlow {
    0%, 100% { text-shadow: 0 0 12px rgba(255, 255, 255, 0.6), 0 0 25px rgba(161, 161, 170, 0.3); }
    50% { text-shadow: 0 0 22px rgba(255, 255, 255, 0.9), 0 0 35px rgba(255, 215, 0, 0.3); }
}
.grok-title {
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
    animation: floatGlow 3s infinite ease-in-out;
}
.grok-sub {
    font-size: 11px;
    color: #
