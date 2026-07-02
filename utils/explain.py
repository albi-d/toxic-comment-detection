import re
import numpy as np
from utils.preprocessing import preprocessing


def get_top_words(teks_bersih: str, model, tfidf, label: int, top_n: int = 5):
    """
    Ambil top-N kata yang paling berkontribusi pada prediksi.
    Menggunakan log-probability dari Naive Bayes per kelas.

    Returns: list of (kata, skor) diurutkan dari tertinggi
    """
    if not teks_bersih.strip():
        return []

    tokens = teks_bersih.split()
    feature_names = tfidf.get_feature_names_out()
    log_probs = model.feature_log_prob_[label]  # log P(kata | kelas)

    hasil = []
    for token in set(tokens):
        if token in feature_names:
            idx = list(feature_names).index(token)
            skor = np.exp(log_probs[idx])
            hasil.append((token, skor))

    hasil.sort(key=lambda x: x[1], reverse=True)
    return hasil[:top_n]


def highlight_toxic_words(teks_asli: str, teks_bersih: str, model, tfidf, stemmer, stop_words):
    """
    Highlight kata-kata pada teks asli yang berkontribusi pada prediksi toxic.
    Kata yang muncul di top_words akan di-highlight merah.

    Returns: HTML string dengan highlight
    """
    top_words = get_top_words(teks_bersih, model, tfidf, label=1, top_n=10)
    top_stems = {w for w, _ in top_words}

    # Tokenisasi teks asli per kata (jaga tanda baca & spasi)
    tokens_raw = re.findall(r'\S+|\s+', teks_asli)

    hasil_html = []
    for token in tokens_raw:
        if token.strip() == '':
            hasil_html.append(token)
            continue

        # Bersihkan token untuk stemming
        kata_bersih = re.sub(r'[^a-zA-Z]', '', token).lower()
        try:
            stem = stemmer.stem(kata_bersih) if kata_bersih else ''
        except Exception:
            stem = kata_bersih

        if stem and stem in top_stems and kata_bersih not in stop_words:
            hasil_html.append(
                f'<mark style="background:#fee2e2;color:#dc2626;border-radius:4px;'
                f'padding:1px 4px;font-weight:600;">{token}</mark>'
            )
        else:
            hasil_html.append(token)

    return ''.join(hasil_html)
