#!/usr/bin/node
/* map */
const list = require('./100-data').list;
let map1 = list.map((i, index) => i * index);
console.log(list);
console.log(map1);
