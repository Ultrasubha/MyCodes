// ==== Problem #2 ====
// The dealer needs the information on the last car in their inventory. Execute a function to find what the make and model of the last car in the inventory is?  Log the make and model into the console in the format of:

// DESIRED OUTPUT : Last car is a Lincoln Town Car

function lastCar(inventory) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }

  return inventory.reduce((lastCar, carInfo) => {
    return carInfo.id == inventory.length
      ? "Last car is a " + carInfo.car_make + " " + carInfo.car_model
      : lastCar;
  }, {});
}

module.exports.lastCar = lastCar;
