from typing import Union
from fastapi import FastAPI
from movies import my_movies, Movie

app = FastAPI()

print(my_movies)
@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: str) -> Union[Movie,None]:
	if movie_id in my_movies:
		movie = my_movies[movie_id]
		if movie.id == movie_id:
			return movie

	return None
