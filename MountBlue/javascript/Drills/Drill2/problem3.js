// ==== Problem #3 ====
// The marketing team wants the car models listed alphabetically on the website. Execute a function to Sort all the car model names into alphabetical order and log the results in the console as it was returned.

let bubbleSort = require("./bubbleSort").bubbleSort;
let models = [];

function carModels(inventory) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }
  
  models = inventory.map((carData) => {
    return carData.car_model;
  });
  bubbleSort(models);
  return models;
}
module.exports.carModels = carModels;
