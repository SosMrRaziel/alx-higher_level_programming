#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  return result;
}
const num1 = process.argv[2];
const num2 = process.argv[3];
const sum = add(num1, num2);
console.log(sum);
