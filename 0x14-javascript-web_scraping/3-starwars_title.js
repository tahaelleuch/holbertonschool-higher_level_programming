#!/usr/bin/node

const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
request(link, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log(JSON.parse(body).title);
});
