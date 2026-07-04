import streamlit as st
import pandas as pd
from utils.preprocessing import prediksi
from utils.history import add_history
from utils.severity import severity_label


def render_batch_detect(model, tfidf, stemmer, stop_words):
    """Tab deteksi batch — beberapa komentar sekaligus."""

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    st.markdown('<span class="section-label">Deteksi Banyak Komentar Sekaligus</span>', unsafe_allow_html=True)
    st.caption("Satu komentar per baris · Maks 100 baris")

    teks_batch = st.text_area(
        "",
        placeholder="kamu bodoh\nbagus sekali karyamu\ndasar goblok\nsemangat terus ya!",
        height=160,
        key="input_batch",
        label_visibility="collapsed"
    )

    batch_btn = st.button("Analisis Semua", use_container_width=True, key="btn_batch")
    st.markdown("<div style='height:0.25rem'></div>", unsafe_allow_html=True)

    if not batch_btn:
        st.markdown("""
        <div class="empty-state">
            <span class="empty-icon">📋</span>
            <div class="empty-text">Hasil akan muncul setelah klik Analisis Semua</div>
        </div>
        """, unsafe_allow_html=True)
        return

    if not teks_batch.strip():
        st.warning("Input tidak boleh kosong.")
        return

    baris_list = [b.strip() for b in teks_batch.splitlines() if b.strip()]
    if len(baris_list) > 100:
        st.warning("Hanya 100 baris pertama yang diproses.")
        baris_list = baris_list[:100]

    with st.spinner(f"Menganalisis {len(baris_list)} komentar..."):
        rows = []
        for i, baris in enumerate(baris_list, 1):
            h, p, _ = prediksi(baris, model, tfidf, stemmer, stop_words)
            rows.append({
                'No'         : i,
                'Komentar'   : baris,
                'Prediksi'   : 'Toxic' if h == 1 else 'Non-Toxic',
                'Keparahan'  : severity_label(p[1]),
                '% Toxic'    : round(p[1] * 100, 1),
                '% Non-Toxic': round(p[0] * 100, 1),
            })
            add_history(baris, h, p[1], p[0])

    df = pd.DataFrame(rows)
    total   = len(df)
    n_toxic = (df['Prediksi'] == 'Toxic').sum()
    n_aman  = total - n_toxic

    # Stat
    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-card"><div class="stat-value">{total}</div><div class="stat-label">Total</div></div>
        <div class="stat-card"><div class="stat-value-toxic">{n_toxic}</div><div class="stat-label">Toxic</div></div>
        <div class="stat-card"><div class="stat-value-safe">{n_aman}</div><div class="stat-label">Non-Toxic</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<span class="section-label">Hasil per Komentar</span>', unsafe_allow_html=True)

    def _s_pred(v):
        return 'color:#dc2626;font-weight:600;' if v == 'Toxic' else 'color:#16a34a;font-weight:600;'

    def _s_kep(v):
        if v == 'SANGAT TOXIC':  return 'color:#dc2626;font-weight:600;'
        if v == 'PERLU PERHATIAN': return 'color:#d97706;font-weight:600;'
        return 'color:#16a34a;font-weight:600;'

    styled = df.style.map(_s_pred, subset=['Prediksi']).map(_s_kep, subset=['Keparahan'])
    st.dataframe(styled, use_container_width=True, hide_index=True)

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    csv_out = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇  Download CSV", data=csv_out,
                       file_name="hasil_batch.csv", mime="text/csv",
                       use_container_width=True)
