from nltk.metrics import edit_distance, jaccard_distance
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def run():
    # Style
    st.title("Text similarity measure")
    
    # Text inputs
    text1 = st.text_area("Type first text:", "")
    text2 = st.text_area("Type second text: ", "")
    
    # Method selector
    similarity = st.selectbox(
        "Choose a similarity measure:",
        ["Cosine Similarity", "Levenshtein Distance", "Jaccard Distance", "Q-Grams (Jaccard on n-grams)"]
    )
    
    if st.button('Measure similarity'):
        
        # Models and measurements
        if similarity == "Cosine Similarity":
            vectorizer = CountVectorizer().fit_transform([text1, text2])
            vectors = vectorizer.toarray()
            cos_sim = cosine_similarity(vectors)
            st.write(f"Cosine similarity is: {cos_sim[0][1]}")
        
        elif similarity == "Levenshtein Distance":
            lev_dist = edit_distance(text1, text2)
            st.write(f"Levenshtein distance is: {lev_dist}")
        
        elif similarity == "Jaccard Distance":
            set1 = set(text1.split())
            set2 = set(text2.split())
            jaccard = jaccard_distance(set1, set2)
            st.write(f"Jaccard distance is: {jaccard}")
        
        elif similarity == "Q-Grams (Jaccard on n-grams)":
            vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 2))
            tf_matrix = vectorizer.fit_transform([text1, text2])
            qgram_sim = cosine_similarity(tf_matrix.toarray())
            st.write(f"Q-Grams similarity is: {qgram_sim[0][1]}")