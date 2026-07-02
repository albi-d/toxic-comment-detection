import streamlit as st
import joblib
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)


@st.cache_resource
def load_model():
    """Load Naive Bayes model, TF-IDF vectorizer, stemmer, dan stopwords."""
    model   = joblib.load('naive_bayes_model.pkl')
    tfidf   = joblib.load('tfidf_vectorizer.pkl')
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stop_words = set(stopwords.words('indonesian'))
    return model, tfidf, stemmer, stop_words
