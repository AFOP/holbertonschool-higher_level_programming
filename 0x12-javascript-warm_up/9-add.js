#!/usr/bin/node
/*
Write a script that prints the addition of 2 integers
The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
You must use console.log(...) to print all output
You are not allowed to use var
*/
const args = process.argv;
let r = 0;
let n1 = 0;
let n2 = 0;
if (args.length < 2) {
  console.log('NaN');
} else {
  n1 = parseInt(args[2]);
  n2 = parseInt(args[3]);
  r = n1 + n2;
  console.log(r);
}
