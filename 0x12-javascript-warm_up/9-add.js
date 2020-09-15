#!/usr/bin/node
/* add two numbers */
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  } else {
    return (a + b);
  }
}

console.log(add(a, b));
