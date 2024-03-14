function invert(obj) {
  // Check if obj is an object
  if (typeof obj !== "object" || obj === null) {
    throw new Error("Invalid argument. The function expects an object.");
  }

  const invertedObject = {};

  // Iterate over the properties of obj
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      // Check if the value is not an object to avoid prototype chain properties
      if (typeof obj[key] !== "object" || obj[key] === null) {
        invertedObject[obj[key]] = key;
      }
    }
  }

  return invertedObject;
}

module.exports.invert = invert;
