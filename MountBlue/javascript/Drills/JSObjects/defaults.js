function defaults(obj, defaultProps) {
  // Check if obj and defaultProps are objects
  if (typeof obj !== "object" || typeof defaultProps !== "object") {
    throw new Error("Invalid arguments. Both arguments must be objects.");
  }

  for (let defaultKey in defaultProps) {
    if (defaultProps.hasOwnProperty(defaultKey)) {
      let objKeyExists = false;

      // Check if obj has the key
      for (let objKey in obj) {
        if (obj.hasOwnProperty(objKey) && objKey === defaultKey) {
          objKeyExists = true;
          break;
        }
      }

      // If obj doesn't have the key or the value is undefined, assign the default value
      if (!objKeyExists || obj[defaultKey] === undefined) {
        obj[defaultKey] = defaultProps[defaultKey];
      }
    }
  }

  return obj;
}

module.exports.defaults = defaults;
