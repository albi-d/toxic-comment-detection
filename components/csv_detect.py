import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.preprocessing import prediksi
from utils.severity import severity_label


def render_csv_detect(model, tfidf, stemmer, stop_words):
    """Tab deteksi komentar dari file CSV dengan filter & sort."""

    st.markdown("<div style='height:0.25rem'></div>", unsafe_allow_html=True)

    st.markdown('<div class="section-label">Upload File CSV</div>', unsafe_allow_html=True)
    st.caption("Pastikan file CSV memiliki kolom bernama **komentar**, **text**, atau **teks**")

    uploaded = st.file_uploader(
        "Pilih file CSV",
        type=['csv'],
        label_visibility="collapsed",
        key="csv_uploader"
    )

    # Reset hasil jika file di-clear
    if uploaded is None:
        st.session_state.pop('csv_result', None)
        st.session_state.pop('csv_col', None)
        return

    try:
        df_upload = pd.read_csv(uploaded)
        st.success(f"File berhasil diupload — **{len(df_upload)} baris** ditemukan")
        st.dataframe(df_upload.head(3), use_container_width=True)

        # Deteksi kolom komentar
        col_komentar = None
        for col in df_upload.columns:
            if col.lower() in ['komentar', 'comment', 'text', 'teks', 'instagram comment text']:
                col_komentar = col
                break
        if col_komentar is None:
            col_komentar = df_upload.columns[0]

        st.caption(f"Kolom yang digunakan: **{col_komentar}**")

        detect_all = st.button("Deteksi Semua Komentar", use_container_width=True, key="btn_csv")

        # Jalankan deteksi dan simpan ke session_state
        if detect_all:
            with st.spinner("Mendeteksi semua komentar..."):
                hasil_list, proba_toxic, proba_non, severity_list = [], [], [], []
                for teks in df_upload[col_komentar]:
                    h, p, _ = prediksi(str(teks), model, tfidf, stemmer, stop_words)
                    hasil_list.append('Toxic' if h == 1 else 'Non-Toxic')
                    proba_toxic.append(round(p[1] * 100, 2))
                    proba_non.append(round(p[0] * 100, 2))
                    severity_list.append(severity_label(p[1]))

            df_upload['Prediksi']    = hasil_list
            df_upload['Keparahan']   = severity_list
            df_upload['% Toxic']     = proba_toxic
            df_upload['% Non-Toxic'] = proba_non
            st.session_state['csv_result'] = df_upload.copy()
            st.session_state['csv_col']    = col_komentar

        # Tampilkan hasil dari session_state (persisten walau dropdown berubah)
        if 'csv_result' not in st.session_state:
            return

        df_res       = st.session_state['csv_result']
        col_komentar = st.session_state['csv_col']

        total_csv    = len(df_res)
        toxic_csv    = (df_res['Prediksi'] == 'Toxic').sum()
        nontoxic_csv = (df_res['Prediksi'] == 'Non-Toxic').sum()

        # ── Statistik
        st.markdown(f"""
        <div class="stat-row">
            <div class="stat-card">
                <div class="stat-value">{total_csv}</div>
                <div class="stat-label">Total</div>
            </div>
            <div class="stat-card">
                <div class="stat-value-toxic">{toxic_csv}</div>
                <div class="stat-label">Toxic</div>
            </div>
            <div class="stat-card">
                <div class="stat-value-safe">{nontoxic_csv}</div>
                <div class="stat-label">Non-Toxic</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Pie chart
        fig, ax = plt.subplots(figsize=(3.5, 2.8))
        fig.patch.set_facecolor('#ffffff')
        ax.set_facecolor('#ffffff')
        _, _, autotexts = ax.pie(
            [toxic_csv, nontoxic_csv],
            labels=['Toxic', 'Non-Toxic'],
            colors=['#ef4444', '#22c55e'],
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'linewidth': 2.5, 'edgecolor': 'white'},
            textprops={'fontsize': 9, 'color': '#475569'}
        )
        for a in autotexts:
            a.set_fontweight('700')
            a.set_color('#ffffff')
            a.set_fontsize(9)
        ax.set_title('Distribusi Hasil', fontsize=10, fontweight='600', color='#0f172a', pad=10)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        # ── Filter & Sort (fitur 6) — semua dalam satu baris rapi
        st.markdown('<div class="section-label">Filter &amp; Urutkan Hasil</div>', unsafe_allow_html=True)

        col_f, col_s, col_n = st.columns(3)

        with col_f:
            filter_opt = st.selectbox(
                "Tampilkan",
                ["Semua", "Toxic saja", "Non-Toxic saja",
                 "Sangat Toxic", "Perlu Perhatian", "Aman"],
                key="csv_filter"
            )
        with col_s:
            sort_opt = st.selectbox(
                "Urutkan berdasarkan",
                ["Default", "% Toxic ↓", "% Toxic ↑", "% Non-Toxic ↓"],
                key="csv_sort"
            )
        with col_n:
            show_n = st.selectbox(
                "Maks baris",
                [50, 100, 200, "Semua"],
                key="csv_show_n"
            )

        # Terapkan filter
        df_hasil = df_res[[col_komentar, 'Prediksi', 'Keparahan', '% Toxic', '% Non-Toxic']].copy()

        if filter_opt == "Toxic saja":
            df_hasil = df_hasil[df_hasil['Prediksi'] == 'Toxic']
        elif filter_opt == "Non-Toxic saja":
            df_hasil = df_hasil[df_hasil['Prediksi'] == 'Non-Toxic']
        elif filter_opt == "Sangat Toxic":
            df_hasil = df_hasil[df_hasil['Keparahan'] == 'SANGAT TOXIC']
        elif filter_opt == "Perlu Perhatian":
            df_hasil = df_hasil[df_hasil['Keparahan'] == 'PERLU PERHATIAN']
        elif filter_opt == "Aman":
            df_hasil = df_hasil[df_hasil['Keparahan'] == 'AMAN']

        # Terapkan sort
        if sort_opt == "% Toxic ↓":
            df_hasil = df_hasil.sort_values('% Toxic', ascending=False)
        elif sort_opt == "% Toxic ↑":
            df_hasil = df_hasil.sort_values('% Toxic', ascending=True)
        elif sort_opt == "% Non-Toxic ↓":
            df_hasil = df_hasil.sort_values('% Non-Toxic', ascending=False)

        # Terapkan limit
        df_tampil = df_hasil if show_n == "Semua" else df_hasil.head(int(show_n))

        st.caption(f"Menampilkan **{len(df_tampil)}** dari **{len(df_hasil)}** hasil")

        def style_prediksi(val):
            return 'color:#dc2626;font-weight:600;' if val == 'Toxic' else 'color:#16a34a;font-weight:600;'

        def style_keparahan(val):
            if val == 'SANGAT TOXIC':
                return 'color:#dc2626;font-weight:600;'
            elif val == 'PERLU PERHATIAN':
                return 'color:#d97706;font-weight:600;'
            return 'color:#16a34a;font-weight:600;'

        styled = df_tampil.style.map(style_prediksi, subset=['Prediksi']) \
                                .map(style_keparahan, subset=['Keparahan'])
        st.dataframe(styled, use_container_width=True, hide_index=True)

        # ── Download
        st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
        csv_out = df_res.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇  Download Semua Hasil CSV",
            data=csv_out,
            file_name="hasil_deteksi_toxic.csv",
            mime="text/csv",
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Error membaca file: {e}")
