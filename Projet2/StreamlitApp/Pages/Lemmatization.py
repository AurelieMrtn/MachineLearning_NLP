import streamlit as st
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def run():
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')

    # Style
    st.title("Lemmatization")

    # Text input
    input = st.text_input("Type a sentence:", "")

    # Method selector
    lemmatizer = st.selectbox(
        "Choose a steammer or lemmatizer: ",
        ["Stemming with PorterStemmer", "Stemming with LancasterStemmer", "Stemming with SnowballStemmer", "Lemmatization"]
    )
    
    # Define word
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN

    # Apply steamer or lemmatizer
    def process_text(text, lemmatizer):
        tokens = nltk.word_tokenize(text)
        if lemmatizer != "Lemmatization":
            if lemmatizer == "Stemming with PorterStemmer":
                stemmer = PorterStemmer()
            elif lemmatizer == "Stemming with LancasterStemmer":
                stemmer = LancasterStemmer()
            elif lemmatizer == "Stemming with SnowballStemmer":
                stemmer = SnowballStemmer("english")
            return ' '.join([stemmer.stem(token) for token in tokens])
        else:
            pos_tags = nltk.pos_tag(tokens)
            lemmatizer = WordNetLemmatizer()
            return ' '.join([lemmatizer.lemmatize(token, get_wordnet_pos(pos)) for token, pos in pos_tags])

    # Output
    if input:
        st.write("Output :")
        st.write(process_text(input, lemmatizer))