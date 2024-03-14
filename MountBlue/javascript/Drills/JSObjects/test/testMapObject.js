let testObject = require("./testObject.js").testObject;
let mapObject = require("../mapObject.js").mapObject;
let uppercaseCallback = require("../mapObject.js").uppercaseCallback;

// Testing the function with the provided object and callback
const mappedObject = mapObject(testObject, uppercaseCallback);
console.log(mappedObject);
