import pandas as pd
import os
import numpy as np

movies_path = 'data/movie_data.csv'
movies = pd.read_csv(movies_path, lineterminator='\n')

def to_psql_array(x):
	if type(x) == str:
		x = x.replace('[', '{')
		x = x.replace(']', '}')
		x = x.replace('"', '')
	return x

movies.genres = movies.genres.apply(lambda x: to_psql_array(x))

# remove carriage return symbols
movies = movies.replace({r'\r': ''}, regex=True)
# add empty arrays to genres column
movies.genres = movies.genres.replace({'': '{}', np.nan: '{}'})

movies.to_csv(movies_path, index=False, encoding='utf-8')

#from IPython.display import display
#display(movies.iloc[0:25])

#print(movies.iloc[22].genres)
#print(type(movies.iloc[22].genres))
