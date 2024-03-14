const userDetailsArray = require("./userDetails.js").userDetailsArray;

console.log(userDetailsArray);

// Q.2 Get all addresses from userDetailsArray using reduce Function and return the result in the following format

// Response : 
// {
//     600dc3b5d617e547a0e74cb9: {
//         streetAddress: '48 Flatlands Avenue',
//             neighbour: 'Cutter',
//                 city: 'North Dakota'
//     },
//     600dc3b5c4e60ba2ebf06569: {
//         streetAddress: '77 Hemlock Street',
//             neighbour: 'Hasty',
//                 city: 'Florida'
//     }

// }