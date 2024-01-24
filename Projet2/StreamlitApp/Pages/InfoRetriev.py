import streamlit as st
import csv
import pandas as pd
import os

def run():

    # Style
    st.title("Restaurant Information Retrieval")
    
    # Import combined_scores
    current_directory = os.getcwd()
    file_path = current_directory + '/Projet2/StreamlitApp/Pages/restaurants.csv'
    
    restaurants = pd.read_csv(file_path)

    restaurant_input = st.text_input("Enter a restaurant name:")

    # Filter the DataFrame based on the entered restaurant name
    if restaurant_input:
        filtered_restaurants = restaurants[restaurants['Restaurant_Name'].str.contains(restaurant_input, case=False, na=False)]
        
        if not filtered_restaurants.empty:
            # Displaying the information about the restaurant
            for _, row in filtered_restaurants.iterrows():
                st.subheader(row['Restaurant_Name'])
                st.write(f"Ranking: {row['Ranking']}")
                st.write(f"Price Range: {row['Price_Range']}")
                st.write(f"Cuisine Type: {row['Cuisine_Type']}")
                st.write(f"Menu Items: {row['Menu Items']}")
        else:
            st.write("No results found for the entered restaurant name.")
    else:
        st.write("Please enter a restaurant name to search.")
