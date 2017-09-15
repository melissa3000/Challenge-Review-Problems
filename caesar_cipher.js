
function rot13(str) { // LBH QVQ VG!
  // go back and refactor using map

  var midPoint = [];
  var result = "";
  var translate = [];
  var punctuation = [32, 46, 33, 63];

  for (var i = 0; i < str.length; i ++) {
    midPoint.push(str.charCodeAt(i));
    }

  for (var k = 0; k < midPoint.length; k ++){
    if (punctuation.indexOf(midPoint[k]) > -1) {
      translate.push(midPoint[k]);
    } else if (midPoint[k] <= 77) {
    translate.push(midPoint[k] + 13);
    }  else {
      translate.push(midPoint[k] - 13);
    }
  }

  for (var j = 0; j < translate.length; j ++){
    result += String.fromCharCode(translate[j]);
  }

  return result;
}

// Change the inputs below to test
rot13("SERR PBQR PNZC"); // FREE CODE CAMP
