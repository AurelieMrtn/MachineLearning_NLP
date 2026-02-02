import streamlit as st
import pandas as pd
import os

def run():
    # Title
    st.title("Review Information Retrieval")

    # Load review data
    review_file_path = 'translated_reviews.csv'
    reviews = pd.read_csv(review_file_path)

    # User input for restaurant name
    review_input = st.text_input("Enter a review:")

    # Filter the DataFrame based on the entered restaurant name
    if review_input:
        filtered_reviews = reviews[reviews['Text'].str.contains(review_input, case=False, na=False)]

        # Display reviews for the restaurant
        if not filtered_reviews.empty:
            st.subheader("Review")
            for _, review_row in filtered_reviews.iterrows():
                st.write(f"Name of the restaurant: {review_row['Restaurant_Name']}")
                # Create a DataFrame for ratings
                ratings_df = pd.DataFrame({
                    'Rating Type': ['Global Rating', 'Meal Rating', 'Service Rating', 'Atmosphere Rating'],
                    'Score': [review_row['Global_Ranking'], review_row['Plats_Ranking'], review_row['Service_Ranking'], review_row['Atmosphere_Ranking']]
                })
                st.table(ratings_df)
                st.write(f"Review: {review_row['Text']}")
                st.write("---")
        else:
            st.write("This review doesn't exist.")
    else:
        st.write("Please enter a review to search (For example, you can try: Loved it, great service, great food. Friendly. Definitely recommend).")
