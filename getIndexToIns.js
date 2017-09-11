function getIndexToIns(arr, num) {
  // Find my place in this sorted array.

  // required to get JS to sort 10 higher than 2
  function sortNumber(a,b) {
    return a - b;
}

  var std = arr.sort(sortNumber);

  if (num > std[arr.length-1]) {
    return arr.length;
  }

  for (var i = 0; i < arr.length; i ++) {
    if (num > std[i]) {
      continue;
    } else {
      return i;
    }
  }
}

getIndexToIns([40, 60], 50); // 1
getIndexToIns([2, 20, 10], 19); // 2