import streamlit as st
import pickle
import pandas as pd

# Load model/data
with open('recommender_Model/final_df.pkl', 'rb') as f:
    final_df = pickle.load(f)

# Page UI
st.title("📖 Books Recommended for You")

if 'selected_tag' not in st.session_state:
    st.warning("Please go back and select a genre first.")
    if st.button("⬅️ Go Back"):
        st.switch_page("pages/tagPage.py")
else:
    tag = st.session_state['selected_tag']
    st.subheader(f"Top 10 books in the **{tag}** genre:")

    # Filter books by genre tag
    def has_tag(genres, tag):
        if isinstance(genres, str):
            try:
                genres = eval(genres)
            except:
                genres = []
        return tag in genres

    genre_books = final_df[final_df['genres'].apply(lambda x: has_tag(x, tag))]

    if genre_books.empty:
        st.error(f"No books found for genre '{tag}'.")
    else:
        # Show 10 random books
        sample_books = genre_books.sample(
            n=min(10, len(genre_books)), random_state=42)

# Split into two parts, 5 books each (or adjust if less)
    left_books = sample_books.iloc[:5]
    right_books = sample_books.iloc[5:]

    col1, col2 = st.columns(2)

# Display books in first column
with col1:
    for i, row in left_books.iterrows():
        st.image(row["coverImg"], width=120)
        st.markdown(
            f"<p style='font-size:18px'><i>{row['title']}</i> by <i>{row['author']}</i></p>", unsafe_allow_html=True)
        if 'genres' in row and isinstance(row['genres'], str):
            st.markdown(
                f"<p style='font-size:14px'>{row['genres'][:1000]}...</p>", unsafe_allow_html=True)
        # Unique key based on bookId for each button
        if st.button("Open Description", key=f"desc_left_{row['bookId']}"):
            st.session_state['selected_book_id'] = row['bookId']
            st.switch_page("pages/DetBooks.py")
        st.divider()

# Display books in second column
with col2:
    for i, row in right_books.iterrows():
        st.image(row["coverImg"], width=120)
        st.markdown(
            f"<p style='font-size:18px'><i>{row['title']}</i> by <i>{row['author']}</i></p>", unsafe_allow_html=True)
        if 'genres' in row and isinstance(row['genres'], str):
            st.markdown(
                f"<p style='font-size:14px'>{row['genres'][:1000]}...</p>", unsafe_allow_html=True)
        # Unique key based on bookId for each button
        if st.button("Open Description", key=f"desc_right_{row['bookId']}"):
            st.session_state['selected_book_id'] = row['bookId']
            st.switch_page("pages/3_BookDet.py")
        st.divider()


if st.button("⬅️ Choose Another Genre"):
    st.switch_page("pages/1_GenrePage.py")
