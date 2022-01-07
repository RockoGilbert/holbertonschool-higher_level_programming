#!/usr/bin/node
//rectangle instance
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    this.cell = c || 'X';
    this.print();
  }
}

module.exports = Square;
