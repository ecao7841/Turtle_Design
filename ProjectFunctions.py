#Function file: Terry and Eric
from myFunctionfile import *
def brick (t,x,y):
    jump(t,x,y)
    t.color('saddlebrown')
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.end_fill()
    t.color('black')
    t.penup()
    t.forward(30)
    t.left(90)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.forward(-30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.forward(-10)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(7)
    t.color('gray')
    t.pensize(1.5)
    t.left(90)
    t.forward(17)
    t.left(90)
    t.forward(85)
    t.left(90)
    t.forward(85)
    t.left(90)
    t.forward(85)
    t.left(90)
    t.forward(85)
    t.left(90)
    t.right(270)
    t.forward(85)
    t.right(90)
    t.forward(56)
    t.color('chocolate')
    t.right(90)
    t.pensize(3)
    t.forward(31)
    t.penup()
    t.forward(5)
    t.pendown()
    t.left(90)
    t.forward(30)
    t.forward(-30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(4)
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(23)
    t.penup()
    t.forward(4)
    t.pendown()
    t.forward(20)
    t.right(90)
    t.forward(4)
    t.left(90)
    t.forward(4)
    t.penup()
    t.left(90)
    t.forward(16)
    t.left(90)
    t.forward(85)
    t.pendown()
    t.right(180)
    t.pensize(2)
    t.color('gray')
    t.forward(86)
    t.right(90)
    t.forward(85)
    t.right(90)
    t.forward(85)
    t.right(90)
    t.forward(85)
    t.right(90)
    t.pensize(4)

def pipe(n):
    n.color('limegreen')
    n.begin_fill()
    n.forward(200)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(200)
    n.right(90)
    n.forward(50)
    n.end_fill()
    n.color('black')
    n.pensize(4)
    n.right(90)
    n.forward(201)
    n.right(90)
    n.forward(51)
    n.right(90)
    n.forward(201)
    n.right(90)
    n.forward(51)
    n.right(90)
    n.forward(45)
    n.begin_fill()
    n.forward(40)
    n.color('greenyellow')
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(40)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.end_fill()
    n.color('black')
    n.forward(156)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(201)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(20)
    n.penup()
    n.right(90)
    n.forward(50)
    n.color('limegreen')
    n.pensize(1)
    n.pendown()
    n.begin_fill()
    n.forward(300)
    n.left(90)
    n.forward(160)
    n.left(90)
    n.forward(300)
    n.left(90)
    n.forward(160)
    n.end_fill()
    n.color('black')
    n.pensize(4)
    n.left(90)
    n.forward(300)
    n.left(90)
    n.forward(160)
    n.left(90)
    n.forward(300)
    n.left(90)
    n.forward(160)
    n.forward(-30)
    n.left(90)
    n.pensize(1)
    n.color('greenyellow')
    n.begin_fill()
    n.forward(300)
    n.left(90)
    n.forward(40)
    n.left(90)
    n.forward(300)
    n.left(90)
    n.forward(40)
    n.end_fill()
    n.color('black')
    n.pensize(4)
    n.forward(30)
    n.left(90)
    n.forward(300)
    n.left(90)
    n.forward(160)
    n.left(90)
    n.forward(300)
    n.left(90)
    n.forward(160)
    n.penup()

def briks(n):
    brick(n,900,-350)
    brick(n,820,-350)
    brick(n,740,-350)
    brick(n,660,-350)
    brick(n,580,-350)
    brick(n,500,-350)
    brick(n,420,-350)
    brick(n,340,-350)
    brick(n,260,-350)
    brick(n,180,-350)
    brick(n,100,-350)
    brick(n,20,-350)
    brick(n,-60,-350)
    brick(n,-140,-350)
    brick(n,-220,-350)
    brick(n,-300,-350)
    brick(n,-380,-350)
    brick(n,-460,-350)
    brick(n,-540,-350)
    brick(n,-620,-350)
    brick(n,-700,-350)
    brick(n,-780,-350)
    brick(n,900,-430)
    brick(n,820,-430)
    brick(n,740,-430)
    brick(n,660,-430)
    brick(n,580,-430)
    brick(n,500,-430)
    brick(n,420,-430)
    brick(n,340,-430)
    brick(n,260,-430)
    brick(n,180,-430)
    brick(n,100,-430)
    brick(n,20,-430)
    brick(n,-60,-430)
    brick(n,-140,-430)
    brick(n,-220,-430)
    brick(n,-300,-430)
    brick(n,-380,-430)
    brick(n,-460,-430)
    brick(n,-540,-430)
    brick(n,-620,-430)
    brick(n,-700,-430)
    brick(n,-780,-430)


def questionblock(n,x,y):
    n.penup()
    n.goto(x,y)
    n.pendown()
    n.color('goldenrod')
    n.begin_fill()
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.end_fill()
    n.color('chocolate')
    n.pensize(2)
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.forward(40)
    n.right(90)
    n.penup()
    n.forward(8)
    n.forward(5)
    n.pendown()
    n.color('darkorange')
    n.pensize(3)
    n.forward(8)
    n.begin_fill()
    n.right(90)
    n.forward(8)
    n.right(90)
    n.forward(8)
    n.right(90)
    n.forward(8)
    n.end_fill()
    n.right(90)
    n.penup()
    n.forward(18)
    n.pendown()
    n.forward(8)
    n.right(90)
    n.forward(5)
    n.left(90)
    n.forward(8)
    n.right(90)
    n.forward(5)
    n.left(90)
    n.forward(23)
    n.left(90)
    n.forward(20)
    n.left(90)
    n.forward(14)
    n.right(90)

def block(n,x,y):
    jump(n,x,y)
    n.color('sienna')
    n.begin_fill()
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.forward(80)
    n.right(90)
    n.end_fill()
    n.forward(20)
    n.color('black')
    n.pensize(2)
    n.penup()
    n.right(90)
    n.forward(1)
    n.pendown()
    n.forward(26)
    n.right(90)
    n.forward(19)
    n.forward(-80)
    n.forward(10)
    n.right(90)
    n.forward(26)
    n.forward(-26)
    n.left(90)
    n.forward(15)
    n.left(90)
    n.forward(26)
    n.right(90)
    n.forward(-24)
    n.forward(80)
    n.forward(-19)
    n.left(90)
    n.forward(27)
    n.forward(-27)
    n.left(90)
    n.forward(30)
    n.right(90)
    n.forward(27)
    n.left(90)

def hill (n,x,y):
    jump(n,x,y)
    n.pensize(1)
    n.color('green')
    n.right(45)
    n.begin_fill()
    n.forward(90)
    n.left(22)
    n.forward(20)
    n.left(22)
    n.forward(20)
    n.left(45)
    n.forward(90)
    n.left(133)
    n.forward(163)
    n.end_fill()
    n.left(136)
    n.color('black')
    n.pensize(2)
    n.forward(90)
    n.left(25)
    n.forward(20)
    n.left(25)
    n.forward(20)
    n.left(43)
    n.forward(90)
    n.left(133)
    n.forward(163)
    n.left(136)
    n.penup()
    n.forward(70)
    n.left(45)
    n.forward(8)
    n.pendown()
    n.pensize(5)
    n.left(90)
    n.forward(5)
    n.penup()
    n.right(90)
    n.forward(8)
    n.left(90)
    n.pendown()
    n.forward(3)
    n.right(90)

def mario(n,x,y):
    n.penup()
    jump(n,x,y)
    n.pendown()

    n.begin_fill()
    n.color('saddlebrown')
    n.forward(100)
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(75)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.end_fill()

    n.penup()
    n.left(90)
    n.forward(200)
    n.pendown()

    n.begin_fill()
    n.forward(100)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(75)
    n.left(90)
    n.end_fill()
    n.forward(50)

    n.penup()
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(50)
    n.pendown()

    n.color('mediumblue')
    n.begin_fill()
    n.forward(50)
    n.left(90)
    n.forward(200)
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(75)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(75)
    n.end_fill()

    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.right(90)

    n.begin_fill()
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(50)
    n.end_fill()

    n.right(180)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.color('yellow')
    n.begin_fill()
    for a in range(4):
        n.forward(25)
        n.right(90)
    n.end_fill()

    n.penup()
    n.forward(75)
    n.pendown()
    n.begin_fill()
    for a in range(4):
        n.forward(25)
        n.right(90)
    n.end_fill()
    n.color('mediumblue')
    n.begin_fill()
    n.forward(25)
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(75)
    n.end_fill()

    n.right(180)
    n.color('red')
    n.begin_fill()
    n.forward(75)
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.end_fill()

    n.right(180)
    n.forward(25)
    n.color('tan')
    n.begin_fill()
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(75)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.end_fill()

    n.penup()
    n.forward(150)
    n.pendown()
    n.begin_fill()
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(75)
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.end_fill()

    n.color('red')
    n.begin_fill()
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(100)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.end_fill()

    n.penup()
    n.right(90)
    n.forward(100)
    n.left(90)
    n.forward(150)
    n.pendown()

    n.color('tan')
    n.begin_fill()
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(125)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(75)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.end_fill()
    n.forward(200)

    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(50)
    n.left(90)

    n.begin_fill()
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(75)
    n.right(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.end_fill()
    n.left(90)

    n.color('black')
    n.begin_fill()
    n.forward(25)
    n.left(90)
    n.forward(100)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.end_fill()

    n.penup()
    n.right(90)
    n.forward(25)
    n.pendown()

    n.begin_fill()
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.end_fill()

    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(25)

    n.color('tan')
    n.begin_fill()
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(75)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.end_fill()

    n.penup()
    n.left(90)
    n.forward(100)
    n.pendown()

    n.color('saddlebrown')
    n.begin_fill()
    n.forward(75)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.end_fill()

    n.left(90)
    n.forward(50)
    n.left(90)
    n.forward(25)

    n.color('tan')
    n.begin_fill()
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(25)
    n.end_fill()

    n.right(90)
    n.forward(50)

    n.color('saddlebrown')
    n.begin_fill()
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.right(90)
    n.forward(75)
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(50)
    n.left(90)
    n.forward(25)
    n.end_fill()
    n.forward(50)

    n.penup()
    n.left(90)
    n.forward(75)
    n.left(90)
    n.forward(75)
    n.pendown()

    n.color('red')
    n.begin_fill()
    n.right(90)
    n.forward(25)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(25)
    n.right(90)
    n.forward(150)
    n.right(90)
    n.forward(25)
    n.left(90)
    n.forward(75)
    n.right(90)
    n.forward(25)
    n.end_fill()



def luigi(n,x,y):
    
    n.penup()
    n.jump(x,y)
    n.pendown()

    n.begin_fill()
    n.color('saddlebrown')
    n.forward(12)
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(9)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.end_fill()

    n.penup()
    n.left(90)
    n.forward(24)
    n.pendown()

    n.begin_fill()
    n.forward(12)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(9)
    n.left(90)
    n.end_fill()
    n.forward(6)

    n.penup()
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(6)
    n.pendown()

    n.color('purple')
    n.begin_fill()
    n.forward(6)
    n.left(90)
    n.forward(24)
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(9)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(9)
    n.end_fill()

    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.right(90)

    n.begin_fill()
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(6)
    n.end_fill()

    n.right(180)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.color('yellow')
    n.begin_fill()
    for a in range(4):
        n.forward(3)
        n.right(90)
    n.end_fill()

    n.penup()
    n.forward(9)
    n.pendown()
    n.begin_fill()
    for a in range(4):
        n.forward(3)
        n.right(90)
    n.end_fill()
    n.color('purple')
    n.begin_fill()
    n.forward(3)
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(9)
    n.end_fill()

    n.right(180)
    n.color('lime')
    n.begin_fill()
    n.forward(9)
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.end_fill()

    n.right(180)
    n.forward(3)
    n.color('tan')
    n.begin_fill()
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(9)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.end_fill()

    n.penup()
    n.forward(18)
    n.pendown()
    n.begin_fill()
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(9)
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.end_fill()

    n.color('lime')
    n.begin_fill()
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(12)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.end_fill()

    n.penup()
    n.right(90)
    n.forward(12)
    n.left(90)
    n.forward(18)
    n.pendown()

    n.color('tan')
    n.begin_fill()
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(15)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(9)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.end_fill()
    n.forward(24)

    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(6)
    n.left(90)

    n.begin_fill()
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(9)
    n.right(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.end_fill()
    n.left(90)

    n.color('black')
    n.begin_fill()
    n.forward(3)
    n.left(90)
    n.forward(12)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.end_fill()

    n.penup()
    n.right(90)
    n.forward(3)
    n.pendown()

    n.begin_fill()
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.end_fill()

    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(3)

    n.color('tan')
    n.begin_fill()
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(9)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.end_fill()

    n.penup()
    n.left(90)
    n.forward(12)
    n.pendown()

    n.color('saddlebrown')
    n.begin_fill()
    n.forward(9)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.end_fill()

    n.left(90)
    n.forward(6)
    n.left(90)
    n.forward(3)

    n.color('tan')
    n.begin_fill()
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(3)
    n.end_fill()

    n.right(90)
    n.forward(6)

    n.color('saddlebrown')
    n.begin_fill()
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.right(90)
    n.forward(9)
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(6)
    n.left(90)
    n.forward(3)
    n.end_fill()
    n.forward(6)

    n.penup()
    n.left(90)
    n.forward(9)
    n.left(90)
    n.forward(9)
    n.pendown()

    n.color('lime')
    n.begin_fill()
    n.right(90)
    n.forward(3)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(3)
    n.right(90)
    n.forward(18)
    n.right(90)
    n.forward(3)
    n.left(90)
    n.forward(9)
    n.right(90)
    n.forward(3)
    n.end_fill() 

