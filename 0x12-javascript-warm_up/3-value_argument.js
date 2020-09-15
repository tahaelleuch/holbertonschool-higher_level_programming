#!/usr/bin/node
/* handling argumenmts */
const ar = process.argv[2];
if (ar) {
  console.log(ar)
} else {
  console.log('No argument');
}
