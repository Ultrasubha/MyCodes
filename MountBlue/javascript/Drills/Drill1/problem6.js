// ==== Problem #6 ====
// A buyer is interested in seeing only BMW and Audi cars within the inventory.  Execute a function and return an array that only contains BMW and Audi cars.  Once you have the BMWAndAudi array, use JSON.stringify() to show the results of the array in the console.

function BMWAndAudi(inventory) {
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }

  cars = [];
  
  for (let car_id = 0; car_id < inventory.length; car_id++) {
    carBrand = inventory[car_id].car_make;
    model = inventory[car_id].car_model;
    if (carBrand == "BMW" || carBrand == "Audi") {
      cars.push(carBrand + " " + model);
    }
  }
  return cars;
}

module.exports.BMWAndAudi = BMWAndAudi;
