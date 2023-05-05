import pandas as pd
import os
import numpy as np
from IPython.display import display

movies_path = 'data/movie_data.csv'
movies_path_pd = 'data/movie_data_pd.csv'
movies = pd.read_csv(movies_path, lineterminator='\n', index_col='_id')


ratings_path = 'data/ratings_export.csv'
ratings_path_pd = 'data/ratings_export_pd.csv'
ratings = pd.read_csv(ratings_path, lineterminator='\n', )


def to_psql_array(x):
	if type(x) == str:
		x = x.replace('[', '{')
		x = x.replace(']', '}')
		x = x.replace('"', '')
	elif x == np.nan:
		x = '{}'
	return x


movies.genres = movies.genres.apply(lambda x: to_psql_array(x))

# remove carriage return symbols
movies = movies.replace({r'\r': ''}, regex=True)


# fix id of the film "(NULL)"

#print("\n================================ np.nan")
#movies_nullid = movies[movies['movie_id']==np.nan]
#display(movies_nullid[['movie_id', 'imdb_id']])

# movies = movies.replace({'movie_id': {np.nan: 'null_id'}}) 
#movies.loc[movies['imdb_id']=='tt3790100'] = \
#	movies.loc[movies['imdb_id']=='tt3790100'].replace({'movie_id': 'nan_id'})
movies.at['60887d7c28f29d0115ea6207', 'movie_id'] = 'nan_id'

#movies.loc[movies['imdb_id']=='tt3572736'] = \
#        movies.loc[movies['imdb_id']=='tt3572736'].replace({'movie_id': 'null_id'})
movies.at['5fd08f22b89a841f5b234f50', 'movie_id'] = 'null_id'

# replace np.nan with null
movies = movies.replace({np.nan: ''})


# fix ratings table
ratings = ratings.replace({'movie_id': {np.nan: 'null_id', 'nan': 'nan_id'} })

ratings = ratings.drop(ratings[ratings.user_id == 'jacksonmaines'].index)

#left_join = ratings.merge(movies, on='movie_id', how='left', indicator=True)
ratings = ratings.drop(ratings[~ratings.movie_id.isin(movies.movie_id)].index)

# save new csv
movies.to_csv(movies_path_pd, index=True)
ratings.to_csv(ratings_path_pd, index=False)


#movies = pd.read_csv(movies_path_pd, lineterminator='\n')

#print("\n================================ null_id")
#movies_nullid = movies[movies['movie_id']=='null_id']
#display(movies_nullid[['movie_id', 'imdb_id']])

#nullrow = movies[movies['imdb_id']=='tt3572736'].iloc[0]
#display(nullrow)

#print(nullrow.movie_id)
#print(type(nullrow.movie_id))
