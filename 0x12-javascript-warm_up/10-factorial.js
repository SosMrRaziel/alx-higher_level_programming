#!/usr/bin/node

function factory (x) {
  if (isNaN(x) || x < 0) {
    return 1;
  }
  if (x === 0 || x === 1) {
    return x;
  }
  return x * factory(x - 1);
}

const num = parseInt(process.argv[2]);

const result = factory(num);
console.log(result);
