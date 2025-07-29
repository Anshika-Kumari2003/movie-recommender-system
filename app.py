import streamlit as st
import pickle
from recommend import recommend_movies
from utils import fetch_poster

# ⬇️ Must be placed immediately here
st.set_page_config(page_title="Movie Recommender", layout="wide")
# ✅ Create session state to store selected page
if 'page' not in st.session_state:
    st.session_state.page = "Home"
# Load data
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Sidebar menu
menu = st.sidebar.radio("📂 Navigate", ["Home", "Recommendations"], index=["Home", "Recommendations"].index(st.session_state.page))



if menu == "Home":
    st.markdown(
        """
        <style>
            .banner {
                position: relative;
                background-image: url("https://images.unsplash.com/photo-1601933470928-c43f7c7f27ad");
                background-size: cover;
                background-position: center;
                height: 500px;
                border-radius: 10px;
                margin-bottom: 20px;
            }

            .overlay {
                position: absolute;
                top: 0;
                left: 0;
                height: 100%;
                width: 100%;
                background-color: rgba(0,0,0,0.6);
                border-radius: 10px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                color: white;
                text-align: center;
                font-family: 'Segoe UI', sans-serif;
            }

            .overlay h1 {
                font-size: 48px;
                margin: 0;
            }

            .overlay p {
                font-size: 20px;
                margin-top: 10px;
            }
        </style>

        <div class="banner">
            <div class="overlay">
                <h1>🎥 Movie Recommender System</h1>
                <p>Discover personalized movie recommendations based on your favorites.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🎬 Start Browsing"):
        st.session_state.page = "Recommendations"
        st.rerun()


# RECOMMENDATION PAGE
elif menu == "Recommendations":
    st.title("🎬 Get Movie Recommendations")
    selected_movie = st.selectbox("Select a movie", movies['title'].values)

    if st.button("Recommend"):
        names, posters = recommend_movies(selected_movie, movies, similarity)
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(posters[i])
                st.text(names[i])
