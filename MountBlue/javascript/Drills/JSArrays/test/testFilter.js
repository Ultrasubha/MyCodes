let items = require("../arrays.js").items;
let filter = require("../filter.js").filter;

// Example: Filter even numbers
const filteredEven = filter(items, (element) => element % 2 === 0);
console.log(filteredEven);

// Example: Filter numbers greater than 3
const filteredGreaterThan3 = filter(items, (element) => element > 3);
console.log(filteredGreaterThan3);