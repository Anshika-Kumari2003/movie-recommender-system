import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', '')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""
