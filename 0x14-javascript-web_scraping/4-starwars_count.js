#!/usr/bin/node

let count = 0;
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const Mybody = JSON.parse(body);
  for (const i in Mybody.results) {
    for (const j in Mybody.results[i].characters) {
      if (Mybody.results[i].characters[j].search('18') !== -1) {
        count++;
      }
    }
  }
  console.log(count);
});
