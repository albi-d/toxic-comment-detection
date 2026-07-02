import re
from nltk.tokenize import word_tokenize


def preprocessing(teks: str, stemmer, stop_words) -> str:
    """Bersihkan dan normalisasi teks komentar."""
    teks = str(teks)
    teks = re.sub(r'<[^>]+>', '', teks)          # hapus HTML tag
    teks = re.sub(r'http\S+|www\S+', '', teks)   # hapus URL
    teks = re.sub(r'@\w+', '', teks)             # hapus mention
    teks = re.sub(r'#\w+', '', teks)             # hapus hashtag
    teks = re.sub(r'[^a-zA-Z\s]', '', teks)      # hapus karakter non-alfabet
    teks = teks.lower()
    tokens = word_tokenize(teks)
    tokens = [k for k in tokens if k not in stop_words]
    tokens = [stemmer.stem(k) for k in tokens]
    return ' '.join(tokens)


def prediksi(komentar: str, model, tfidf, stemmer, stop_words):
    """
    Prediksi apakah komentar toxic atau tidak.
    Returns: (label, probabilities, teks_bersih)
    """
    bersih = preprocessing(komentar, stemmer, stop_words)
    vec    = tfidf.transform([bersih])
    hasil  = model.predict(vec)[0]
    proba  = model.predict_proba(vec)[0]
    return hasil, proba, bersih
