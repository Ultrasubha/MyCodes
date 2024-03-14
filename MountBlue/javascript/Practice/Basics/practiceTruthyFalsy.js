/* Truthy Falsy */

function checkAllTruthyValues(value) {
  return (
    Boolean(value) ||
    (typeof value === "object" && Object.keys(value).length > 0) ||
    (typeof value === "string" && value.trim() !== "") ||
    (typeof value === "number" && !isNaN(value))
    // More to be added
  );
}

let truthyValue = [true, 1, "Hello", { key: "value" }];
let resultTruthy = checkAllTruthyValues(truthyValue);
console.log("All values truthy:", resultTruthy);

/*-----------------------------------------------------------------------------------------------------*/

function checkAllFalsyValues(value) {
  // Check for all types of falsy values
  return (
    !value ||
    value === false ||
    value === 0 ||
    value === "" ||
    value === null ||
    value === undefined ||
    (typeof value === "object" && Object.keys(value).length === 0) ||
    (typeof value === "number" && isNaN(value))
    // More to be added
  );
}

let falsyValue = [false, 0, "", null, undefined, NaN];
let resultFalsy = checkAllFalsyValues(falsyValue);
console.log("All values falsy:", resultFalsy);
