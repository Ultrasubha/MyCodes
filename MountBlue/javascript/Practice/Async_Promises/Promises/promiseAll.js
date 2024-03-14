const p1 = new Promise((resolve, reject) => {
  resolve("Drill1");
});
const p2 = new Promise((resolve, reject) => {
  resolve("Drill2");
});
const p3 = new Promise((resolve, reject) => {
  resolve("Drill3");
});

Promise.all([p1, p2, p3]).then((msg) => {
  console.log(`Completed ${msg} as promised.`);
});
