function flatten(elements) {
  // Check if elements is an array
  if (!Array.isArray(elements)) {
    throw new Error("Invalid argument. The function expects an array.");
  }

  let result = [];

  for (let index = 0; index < elements.length; index++) {
    if (Array.isArray(elements[index])) {
      // Recursively flatten nested arrays
      result = result.concat(flatten(elements[index]));
    } else {
      result.push(elements[index]);
    }
  }

  return result;
}

module.exports.flatten = flatten;
