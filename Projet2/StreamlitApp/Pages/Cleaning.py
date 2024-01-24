import streamlit as st
import string
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def run():
    # Style
    st.title("Text Cleaning")
    
    # Language
    language = st.selectbox("Choose a language: ", stopwords.fileids())
    stop_words = sw(language)
    
    input = st.text_area("Type a text to clean: ", "")
    
    options = st.multiselect(
        "Select a cleaning operations: ",
        ("Convert to Lowercase", "Remove Stop Words", "Remove Punctuation", "Trim Extra White Space"),
    )
    
    if st.button("Clean Text"):
        cleaned = input
        if "Convert to lowercase" in options:
            cleaned = lowercase(cleaned)
        if "Remove stopwords" in options:
            cleaned = removeSW(cleaned, stop_words)
        if "Remove punctuation" in options:
            cleaned = removeP(cleaned)
        if "Trim extra white spaces" in options:
            cleaned = trim(cleaned)
        
        st.write("#### Original Text")
        st.write(input)

        st.write("#### Cleaned Text")
        st.write(cleaned)

def sw(language):
    try:
        return set(stopwords.words(language))
    except LookupError:
        return set(stopwords.words(language))

def lowercase(text):
    return text.lower()

def removeSW(text, stop_words):
    return " ".join([word for word in text.split() if word.lower() not in stop_words])

def removeP(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def trim(text):
    return re.sub(' +', ' ', text).strip()