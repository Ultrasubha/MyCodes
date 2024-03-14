function delay(time, car) {
  return new Promise((resolve) => setTimeout(()=>resolve(car), time));
}

car1 = delay(2000, "car1");
car2 = delay(500, "car2");
car3 = delay(1000, "car3");

Promise.race([car1, car2, car3]).then((msg) =>
  console.log(`winner is : ${msg}`)
);
