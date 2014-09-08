"""
2014-09-07
Creates artistic "random" line art 
"""
import turtle
from random import randint
from Tkinter import *

turtle.setup(650,500)
turtle.colormode(255)
turtle.bgcolor(99,79,52)
print turtle.position()
turtle.speed(10)
turtle.hideturtle()

def drawCrazy(vertHeight, iterLength, backAgain):
    def drawIt(backAgain):
        turtle.penup()
        turtle.setpos(0,vertHeight)
        turtle.pendown()
        upDown = True
        start = turtle.xcor()
        for i in range(iterLength):
            randomyUpDownVariance = randint(1,55)
            randomyBetweenLineVariance = randint(1,25)
            randPenSize = randint(2,10)
            randPenColor1 = randint(1,187)
            randPenColor2 = randint(1,193)
            randPenColor3 = randint(1,182)
            turtle.pensize(randPenSize)
            print turtle.xcor()
            tup = (randPenColor1, randPenColor2, randPenColor3)
            turtle.pencolor(tup)
            if upDown == True:
                upDown = False
                turtle.goto(start, (vertHeight + randomyUpDownVariance))
            elif upDown == False:
                upDown = True
                turtle.goto(start, -(vertHeight + randomyUpDownVariance))
            if backAgain == True:
                start -= randomyBetweenLineVariance
            elif backAgain == False:
                start += randomyBetweenLineVariance
        if (backAgain == True):
            drawIt(False)
    drawIt(True)

count = 0
for i in range(10):
    drawCrazy(250,25,True)
    count += 1
    print "count: %s" % count
turtle.done()

