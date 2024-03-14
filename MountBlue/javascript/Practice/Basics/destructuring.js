const bc = {
  a: "asd",
  b: 12,
  c: { n: 34, j: 8 },
};
const {
  a,
  b,
  c: { n: inner1, j: inner2 },
} = bc;
//console.log(inner1)

function swapping(x, y) {
  return ([x, y] = [y, x]);
}

const users = [{ id: 1 }, { id: 2 }, { id: 3 }];

// for ({id} of users) {
//     console.log(id);
// }

const rando = "hello";
const obj = {
  [rando]: 23,
  "kol" : 12
};

const {[rando]:subho} = obj
console.log(subho)