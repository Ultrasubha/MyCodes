let items = require("../arrays.js").items;
let each = require("../each.js").each;

each(items, (element, index) => {
    console.log(`Element at index ${index}: ${element}`);
});