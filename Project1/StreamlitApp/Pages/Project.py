import streamlit as st
import json

def run():

    # Style
    st.title("Information Retrieval")

    # Text input
    query_input = st.text_input("Type a query number:", "PLAIN-1")
    
    # Import combined_scores
    file_path = 'combined_scores.json'

    with open(file_path, 'r') as file:
        combined_scores = json.load(file)
    
    if query_input in combined_scores:
        # Find the document with the highest score for the given query
        highest_score_doc = max(combined_scores[query_input], key=combined_scores[query_input].get)
        highest_score = combined_scores[query_input][highest_score_doc]

        # Display the result
        st.write("Output :")
        st.write(f"Document with the highest score for query '{query_input}': {highest_score_doc} (Score: {highest_score})")
    else:
        st.write("No results found for the given query.")