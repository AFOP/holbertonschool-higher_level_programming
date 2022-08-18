#!/usr/bin/node
/*
Write a script that prints the number of movies where the character “Wedge Antilles” is present.
The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module axios
*/
const url = process.argv[2];
const axios = require('axios').default;
axios.get(url)
  .then((response) => {
    const films = response.data.results;
    let cont = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('/18')) {
          cont++;
        }
      }
    }
    console.log(cont);
  })
  .catch((error) => {
    console.log('code: ' + error);
  });
