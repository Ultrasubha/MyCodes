let items = require("../arrays.js").items;
let find = require("../find.js").find;

// Example 1: Find the first even number
const foundEven = find(items, (element) => element % 2 === 0);
console.log(foundEven);

// Example 2: Find the first element greater than 5
const foundGreaterThan5 = find(items, (element) => element > 5);
console.log(foundGreaterThan5);
