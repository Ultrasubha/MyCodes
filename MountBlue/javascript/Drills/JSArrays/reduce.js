function reduce(elements, callBack, startingValue) {
  // Check if elements is an array and callBack is a function
  if (!Array.isArray(elements) || typeof callBack !== "function") {
    throw new Error(
      "Invalid arguments. The first argument must be an array, and the second argument must be a function."
    );
  }

  // Check if startingValue is provided and elements is not empty
  if (startingValue === undefined && elements.length === 0) {
    throw new Error("Cannot reduce an empty array without an initial value.");
  }

  let result = startingValue !== undefined ? startingValue : elements[0];
  const startIndex = startingValue !== undefined ? 0 : 1;

  for (let index = startIndex; index < elements.length; index++) {
    result = callBack(result, elements[index], index, elements);
  }

  return result;
}

module.exports.reduce = reduce;
