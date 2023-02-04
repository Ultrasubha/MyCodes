from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.turtlesize(3)

while True:
    timmy.left(45)
    timmy.forward(400)
    timmy.tilt(180)
    timmy.back(400)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()