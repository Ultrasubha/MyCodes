# Asynchronous-javascript

## Callbacks
**Definition:** Callbacks are functions that are passed as arguments to another function and are executed after the completion of some asynchronous operation or task.
<br>

**Example:**

```javascript
function fetchData(callback) {
    // Simulating an asynchronous operation, like fetching data from a server
    setTimeout(function () {
        const data = "This is the fetched data";
        // Calling the callback function with the fetched data
        callback(data);
    }, 2000);
}

// Using the callback function
fetchData(function (result) {
    console.log(result); // Output: This is the fetched data
});
```

## Promises
**Definition:** Promises are javascript placeholder objects that represents the eventual completion of an asynchronous javascript operation.<br>
It has 3 states.
- *pending*
- *fulfilled*
- *rejected*
<br>
A promise object contains information regarding 3 things.

- *promiseType*
- *promiseState*
- *promiseValue*

**Example:**

```javascript
function fetchData() {
    // Simulating an asynchronous operation, like fetching data from a server
    return new Promise(function (resolve, reject) {
        setTimeout(function () {
            const data = "This is the fetched data";
            // Resolving the promise with the fetched data
            resolve(data);
        }, 2000);
    });
}

// Using the promise
fetchData()
    .then(function (result) {
        console.log(result); // Output: This is the fetched data
    })
    .catch(function (error) {
        console.error(error);
    });
```

## Code Control

- **Inversion of Control with Callbacks:** 
For the 1st example, **fetchData** is a function that performs an *asynchronous operation*, and it takes a callback function (processData) as an argument. The control is inverted because fetchData decides when to call the callback, giving control to the asynchronous operation.

- **Using Promises to Solve Inversion of Control:** 
For Promises we can see, fetchData returns a promise. The control is inverted to the consumer of the promise, allowing them to use .then() to handle the asynchronous result. This way, the consumer has more control over how to handle the data when it becomes available, and it avoids the callback-based inversion of control.