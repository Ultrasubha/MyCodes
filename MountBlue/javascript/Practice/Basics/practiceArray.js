/* Arrays (Create, Read, Update operations) :*/ 

/* 
join
flat
push
pop
slice
splice
*/

const nestedArr = [1, [2, 3], [4, [5, 6]]];
arr = nestedArr.flat(2)
arr.push(7)
arr.splice(2,2,42,23)
arr = arr.slice(0,3)
arr.pop()
s = arr.join(":")
s += " -> After Mult : "

/*
forEach
map
reduce
some
every
filter
reverse
*/
arr.forEach(element => {
    s+=(element * 2).toString()
});

arr = arr.map((x) => x*3)
product = arr.reduce((acc,curr) => acc*curr ,1)
filtrate = arr.filter((x)=>x%2 == 0)
atleast = arr.some((x)=>x%4 == 0)
atAll = arr.every((x)=>x%4 == 0)
arr.reverse()

arr = [...arr , ...[4,5,6,7]]

/*
indexOf
lastIndexOf
findIndex
includes
find
*/

console.log(arr.indexOf(6))
console.log(arr.lastIndexOf(6))
console.log(arr.findIndex((x)=> x>9))
console.log(arr.includes(6))
console.log(arr.find(x=> x==5))

/* 
shift
unshift 
*/

shifted = arr.shift()
arr.unshift(2)
console.log(arr)