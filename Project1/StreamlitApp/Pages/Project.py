import streamlit as st
import json

def run():
    # Style
    st.title("Information Retrieval")

    # Text input
    input = st.text_input("Type a query number:", "PLAIN-1")
    
    file_path = 'combined_scores.json'

    with open(file_path, 'r') as file:
        loaded_dict = json.load(file)
    print(f"The dictionary has been loaded from {file_path}: {loaded_dict}")
    