function divideNumbers(a, b) {
    try {
      if (b === 0) {
        throw new Error("Cannot divide by zero!");
      }
  
      const result = a / b;
      console.log(`Result of ${a} divided by ${b}: ${result}`);
      return result;
    } catch (error) {
      console.error(`Error: ${error.message}`);
      // You can choose to re-throw the error if needed
      // throw error;
    } finally {
      console.log("This block always executes, regardless of whether there was an error or not.");
    }
  }
  
  // Example usage:
  divideNumbers(10, 2); // Outputs: "Result of 10 divided by 2: 5"
  divideNumbers(8, 0);  // Outputs: "Error: Cannot divide by zero!" and "This block always executes, regardless of whether there was an error or not."
  divideNumbers(12, 3); // Outputs: "Result of 12 divided by 3: 4" and "This block always executes, regardless of whether there was an error or not."
  