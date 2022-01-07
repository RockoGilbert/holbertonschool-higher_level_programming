#!/usr/bin/node
// Writing a class rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if (w < 1 || h < 1) { return; }
    if (w === undefined || h === undefined) { }
  }
}

module.exports = Rectangle;
