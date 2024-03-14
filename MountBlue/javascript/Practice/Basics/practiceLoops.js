/*Loops, for..of, for..in*/

// For
arr=[]
for(let i=0;i<5;i++){
    arr.push(i);
}

console.log(...arr);

// While
let i=0;
while(i<5){
    arr.pop()
    i++;
}

console.log(arr);

//For..of
arr = [9,8,7,6,5]
for(item of arr) {console.log(item)}

//For..in
obj = {
    a:1,
    b:2,
    c:3
};
for(key in obj) {console.log(key,obj[key])}

//For..each
arr.forEach(element => {
    console.log(element - 5)
});