import turtle
import math
from time import sleep
t = turtle.Turtle()
turtle.bgcolor("black")
t.pencolor("white")
s = turtle.getscreen()
t.speed(0)
def circles():
    colors=["orange","yellow","white","blue","red"]
    j=0
    diagonal=28.97777479
    for i in range(360):
        if i%50==0 and j<len(colors):
            t.pencolor(colors[j])
            j+=1
        t.penup()
        t.goto(diagonal*math.sin(75)+4,-1*diagonal*math.cos(75)-120+i/3)
        t.pendown()
        t.circle(120-i/3)
def flower():
    t.right(26)
    colors=["purple","yellow", "white", "red", "yellow", "white"]
    j=0
    for i in range(300):
        if i%50==0 and j<len(colors):
            t.pencolor(colors[j])
            j+=1
        t.circle(100-i/3,90)
        t.left(90)
        t.circle(100-i/3,90)
        t.left(18)
def rangoli():
    k=0
    while k!=360:
        j=0
        while j!=390:
            for i in range(4):
                t.forward(110)
                t.right(90)
            t.right(30)
            j+=30
        t.forward(12.99)
        k+=30
sleep(3)
t.home()
t.pencolor("green")
rangoli()
diagonal=28.97777479
t.penup()
t.goto(diagonal*math.sin(75),-1*diagonal*math.cos(75))
t.pendown()
circles()
t.goto(diagonal*math.sin(75),-1*diagonal*math.cos(75))
t.pencolor("purple")
flower()
turtle.hideturtle()
turtle.done()
