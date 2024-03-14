let items = require("../arrays.js").items;
let reduce = require("../reduce.js").reduce;

// Example 1: Summing all elements
const sum = reduce(items, (accumulator, element) => accumulator + element, 0);
console.log(sum);

// Example 2: Multiplying all elements
const product = reduce(
  items,
  (accumulator, element) => accumulator * element,
  1
);
console.log(product);
