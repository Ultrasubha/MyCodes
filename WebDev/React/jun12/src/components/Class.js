class Student{
    constructor(){
        console.log("constructor");
    }
    hello(){
        console.log("hello Parent");
    }
    static adfar(){
        console.log("static");
    }
}

class Profile extends Student{
    constructor(){
        super();
        console.log("constructor child called");
        super.hello();
        
    }
};
let a = new Student();
a.hello();
Student.adfar();
var profile1 = new Profile();