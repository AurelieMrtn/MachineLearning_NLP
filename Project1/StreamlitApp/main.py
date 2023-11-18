import importlib
import streamlit as st

home = importlib.import_module("Pages.Home")
project = importlib.import_module("Pages.Project")

PAGES = {
    "Home": home,
    "Information Retrieval" : project
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.run()