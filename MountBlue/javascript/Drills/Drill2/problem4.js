// ==== Problem #4 ====
// The accounting team needs all the years from every car on the lot. Execute a function that will return an array from the dealer data containing only the car years and log the result in the console as it was returned.
// function removeDuplicates(arr) {
//   return [...new Set(arr)];
// }

let bubbleSort = require("./bubbleSort").bubbleSort;
let years = [];

function carYears(inventory) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }
  
  years = inventory.map((carData) => {
    return carData.car_year;
  });
  bubbleSort(years);
  return years;
}
module.exports.carYears = carYears;
