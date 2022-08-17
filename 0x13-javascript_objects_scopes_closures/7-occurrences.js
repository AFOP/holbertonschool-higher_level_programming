#!/usr/bin/node
/*
Write a function that returns the number of occurrences in a list:
Prototype: exports.nbOccurences = function (list, searchElement)
*/
exports.nbOccurences = function (array, value) {
  return (array.filter((cElm) => cElm === value).length);
};