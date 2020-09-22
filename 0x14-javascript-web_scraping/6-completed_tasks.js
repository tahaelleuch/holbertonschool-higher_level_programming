#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const Mybody = JSON.parse(body);
  const dict = {};
  for (const i in Mybody) {
    dict[Mybody[i].userId] = 0;
  }
  for (const j in Mybody) {
    if (Mybody[j].completed === true) {
      if (dict[Mybody[j].userId] === undefined) {
        dict[Mybody[j].userId] = 1;
      }
      dict[Mybody[j].userId]++;
    }
  }
  console.log(dict);
});
