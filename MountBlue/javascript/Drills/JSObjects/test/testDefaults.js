let testObject = require("./testObject.js").testObject;
let defaults = require("../defaults.js").defaults;

const defaultProperties = { age: 30, occupation: 'Superhero' };
const objectWithDefaults = defaults(testObject, defaultProperties);

console.log(objectWithDefaults);