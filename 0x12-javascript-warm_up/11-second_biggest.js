#!/usr/bin/node
/* second biggest */
const args = process.argv.slice(2);
let secndbig = 0;
let biggest = 0;
for (const i in args) {
  if (isNaN(args[i])) {
    continue;
  }
  if (parseInt(args[i]) > biggest) {
    secndbig = biggest;
    biggest = parseInt(args[i]);
  }
  if (biggest > parseInt(args[i]) && parseInt(args[i]) > secndbig) {
    secndbig = parseInt(args[i]);
  }
}
console.log(secndbig);
