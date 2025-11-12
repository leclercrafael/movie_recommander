import numpy as np
import pandas as pd
import sklearn 
import warnings
import math

import recommender_functions as rf

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print('Imports success')




movies = pd.read_csv('data/movie_dataset.csv')



features = ['keywords', 'cast', 'genres', 'director']


for feature in features:
	movies[feature] = movies[feature].fillna('')

def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print('Error', row	)
		
movies["combined_features"] = movies.apply(combine_features,axis=1)

vectorized = rf.myCountVectorizer(movies.combined_features)

cosined = cosine_similarity(vectorized[0])

movie_liked = str(input('What movie did you like ?'))
movie_liked==movies.original_title


if not(any(movie_liked == movies.original_title)) :
    print('Movie not in the database')
	
movie_index = rf.get_index_from_title(title=movie_liked, df=movies)

similar_movies =  list(enumerate(cosined[movie_index]))

## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

## Step 8: Print titles of first 50 movies
i=0
for element in sorted_similar_movies:
		print(rf.get_title_from_index(df=movies, index=element[0]))
		i=i+1
		if i>10:
			break
