#!/usr/bin/node
/* print a scare */
const arg = process.argv[2];
if (arg) {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}
