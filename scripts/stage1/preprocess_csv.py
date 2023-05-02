import pandas as pd
import os

movies_path = 'data/movie_data.csv'
movies = pd.read_csv(movies_path, lineterminator='\n')

def to_psql_array(x):
	if type(x) == str:
		x = x.replace('[', '{')
		x = x.replace(']', '}')
		x = x.replace('"', '')
	return x

movies.genres = movies.genres.apply(lambda x: to_psql_array(x))

movies.to_csv(movies_path)
