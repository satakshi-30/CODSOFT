import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# -----------------------------
# Sample Movies Dataset
# -----------------------------
movies = pd.DataFrame({
    "movie_id": [1, 2, 3, 4, 5],
    "title": ["The Matrix", "John Wick", "The Lord of the Rings",
              "Harry Potter", "Avengers"],
    "genre": ["sci-fi action", "action thriller", "fantasy adventure",
              "fantasy magic", "action superhero"]
})

# -----------------------------
# Content-Based Filtering
# -----------------------------
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(movies['genre'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

def recommend_content(movie_title, n=3):
    """Recommend movies based on genre similarity"""
    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# -----------------------------
# Collaborative Filtering (User-User)
# -----------------------------
ratings = pd.DataFrame({
    "The Matrix": [5, 4, 0, 0, 3],
    "John Wick": [4, 0, 5, 4, 0],
    "The Lord of the Rings": [0, 4, 4, 5, 3],
    "Harry Potter": [0, 5, 4, 4, 0],
    "Avengers": [3, 0, 5, 0, 4]
}, index=["user1", "user2", "user3", "user4", "user5"])

user_sim = cosine_similarity(ratings)
user_sim_df = pd.DataFrame(user_sim, index=ratings.index, columns=ratings.index)

def recommend_collaborative(user, n=3):
    """Recommend movies based on similar users' ratings"""
    similar_users = user_sim_df[user].sort_values(ascending=False)
    similar_users = similar_users.drop(user)  

    weighted_scores = pd.Series(0, index=ratings.columns)
    for other_user, score in similar_users.items():
        weighted_scores += ratings.loc[other_user] * score

    unrated = ratings.loc[user] == 0
    ranked = weighted_scores[unrated].sort_values(ascending=False)
    return ranked.head(n).index.tolist()
print("🎬 Content-based recommendations for 'The Matrix':")
print(recommend_content("The Matrix"))

print("\n👥 Collaborative filtering recommendations for user2:")
print(recommend_collaborative("user2"))