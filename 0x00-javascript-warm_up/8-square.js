#!/usr/bin/node
const sq = parseInt(process.argv[2]);

if (sq) {
  for (let x = 0; x < sq; ++x) {
    console.log('X'.repeat(sq));
  }
} else {
    console.log('Missing size');
}
