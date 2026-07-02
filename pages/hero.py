import streamlit as st


def render_hero():
    """Render hero section — minimalist dark landing page."""

    # Inject dark background hanya untuk halaman ini
    st.markdown("""
    <style>
    .stApp { background: #07070f !important; }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 2rem !important;
        max-width: 680px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Spacer atas
    st.markdown("<div style='height:4rem'></div>", unsafe_allow_html=True)

    # ── Badge
    st.markdown("""
    <div style="text-align:center; margin-bottom:1.75rem;">
        <span style="
            display:inline-flex; align-items:center; gap:8px;
            background:rgba(99,102,241,0.1);
            border:1px solid rgba(99,102,241,0.25);
            color:#a5b4fc;
            font-size:0.68rem; font-weight:600;
            letter-spacing:0.12em; text-transform:uppercase;
            padding:6px 18px; border-radius:100px;
        ">
            <span style="width:6px;height:6px;background:#818cf8;border-radius:50%;display:inline-block;flex-shrink:0;"></span>
            Naive Bayes &nbsp;&middot;&nbsp; TF-IDF &nbsp;&middot;&nbsp; NLP
        </span>
    </div>
    """, unsafe_allow_html=True)

    # ── Title
    st.markdown("""
    <div style="text-align:center; margin-bottom:1.25rem;">
        <h1 style="
            font-size:clamp(2.4rem,5vw,3.6rem);
            font-weight:800; line-height:1.1;
            letter-spacing:-0.04em; margin:0;
        ">
            <span style="color:#f1f5f9; display:block;">Deteksi Komentar</span>
            <span style="
                background:linear-gradient(135deg,#6366f1 0%,#a855f7 55%,#ec4899 100%);
                -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                background-clip:text; display:block;
            ">Toxic &amp; Non-Toxic</span>
        </h1>
    </div>
    """, unsafe_allow_html=True)

    # ── Subtitle
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <p style="
            font-size:0.95rem; color:#64748b;
            line-height:1.75; max-width:460px;
            margin:0 auto; font-weight:400;
        ">
            Analisis otomatis komentar Instagram menggunakan
            <span style="color:#94a3b8;font-weight:500;">Naive Bayes</span>
            &amp;
            <span style="color:#94a3b8;font-weight:500;">TF-IDF</span>
            untuk mendeteksi bahasa kasar secara instan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Divider accent
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <div style="width:40px;height:2px;background:linear-gradient(90deg,#6366f1,#a855f7);border-radius:2px;margin:0 auto;"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Feature pills
    st.markdown("""
    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;justify-content:center;margin-bottom:2.5rem;">
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);color:#64748b;font-size:0.75rem;font-weight:500;padding:6px 14px;border-radius:100px;">Naive Bayes Classifier</span>
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);color:#64748b;font-size:0.75rem;font-weight:500;padding:6px 14px;border-radius:100px;">TF-IDF Vectorizer</span>
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);color:#64748b;font-size:0.75rem;font-weight:500;padding:6px 14px;border-radius:100px;">Bahasa Indonesia</span>
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);color:#64748b;font-size:0.75rem;font-weight:500;padding:6px 14px;border-radius:100px;">Bulk CSV Upload</span>
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);color:#64748b;font-size:0.75rem;font-weight:500;padding:6px 14px;border-radius:100px;">Real-time Detection</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats row
    st.markdown("""
    <div style="
        display:flex; justify-content:center;
        border:1px solid rgba(255,255,255,0.07);
        border-radius:14px;
        background:rgba(255,255,255,0.02);
        overflow:hidden;
        max-width:380px;
        margin:0 auto 3rem;
    ">
        <div style="flex:1;padding:1.2rem 0.75rem;text-align:center;border-right:1px solid rgba(255,255,255,0.07);">
            <div style="font-size:1.3rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.03em;">NLP</div>
            <div style="font-size:0.65rem;color:#475569;margin-top:4px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;">Teknologi</div>
        </div>
        <div style="flex:1;padding:1.2rem 0.75rem;text-align:center;border-right:1px solid rgba(255,255,255,0.07);">
            <div style="font-size:1.3rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.03em;">2</div>
            <div style="font-size:0.65rem;color:#475569;margin-top:4px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;">Kelas Label</div>
        </div>
        <div style="flex:1;padding:1.2rem 0.75rem;text-align:center;">
            <div style="font-size:1.3rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.03em;">Instan</div>
            <div style="font-size:0.65rem;color:#475569;margin-top:4px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;">Prediksi</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── CTA Button — native Streamlit agar bisa diklik
    col_l, col_c, col_r = st.columns([1.2, 2, 1.2])
    with col_c:
        # Style khusus tombol hero
        st.markdown("""
        <style>
        div[data-testid="stVerticalBlock"] .stButton > button {
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 12px !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            padding: 0.8rem 1.5rem !important;
            width: 100% !important;
            letter-spacing: 0.01em !important;
        }
        div[data-testid="stVerticalBlock"] .stButton > button:hover {
            opacity: 0.9 !important;
            transform: translateY(-1px) !important;
        }
        </style>
        """, unsafe_allow_html=True)
        clicked = st.button("Mulai Deteksi  →", use_container_width=True, key="btn_start")

    # ── Footer hint
    st.markdown("""
    <div style="text-align:center; margin-top:2.5rem;">
        <p style="font-size:0.72rem;color:#334155;font-weight:500;letter-spacing:0.05em;text-transform:uppercase;">
            Gratis &nbsp;·&nbsp; No Login &nbsp;·&nbsp; Open Source
        </p>
    </div>
    """, unsafe_allow_html=True)

    return clicked
