#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle:
You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
Create an instance method called rotate() that exchanges the width and the height of the rectangle
Create an instance method called double() that multiples the width and the height of the rectangle by 2
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return (undefined);
    }
  }

  print (c) {
    let i = 1;
    let j = 1;
    let resultado = '';
    if (!c) {
      c = "X";
    }
    while (i <= this.height) {
      while (j <= this.width) {
        resultado += c;
        j++;
      }
      if (i === this.height) {
        resultado += '';
      } else {
        resultado += '\n';
      }
      j = 1;
      i++;
    }
    console.log(resultado);
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
