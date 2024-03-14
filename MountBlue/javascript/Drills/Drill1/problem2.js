// ==== Problem #2 ====
// The dealer needs the information on the last car in their inventory. Execute a function to find what the make and model of the last car in the inventory is?  Log the make and model into the console in the format of:

function lastCar(inventory) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }

  len = inventory.length;
  
  return (
    "Last car is a " +
    inventory[len - 1].car_make +
    " " +
    inventory[len - 1].car_model
  );
}

module.exports.lastCar = lastCar;
