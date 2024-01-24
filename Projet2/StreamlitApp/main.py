import importlib
import streamlit as st

home = importlib.import_module("Pages.Home")
explanations = importlib.import_module("Pages.Explanations")
summary = importlib.import_module("Pages.RestoSummary")
info = importlib.import_module("Pages.InfoRetriev")
qa = importlib.import_module("Pages.QuestAnsw")

PAGES = {
    "Home": home,
    "Project Explanations" : explanations,
    "Restaurant Summary": summary,
    "Review Information Retrieval": info,
    "Question and Answer": qa
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.run()
