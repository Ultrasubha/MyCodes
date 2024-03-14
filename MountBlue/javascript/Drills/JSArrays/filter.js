function filter(elements, callBack) {
  // Check if elements is an array and callBack is a function
  if (!Array.isArray(elements) || typeof callBack !== "function") {
    throw new Error(
      "Invalid arguments. The first argument must be an array, and the second argument must be a function."
    );
  }

  const result = [];
  for (let index = 0; index < elements.length; index++) {
    // Check if callBack is a function before using it
    if (typeof callBack !== "function") {
      throw new Error("Callback must be a function.");
    }

    if (callBack(elements[index])) {
      result.push(elements[index]);
    }
  }
  return result;
}

module.exports.filter = filter;
