from turtle import *
from house2 import *


speed(10)
xhome = -135
yhome = -100
xwind = -100
ywind = 0
xdoor = 0
ydoor = -100
xtree = 200
ytree = 0
xsun = 100
ysun = 300
linkx = 220
linky = -180


penup()
goto(-250,400)
pendown()
begin_fill()
color('royal blue')#меняет цвет на голубой
for i in range (4):
    forward(600)
    right(90)
end_fill()
penup()
goto(-250,-300)
pendown()
color('lime green')
begin_fill()

forward(600)
left(90)
forward(300)
left(90)
forward(600)
left(90)
forward(300)
end_fill()
left(90)
home(xhome,yhome)
window(xwind,ywind)
door(xdoor,ydoor)
right(90)
tree(xtree,ytree)
sun(xsun,ysun)
left(90)
fence_link(linkx,linky)
hideturtle()
exitonclick()