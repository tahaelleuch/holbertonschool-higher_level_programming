#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const Mybody = JSON.parse(body);
  const dict = {};
  for (const j in Mybody) {
    if (Mybody[j].completed === true) {
      if (dict[Mybody[j].userId] === undefined) {
        dict[Mybody[j].userId] = 1;
      } else {
        dict[Mybody[j].userId]++;
      }
    }
  }
  console.log(dict);
});
