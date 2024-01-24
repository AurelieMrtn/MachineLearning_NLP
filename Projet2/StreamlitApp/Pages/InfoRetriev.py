import streamlit as st
import pandas as pd
import os

def run():
    # Title
    st.title("Review Information Retrieval")

    # Load review data
    current_directory = os.getcwd()
    review_file_path = current_directory + '/Projet2/StreamlitApp/Pages/translated_reviews.csv'
    reviews = pd.read_csv(review_file_path)

    # User input for restaurant name
    review_input = st.text_input("Enter a review:")

    # Filter the DataFrame based on the entered restaurant name
    if review_input:
        filtered_reviews = reviews[reviews['Restaurant_Name'].str.contains(review_input, case=False, na=False)]

        # Display reviews for the restaurant
        if not filtered_reviews.empty:
            st.subheader("Reviews")
            for _, review_row in filtered_reviews.iterrows():
                st.write(f"Name of the restaurant: {review_row['Restaurant_Name']}")
                st.write(f"Global Rating: {review_row['Global_Ranking']}")
                st.write(f"Meal Rating: {review_row['Plats_Ranking']}")
                st.write(f"Service Rating: {review_row['Service_Ranking']}")
                st.write(f"Atmoshpere Rating: {review_row['Atmosphere_Ranking']}")
                st.write(f"Review: {review_row['Text']}")
        else:
            st.write("This review doesn't exist.")
    else:
        st.write("Please enter a review to search.")
