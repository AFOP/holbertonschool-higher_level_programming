#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file.
The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module axios
*/
const url = process.argv[2];
const file = process.argv[3];
const axios = require('axios').default;
const fs = require('fs');

axios.get(url)
  .then(function (response) {
    const content = response.data;
    fs.writeFile(file, content, err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch(function (error) {
    console.log('code: ' + error);
  });
