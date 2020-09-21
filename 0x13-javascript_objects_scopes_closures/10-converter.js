#!/usr/bin/node
/* base exporter */
exports.converter = function (base) {
  function conv (number) {
    return number.toString(base);
  }
  return conv;
};
