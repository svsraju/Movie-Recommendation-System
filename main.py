import pandas as pd
import numpy as np
from math import sqrt
from flask import Flask, render_template, request
# libraries for making count matrix and similarity matrix
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.metrics.pairwise import cosine_similarity

		
def allmovies(userinput):
	inputMovies = pd.DataFrame(userinput)
	genre_movies_df = pd.read_csv('genre_movies_df.csv')
	inputId = genre_movies_df[genre_movies_df['title'].str.lower().isin(inputMovies['title'].str.lower().tolist())]
	#Then merging it so we can get the movieId. It's implicitly merging it by title.
	inputMovies = pd.merge(inputId, inputMovies)
	#Dropping information we won't use from the input dataframe
	inputMovies = inputMovies.drop('genres', 1).drop('year', 1)
	userMovies = genre_movies_df[genre_movies_df['title'].str.lower().isin(inputMovies['title'].str.lower().tolist())]
	genreTable = genre_movies_df.set_index(genre_movies_df['movieId'])
	#And drop the unnecessary information
	genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

	userMovies = userMovies.reset_index(drop=True)
	userGenreTable = userMovies.drop('movieId' , 1).drop('title', 1).drop('genres', 1).drop('year', 1)

	#Dot produt to get weights
	userProfile = userGenreTable.transpose().dot(inputMovies['rating'])
	
	recommendationTable_df = ((genreTable*userProfile).sum(axis=1))/(userProfile.sum())
	
	recommendationTable_df = recommendationTable_df.sort_values(ascending=False)
	
	topmovies = genre_movies_df.loc[genre_movies_df['movieId'].isin(recommendationTable_df.head(10).keys())]

	return topmovies


def topmovies(movies,userinput):
	final_movies = []
	for i in range(len(userinput)):
		for j in range(len(movies['title'].values)):
			if userinput[i]['title'] != movies['title'].values[j]:
				final_movies.append(movies['title'].values[j])

	final_movies = set(final_movies)
	final_movies = (list(final_movies))
	final_movies = final_movies[0:11]
	return final_movies
	
def checkduplicate(userInput):
  for i in range(len(userInput)):
    for j in range(len(userInput)):
      if i!= j:
        if userInput[i]['title'] == userInput[j]['title']:
          return('This movie is not in our database.\nPlease check if you spelled it correct.')
	
	
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
	userinput = []
	key_values = {}
	titles = []
	ratings = []
	titles.append(request.args.get('movie'))
	ratings.append(float(request.args.get('rating')))
	titles.append(request.args.get('movie2'))
	ratings.append(float(request.args.get('rating2')))
	titles.append(request.args.get('movie3'))
	ratings.append(float(request.args.get('rating3')))
	titles.append(request.args.get('movie4'))
	ratings.append(float(request.args.get('rating4')))
	titles.append(request.args.get('movie5'))
	ratings.append(float(request.args.get('rating5')))
	for i in range(len(titles)):
		key_values['title'] = titles[i]
		key_values['rating'] = ratings[i]
		userinput.append(key_values.copy())
	
	print(userinput)
	
	r = checkduplicate(userinput)
	
	if type(r)==type('string'):
		return render_template('recommend.html',r=r,t='s')
    
	else:
		movies = allmovies(userinput)
	
		r = topmovies(movies,userinput)
   
		return render_template('recommend.html',r=r, t='l')
        



if __name__ == '__main__':
    app.run()
