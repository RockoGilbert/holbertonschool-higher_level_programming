#!/usr/bin/node
//Write a script that prints a message depending on the # of passed args.
const arrArgs = process.argv;
const len = arrArgs.length;
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
