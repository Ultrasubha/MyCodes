// ==== Problem #6 ====
// A buyer is interested in seeing only BMW and Audi cars within the inventory.  Execute a function and return an array that only contains BMW and Audi cars.  Once you have the BMWAndAudi array, use JSON.stringify() to show the results of the array in the console.

function BMWAndAudi(inventory) {
  // Check if inventory is an array and has elements
  if (!Array.isArray(inventory) || inventory.length === 0) {
    throw new Error("Invalid inventory. It must be a non-empty array.");
  }
  
  return inventory.map(car_id => {
    carBrand = car_id.car_make;
    model = car_id.car_model;
    if (carBrand == "BMW" || carBrand == "Audi") {
      return (carBrand + " " + model);
    }
  }).filter((x) => { return x !== undefined})
}

module.exports.BMWAndAudi = BMWAndAudi;
