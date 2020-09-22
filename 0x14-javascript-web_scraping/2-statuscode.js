#!/usr/bin/node

const request = require('request');
const req = request.get(process.argv[2]);
req.on('response', function (response) {
  console.log('code: ' + response.statusCode);
});
