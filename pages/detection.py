import streamlit as st
from components.single_detect import render_single_detect
from components.batch_detect import render_batch_detect
from components.csv_detect import render_csv_detect
from components.history_view import render_history
from utils.history import init_history


def render_detection_page(model, tfidf, stemmer, stop_words):
    """Render halaman utama deteksi."""

    init_history()

    st.markdown("""
    <style>
    .stApp { background: #f8f9fc !important; }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 3rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 680px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* ── Tombol kembali — subtle, proporsional ── */
    .back-wrap {
        display: flex;
        justify-content: center;
        margin-bottom: 1.25rem;
    }
    .back-wrap .stButton > button {
        background: #ffffff !important;
        color: #64748b !important;
        border: 1px solid #e2e6f0 !important;
        border-radius: 8px !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        padding: 0.45rem 1.25rem !important;
        width: auto !important;
        min-width: 160px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    }
    .back-wrap .stButton > button:hover {
        background: #f8f9fc !important;
        color: #0f172a !important;
        border-color: #cbd5e1 !important;
    }

    /* ── Konsistenkan semua tombol aksi (detect/batch/csv) ── */
    .stButton > button[kind="secondary"],
    div[data-testid="stVerticalBlock"] .stButton > button {
        background: #0f172a !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        padding: 0.65rem 1.5rem !important;
        width: 100% !important;
        letter-spacing: 0.01em !important;
        box-shadow: none !important;
    }
    div[data-testid="stVerticalBlock"] .stButton > button:hover {
        background: #1e293b !important;
    }

    /* ── Tabs mobile friendly ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0 !important;
        background: #f1f3f8 !important;
        border-radius: 10px !important;
        padding: 4px !important;
        margin-bottom: 1.25rem !important;
        border: none !important;
        overflow-x: auto !important;
        flex-wrap: nowrap !important;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 7px !important;
        font-size: 0.78rem !important;
        font-weight: 500 !important;
        color: #64748b !important;
        padding: 0.4rem 0.8rem !important;
        border: none !important;
        white-space: nowrap !important;
        flex-shrink: 0 !important;
    }
    .stTabs [aria-selected="true"] {
        background: #ffffff !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08) !important;
    }

    /* ── Textarea ── */
    .stTextArea textarea {
        border: 1.5px solid #e2e6f0 !important;
        border-radius: 12px !important;
        font-size: 0.88rem !important;
        color: #0f172a !important;
        background: #ffffff !important;
        padding: 0.85rem 1rem !important;
        resize: none !important;
    }
    .stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99,102,241,0.1) !important;
    }

    /* ── Mobile responsive ── */
    @media (max-width: 640px) {
        .block-container {
            padding-left: 0.75rem !important;
            padding-right: 0.75rem !important;
        }
        .prob-row { flex-direction: row !important; }
        .stat-row { flex-direction: row !important; }
        .stTabs [data-baseweb="tab"] {
            font-size: 0.72rem !important;
            padding: 0.35rem 0.6rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Header — selalu center
    st.markdown("""
    <style>
    /* Paksa semua elemen dalam header block tetap center */
    [data-testid="stMarkdownContainer"] {
        text-align: center !important;
    }
    </style>
    <div style="
        text-align: center;
        width: 100%;
        padding: 2rem 0 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid #e8eaf0;
        box-sizing: border-box;
    ">
        <div style="
            display: inline-block;
            background: #ede9fe;
            color: #6d28d9;
            font-size: 0.65rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            padding: 4px 14px;
            border-radius: 100px;
            margin-bottom: 0.75rem;
        ">Naive Bayes · TF-IDF · NLP</div>
        <h1 style="
            font-size: clamp(1.4rem, 5vw, 1.7rem);
            font-weight: 700;
            color: #0f172a;
            letter-spacing: -0.02em;
            margin: 0 0 0.4rem;
            line-height: 1.2;
            width: 100%;
            display: block;
            text-align: center;
        ">Deteksi Komentar Toxic</h1>
        <p style="
            font-size: 0.83rem;
            color: #94a3b8;
            margin: 0;
            font-weight: 400;
            text-align: center;
            width: 100%;
            display: block;
        ">Masukkan komentar untuk mendeteksi apakah mengandung bahasa kasar</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Tombol kembali — center, icon SVG via CSS
    st.markdown("""
    <style>
    /* Ganti teks tombol kembali dengan versi bericon */
    .back-wrap .stButton > button::before {
        content: "";
        display: inline-block;
        width: 16px;
        height: 16px;
        margin-right: 6px;
        vertical-align: middle;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M19 12H5'/%3E%3Cpath d='M12 19l-7-7 7-7'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: contain;
        position: relative;
        top: -1px;
    }
    .back-wrap .stButton > button:hover::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230f172a' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M19 12H5'/%3E%3Cpath d='M12 19l-7-7 7-7'/%3E%3C/svg%3E");
    }
    </style>
    <div class="back-wrap">
    """, unsafe_allow_html=True)
    back = st.button("Beranda", key="btn_back")
    st.markdown('</div>', unsafe_allow_html=True)

    if back:
        st.session_state.page = "hero"
        st.rerun()

    # ── Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        " 💬 Deteksi ",
        " 📋 Batch ",
        " 📂 CSV ",
        " 🕓 Riwayat ",
    ])

    with tab1:
        render_single_detect(model, tfidf, stemmer, stop_words)

    with tab2:
        render_batch_detect(model, tfidf, stemmer, stop_words)

    with tab3:
        render_csv_detect(model, tfidf, stemmer, stop_words)

    with tab4:
        render_history()
