let testObject = require("./testObject.js").testObject;
let invert = require("../invert.js").invert;

const invertedObject = invert(testObject);

console.log(invertedObject);
