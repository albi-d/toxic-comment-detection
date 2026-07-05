import streamlit as st
from components.styles import HERO_CSS
from utils.model import load_model
from pages.hero import render_hero
from pages.detection import render_detection_page

st.set_page_config(
    page_title="ToxicGuard — Deteksi Komentar Toxic",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(HERO_CSS, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "hero"

model, tfidf, stemmer, stop_words = load_model()

if st.session_state.page == "hero":
    start_clicked = render_hero()
    if start_clicked:
        st.session_state.page = "detection"
        st.rerun()

elif st.session_state.page == "detection":
    render_detection_page(model, tfidf, stemmer, stop_words)
