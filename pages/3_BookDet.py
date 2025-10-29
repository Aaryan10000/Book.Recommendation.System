import streamlit as st
import pickle

# Load the data
with open('models/final_df.pkl', 'rb') as f:
    final_df = pickle.load(f)

st.title("Book Details")

book_id = st.session_state.get('selected_book_id')

if not book_id:
    st.write("No book selected. Please select a book from previous page.")
else:
    book = final_df[final_df['bookId'] == book_id]

    if book.empty:
        st.write("Book not found.")
    else:
        book = book.iloc[0]
        # Center image
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="{book['coverImg']}" width="200px" />
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Title
        st.markdown(
            f"<h1>{book['title']}</h1>",
            unsafe_allow_html=True,
        )

        # Author with bigger font
        st.markdown(
            f"<h3 style='center; font-size: 22px;'>by {book['author']}</h3>",
            unsafe_allow_html=True,
        )

        # Genres with bigger font
        if 'genres' in book and book['genres']:
            genres_list = (
                eval(book["genres"]) if isinstance(
                    book["genres"], str) else book["genres"]
            )
            st.markdown(
                f"<p style='font-size: 20px;'>Genres: {', '.join(genres_list)}</p>",
                unsafe_allow_html=True,
            )

        # Publication with medium font
        if 'publication' in book and book['publication']:
            st.markdown(
                f"<p style='font-size: 16px;'>Publication: {book['publication']}</p>",
                unsafe_allow_html=True,
            )

        # Description with larger font and justified text
        if 'description' in book and book['description']:
            st.markdown(
                f"<div style='text-align: justify; font-size: 20px; margin: 20px 0;'>{book['description']}</div>",
                unsafe_allow_html=True,
            )

        # Centered back button at bottom
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
        with col5:
            if st.button("Recommend Similar Books", use_container_width=True):
                st.session_state["selected_book_id"] = book_id
                st.switch_page("pages/4_Recommendations.py")
