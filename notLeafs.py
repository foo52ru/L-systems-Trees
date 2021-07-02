#---- foo52ru  ---------
# генерация дерева без листьев
# https://youtu.be/mAz46Z5curo
import turtle
from random import randint
turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(0,-300)
turtle.left(90)
turtle.pendown()
thick = 16
turtle.pensize(thick)

axiom = "22220"
axmTemp = ""
itr = 11
angl = 20
dl = 10
stc = []

translate={"1":"21",
           "0":"1[-20]+20"}

for k in range(itr):
    for ch in axiom:
        if ch in translate:
            axmTemp+=translate[ch]
        else:
            axmTemp+=ch
    axiom = axmTemp
    axmTemp = ""

for ch in axiom:
    if   ch == "+":
        turtle.right(angl - randint(-13,13))
    elif ch == "-":
        turtle.left(angl - randint(-13,13))
    elif ch == "2":
        if randint(0,10)>5:
            turtle.forward(dl)        
    elif ch == "1":
        turtle.forward(dl)
    elif ch == "0":
        turtle.forward(dl)        
    elif ch == "[":
        thick = thick*0.75
        turtle.pensize(thick)
        stc.append(thick)
        stc.append(turtle.xcor())
        stc.append(turtle.ycor())
        stc.append(turtle.heading())
    elif ch == "]":
        turtle.penup()
        turtle.setheading(stc.pop())
        turtle.sety(stc.pop())
        turtle.setx(stc.pop())
        thick = stc.pop()
        turtle.pensize(thick)
        turtle.pendown()
turtle.update()        
turtle.mainloop()
