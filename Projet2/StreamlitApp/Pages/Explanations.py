import streamlit as st

def run():
    # Style
    st.title("Project Explanation")

    # Project Description
    st.header("Project Overview")
    st.write("Provide a detailed overview of your project here. "
             "Explain the goals, the scope, and what you are trying to achieve.")

    # Dataset Descriptions
    st.header("Datasets Used")
    st.subheader("Restaurant Dataset")
    st.write("Describe your restaurant dataset here. "
             "Include details about the data source, the kind of information it contains, "
             "such as restaurant names, cuisine types, price ranges, etc.")

    st.subheader("Review Dataset")
    st.write("Describe your review dataset here. "
             "Detail the type of reviews included, the ratings, and how they relate to the restaurants.")

    # Additional Information
    st.header("Additional Information")
    st.write("Any additional information about your project can go here. "
             "This might include your methodology, tools used, or any challenges faced during development.")