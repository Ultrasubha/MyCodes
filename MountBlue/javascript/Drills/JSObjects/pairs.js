//Instead of return Object.entries(obj);
function pairs(obj) {
  // Check if obj is an object
  if (typeof obj !== "object" || obj === null) {
    throw new Error("Invalid argument. The function expects an object.");
  }

  const result = [];

  // Iterate over the properties of obj
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      // Create an array of key-value pairs
      result.push([key, obj[key]]);
    }
  }

  return result;
}

module.exports.pairs = pairs;
