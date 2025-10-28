import streamlit as st

# Page UI
st.set_page_config(page_title="Book Recommender", page_icon="📚", layout="wide")

st.title("📚 Welcome to the Book Recommendation System")
st.markdown("""
This app helps you discover new books based on genres and content similarity.
Explore genres and find books that match your interests!
""")

if st.button("🎯 Start Exploring Genres"):
    st.switch_page("pages/1_GenrePage.py")
