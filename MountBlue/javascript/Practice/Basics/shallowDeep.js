const originalArray = [1, 2, [3, 4]];

// Shallow copy using spread operator
const shallowCopy = [...originalArray];

// Modifying the nested array in the shallow copy
shallowCopy[2][0] = 99;

console.log(originalArray);   // Output: [1, 2, [99, 4]]


const arr = [1, 2, [3, 4]];

// Deep copy using a function (e.g., JSON.parse and JSON.stringify)
const deepCopy = JSON.parse(JSON.stringify(arr));

// Modifying the nested array in the deep copy
deepCopy[2][0] = 99;

console.log(arr);   // Output: [1, 2, [3, 4]]
