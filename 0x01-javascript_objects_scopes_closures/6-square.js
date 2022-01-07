#!/usr/bin/node
// Print function with custom characters to represent the square

const oldSq = require('./5-square');

module.exports = class square extends oldSq {
  charPrint (c) {
    let l = 'X';
    if (c !== undefined) {
      l = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
