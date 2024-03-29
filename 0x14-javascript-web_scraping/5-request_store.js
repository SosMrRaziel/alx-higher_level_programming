#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf8', function (error) {
      if (error) {
        console.error(error);
      }
    });
  }
});
