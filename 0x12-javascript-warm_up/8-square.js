#!/usr/bin/node

const size = process.argv[2];
let x;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    x = '';
    for (let j = 0; j < size; j++) { x += 'X'; }
    console.log(x);
  }
}
