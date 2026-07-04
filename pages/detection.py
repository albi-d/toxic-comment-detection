import streamlit as st
from components.single_detect import render_single_detect
from components.batch_detect import render_batch_detect
from components.csv_detect import render_csv_detect
from components.history_view import render_history
from utils.history import init_history


def render_detection_page(model, tfidf, stemmer, stop_words):
    """Halaman utama deteksi — light minimalist."""

    init_history()

    st.markdown("""
    <style>
    .stApp { background: #f8fafc !important; }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 3rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 660px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* Override button untuk halaman ini — dark */
    div[data-testid="stVerticalBlock"] .stButton > button {
        background: #0f172a !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 9px !important;
        font-size: 0.86rem !important;
        font-weight: 600 !important;
        padding: 0.65rem 1.5rem !important;
        width: 100% !important;
        box-shadow: none !important;
    }

    div[data-testid="stVerticalBlock"] .stButton > button:hover {
        background: #1e293b !important;
    }

    /* Tabs override */
    .stTabs [data-baseweb="tab-list"] {
        background: #f1f5f9 !important;
        border: none !important;
    }

    @media (max-width: 640px) {
        .block-container {
            padding-left: 0.75rem !important;
            padding-right: 0.75rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Header
    st.markdown("""
    <div style="
        padding: 1.75rem 0 1.4rem;
        margin-bottom: 0.875rem;
        border-bottom: 1px solid #e2e8f0;
        text-align: center;
        width: 100%;
    ">
        <span style="
            display: inline-block;
            background: #ede9fe;
            color: #6d28d9;
            font-size: 0.62rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            padding: 3px 12px;
            border-radius: 100px;
            margin-bottom: 0.65rem;
        ">Naive Bayes · TF-IDF · NLP</span>
        <div style="
            font-size: clamp(1.3rem, 4vw, 1.6rem);
            font-weight: 700;
            color: #0f172a;
            letter-spacing: -0.025em;
            margin-bottom: 0.35rem;
            line-height: 1.2;
        ">Deteksi Komentar Toxic</div>
        <div style="
            font-size: 0.82rem;
            color: #94a3b8;
            font-weight: 400;
            line-height: 1.5;
        ">Analisis teks untuk mendeteksi bahasa kasar secara instan</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Tombol kembali
    st.markdown("""
    <style>
    .back-wrap .stButton > button::before {
        content: "";
        display: inline-block;
        width: 14px; height: 14px;
        margin-right: 6px;
        vertical-align: middle;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M19 12H5'/%3E%3Cpath d='M12 19l-7-7 7-7'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: contain;
        position: relative; top: -1px;
    }
    .back-wrap .stButton > button:hover::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230f172a' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M19 12H5'/%3E%3Cpath d='M12 19l-7-7 7-7'/%3E%3C/svg%3E");
    }
    </style>
    <div class="back-wrap">
    """, unsafe_allow_html=True)
    back = st.button("Beranda", key="btn_back")
    st.markdown("</div>", unsafe_allow_html=True)

    if back:
        st.session_state.page = "hero"
        st.rerun()

    # ── Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        " 💬  Deteksi ",
        " 📋  Batch ",
        " 📂  CSV ",
        " 🕓  Riwayat ",
    ])

    with tab1:
        render_single_detect(model, tfidf, stemmer, stop_words)
    with tab2:
        render_batch_detect(model, tfidf, stemmer, stop_words)
    with tab3:
        render_csv_detect(model, tfidf, stemmer, stop_words)
    with tab4:
        render_history()
