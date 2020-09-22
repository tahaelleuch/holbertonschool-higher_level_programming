#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const Mybody = JSON.parse(body);
  const dict = {};
  for (let i = 1; i < 11; i++) {
    dict[i] = 0;
    for (const j in Mybody) {
      if (Mybody[j].userId === i && Mybody[j].completed === true) {
        dict[i]++;
      }
    }
  }
  console.log(dict);
});
