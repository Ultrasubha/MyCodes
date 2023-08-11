import UIKit

var str = "Hello, playground"
print(str)
var vl:Set <Int> = []
vl.insert(13)
vl.insert(90)
vl.insert(13)
print(vl)

var age:Int = 2
switch (age) {
case 1:
    print("BABY")
case 2...10:
    print("child")
case 1...17:
    print("underaged")
case 18,19:
    print("can vote")
default:
    print("vote vote")
}
var a:Int?
print(a)
a = 5
print(3+a!)
var b:Int? = 90
print(b)
print(b!)

//functions

func add(a:Int, b:Int) -> Int
{
    var c = a + b
    print(c)
    return c
    
}
add(a:4,b:5)

func sub(_ a:Int, _ b:Int = 90) -> Int
{
    let c = a - b
    return c
}

sub(3,2)
sub(9)

class mobile
{
    var brand:String?
    var price:Int
    init(price:Int)
    {
        self.price = price
    }
    
}
var obj = mobile(price:0)

print(obj.brand)
print(obj.price)

var roll:[Int] = [2,4,6,8]
print("Array : \(roll)")

var someints = [Int]()
someints.append(34)
someints.append(78)
someints+=[40]

print(someints[0])
print(someints[1])

var item = [String]()
item+=["apple"]
item+=["banana"]
item.append("honey")

for x in item
{
    print(x)
}

var somestr = [String]()
print("total item in item is \(item.count)")
print("in somestr is \(somestr.count)")
print("is empty \(item.isEmpty)")
print("is empty \(somestr.isEmpty)")

var val = [String]()
val.append("po")
val += ["pi"]
val.append("py")

for(index,item) in val.enumerated()
{
    print("value at index = \(index) snd \(item)")
    
}

//methods

func mimax(arrp : [Int])
{
    let sortedarray=arrp.sorted()
    
    var mini = sortedarray.first
    var maxy = sortedarray.last
    var mini1 = sortedarray[0]
    
    print("minimun is \(mini!)")
    print("minimun is also \(mini1)")
    print("maximum is \(maxy!)")
    
}

let arry = [1,2,3,4,54,12,56,-0,-345,123,45621,356]
mimax(arrp:arry)

func minMax(array:[Int])-> (min:Int,max:Int){
    var currentMin = array[0]
    var currentMax = array[0]
    for value in array[1..< array.count] {
        if value < currentMin {
            currentMin = value
        }
        else if value > currentMax{
            currentMax = value
        }
        
    }
    return(currentMin,currentMax)
}
let bounds = minMax(array:[8,-9,7,0,56,9878,-09,-88,13245])
print("min is \(bounds.min) and max ix \(bounds.max)")
