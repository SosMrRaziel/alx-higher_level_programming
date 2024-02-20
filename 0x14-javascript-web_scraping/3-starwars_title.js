#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + movieID, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const date = JSON.parse(body);
    console.log(date.title);
  }
});
