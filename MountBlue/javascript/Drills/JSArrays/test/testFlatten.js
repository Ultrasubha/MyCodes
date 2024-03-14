let flatten = require("../flatten.js").flatten;

const nestedArray = [1, [2], [[3]], [[[4]]]];
const flattenedArray = flatten(nestedArray);

console.log(flattenedArray);
