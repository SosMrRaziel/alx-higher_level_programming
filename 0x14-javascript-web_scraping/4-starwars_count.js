#!/usr/bin/node

const request = require("request");
const link = process.argv[2];

request(link, function(error, response, body) {
    if (error) {
        console.error(error);
    }
    else {
        const data = JSON.parse(body);
        const results = data.results;
        let counter = 0;
        for (let i = 0; i < results.length; i++) {
            const movie = results[i];
            const charac = movie.characters;
            if (charac.includes("https://swapi-api.alx-tools.com/api/films/people/18")) {
                counter ++;
            }
        }
        console.log(counter)
    }

}
)