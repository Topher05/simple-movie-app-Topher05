import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
import {List, ListItemIcon, ListItem, ListItemText, TextField} from '@mui/material'
import LocalMoviesIcon from '@mui/icons-material/LocalMovies';
function App() {
  const [movieId, setMovieId] = useState("2")
  const [movie, setMovie] = useState(null)

  useEffect(() => {
    if (movieId == ""){
      setMovie(null);
    } else{
      fetch (`http://localhost:3000/movies/${movieId}`)
      .then( result => result.json() )
      .then(result => {
        console.log(`http://localhost:3000/movies/${movieId}`)
        setMovie(result);
      });
    }
    console.log(movieId);
  }, [movieId]);

  useEffect(() => {
    console.log(movieId);
  }, [movie]);

  return (
    <div className="App">
      <header className="App-header">
        <TextField id ="outlined-basic" label = "Movie ID" variant='outlined'
        color = 'warning' focused value={movieId}
        on onChange={e => setMovieId(e.targe.value)}/>
        <List>
          { movie && 
          <ListItem>
            <ListItemIcon>
              <LocalMoviesIcon/>
            </ListItemIcon>
            <ListItemText primary={movie['movie_name']} />
          </ListItem>}
        </List>
      </header>
    </div>
  );
}

export default App;
