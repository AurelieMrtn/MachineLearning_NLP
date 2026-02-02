import streamlit as st
import pandas as pd

def run():

    st.title("Search Restaurants by Cuisine or Price")

    # Import combined_scores
    file_path = 'translated_restaurants.csv'
    restaurants = pd.read_csv(file_path)

    # User input for cuisine type and price range
    cuisine_input = st.text_input("Enter desired cuisine type:")
    price_input = st.text_input("Enter desired price range:")

    filtered_restaurants = restaurants.copy()

    # Filter and display matching restaurants
    if cuisine_input or price_input:
        if cuisine_input:
            filtered_restaurants = filtered_restaurants[
                filtered_restaurants['Cuisine_Type'].str.contains(cuisine_input, case=False, na=False)
            ]

        if price_input:
            filtered_restaurants = filtered_restaurants[
                filtered_restaurants['Price_Range'].str.contains(price_input, case=False, na=False)
            ]

        if not filtered_restaurants.empty:
            st.subheader("Matching Restaurants:")
            result_df = (
                filtered_restaurants[['Restaurant_Name', 'Ranking', 'Cuisine_Type', 'Price_Range']]
                .rename(columns={
                    'Restaurant_Name': 'Name of the restaurant',
                    'Ranking': 'Ranking',
                    'Cuisine_Type': 'Cuisine Type',
                    'Price_Range': 'Price Range'
                })
            )
            st.table(result_df.reset_index(drop=True))
        else:
            st.write("No matching restaurants found.")
    else:
        st.write("Please enter a cuisine type or price range to search (For example, you can try: De 31 € à 50 € and Française).")