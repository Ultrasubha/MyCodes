/* Object (Create, Read, Update operations):*/

/* Object.entries
Object.keys
Object.values
hasOwnProperty
Object.entries*/

const myObject = {
  a: 10,
  b: 5,
  c: 15,
  d: 8,
};

firstValue = myObject[Object.keys(myObject)[0]];
keys = Object.keys(myObject);
values = Object.values(myObject);
console.log(myObject.hasOwnProperty("a"), myObject.hasOwnProperty("z"));
entries = Object.entries(myObject).flat()

/* Object.create
Object.assign  */

const obj = {
  e:9,
  f:10,
  g:11,
  h:(x)=>console.log(`This is ${x}`)
}

combined = Object.assign(myObject, obj)
obj1 = Object.create(obj)
obj1.i = 13
obj.h("subho")

console.log(obj1)
