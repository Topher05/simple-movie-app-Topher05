from typing import Union
from fastapi import FastAPI
from movies import my_movies, Movie, MovieNew, MovieUpdate, MaxId, my_max_id
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
	"http://localhost:3000",
]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)



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

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: str) ->Union[Movie,None]:
	if movie_id in my_movies:
		movie = my_movies[movie_id]
		if movie.id == movie_id:
			del my_movies[movie_id]
			return movie

	return None

@app.post("/movies/add")
def add_movie(new_movie: MovieNew) -> Union[Movie, None]:
	new_id = my_max_id.get_max_id() + 1
	print(new_id)
	my_new_movie= Movie(
		id = str(new_id),
		name = new_movie.name,
		cast = new_movie.cast
	)
	my_movies[my_new_movie.id] = my_new_movie
	my_max_id.set_max_id(str(new_id))
	return my_movies[str(new_id)]