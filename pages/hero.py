import streamlit as st


def render_hero():
    """Hero section — dark minimalist landing page."""

    st.markdown("""
    <style>
    .stApp { background: #080810 !important; }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        max-width: 600px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }
    /* Hero button override */
    div[data-testid="stVerticalBlock"] .stButton > button {
        background: #6366f1 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 9px !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.5rem !important;
        width: 100% !important;
        letter-spacing: 0.01em !important;
        transition: background 0.15s, transform 0.1s !important;
    }
    div[data-testid="stVerticalBlock"] .stButton > button:hover {
        background: #4f46e5 !important;
        transform: translateY(-1px) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:3.5rem'></div>", unsafe_allow_html=True)

    # Badge
    st.markdown("""
    <div style="text-align:center; margin-bottom:1.75rem;">
        <span style="
            display: inline-flex; align-items: center; gap: 7px;
            background: rgba(99,102,241,0.1);
            border: 1px solid rgba(99,102,241,0.2);
            color: #a5b4fc;
            font-size: 0.67rem; font-weight: 600;
            letter-spacing: 0.12em; text-transform: uppercase;
            padding: 5px 16px; border-radius: 100px;
        ">
            <span style="width:5px;height:5px;background:#818cf8;border-radius:50%;display:inline-block;"></span>
            Naive Bayes &nbsp;·&nbsp; TF-IDF &nbsp;·&nbsp; NLP
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("""
    <div style="text-align:center; margin-bottom:1.1rem;">
        <h1 style="
            font-size: clamp(2.2rem, 7vw, 3.25rem);
            font-weight: 800;
            line-height: 1.1;
            letter-spacing: -0.04em;
            margin: 0;
            color: #f1f5f9;
        ">Deteksi Komentar<br><span style="
            background: linear-gradient(135deg, #6366f1 0%, #a78bfa 50%, #e879f9 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        ">Toxic &amp; Non-Toxic</span></h1>
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <p style="
            font-size: 0.93rem;
            color: #64748b;
            line-height: 1.75;
            margin: 0 auto;
            font-weight: 400;
            max-width: 400px;
        ">
            Analisis komentar Instagram secara otomatis menggunakan
            <span style="color:#94a3b8;font-weight:500;">machine learning</span>
            untuk mendeteksi bahasa kasar.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Divider
    st.markdown("""
    <div style="display:flex;justify-content:center;margin-bottom:2rem;">
        <div style="width:32px;height:2px;background:linear-gradient(90deg,#6366f1,#a78bfa);border-radius:2px;"></div>
    </div>
    """, unsafe_allow_html=True)

    # Feature pills
    st.markdown("""
    <div style="display:flex;flex-wrap:wrap;gap:0.45rem;justify-content:center;margin-bottom:2.25rem;">
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);color:#475569;font-size:0.73rem;font-weight:500;padding:5px 13px;border-radius:100px;">Naive Bayes</span>
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);color:#475569;font-size:0.73rem;font-weight:500;padding:5px 13px;border-radius:100px;">TF-IDF</span>
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);color:#475569;font-size:0.73rem;font-weight:500;padding:5px 13px;border-radius:100px;">Bahasa Indonesia</span>
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);color:#475569;font-size:0.73rem;font-weight:500;padding:5px 13px;border-radius:100px;">Bulk CSV</span>
        <span style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);color:#475569;font-size:0.73rem;font-weight:500;padding:5px 13px;border-radius:100px;">Real-time</span>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div style="
        display: flex;
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 12px;
        background: rgba(255,255,255,0.02);
        overflow: hidden;
        margin: 0 auto 2.75rem;
        max-width: 360px;
    ">
        <div style="flex:1;padding:1.1rem 0.5rem;text-align:center;border-right:1px solid rgba(255,255,255,0.06);">
            <div style="font-size:1.2rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.03em;line-height:1;">NLP</div>
            <div style="font-size:0.62rem;color:#334155;margin-top:5px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;">Teknologi</div>
        </div>
        <div style="flex:1;padding:1.1rem 0.5rem;text-align:center;border-right:1px solid rgba(255,255,255,0.06);">
            <div style="font-size:1.2rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.03em;line-height:1;">3</div>
            <div style="font-size:0.62rem;color:#334155;margin-top:5px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;">Level</div>
        </div>
        <div style="flex:1;padding:1.1rem 0.5rem;text-align:center;">
            <div style="font-size:1.2rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.03em;line-height:1;">Instan</div>
            <div style="font-size:0.62rem;color:#334155;margin-top:5px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;">Prediksi</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CTA button
    col_l, col_c, col_r = st.columns([1, 2.2, 1])
    with col_c:
        clicked = st.button("Mulai Analisis →", use_container_width=True, key="btn_start")

    # Footer
    st.markdown("""
    <div style="text-align:center; margin-top:2rem; padding-bottom:3rem;">
        <p style="font-size:0.68rem;color:#1e293b;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;margin:0;">
            Gratis &nbsp;·&nbsp; No Login &nbsp;·&nbsp; Open Source
        </p>
    </div>
    """, unsafe_allow_html=True)

    return clicked
