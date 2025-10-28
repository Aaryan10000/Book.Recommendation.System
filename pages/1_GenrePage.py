from collections import Counter
import streamlit as st
import pandas as pd
import pickle
import os

# Load objects from disk (at the start of your script)
with open('recommender_Model/final_df.pkl', 'rb') as f:
    final_df = pickle.load(f)
with open('recommender_Model/tfidf_matrices.pkl', 'rb') as f:
    tfidf_matrices = pickle.load(f)
with open('recommender_Model/similarity_matrices.pkl', 'rb') as f:
    similarity_matrices = pickle.load(f)


def clean_genre_list(genres):
    # Convert string to list if necessary
    if isinstance(genres, str):
        try:
            genres_list = eval(genres)
        except:
            return []  # fallback to empty list if eval fails
    elif isinstance(genres, list):
        genres_list = genres
    else:
        return []

    # Remove empty, whitespace-only, or single-letter strings
    cleaned = [g.strip()
               for g in genres_list if g and g.strip() and len(g.strip()) > 1]
    return cleaned


# Apply cleaning to your dataframe column
final_df['genres_list'] = final_df['genres'].apply(clean_genre_list)
# Assuming final_df['genres_list'] is a list of genre tags per book
all_tags = [tag for sublist in final_df['genres_list'] for tag in sublist]
# Count frequency of each tag
tag_counts = Counter(all_tags)
# Get top 50 most common tags as a list of strings
top_50_tags = [tag for tag, count in tag_counts.most_common(50)]

# PAGE BELOW

# --- Page UI ---
st.title("🎭 Select a Genre Tag")

# Split tags into 5 columns × 10 buttons each
chunks = [top_50_tags[i:i+10] for i in range(0, len(top_50_tags), 10)]
cols = st.columns(5)

for col, chunk in zip(cols, chunks):
    with col:
        for tag in chunk:
            if st.button(tag):
                st.session_state['selected_tag'] = tag
                st.switch_page("pages/2_SuggBooks.py")
