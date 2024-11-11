from turtle import *
from random import randint

speed(0)
pensize(3)
colormode(255)

for i in range(200):
    color(randint(0,255), randint(0,255), randint(0,255))
    begin_fill()
    circle(randint(10,60))
    end_fill()
    up()
    goto(randint(-500,500),randint(-1000,1000))
    down()
    
done()