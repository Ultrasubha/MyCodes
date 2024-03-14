let testObject = require("./testObject.js").testObject;
let pairs = require("../pairs.js").pairs;

// Testing the function with the provided object
const result = pairs(testObject);
console.log(result);