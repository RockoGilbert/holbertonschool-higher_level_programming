#!/usr/bin/node
// Status codes

const request = require('request');

request(process.argv[2], function (err, res) {
  console.log('code:', res.statusCode);
});
