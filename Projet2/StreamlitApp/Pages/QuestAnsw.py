import streamlit as st
import pandas as pd
import os

def run():

    st.title("Search Restaurants by Cuisine or Price")

    # Import combined_scores
    current_directory = os.getcwd()
    file_path = current_directory + '/Projet2/StreamlitApp/Pages/translated_restaurants.csv'
    restaurants = pd.read_csv(file_path)
    
    # User input for cuisine type and price range
    cuisine_input = st.text_input("Enter desired cuisine type:")
    price_input = st.text_input("Enter desired price range:")

    # Filter and display matching restaurants
    if cuisine_input or price_input:
        filtered_restaurants = restaurants.copy()
        if cuisine_input:
            filtered_restaurants = filtered_restaurants[filtered_restaurants['Cuisine_Type'].str.contains(cuisine_input, case=False, na=False)]
        if price_input:
            filtered_restaurants = filtered_restaurants[filtered_restaurants['Price_Range'].str.contains(price_input, case=False, na=False)]

        if not filtered_restaurants.empty:
            st.write("Matching Restaurants:")
            for restaurant in filtered_restaurants['Restaurant_Name']:
                st.write(restaurant)
        else:
            st.write("No matching restaurants found.")
    else:
        st.write("Please enter a cuisine type or price range to search (For exemple, you can try: De 31 € à 50 € and Française - Traditionnelle.")