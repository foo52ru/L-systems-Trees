#---- foo52ru  ---------
# генерация дерева с листьями
# добавлены дополнительные ветки
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
itr = 12
angl = 14
dl = 10
level = 0
stc = []
#--------------------------------------------
for k in range(itr):
    for ch in axiom:
        if ch == '0':
            axmTemp+= '1[-20][+20]'
        elif ch == '1':
            axmTemp+= '21' 
        elif ch == '[':
            axmTemp+= '[' 
            level += 1
        elif ch == ']':
            axmTemp+= ']'
            level -= 1
        elif ch == '2':
            if randint(0,100) < 12 and level > 3 :
            	axmTemp+= '3[^30]'  
            else:
            	axmTemp+='2'
        else:
            axmTemp+=ch
    axiom = axmTemp
    axmTemp = ""   
#--------------------------------------------

for ch in axiom:
    if   ch == "+":
        turtle.right(angl - randint(-13,13))
    elif ch == "-":
        turtle.left(angl - randint(-13,13))
    elif ch == "^":
        ug = randint(-30,30)
        if ug < 0:
        	turtle.left(ug-25)
        else:
        	turtle.left(ug+25)
    elif ch == "[":
        level += 1
        stc.append(thick)
        stc.append(turtle.xcor())
        stc.append(turtle.ycor())
        stc.append(turtle.heading())
        thick = thick*0.75
        turtle.pensize(thick)      
    elif ch == "]":
        level -= 1
        turtle.penup()
        turtle.setheading(stc.pop())
        turtle.sety(stc.pop())
        turtle.setx(stc.pop())
        thick = stc.pop()
        turtle.pensize(thick)
        turtle.pendown()
    elif ch == "0":
        stc.append(turtle.pensize())
        turtle.pensize(4)
        r = randint(0,10)
        if r<3:
        	turtle.pencolor('#009900')
        elif r>6:
        	turtle.pencolor('#667900')
        else:
        	turtle.pencolor('#20BB00')
        turtle.forward(dl-2)
        turtle.pensize(stc.pop())   
        turtle.pencolor('#000000')
    else:
        if randint(0,10)>4:
            turtle.forward(dl) 

turtle.update()        
turtle.mainloop()











