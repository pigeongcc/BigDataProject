import pandas as pd
import numpy as np
from IPython.display import display


# read the table
movies_path = 'data/movie_data.csv'
movies_path_pd = 'data/movie_data_pd.csv'
movies = pd.read_csv(movies_path, lineterminator='\n', index_col='_id')

# drop unused columns
movies = movies.drop(columns=['image_url', 'imdb_id', 'imdb_link', 'movie_title', 'original_language', 'overview', 'production_countries', 'runtime', 'spoken_languages', 'tmdb_id', 'tmdb_link', 'vote_average', 'vote_count'])

# remove carriage return symbols
movies = movies.replace({r'\r': ''}, regex=True)

# fix id of the films "(NULL)" and "Nan"
movies.at['60887d7c28f29d0115ea6207', 'movie_id'] = 'nan_id'
movies.at['5fd08f22b89a841f5b234f50', 'movie_id'] = 'null_id'

# replace np.nan with null
movies = movies.replace({np.nan: ''})

# save new csv
movies.to_csv(movies_path_pd, index=False)


# read the table
ratings_path = 'data/ratings_export.csv'
ratings_path_pd = 'data/ratings_export_pd.csv'
ratings = pd.read_csv(ratings_path, lineterminator='\n', )

# drop unused columns
ratings = ratings.drop(columns=['_id'])

# fix ratings table
ratings = ratings.replace({'movie_id': {np.nan: 'null_id', 'nan': 'nan_id'} })

# this step below is not necessary after removing users table from consideration
#ratings = ratings.drop(ratings[ratings.user_id == 'jacksonmaines'].index)

#left_join = ratings.merge(movies, on='movie_id', how='left', indicator=True)
ratings = ratings.drop(ratings[~ratings.movie_id.isin(movies.movie_id)].index)

# save new csv
ratings.to_csv(ratings_path_pd, index=False)
del ratings