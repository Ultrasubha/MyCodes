values = require("../values.js").values;
let testObject = require("./testObject.js").testObject;

testObject.sayHello = function() {
  console.log('Hello!');
};

const objectValues = values(testObject);
console.log(objectValues);
