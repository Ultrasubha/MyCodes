# DataTypes

## Primitive Data Types:

- They are immutable, meaning their values cannot be changed.
- They are passed by value.
- Examples: **Number, String, Boolean, Null, Undefined, NaN.**

## Non-Primitive (Object) Data Type:

- They are mutable, meaning their values can be changed.
- They are passed by reference.
- Examples: **Object, Array, Function.**

# Loops

To Iterate through an iterable entity.

## for
```javascript
    for (let i = 0; i < 5; i++) { console.log(i); }
    // Iterates from 0 to 4 with a step of 1.
```

## forEach
```javascript
    const arr = [1, 2, 3];
    arr.forEach(item => console.log(item));
    // Iterates through each element in the array.
```
## for .. in
```javascript
    const obj = { a: 1, b: 2, c: 3 };
    for (const key in obj) { console.log(key, obj[key]); }
    // Iterates over the keys of an object.
```
## for .. of
```javascript
    const arr = [1, 2, 3];
    for (const item of arr) { console.log(item); }
    // Iterates over the values of an iterable (e.g., array).
```
## while
```javascript
    let i = 0;
    while (i < 5) { console.log(i); i++; }
    // Executes a block of code while a condition is true.
```

# Methods

## Mutable and Immutable Methods

- **Strings (Immutable):**
```javascript
    const str = "Hello";
    const newStr = str.concat(" World");
    console.log(str, newStr);
    // Strings are immutable, so concat creates a new string.

```

- **Arrays (Mutable):**
```javascript
const arr = [1, 2, 3];
arr.push(4);
console.log(arr);
// Arrays are mutable, push modifies the original array.

```

## Pass by Value (Primitive types)
```javascript
let a = 5;
let b = a;
b = 10;
console.log(a, b);
// Changes to 'b' don't affect the value of 'a'.

```
## Pass by Reference (Objects/Arrays)
```javascript
const arr1 = [1, 2, 3];
const arr2 = arr1;
arr2.push(4);
console.log(arr1, arr2);
// Both arr1 and arr2 refer to the same array in memory.

```

## Basic Array methods

- **Array.pop**
```javascript
    const arr = [1, 2, 3];
    const poppedItem = arr.pop();
    console.log(arr, poppedItem);
    // Removes and returns the last element of the array.

```

- **Array.push**
```javascript
    const arr = [1, 2, 3];
    arr.push(4);
    console.log(arr);
    // Adds one or more elements to the end of the array.

```

- **Array.concat**
```javascript
    const arr1 = [1, 2];
    const arr2 = [3, 4];
    const concatenatedArr = arr1.concat(arr2);
    console.log(concatenatedArr);
    // Combines two or more arrays and returns a new array.

```

- **Array.slice**
```javascript
    const arr = [1, 2, 3, 4, 5];
    const slicedArr = arr.slice(1, 4);
    console.log(slicedArr);
    // Returns a shallow copy of a portion of the array.

```

- **Array.splice**
```javascript
    const arr = [1, 2, 3, 4, 5];
    const removedItems = arr.splice(1, 2);
    console.log(arr, removedItems);
    // Changes the contents of an array by removing or replacing existing elements.

```

- **Array.join**
```javascript
    const arr = ["apple", "banana", "orange"];
    const joinedString = arr.join(", ");
    console.log(joinedString);
    // Joins all elements of an array into a string, separated by the specified separator.

```

- **Array.flat**
```javascript
    const nestedArr = [1, [2, 3], [4, [5, 6]]];
    const flattenedArr = nestedArr.flat(2);
    console.log(flattenedArr);
    // Flattens a nested array by a specified depth.

```

### Finding:

- **Array.find**
```javascript
    const arr = [1, 2, 3, 4, 5];
    const foundItem = arr.find(item => item > 2);
    console.log(foundItem);
    // Returns the first element in the array that satisfies the provided testing function.

```

- **Array.indexOf**
```javascript
    const arr = [1, 2, 3, 4, 5];
    const index = arr.indexOf(3);
    console.log(index);
    // Returns the first index at which a given element is found in the array, or -1 if not present.

```

- **Array.includes**
```javascript
    const arr = [1, 2, 3, 4, 5];
    const includesItem = arr.includes(3);
    console.log(includesItem);
    // Determines whether an array includes a certain element, returning true or false.

```

- **Array.findIndex**
```javascript
    const arr = [1, 2, 3, 4, 5];
    const index = arr.findIndex(item => item > 2);
    console.log(index);
    // Returns the index of the first element in the array that satisfies the provided testing function, or -1 if not found.

```

### Higher Order Functions:

- **Array.forEach**
```javascript
    const arr = [1, 2, 3];
    arr.forEach(item => console.log(item));
    // Executes a provided function once for each array element.

```
- **Array.filter**
```javascript
    const arr = [1, 2, 3, 4, 5];
    const filteredArr = arr.filter(item => item % 2 === 0);
    console.log(filteredArr);
    // Creates a new array with elements that pass the test implemented by the provided function.

```

- **Array.map**
```javascript
    const arr = [1, 2, 3];
    const doubledArr = arr.map(item => item * 2);
    console.log(doubledArr);
    // Creates a new array with the results of calling a provided function on every element in the array.

```
- **Array.reduce**
```javascript
    const arr = [1, 2, 3, 4, 5];
    const sum = arr.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    console.log(sum);
    // Applies a function against an accumulator and each element in the array to reduce it to a single value.
```
- **Array.sort**
```javascript
    const arr = [3, 1, 4, 1, 5, 9, 2, 6];
    arr.sort((a, b) => a - b);
    console.log(arr);
    // Sorts the elements of an array in place based on a provided function.

```

## Advanced Array methods:
- **chaining**
```javascript
    const numbers = [1, 2, 3, 4, 5];

    const result = numbers
    .filter(item => item % 2 === 0) // Keep only even numbers
    .map(item => item * 2)           // Double each remaining number
    .reduce((sum, current) => sum + current, 0);  // Sum the doubled numbers

    console.log(result);
    // Chaining higher-order functions to filter, map, and reduce the array in a single operation.

```

## String methods
```javascript
    const str = "   Hello, World!   ";

    // String length
    const length = str.length;

    // String charAt()
    const charAt3 = str.charAt(3);

    // String charCodeAt()
    const charCodeAt3 = str.charCodeAt(3);

    // String at() - (Not a standard method as of my knowledge cutoff in Jan 2022)
    const atIndex3 = str.at(3);

    // String [ ]
    const bracketAt3 = str[3];

    // String slice()
    const slicedString = str.slice(3, 8);

    // String substring()
    const substring = str.substring(3, 8);

    // String substr()
    const substr = str.substr(3, 5);

    // String toUpperCase()
    const upperCaseString = str.toUpperCase();

    // String toLowerCase()
    const lowerCaseString = str.toLowerCase();

    // String concat()
    const concatenatedString = str.concat(" Welcome");

    // String trim()
    const trimmedString = str.trim();

    // String trimStart() - (Not a standard method as of my knowledge cutoff in Jan 2022)
    const trimStartString = str.trimStart();

    // String trimEnd() - (Not a standard method as of my knowledge cutoff in Jan 2022)
    const trimEndString = str.trimEnd();

    // String padStart()
    const paddedStartString = str.padStart(20, "*");

    // String padEnd()
    const paddedEndString = str.padEnd(20, "*");

    // String repeat()
    const repeatedString = str.repeat(2);

    // String replace()
    const replacedString = str.replace("Hello", "Hi");

    // String replaceAll() - (Introduced in ECMAScript 2021)
    const replacedAllString = str.replaceAll("o", "0");

    // String split()
    const splitArray = str.split(",");
```

## Object methods & operations

### Mutable Object:
```javascript
    let mutableObject = { key: "value" };
    mutableObject.key = "new value";  // Mutating the object
    console.log(mutableObject);  // Outputs: { key: "new value" }
```
In this example, the object **mutableObject** is mutable because we can change the value of its property key after the object is created.

### Immutable Object:
```javascript
    const immutableObject = Object.freeze({ key: "value" });

    // Trying to mutate the frozen object will result in an error
    // immutableObject.key = "new value"; // Error: Cannot assign to read-only property 'key' of object

    console.log(immutableObject);  // Outputs: { key: "value" }
```
In this example, the object **immutableObject** is made immutable by using **Object.freeze()**. Any attempt to modify the object, such as changing the value of its property, will result in an error. The object remains unchanged, maintaining its initial state.

# Hoisting
```javascript
console.log(x); // Outputs: undefined
var x = 5;
console.log(x); // Outputs: 5
// Variables using 'var' are hoisted to the top of their scope, but only the declaration, not the initialization.

```
# Scopes
```javascript
function exampleScope() {
  var a = 5;           // Has function scope and can be reassigned.
  let b = "Hello";     // Has block scope and can be reassigned.
  const c = [1, 2, 3];  // Has block scope and cannot be reassigned.

  if (true) {
    var a = 10;         // This reassigns the outer 'a'.
    let b = "World";   // This creates a new 'b' with block scope.
    const c = [4, 5, 6]; // This creates a new 'c' with block scope.

    console.log(a, b, c); // Outputs: 10, "World", [4, 5, 6]
  }

  console.log(a, b, c);   // Outputs: 10, "Hello", [1, 2, 3]
}

exampleScope();
```
- **var** has function scope and can be reassigned throughout the function.
- **let** has block scope and can be reassigned within the block where it's defined.
- **const** has block scope and cannot be reassigned after initialization within the block where it's defined.

# Closures
```javascript
    function outer() {
    let outerVar = "I am outside";
    function inner() {
        console.log(outerVar);
    }
    return inner;
    }
    const closureExample = outer();
    closureExample(); // Outputs: I am outside
    // Closures allow inner functions to access the scope of their outer functions even after the outer function has finished executing.

```

# Best Practices
- Use **const** for variables that don't need to be reassigned.
- Prefer **let** over **var** to avoid unintended hoisting issues.
- Use arrow functions for concise and clear syntax.
- Use template literals for string interpolation.

# Debugging
- Use **console.log** or breakpoints for basic debugging.
- Utilize browser developer tools or a debugger for more complex issues.
- Step through code and inspect variables to identify problems.

# Throw new Error vs Throw someObject

## Throw new Error
- When you use throw new Error, you are explicitly creating and throwing an Error object.
- This is commonly used for throwing custom error messages or signaling exceptional conditions.
- The Error object can contain a message property, providing information about the error.

```javascript
    throw new Error("This is a custom error message");
```
## Throw someObject
- When you use throw someObject, you are throwing an existing object (which can be of any type, not necessarily an Error object).
- This is often used to propagate specific types of errors or objects that represent exceptional conditions.
- The object being thrown may contain additional information or properties related to the error.

```javascript
    const customErrorObject = { code: 500, message: "Server error" };
    throw customErrorObject;
```