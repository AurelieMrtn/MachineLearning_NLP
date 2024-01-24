import streamlit as st
import pandas as pd
import os

def run():

    # Style
    st.title("Restaurant Information Retrieval")
    
    # Import combined_scores
    current_directory = os.getcwd()
    file_path = current_directory + '/Projet2/StreamlitApp/Pages/translated_restaurants.csv'
    restaurants = pd.read_csv(file_path)
    
    # Load review data
    review_file_path = current_directory + '/Projet2/StreamlitApp/Pages/translated_reviews.csv'
    reviews = pd.read_csv(review_file_path)
    
    restaurants_name = restaurants[restaurants['Restaurant_Name']]
    
    restaurant_input = st.selectbox("Choose a restaurant name:", restaurants_name)

    # Filter the DataFrame based on the entered restaurant name
    if restaurant_input:
        filtered_restaurants = restaurants[restaurants['Restaurant_Name'].str.contains(restaurant_input, case=False, na=False)]
        filtered_reviews = reviews[reviews['Restaurant_Name'].str.contains(restaurant_input, case=False, na=False)]

        if not filtered_restaurants.empty:
            # Displaying the information about the restaurant
            for _, row in filtered_restaurants.iterrows():
                st.subheader(row['Restaurant_Name'])
                st.write(f"Ranking: {row['Ranking']}")
                st.write(f"Price Range: {row['Price_Range']}")
                st.write(f"Cuisine Type: {row['Cuisine_Type']}")

            # Display reviews for the restaurant
            if not filtered_reviews.empty:
                st.subheader("Reviews")
                for _, review_row in filtered_reviews.iterrows():
                    st.write(f"Global Rating: {review_row['Global_Ranking']}")
                    st.write(f"Meal Rating: {review_row['Plats_Ranking']}")
                    st.write(f"Service Rating: {review_row['Service_Ranking']}")
                    st.write(f"Atmoshpere Rating: {review_row['Atmosphere_Ranking']}")
                    st.write(f"Review: {review_row['Text']}")
            else:
                st.write("No reviews available for this restaurant.")
        else:
            st.write("No results found for the entered restaurant name.")
    else:
        st.write("Please enter a restaurant name to search.")