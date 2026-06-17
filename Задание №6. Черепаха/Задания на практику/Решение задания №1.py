from turtle import *
tracer(0)
screensize(5000,5000)
r = 25
for i in range(3):
    fd(5*r)
    lt(270)
    bk(8*r)
    lt(270)
up()
fd(2*r)
rt(90)
bk(3*r)
lt(90)
down()
for i in range(3):
    fd(4*r)
    rt(90)
    fd(6*r)
    rt(90)
up()
fd(4)
rt(180)
bk(2)
down()
for i in range(2):
    fd(5*r)
    rt(90)
    fd(7*r)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'blue')
update()
mainloop()