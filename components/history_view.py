import streamlit as st
import pandas as pd
from utils.history import get_history, clear_history


def render_history():
    """Tab riwayat deteksi sesi ini."""

    st.markdown("<div style='height:0.25rem'></div>", unsafe_allow_html=True)

    history = get_history()

    if not history:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">🕓</div>
            <div class="empty-text">Belum ada riwayat deteksi.<br>Mulai deteksi komentar untuk melihat riwayat di sini.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    df = pd.DataFrame(history)
    total   = len(df)
    n_toxic = (df['prediksi'] == 'Toxic').sum()
    n_aman  = (df['prediksi'] == 'Non-Toxic').sum()

    # ── Ringkasan sesi
    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-card">
            <div class="stat-value">{total}</div>
            <div class="stat-label">Dianalisis</div>
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
    st.markdown('<div class="section-label">Riwayat Deteksi Sesi Ini</div>', unsafe_allow_html=True)

    # Rename kolom untuk tampilan
    df_tampil = df.rename(columns={
        'waktu': 'Waktu',
        'komentar': 'Komentar',
        'prediksi': 'Prediksi',
        '% toxic': '% Toxic',
        '% non-toxic': '% Non-Toxic',
    })

    def style_prediksi(val):
        if val == 'Toxic':
            return 'color: #dc2626; font-weight: 600;'
        return 'color: #16a34a; font-weight: 600;'

    styled = df_tampil.style.map(style_prediksi, subset=['Prediksi'])
    st.dataframe(styled, use_container_width=True, hide_index=True)

    # ── Tombol hapus riwayat
    st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
    col_l, col_r = st.columns([3, 1])
    with col_r:
        if st.button("🗑  Hapus Riwayat", key="btn_clear_history", use_container_width=True):
            clear_history()
            st.rerun()
