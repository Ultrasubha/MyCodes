console.log(name);
var name = function (val) {
    return "hello " + val;
}
var fatArrow = (val) => val + ", Nake Benihime"
console.log(name("subho"));
console.log(fatArrow("Bankai"));

var arr = [1,2,3,4,5];
var squares = arr.map((x, i)=>x*x);
console.log(squares);
console.log(arr.slice(3))
arr.splice(1,3,'s','u','b')
console.log(arr)
arr3 = ["cat","dog"]
arr4=[].concat(arr,arr3);
console.log(arr4);
arr = [1,2,3,4,5];
var arr5=arr
arr5[1]='a'
console.log(arr);
arr10=[1,2,3]
arr11=[4,5,6]
arr12=[7,8,9]
arr13=[...arr10,...arr11,...arr12]
function addition(...other) {
    val=0
    for(i=0;i<other.length;i++) val+=other[i]
    return val
}
console.log(addition(...arr13));

var people = {
    name : 'Subhadeep',
    surname : "Mandal",
    fullname : this.name + ' ' + this.surname,
    age : 27,
    Gender : 'Male'
}

var keyArr = Object.keys(people)
var valArr = Object.values(people)
console.log(keyArr, valArr)

//setTimeout(()=>console.log("Hi"),3000)
///setInterval(()=>console.log("Subho"),1000)

var promise = new Promise((resolve,reject) => {})