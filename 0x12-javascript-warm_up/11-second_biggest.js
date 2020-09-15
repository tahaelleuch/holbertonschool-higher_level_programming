#!/usr/bin/node
/* second biggest */
let args = process.argv.slice(2);
let secnd_big = 0;
let biggest = 0;
for (const i in args) {
  if (parseInt(args[i]) > biggest) {
    secnd_big = biggest;
    biggest = parseInt(args[i]);
  }
}
console.log(secnd_big);
