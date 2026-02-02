import streamlit as st
import pandas as pd
import os

def run():

    st.title("Search Restaurants by Cuisine or Price")

    # Import combined_scores
    file_path = 'translated_restaurants.csv'
    restaurants = pd.read_csv(file_path)

    # User input for cuisine type and price range
    cuisine_input = st.text_input("Enter desired cuisine type:")
    price_input = st.text_input("Enter desired price range:")

    # Filter and display matching restaurants
    if cuisine_input or price_input:
        if cuisine_input:
            filtered_restaurants = restaurants[restaurants['Cuisine_Type'].str.contains(cuisine_input, case=False, na=False)]
        if price_input:
            filtered_restaurants = restaurants[restaurants['Price_Range'].str.contains(price_input, case=False, na=False)]

        if not filtered_restaurants.empty:
            st.subheader("Matching Restaurants:")
            for index, row in filtered_restaurants.iterrows():
                st.write((f"Name of the restaurant: {row['Restaurant_Name']}"))
                st.write((f"Ranking: {row['Ranking']}"))
        else:
            st.write("No matching restaurants found.")
    else:
        st.write("Please enter a cuisine type or price range to search (For exemple, you can try: De 31 € à 50 € and Française).")