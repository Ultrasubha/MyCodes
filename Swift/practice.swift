import UIKit

var num = 10

switch num {
    case 1:
        print("asd")
case 10,15:
    print("good num")
default:
    print("nothing")
}

enum races {
    case Indian, American, Japanese
}

enum direction {
    case north
    case south
    case east
    case west
}
print(direction.south)

var s=""
var dir = direction.south
switch dir {
    case .north:
        s="For the king in the north"
    case .south:
        s="For the ales of south"
    case .east:
        s="For the dothraki in the east"
    case .west:
        s="For the Lannisters of the west"
}
print(s)

struct Person {
    var name=""
    mutating func setName(n:String){
        name = n
    }
    func getName()->String{
        return name
    }
}
var p = Person()
p.setName(n:"Subho")
print(p.getName())*/
struct check {
    private var name = "value"
    init(){
        print("Mirai e yokoso")
    }
    init(n:String,posi:Int){
        name = "I am " + n + " no."+String(posi)+" pirate"
    }
    func getName()->String{
        return name
    }
}
var c = check()
var ck = check(n:"shirohige",posi:1)
print(ck.getName())

/*class Animal{
    var animal:String
    init(animal:String){
        self.animal = animal
        print(animal)
    }
}

class fourLegged:Animal {
    var legs:Int
    init(legs:Int, animal:String){
        self.legs = legs
        self.animal = animal
        //super.init(animal:"cow")
        print(legs)
    }
}

//var animal1 = Animal(animal:"cow")
var legs = fourLegged(legs:4, animal:"cow")*/

class Person{
    var name:String
    var age:Int
    init(n:String, a:Int){
        name = n
        age = a
    }
    func show(){
        print(name, age)
    }
}
class Student:Person{
    var reg:Int

    init(R:Int, n:String, a:Int){
        reg = R
        super.init(n:n,a:a)
    }
    override func show(){
        print(reg,name,age)
    }
}

Student(R:12006389,n:"Subhadeep",a:27).show()
