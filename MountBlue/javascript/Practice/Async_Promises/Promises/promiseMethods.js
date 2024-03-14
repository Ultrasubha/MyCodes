// Promise.resolve
// Promise.reject
// Promise.all
// Promise.allSettled
// Promise.any
// Promise.race

Promise.all([
  Promise.resolve("Nikki Haley"),
  Promise.resolve("Donald Trump"),
  Promise.reject("Joe Biden"),
])
  .then((msg) => {
    console.log(`${msg} are presidential candidates`);
  })
  .catch((err) => {
    console.error(`${err} is too old to be president`);
  })
  .finally(() => console.log("All are trash"));

Promise.allSettled([Promise.resolve("resolved"), Promise.reject("reject")])
  .then((msg) => {
    console.log(msg);
  })
  .catch((err) => {
    console.error("Error : ", err);
  });

Promise.any([
  new Promise((resolve, reject) => {
    setTimeout(resolve("first finished in 2.5sec"), 2500);
  }),
  new Promise((resolve, reject) => {
    setTimeout(resolve("second finished in 1.5sec"), 1500);
  }),
  new Promise((resolve, reject) => {
    setTimeout(reject("third finished in 0.5sec"), 500);
  }),
  new Promise((resolve, reject) => {
    setTimeout(resolve("fourth finished in 3.5sec"), 3500);
  }),
])
  .then((msg) => {
    console.log(msg);
  })
  .catch((err) => {
    console.error(err);
  });
