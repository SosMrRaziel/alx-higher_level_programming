#!/usr/bin/node

const fs = require('fs')
const file_path = process.argv[2]

fs.readFile(file_path, 'utf8', function(err, data) {
    if (err) {
        console.error(err);
    }
    else {
        console.log(data);
    }
})