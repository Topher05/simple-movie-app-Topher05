from pydantic import BaseModel
from typing import Set 

class MovieNew(BaseModel):
	id: str
	name: str
	cast: Set[str]

class Movie(BaseModel):
	id: str
	name: str
	cast: Set[str]

my_movies = {}

with open("./movies.txt", encoding="utf-8") as file:
            row_idx = 0
            id_count = 0
            for line in file:
               if row_idx%3 == 0:
                  movie_name = line.rstrip()
               if row_idx%3 == 1:
                  movie_cast = line.rstrip().split(',')
               if row_idx%3 == 2:
                  id_count +=1
                  my_movies[str(id_count)] = Movie(
                              id = str(id_count),
                              name = movie_name,
                              cast = movie_cast
                              )      
               		
               row_idx += 1

print(__name__)
if __name__ == "__main__":
	movie = Movie()