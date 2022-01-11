#!/usr/bin/node

require('request').get(process.argv[2], function (err, r, body) {
  if (err) {
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
