#!/usr/bin/node
/* get factorial */
const arg = process.argv[2];

function fact (arg) {
  if (isNaN(arg) || arg === 1 || arg === 0) {
    return (1);
  } else {
    return (arg * fact(arg - 1));
  }
}

console.log(fact(parseInt(arg)));
