#Project file:Terry and Eric
import turtle
n=turtle.Turtle()
from myFunctionfile import *
from ProjectFunctions import *
turtle.bgcolor('skyblue')
n.speed(0)
pipe(n)
block(n,520,50)
questionblock(n,600,50)
block(n,680,50)
hill(n,-420,-360)
briks(n)
n.right(180)
mario(n,-398,-348)
n.penup()
jump(n,9000,9000)
n.pendown()
