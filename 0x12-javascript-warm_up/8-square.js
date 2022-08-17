#!/usr/bin/node
/*
Write a script that prints a square
The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
*/
const args = process.argv;
const size = parseInt(args[2]);
let i = 1, j = 1;
let resultado = "";
if (args[2]) {
  if (size > 0) {
    while (i <= size) {
      while (j <= size) {
        resultado += 'X';
        j++;
      }
      if (i === size) {
        resultado += '';
      } else {
        resultado += '\n';
      }
      j = 1;
      i++;
    }
    console.log(resultado);
  }
} else {
  console.log('Missing size');
}
