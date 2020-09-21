#!/usr/bin/node
/* create square class */
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
