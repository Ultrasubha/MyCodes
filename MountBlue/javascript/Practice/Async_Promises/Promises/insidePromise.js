const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Promise resolved!");
  }, 1000);
});

// Display Promise details
function displayPromiseDetails(promise) {
  console.log(`[[Prototype]]: ${Object.getPrototypeOf(promise)}`);

  if (promise instanceof Promise) {
    console.log(`[[PromiseState]]: ${promise._state}`);
    console.log(`[[PromiseResult]]: ${promise._result}`);
  } else {
    console.log("Not a valid Promise object");
  }
}

// Access internal properties using custom properties (Not recommended in production code)
myPromise._state = "pending";
myPromise._result = undefined;

// Display the details
displayPromiseDetails(myPromise);
