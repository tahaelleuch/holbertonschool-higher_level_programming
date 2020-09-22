#!/usr/bin/node

const chardict = {};
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
request(link, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const Mybody = JSON.parse(body);
  for (const car in Mybody.characters) {
    request(Mybody.characters[car], exports.dataMydata = function (errorr, responser, bodyr) {
      if (errorr) {
        return console.log(errorr);
      }
      const Mybodychar = JSON.parse(bodyr);
      chardict[car] = Mybodychar.name;
      if (Object.values(chardict).length === Mybody.characters.length) {
        for (const car in Mybody.characters) {
          console.log(chardict[car]);
        }
      }
    });
  }
});
