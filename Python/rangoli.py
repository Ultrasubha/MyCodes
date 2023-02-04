from turtle import *

bgcolor('black')
red = [210, 0, 0, 255, 255, 255]
green = [0, 128, 0, 128, 255, 255]
blue = [0, 128, 128, 0, 0, 255]

x = 10
speed(200)
pensize(5)

while x < (410):
    colormode(255)
    pencolor((red[x % 6]), (green[x % 6]), (blue[x % 6]))
    fd(30 + x)
    rt(60.5)
    x = x + 1
