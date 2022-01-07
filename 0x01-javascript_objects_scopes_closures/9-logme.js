#!/usr/bin/node
// Prints the number of args printed and new arg values

let occur = 0;
exports.logMe = function (item) {
  console.log(occur + ': ' + item);
  occur += 1;
};
