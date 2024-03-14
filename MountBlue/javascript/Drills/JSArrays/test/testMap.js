let items = require("../arrays.js").items;
let map = require("../map.js").map;

const mappedArray = map(items, (element) => element * 2);
console.log(mappedArray);
