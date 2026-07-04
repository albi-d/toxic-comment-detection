import streamlit as st
import pandas as pd
from utils.history import get_history, clear_history


def render_history():
    """Tab riwayat deteksi sesi ini."""

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    history = get_history()

    if not history:
        st.markdown("""
        <div class="empty-state">
            <span class="empty-icon">🕓</span>
            <div class="empty-text">Belum ada riwayat.<br>Mulai deteksi komentar untuk melihat hasilnya di sini.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    df = pd.DataFrame(history)
    total   = len(df)
    n_toxic = (df['prediksi'] == 'Toxic').sum()
    n_aman  = total - n_toxic

    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-card"><div class="stat-value">{total}</div><div class="stat-label">Total</div></div>
        <div class="stat-card"><div class="stat-value-toxic">{n_toxic}</div><div class="stat-label">Toxic</div></div>
        <div class="stat-card"><div class="stat-value-safe">{n_aman}</div><div class="stat-label">Non-Toxic</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<span class="section-label">Riwayat Sesi Ini</span>', unsafe_allow_html=True)

    df_tampil = df.rename(columns={
        'waktu': 'Waktu', 'komentar': 'Komentar',
        'prediksi': 'Prediksi', '% toxic': '% Toxic', '% non-toxic': '% Non-Toxic',
    })

    def _s(v):
        return 'color:#dc2626;font-weight:600;' if v == 'Toxic' else 'color:#16a34a;font-weight:600;'

    st.dataframe(df_tampil.style.map(_s, subset=['Prediksi']),
                 use_container_width=True, hide_index=True)

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    col_l, col_r = st.columns([3, 1])
    with col_r:
        if st.button("Hapus", key="btn_clear_history", use_container_width=True):
            clear_history()
            st.rerun()
