#!/usr/bin/node
const rocks = parseInt(process.argv[2]);

if (rocks) {
    for (let i = 0; i < rocks; i++) {
    console.log('C is fun');
  }
}else {
    console.log('Missing number of occurrences');
};
