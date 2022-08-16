#!/usr/bin/node
/*
Write a script that prints the first argument passed to it:
If no arguments are passed to the script, print “No argument”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use length
*/
const args = process.argv;
let i = 0;
while (args[i])
{ 
  if (i > 1) {
    console.log(args[i]);
  }
  i++;
}
if (i <= 2) {
  console.log('No argument');
}
