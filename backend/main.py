from typing import Union
from fastapi import FastAPI
from movies import my_movies, Movie, MovieNew, MovieUpdate

app = FastAPI()

#print(my_movies)
@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: str) -> Union[Movie,None]:
	if movie_id in my_movies:
		movie = my_movies[movie_id]
		if movie.id == movie_id:
			return movie

	return None

@app.put("/movies/{movie_id}", response_model=MovieUpdate)
def update_movie(movie_id: str, update_movie: MovieUpdate) -> Union[Movie,None]:
	if movie_id in my_movies:
		movie = my_movies[movie_id]
		if movie.id == movie_id:
			my_update_movie = Movie(
				id = movie_id,
				name = update_movie.name,
				cast = update_movie.cast
			)
			my_movies[movie_id] = my_update_movie
			return my_movies[movie_id]
	return None

