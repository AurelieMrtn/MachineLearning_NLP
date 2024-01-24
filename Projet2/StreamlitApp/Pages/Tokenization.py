import streamlit as st
import spacy
from nltk.tokenize import word_tokenize, WhitespaceTokenizer, TreebankWordTokenizer, WordPunctTokenizer
import nltk

nltk.download('punkt')
  
def run(): 
    # Style
    st.title("Tokenization")

    # Text input
    input = st.text_area("Type text to tokenize:", height=200)

    # Method selector
    tokenizer = st.selectbox(
        "Choose a tokenizer:",
        ["Word Tokenize", "Whitespace Tokenize", "Treebank Word Tokenize", "WordPunct Tokenize", "Spacy Tokenize"]
    )

    # Apply tokenization
    def tokenize(input, tokenizer):
        if tokenizer == "Word Tokenize":
            return word_tokenize(input)
        elif tokenizer == "Whitespace Tokenize":
            tokenizer = WhitespaceTokenizer()
            return tokenizer.tokenize(input)
        elif tokenizer == "Treebank Word Tokenize":
            tokenizer = TreebankWordTokenizer()
            return tokenizer.tokenize(input)
        elif tokenizer == "WordPunct Tokenize":
            tokenizer = WordPunctTokenizer()
            return tokenizer.tokenize(input)
        elif tokenizer == "Spacy Tokenize":
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(input)
            return [token.text for token in doc]

    # Output
    if input:
        st.markdown("<h2 style='text-align: center;'>Tokenized text: </h2>", unsafe_allow_html=True)
        st.write(tokenize(input, tokenizer))