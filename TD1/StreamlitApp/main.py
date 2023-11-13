import importlib
import streamlit as st
import nltk

nltk.download()

home = importlib.import_module("Pages.Home")

cleaning = importlib.import_module("Pages.Cleaning")
tokenization = importlib.import_module("Pages.Tokenization")
lemmatization = importlib.import_module("Pages.Lemmatization")
similarityMeasure = importlib.import_module("Pages.SimilarityMeasure")
zipfLawVerification = importlib.import_module("Pages.Zipf")

PAGES = {
    "Home": home,
    "Text cleaning" : cleaning,
    "Tokenization": tokenization,
    "Lemmatization": lemmatization,
    "Similarity Measure": similarityMeasure,
    "Zipf's law verification" : zipfLawVerification
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.run()