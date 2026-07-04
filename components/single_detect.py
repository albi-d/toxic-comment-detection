import streamlit as st
from utils.preprocessing import prediksi
from utils.explain import get_top_words, highlight_toxic_words
from utils.history import add_history
from utils.severity import get_severity


def render_single_detect(model, tfidf, stemmer, stop_words):
    """Tab deteksi komentar tunggal."""

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    komentar = st.text_area(
        "",
        placeholder="Tulis atau tempel komentar di sini...",
        height=110,
        key="input_komentar",
        label_visibility="collapsed"
    )

    detect_btn = st.button("Analisis Komentar", use_container_width=True, key="btn_detect")
    st.markdown("<div style='height:0.25rem'></div>", unsafe_allow_html=True)

    if detect_btn and komentar.strip():
        hasil, proba, bersih = prediksi(komentar, model, tfidf, stemmer, stop_words)
        add_history(komentar, hasil, proba[1], proba[0])
        sv = get_severity(proba[1])
        pct = proba[1] * 100

        # ── Result card
        st.markdown(f"""
        <div style="
            background: {sv['bg']};
            border: 1px solid {sv['border']};
            border-radius: 12px;
            padding: 1.4rem 1.25rem;
            text-align: center;
            margin-bottom: 0.75rem;
        ">
            <div style="font-size:1.9rem;line-height:1;margin-bottom:0.35rem;">{sv['emoji']}</div>
            <div style="
                font-size: 1.1rem; font-weight: 800;
                color: {sv['color']}; letter-spacing: -0.01em;
                margin-bottom: 0.2rem;
            ">{sv['label']}</div>
            <div style="font-size:0.78rem;color:{sv['color']};opacity:0.8;">{sv['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Pills: severity + prob
        st.markdown(f"""
        <div class="prob-row">
            <div class="prob-pill" style="background:{sv['badge_bg']};border-color:{sv['border']};">
                <div style="font-size:0.58rem;font-weight:700;color:{sv['badge_color']};
                            text-transform:uppercase;letter-spacing:0.08em;margin-bottom:3px;">Keparahan</div>
                <div style="font-size:0.82rem;font-weight:800;color:{sv['color']};line-height:1;">{sv['label']}</div>
            </div>
            <div class="prob-pill">
                <div class="prob-value-safe">{proba[0]*100:.1f}%</div>
                <div class="prob-label">Non-Toxic</div>
            </div>
            <div class="prob-pill">
                <div class="prob-value-toxic">{proba[1]*100:.1f}%</div>
                <div class="prob-label">Toxic</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Severity bar
        st.markdown(f"""
        <div style="margin-bottom:0.875rem;">
            <div style="
                display:flex; justify-content:space-between;
                font-size:0.62rem; font-weight:600; color:#94a3b8;
                text-transform:uppercase; letter-spacing:0.07em; margin-bottom:5px;
            ">
                <span>Indikator Keparahan</span>
                <span style="color:{sv['color']};">{pct:.1f}%</span>
            </div>
            <div style="background:#f1f5f9;border-radius:100px;height:6px;overflow:hidden;">
                <div style="
                    width:{pct:.1f}%;height:100%;border-radius:100px;
                    background:linear-gradient(90deg,#22c55e 0%,#f59e0b 45%,#ef4444 75%);
                "></div>
            </div>
            <div style="
                display:flex; justify-content:space-between;
                font-size:0.6rem; color:#cbd5e1; margin-top:3px;
            ">
                <span>Aman</span><span>Perlu Perhatian</span><span>Sangat Toxic</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Highlight kata
        if sv['level'] in ('perhatian', 'toxic') and bersih.strip():
            highlighted = highlight_toxic_words(komentar, bersih, model, tfidf, stemmer, stop_words)
            st.markdown('<span class="section-label">Highlight Kata Bermasalah</span>', unsafe_allow_html=True)
            st.markdown(f'<div class="highlight-box">{highlighted}</div>', unsafe_allow_html=True)

        # ── Top kata
        if bersih.strip():
            top_words = get_top_words(bersih, model, tfidf, label=hasil, top_n=5)
            if top_words:
                max_skor  = top_words[0][1]
                bar_col   = "#ef4444" if hasil == 1 else "#22c55e"
                lbl_text  = "Toxic" if hasil == 1 else "Non-Toxic"

                st.markdown(
                    f'<span class="section-label" style="margin-top:0.5rem;display:block;">'
                    f'Kata Paling Berpengaruh ({lbl_text})</span>'
                    '<div class="topword-container">',
                    unsafe_allow_html=True
                )
                for kata, skor in top_words:
                    pct_bar = (skor / max_skor) * 100
                    st.markdown(f"""
                    <div class="topword-row">
                        <div class="topword-label">{kata}</div>
                        <div class="topword-bar-wrap">
                            <div class="topword-bar" style="width:{pct_bar:.0f}%;background:{bar_col};"></div>
                        </div>
                        <div class="topword-score">{skor:.4f}</div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        # ── Preprocessing detail
        with st.expander("Detail preprocessing"):
            st.markdown('<span class="preproc-label">Teks Asli</span>', unsafe_allow_html=True)
            st.markdown(f'<div class="preproc-box">{komentar}</div>', unsafe_allow_html=True)
            st.markdown('<div style="height:0.5rem"></div><span class="preproc-label">Setelah Preprocessing</span>',
                        unsafe_allow_html=True)
            cleaned = bersih if bersih.strip() else "(kosong setelah preprocessing)"
            st.markdown(f'<div class="preproc-box">{cleaned}</div>', unsafe_allow_html=True)

    elif detect_btn and not komentar.strip():
        st.warning("Komentar tidak boleh kosong.")

    else:
        st.markdown("""
        <div class="empty-state">
            <span class="empty-icon">🔍</span>
            <div class="empty-text">Hasil analisis akan muncul di sini</div>
        </div>
        """, unsafe_allow_html=True)
