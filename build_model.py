import requests
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"  # replace with your own if needed

def fetch_tmdb_movies():
    all_movies = []
    for page in range(1, 6):  # fetch first 2 pages (40 movies)
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
        response = requests.get(url).json()
        for movie in response['results']:
            all_movies.append({
                'movie_id': movie['id'],
                'title': movie['title'],
                'overview': movie['overview']
            })
    return pd.DataFrame(all_movies)

# Fetch movies
df = fetch_tmdb_movies()

# Save movie list
import os
os.makedirs('model', exist_ok=True)
pickle.dump(df, open('model/movie_list.pkl', 'wb'))

# Calculate similarity based on overview
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['overview'].fillna(''))
similarity = cosine_similarity(tfidf_matrix)
pickle.dump(similarity, open('model/similarity.pkl', 'wb'))

print("✅ movie_list.pkl and similarity.pkl generated!")
