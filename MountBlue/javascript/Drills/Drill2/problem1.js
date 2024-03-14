// ==== Problem #1 ====
// The dealer can't recall the information for a car with an id of 33 on his lot. Help the dealer find out which car has an id of 33 by calling a function that will return the data for that car. Then log the car's year, make, and model in the console log in the format of:

// DESIRED OUTPUT : Car 33 is a 1991 Ford Escort

function findCarDetails(inventory) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }

  return inventory.reduce((targetCar, carInfo) => {
    return carInfo.id == 33
      ? "Car 33 is a " +
          carInfo.car_year +
          " " +
          carInfo.car_make +
          " " +
          carInfo.car_model
      : targetCar;
  }, {});
}
module.exports.findCarDetails = findCarDetails;
