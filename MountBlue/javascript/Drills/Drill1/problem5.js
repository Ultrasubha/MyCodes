// ==== Problem #5 ====
// The car lot manager needs to find out how many cars are older than the year 2000. Using the array you just obtained from the previous problem, find out how many cars were made before the year 2000 and return the array of older cars and log its length.

let inventory = require("../inventory").inventory;
let carYears = require("./problem4.js").carYears(inventory);

function oldCarsCount(carYears) {
  if (!Array.isArray(carYears) || carYears.length === 0) {
    throw new Error("Invalid carYears. It must be a non-empty array.");
  }

  let count = 0;

  for (idx = 0; idx < carYears.length; idx++) {
    if (carYears[idx] < 2000) {
      count++;
    }
  }

  return count;
}

function oldCars(inventory) {
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }

  cars = [];

  for (let car_id = 0; car_id < inventory.length; car_id++) {
    selectedCar = inventory[car_id];
    if (selectedCar.car_year < 2000) {
      cars.push(selectedCar.car_make + " " + selectedCar.car_model);
    }
  }

  return cars;
}

module.exports.oldCars = oldCars(inventory);
module.exports.oldCarsCount = oldCarsCount(carYears);
