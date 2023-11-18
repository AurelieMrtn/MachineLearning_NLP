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
    file_path = current_directory + '/Project1/StreamlitApp/Pages/combined_scores.json'
    
    with open(file_path, 'r') as file:
        combined_scores = json.load(file)
    print(combined_scores)
    
    if query_input and query_input in combined_scores:
        # Sorting the documents for the given query based on their scores
        sorted_docs = sorted(combined_scores[query_input].items(), key=lambda x: x[1], reverse=True)

        # Display the top 3 results
        st.write("Top 3 Documents for Query:", query_input)
        for doc_id, score in sorted_docs[:3]:
            st.write(f"{doc_id}: Score = {score}")
    else:
        st.write("No results found for the given query or invalid query number.")
        
run()