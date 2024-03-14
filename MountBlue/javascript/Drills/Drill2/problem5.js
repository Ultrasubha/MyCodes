// ==== Problem #5 ====
// The car lot manager needs to find out how many cars are older than the year 2000. Using the array you just obtained from the previous problem, find out how many cars were made before the year 2000 and return the array of older cars and log its length.

let inventory = require("../inventory").inventory;
let carYears = require("./problem4.js").carYears(inventory);

function oldCarsCount(carYears) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(carYears) || carYears.length === 0) {
    throw new Error("Invalid carYears. It must be a non-empty array.");
  }

  return carYears.reduce((acc, curr) => {return (curr < 2000 ? acc + 1 : acc)}, 0);
}

function oldCars(inventory) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }

  return inventory
    .map((x) => {return (x.car_year < 2010 ? x.car_make + " " + x.car_model : null)})
    .filter((x) => {return x !== null});
}

module.exports.oldCars = oldCars(inventory);
module.exports.oldCarsCount = oldCarsCount(carYears);
