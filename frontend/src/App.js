import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState, Component} from 'react';
import {List, ListItemIcon, ListItem, ListItemText, TextField} from '@mui/material'
import LocalMoviesIcon from '@mui/icons-material/LocalMovies';
// function App() {
//   const [movieId, setMovieId] = useState("2")
//   const [movie, setMovie] = useState(null)

//   useEffect(() => {
//     if (movieId == ""){
//       setMovie(null);
//     } else{
//       fetch (`http://localhost:3000/movies/${movieId}`)
//       .then( result => result.json() )
//       .then(result => {
//         console.log(`http://localhost:3000/movies/${movieId}`)
//         setMovie(result);
//       });
//     }
//     console.log(movieId);
//   }, [movieId]);

//   useEffect(() => {
//     console.log(movieId);
//   }, [movie]);

//   return (
//     <div className="App">
//       <header className="App-header">
//         <TextField id ="outlined-basic" label = "Movie ID" variant='outlined'
//         color = 'warning' focused value={movieId}
//         on onChange={e => setMovieId(e.targe.value)}/>
//         <List>
//           { movie && 
//           <ListItem>
//             <ListItemIcon>
//               <LocalMoviesIcon/>
//             </ListItemIcon>
//             <ListItemText primary={movie['movie_name']} />
//           </ListItem>}
//         </List>
//       </header>
//     </div>
//   );
// }
class App extends Component {
  render() {
    return(
      <div className="App">
        <header className="App-header">
          <img src={logo} className='App_logo' alt="logo"/>
          <h1 className='App-title'>Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
