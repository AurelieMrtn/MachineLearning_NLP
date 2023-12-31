import streamlit as st
import collections
import matplotlib.pyplot as plt
import numpy as np

def run():
    # Style
    st.title("Zipf's law's verification ")
    st.write("Zipf's law: the frequency of any word is inversely proportional to its rank in the frequency table.")

    articles = []

    # File upload for articles
    uploaded_files = st.file_uploader("Upload articles", type=["txt"], accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            articles.append(file.read().decode('utf-8'))
      
    if len(articles) == 3:
        article_1, article_2, article_3 = articles
        
        if st.button("Verify Zipf's law"):
            st.write("#### Article 1")
            verify(article_1)
            
            st.write("#### Article 2")
            verify(article_2)
            
            st.write("#### Article 3")
            verify(article_3)
    else:
        st.warning("Please upload at least three text files to verify Zipf's law.")

            
# Verify law        
def verify(text):
    words = text.split()
    freq_counter = collections.Counter(words)
    sorted_freq = sorted(freq_counter.values(), reverse=True)
    
    ranks = np.arange(1, len(sorted_freq) + 1)
    frequencies = np.array(sorted_freq)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(ranks, frequencies, color='blue')
    ax.set_title("Zipf's Law")
    ax.set_xlabel("Rank of the word")
    ax.set_ylabel("Frequency")
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(True)
    st.pyplot(fig)