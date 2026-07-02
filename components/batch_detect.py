import streamlit as st
import pandas as pd
from utils.preprocessing import prediksi
from utils.history import add_history
from utils.severity import severity_label


def render_batch_detect(model, tfidf, stemmer, stop_words):
    """Tab deteksi batch — paste beberapa komentar sekaligus (dipisah newline)."""

    st.markdown("<div style='height:0.25rem'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-label">Deteksi Banyak Komentar Sekaligus</div>
    """, unsafe_allow_html=True)
    st.caption("Tulis satu komentar per baris. Maksimal 100 baris sekaligus.")

    teks_batch = st.text_area(
        "",
        placeholder="kamu bodoh\nbagus sekali karyamu\ndasar goblok kamu\nsemangat terus ya!",
        height=180,
        key="input_batch",
        label_visibility="collapsed"
    )

    batch_btn = st.button("Deteksi Semua", use_container_width=True, key="btn_batch")

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    if not batch_btn:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">📋</div>
            <div class="empty-text">Hasil akan muncul di sini setelah kamu klik Deteksi Semua</div>
        </div>
        """, unsafe_allow_html=True)
        return

    if not teks_batch.strip():
        st.warning("Input tidak boleh kosong.")
        return

    # Pisah per baris, buang baris kosong
    baris_list = [b.strip() for b in teks_batch.splitlines() if b.strip()]

    if len(baris_list) > 100:
        st.warning("Maksimal 100 komentar sekaligus. Hanya 100 baris pertama yang diproses.")
        baris_list = baris_list[:100]

    with st.spinner(f"Mendeteksi {len(baris_list)} komentar..."):
        rows = []
        for i, baris in enumerate(baris_list, 1):
            h, p, _ = prediksi(baris, model, tfidf, stemmer, stop_words)
            label = 'Toxic' if h == 1 else 'Non-Toxic'
            rows.append({
                'No'        : i,
                'Komentar'  : baris,
                'Prediksi'  : label,
                'Keparahan' : severity_label(p[1]),
                '% Toxic'   : round(p[1] * 100, 1),
                '% Non-Toxic': round(p[0] * 100, 1),
            })
            add_history(baris, h, p[1], p[0])

    df = pd.DataFrame(rows)

    # ── Ringkasan
    total   = len(df)
    n_toxic = (df['Prediksi'] == 'Toxic').sum()
    n_aman  = (df['Prediksi'] == 'Non-Toxic').sum()

    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-card">
            <div class="stat-value">{total}</div>
            <div class="stat-label">Total</div>
        </div>
        <div class="stat-card">
            <div class="stat-value-toxic">{n_toxic}</div>
            <div class="stat-label">Toxic</div>
        </div>
        <div class="stat-card">
            <div class="stat-value-safe">{n_aman}</div>
            <div class="stat-label">Non-Toxic</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── Tabel hasil dengan warna per baris
    st.markdown('<div class="section-label">Hasil per Komentar</div>', unsafe_allow_html=True)

    def style_prediksi(val):
        if val == 'Toxic':
            return 'color: #dc2626; font-weight: 600;'
        return 'color: #16a34a; font-weight: 600;'

    def style_keparahan(val):
        if val == 'SANGAT TOXIC':
            return 'color:#dc2626;font-weight:600;'
        elif val == 'PERLU PERHATIAN':
            return 'color:#d97706;font-weight:600;'
        return 'color:#16a34a;font-weight:600;'

    styled = df.style.map(style_prediksi, subset=['Prediksi']) \
                     .map(style_keparahan, subset=['Keparahan'])
    st.dataframe(styled, use_container_width=True, hide_index=True)

    # ── Download
    st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
    csv_out = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇  Download Hasil CSV",
        data=csv_out,
        file_name="hasil_batch_deteksi.csv",
        mime="text/csv",
        use_container_width=True
    )
