// ==== Problem #1 ====
// The dealer can't recall the information for a car with an id of 33 on his lot. Help the dealer find out which car has an id of 33 by calling a function that will return the data for that car. Then log the car's year, make, and model in the console log in the format of:

function findCarDetails(inventory,targetCarId) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }

  for (let car_id = 0; car_id < inventory.length; car_id++) {

    if (car_id == targetCarId - 1) {
      return (
        "Car 33 is a " +
        inventory[car_id].car_year +
        " " +
        inventory[car_id].car_make +
        " " +
        inventory[car_id].car_model
      );
    }
  }
  
  return `Car with ID ${targetCarId} not found in inventory`;
}

module.exports.findCarDetails = findCarDetails;
