#!/usr/bin/node

const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(link, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const Mybody = JSON.parse(body);
  for (const car in Mybody.characters) {
    request(Mybody.characters[car], function (errorr, responser, bodyr) {
      if (errorr) {
        return console.log(errorr);
      }
      const Mybodychar = JSON.parse(bodyr);
      console.log(Mybodychar.name);
    });
  }
});
