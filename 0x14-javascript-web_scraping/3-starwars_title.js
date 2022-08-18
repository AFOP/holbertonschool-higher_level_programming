#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
The first argument is the movie ID
You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
You must use the module axios
*/
const args = process.argv;
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + args[2])
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
