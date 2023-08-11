import UIKit

//OPTIONAL & FORCED UNWRAPPING
var s1:String?
s1="fg"
print(s1!)

var ar2:[String]?
ar2=["red","blue"]
print(ar2!)

var r:Int?
r=90
if let a=r{
    print(a)
}

//UNDERSCORE PARAMETER
class Person {
    var age:Int?
    var name:String?
    func set(_ a:Int, _ n:String) {
        age = a
        name = n
    }
    func show() -> String {
        return String(age!) + name!
    }
}

var p = Person()
p.set(61,"subho")
print(p.show())

//CLOSURE
var sum = {(a:Int, b:Int) -> Int in return a + b }
print(sum(2,3))

//CLOSURE AS FUNCTION PARAM
func set(_ a1:Int, _ a2:Int, S:(Int,Int) -> Int) -> Int {
    return S(a1, a2)
}
print(set(23, 21, S:sum))

//TUPLE
var tuple = (101,"lpu","GT road")
print("This is \(tuple.0)", tuple.1)

