#!/usr/bin/node
/*
Write a function that returns the reversed version of a list:
Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
*/
exports.esrever = function (list) {
  const reverse = [];
  let size = list.length - 1;
  let i = 0;
  while (i < list.length) {
    reverse[i] = list[size];
    i++;
    size--;
  }
  return (reverse);
};
