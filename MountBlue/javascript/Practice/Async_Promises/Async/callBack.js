function outerFunction(callback) {
    // Invoke the callback function
    callback();
  
    // Modify a variable within the outer function
    let outerVariable = "Original Value";
    console.log("Before callback:", outerVariable);
  
    // Pass the variable to the callback function
    callback(outerVariable);
  
    console.log("After callback:", outerVariable);
  }
  
  function callbackFunction(value) {
    console.log("Inside callback:", value);
  
    // Modify the variable passed from the outer function
    if (typeof value !== 'undefined') {
      value = "Modified Value";
    }
  }
  
  // Call the outer function and pass the callback function
  outerFunction(callbackFunction);
  