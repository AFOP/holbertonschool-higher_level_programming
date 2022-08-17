#!/usr/bin/node
/*
Write a script that searches the second biggest integer in the list of arguments.
You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
You must use console.log(...) to print all output
You are not allowed to use var
*/
const args = process.argv;
let sort = [];
const size = args.length - 3;
let i = 2;
let j = 0;
if (args && args.length > 3) {
  while (args[i]) {
    sort[j] = args[i];
    i++;
    j++;
  }
  sort = sort.sort((a, b) => a - b);
  console.log(sort[size - 1]);
} else {
  console.log(0);
}
