#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  return result;
}
num1 = process.argv[2];
num2 = process.argv[3];
const sum = add(num1, num2);
console.log(sum);
