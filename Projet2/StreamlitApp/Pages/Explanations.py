import streamlit as st

def run():
    # Style
    st.title("Project Explanation")

    # Project Description
    st.header("Project Overview")
    st.write("In this project, we have retrieved Paris' restaurant data from OpenTable. On this app, we can retrieve a restaurant's summary from its name, information from a review and ask question to find a restaurant.")

    # Restaurant Dataset Description
    st.subheader("Restaurant Dataset")
    st.write("The restaurant dataset provides comprehensive details about various dining establishments. "
             "It includes the following key information: "
             "\n- **Restaurant_Name**: The name of each restaurant. "
             "\n- **Ranking**: A numeric score reflecting the restaurant's quality or popularity. "
             "\n- **Price_Range**: Textual representation of the cost of dining, indicating the budget for a meal. "
             "\n- **Cuisine_Type**: The type of cuisine offered, highlighting the culinary variety. "
             "\n- **Menu Items**: A list of dishes available, giving insights into the menu offerings.")

    # Review Dataset Description
    st.subheader("Review Dataset")
    st.write("The review dataset contains detailed customer reviews for the restaurants. Key components include: "
             "\n- **Restaurant_Name**: Name of the restaurant being reviewed, linking the feedback to the establishment. "
             "\n- **Ranking**: Overall customer rating, reflecting general satisfaction. "
             "\n- **Global_Ranking**: A broader evaluation score, potentially aggregating various aspects. "
             "\n- **Plats_Ranking**: Rating specifically for the dishes served. "
             "\n- **Service_Ranking**: Assessment of the service quality. "
             "\n- **Atmosphere_Ranking**: Rating for the ambiance and environment. "
             "\n- **Text**: Written reviews providing qualitative customer feedback.")
