import streamlit as st
from components.single_detect import render_single_detect
from components.batch_detect import render_batch_detect
from components.csv_detect import render_csv_detect
from components.history_view import render_history
from utils.history import init_history


def render_detection_page(model, tfidf, stemmer, stop_words):
    """Render halaman utama deteksi."""

    init_history()

    # Override background ke light
    st.markdown("""
    <style>
    .stApp { background: #f8f9fc !important; }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 3rem !important;
        max-width: 700px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Header
    st.markdown("""
    <div style="text-align:center; padding: 2.25rem 0 1.75rem; margin-bottom:1.5rem;
                border-bottom: 1px solid #e8eaf0;">
        <span style="
            display:inline-block;
            background:#ede9fe; color:#6d28d9;
            font-size:0.65rem; font-weight:700;
            letter-spacing:0.1em; text-transform:uppercase;
            padding:4px 14px; border-radius:100px;
            margin-bottom:0.7rem;
        ">Naive Bayes · TF-IDF · NLP</span>
        <h1 style="
            font-size:1.65rem; font-weight:700;
            color:#0f172a; letter-spacing:-0.02em;
            margin:0 0 0.35rem; line-height:1.2;
        ">Deteksi Komentar Toxic</h1>
        <p style="font-size:0.83rem; color:#94a3b8; margin:0; font-weight:400;">
            Masukkan komentar untuk mendeteksi apakah mengandung bahasa kasar
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Tombol kembali
    col_l, col_c, col_r = st.columns([1, 1.6, 1])
    with col_c:
        st.markdown("""
        <style>
        .back-wrap .stButton > button {
            background: transparent !important;
            color: #64748b !important;
            border: 1px solid #e2e6f0 !important;
            border-radius: 8px !important;
            font-size: 0.78rem !important;
            font-weight: 500 !important;
            padding: 0.4rem 1rem !important;
            width: 100% !important;
            box-shadow: none !important;
        }
        .back-wrap .stButton > button:hover {
            background: #f1f3f8 !important;
            color: #0f172a !important;
        }
        </style>
        <div class="back-wrap">
        """, unsafe_allow_html=True)
        back = st.button("← Kembali ke Beranda", key="btn_back", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if back:
        st.session_state.page = "hero"
        st.rerun()

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # ── Tabs (4 tab)
    tab1, tab2, tab3, tab4 = st.tabs([
        "  💬  Deteksi Komentar  ",
        "  📋  Deteksi Batch  ",
        "  📂  Upload CSV  ",
        "  🕓  Riwayat  ",
    ])

    with tab1:
        render_single_detect(model, tfidf, stemmer, stop_words)

    with tab2:
        render_batch_detect(model, tfidf, stemmer, stop_words)

    with tab3:
        render_csv_detect(model, tfidf, stemmer, stop_words)

    with tab4:
        render_history()
