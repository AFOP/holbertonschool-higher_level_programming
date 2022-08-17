#!/usr/bin/node
/*
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
You must use the class notation for defining your class and extends
Create an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X
*/
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c || c != 'C') {
      c = 'X';
    }
    this.print(c);
  }
}
module.exports = Square;
