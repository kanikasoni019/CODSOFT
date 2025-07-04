import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie data
data = {
    'title': [
        'The Matrix', 'John Wick', 'Avengers: Endgame', 
        'The Lion King', 'Toy Story', 'Finding Nemo', 
        'Iron Man', 'Thor: Ragnarok', 'Frozen', 'Aladdin'
    ],
    'genre': [
        'Action Sci-Fi', 'Action Thriller', 'Action Adventure Sci-Fi',
        'Animation Drama', 'Animation Comedy', 'Animation Adventure',
        'Action Sci-Fi', 'Action Comedy', 'Animation Musical', 'Animation Adventure'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Vectorize genres using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Compute cosine similarity between all movies
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def recommend_movies(title, cosine_sim=cosine_sim):
    """
    Given a movie title, return a list of 3 most similar movies.
    """
    if title not in df['title'].values:
        return None, f"Movie '{title}' not found in the database."

    # Get index of the movie
    idx = df.index[df['title'] == title][0]

    # Compute similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Remove the movie itself from the recommendations
    sim_scores = [score for score in sim_scores if score[0] != idx]

    # Sort by similarity score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 3 similar movies
    top_scores = sim_scores[:3]
    movie_indices = [i[0] for i in top_scores]

    recommendations = df['title'].iloc[movie_indices].tolist()
    return recommendations, None

# Main program
print("Welcome to the Movie Recommender!")
print("Available movies:")
for title in df['title']:
    print(f"- {title}")

# Get user input
user_movie = input("\nEnter the movie you like: ")

# Get recommendations
recommendations, error = recommend_movies(user_movie)

# Display results
if error:
    print(error)
else:
    print(f"\nBecause you liked '{user_movie}', you might also enjoy:")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")
