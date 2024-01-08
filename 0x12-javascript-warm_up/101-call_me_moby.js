#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (x; x > 0; x--) {
    theFunction();
  }
};
