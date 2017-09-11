
function destroyer(arr) {
  // Remove all the values


  var args = Array.prototype.slice.call(arguments);


  var lst = args[0]; // array to check
  var toRemove = args.slice(1); // array of things to exclude


  return arr.filter(function(val) {
    return !toRemove.includes(val);
  });

}

destroyer([1, 2, 3, 1, 2, 3], 2, 3); // [1, 1]
destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3); // [1, 5, 1]