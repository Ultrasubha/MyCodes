function values(obj) {
  // Check if obj is an object
  if (typeof obj !== "object" || obj === null) {
    throw new Error("Invalid argument. The function expects an object.");
  }

  const result = [];

  // Iterate over the properties of obj
  for (let key in obj) {
    if (obj.hasOwnProperty(key) && typeof obj[key] !== "function") {
      // Push the value to the result array
      result.push(obj[key]);
    }
  }

  return result;
}

module.exports.values = values;
