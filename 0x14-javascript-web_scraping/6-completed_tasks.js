#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id.
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module axios
*/
const url = process.argv[2];
const axios = require('axios').default;
axios.get(url)
  .then((response) => {
    const completed = {};
    const tasks = response.data;
    tasks.forEach((task) => {
      if (task.completed) {
        if (task.userId in completed) {
          completed[task.userId]++;
        } else {
          completed[task.userId] = 1;
        }
      }
    });
    console.log(completed);
  })
  .catch((error) => {
    console.log('code: ' + error);
  });
