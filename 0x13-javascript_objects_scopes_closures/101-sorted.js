#!/usr/bin/node
/* sorted */
const dict = require('./101-data').dict;
const sorted = {};
for (const key in dict) {
  if (sorted[dict[key]] === undefined) {
    sorted[dict[key]] = [];
  }
  sorted[dict[key]].push(key);
}
console.log(sorted);
