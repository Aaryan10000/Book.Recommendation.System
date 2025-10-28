import streamlit as st
import pickle

with open('recommender_Model/final_df.pkl', 'rb') as f:
    final_df = pickle.load(f)
with open('recommender_Model/similarity_matrices.pkl', 'rb') as f:
    similarity_matrices = pickle.load(f)

selected_book_id = st.session_state.get("selected_book_id")

if not selected_book_id:
    st.write("No book selected for recommendations.")
else:
    # Get index of selected book in final_df
    book_idx = int(final_df[final_df['bookId'] == selected_book_id].index[0])

    # Get similarity scores for this book
    sim_scores = list(enumerate(similarity_matrices['English'][book_idx]))

    # Sort by similarity score descending excluding the selected book itself
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 9 similar books excluding itself
    top_indices = [i for i, score in sim_scores[1:10]]
    recommended_books = final_df.iloc[top_indices]

    st.title("Recommended Books")

    # Show 3x3 grid of recommended books
    for i in range(0, len(recommended_books), 3):
        cols = st.columns(3)
        for col, (_, book) in zip(cols, recommended_books.iloc[i:i+3].iterrows()):
            with col:
                st.image(book["coverImg"], width=120)
                st.markdown(f"*{book['title']}* by *{book['author']}*")
                if 'genres' in book and isinstance(book['genres'], str):
                    st.write(book['genres'][:1000] + "...")
                if st.button("Open Description", key=f"desc_right_{book['bookId']}"):
                    st.session_state['selected_book_id'] = book['bookId']
                    st.switch_page("pages/3_BookDet.py")
                st.divider()
