// ==== Problem #3 ====
// The marketing team wants the car models listed alphabetically on the website. Execute a function to Sort all the car model names into alphabetical order and log the results in the console as it was returned.

let bubbleSort = require("./bubbleSort").bubbleSort;
let models = [];

function carModels(inventory) {
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }

  for (let car_id = 0; car_id < inventory.length; car_id++) {
    models.push(inventory[car_id].car_model);
  }

  bubbleSort(models);
  return models;
}
module.exports.carModels = carModels;
console.log(bubbleSort);
