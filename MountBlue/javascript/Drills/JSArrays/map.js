function map(elements, callBack) {
  // Check if elements is an array and callBack is a function
  if (!Array.isArray(elements) || typeof callBack !== "function") {
    throw new Error(
      "Invalid arguments. The first argument must be an array, and the second argument must be a function."
    );
  }

  const result = [];

  for (let index = 0; index < elements.length; index++) {
    result.push(callBack(elements[index], index));
  }

  return result;
}

module.exports.map = map;
