from pydantic import BaseModel
from typing import Set 

class MaxId:
      def __init__(self):
         self.max_id=0
      
      def get_max_id(self):
         return self.max_id
      def set_max_id(self, new_id):
            self.max_id=new_id

my_max_id = MaxId()

class MovieNew(BaseModel):
	id: str
	name: str
	cast: Set[str]

class MovieUpdate(BaseModel):
      name: str
      cast: Set[str]

class Movie(BaseModel):
	id: str
	name: str
	cast: Set[str]

my_movies = {}

with open("./movies.txt", encoding="utf-8") as file:
            row_idx = 0
            for line in file:
               if row_idx%3 == 0:
                  movie_name = line.rstrip()
               if row_idx%3 == 1:
                  movie_cast = line.rstrip().split(',')
               if row_idx%3 == 2:
                  my_max_id.set_max_id(my_max_id.get_max_id()+1)
                  my_movies[str(my_max_id.get_max_id())] = Movie(
                              id = str(my_max_id.get_max_id()),
                              name = movie_name,
                              cast = movie_cast
                              )      
               		
               row_idx += 1

print(__name__)
if __name__ == "__main__":
	movie = Movie()