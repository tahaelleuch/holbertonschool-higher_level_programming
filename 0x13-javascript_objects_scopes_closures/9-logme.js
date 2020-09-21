#!/usr/bin/node
/* number */
let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
