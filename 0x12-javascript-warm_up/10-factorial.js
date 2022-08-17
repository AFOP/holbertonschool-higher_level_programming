#!/usr/bin/node
/*
Function factorialize for recurtion
*/
function factorialize(num) {
  if (num < 0)
    return -1;
  else if (num == 0) 
    return 1;
  else
    return (num * factorialize(num - 1));
}
/*
Write a script that computes and prints a factorial
The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
You must use console.log(...) to print all output
You are not allowed to use var
*/
const args = process.argv;
let fac = 0;
let n1 = 0;
if (parseInt(args[2])) {
  n1 = parseInt(args[2]);
  fac = factorialize(n1);
  console.log(fac);
} else {
  console.log(1);
}
