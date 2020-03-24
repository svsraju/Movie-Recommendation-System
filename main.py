import pandas as pd
import numpy as np
#from math import sqrt
from flask import Flask, render_template, request
# libraries for making count matrix and similarity matrix
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.metrics.pairwise import cosine_similarity

		
def recommend(userinput):
	inputMovies = pd.DataFrame(userinput)
	genre_movies_df = pd.read_csv('genre_movies_df.csv')
	userMovies = genre_movies_df[genre_movies_df['title'].isin(inputMovies['title'].tolist())]
	genreTable = genre_movies_df.set_index(genre_movies_df['movieId'])
	#And drop the unnecessary information
	genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

	userMovies = userMovies.reset_index(drop=True)
	userGenreTable = userMovies.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)
	

	#Dot produt to get weights
	userProfile = userGenreTable.transpose().dot(inputMovies['rating'])
	
	recommendationTable_df = ((genreTable*userProfile).sum(axis=1))/(userProfile.sum())
	
	recommendationTable_df = recommendationTable_df.sort_values(ascending=False)
	
	topmovies = genre_movies_df.loc[genre_movies_df['movieId'].isin(recommendationTable_df.head(10).keys())]

	return topmovies


def topmovies(movies):
	final_movies = []
	for i in range(len(userinput)):
		for j in range(len(movies['title'].values)):
			if userinput[i]['title'] != movies['title'].values[j]:
				final_movies.append(movies['title'].values[j])

	final_movies = set(final_movies)
	final_movies = (list(final_movies))
	final_movies = final_movies[0:11]
	return final_movies
	
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
	userinput = []
	key_values = {}
        title = request.args.get('movie')
	rating = request.args.get('rating')
	key_values['title'] = title
	key_values['rating'] = rating
	userinput.append(key_values.copy())
	
	movies = userProfile(userinput)
	
	r = topmovies(movies)
	
	return render_template('recommend.html',movie=title,r=r)
        #if type(r)==type('string'):
        	#return render_template('recommend.html',movie=title,r=r,t='s')
    	#else:
        	#return render_template('recommend.html',movie=title,r=r,t='l')



if __name__ == '__main__':
    app.run()
