import streamlit as st
import json
import os
import requests

def run():

    # Style
    st.title("Information Retrieval")

    # Text input
    query_input = st.text_input("Type a query number:", "PLAIN-1")
    
    # Import combined_scores
    current_directory = os.getcwd()
    file_path = current_directory + '/StreamlitApp/Pages/combined_scores.json'
    file_URL = 'https://drive.google.com/uc?export=download&id=1vhfW6KvAit-v0YBoTbpqSSnPPjs1X3N9'
    
    def download_file(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    file_content = download_file(file_URL)
    print(file_content)
    

    
    if query_input in combined_scores:
        # Find the document with the highest score for the given query
        highest_score_doc = max(combined_scores[query_input], key=combined_scores[query_input].get)
        highest_score = combined_scores[query_input][highest_score_doc]

        # Display the result
        st.write("Output :")
        st.write(f"Document with the highest score for query '{query_input}': {highest_score_doc} (Score: {highest_score})")
    else:
        st.write("No results found for the given query.")
        
run()