import streamlit as st
from datetime import datetime


def init_history():
    """Inisialisasi riwayat deteksi di session_state."""
    if 'history' not in st.session_state:
        st.session_state.history = []


def add_history(komentar: str, label: int, proba_toxic: float, proba_nontoxic: float):
    """Tambahkan satu hasil deteksi ke riwayat."""
    init_history()
    st.session_state.history.append({
        'waktu': datetime.now().strftime('%H:%M:%S'),
        'komentar': komentar[:80] + ('...' if len(komentar) > 80 else ''),
        'prediksi': 'Toxic' if label == 1 else 'Non-Toxic',
        '% toxic': round(proba_toxic * 100, 1),
        '% non-toxic': round(proba_nontoxic * 100, 1),
    })


def get_history():
    """Ambil list riwayat deteksi."""
    init_history()
    return st.session_state.history


def clear_history():
    """Hapus semua riwayat."""
    st.session_state.history = []
