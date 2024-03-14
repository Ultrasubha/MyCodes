function mapObject(obj, callBack) {
  // Check if obj is an object
  if (typeof obj !== "object" || obj === null) {
    throw new Error("Invalid argument. The function expects an object.");
  }

  // Check if callBack is a function
  if (typeof callBack !== "function") {
    throw new Error("Invalid callback. The callback must be a function.");
  }

  const result = {};

  // Iterate over the properties of obj
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      // Apply the callback function to the value
      result[key] = callBack(obj[key]);
    }
  }

  return result;
}

// callback function: values to uppercase
function uppercaseCallback(value) {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else {
    return value;
  }
}

module.exports.mapObject = mapObject;
module.exports.uppercaseCallback = uppercaseCallback;
