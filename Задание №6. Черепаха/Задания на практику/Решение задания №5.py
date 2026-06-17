from turtle import *
tracer(0)
screensize(5000,5000)
r=15
for i in range(4):
    fd(36*r)
    rt(90)
    fd(41*r)
    rt(90)
up()
rt(90)
fd(20*r)
lt(90)
fd(20*r)
down()
for i in range(4):
    fd(25*r)
    rt(90)
up()
fd(7*r)
lt(90)
fd(7*r)
rt(90)
down()
for i in range(7):
    fd(16*r)
    rt(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*r,y*r)
        dot(3,"blue")
update()
mainloop()