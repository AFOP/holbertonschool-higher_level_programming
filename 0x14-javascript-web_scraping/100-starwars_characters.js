#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:
The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module axios
*/
const idFilm = process.argv[2];
const axios = require('axios').default;
axios.get('https://swapi-api.hbtn.io/api/films/' + idFilm)
  .then((response) => {
    const characters = response.data.characters;
    characters.forEach((linkCharacter) => {
      axios.get(linkCharacter)
        .then((response) => {
          console.log(response.data.name);
        })
        .catch((error) => {
          console.log('code: ' + error);
        });
    });
  })
  .catch((error) => {
    console.log('code: ' + error);
  });
