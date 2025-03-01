import pickle
import pandas as pd
import os

# Dynamically get the current directory where utils.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
movie_file_path = os.path.join(current_dir, 'movie_df.pkl')
similarity_file_path = os.path.join(current_dir, 'similarity.pkl')

# Loading the pickle files
with open(movie_file_path, 'rb') as f:
    movies_df = pickle.load(f)

with open(similarity_file_path, 'rb') as f:
    similarity = pickle.load(f)

movies = pd.DataFrame(movies_df)

def get_recommendations(movie):
    if movie not in movies['title'].values:
        return None

    index = movies[movies['title'].str.lower() == movie.lower()].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommendations = []
    for i in distances[1:6]: 
        recommendations.append(movies.iloc[i[0]]['title'])

    return recommendations
