#!/usr/bin/node
/* func */
exports.callMeMoby = (num, functionn) => {
  for (let i = 0; i < num; i++) {
    functionn();
  }
};
