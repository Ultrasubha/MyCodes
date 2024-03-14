let testObject = require("./testObject.js").testObject;
let keys = require("../keys.js").keys;

const objectKeys = keys(testObject);
console.log(objectKeys);
