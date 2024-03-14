function each(elements, callBack) {
  // Check if elements is an array and callBack is a function
  if (!Array.isArray(elements) || typeof callBack !== "function") {
    throw new Error(
      "Invalid arguments. The first argument must be an array, and the second argument must be a function."
    );
  }

  for (let index = 0; index < elements.length; index++) {
    // Check if callBack is a function before calling it
    if (typeof callBack !== "function") {
      throw new Error("Callback must be a function.");
    }

    callBack(elements[index], index);
  }
}

module.exports.each = each;
