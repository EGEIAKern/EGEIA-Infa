from turtle import *
tracer(0)
screensize(5000,5000)
r = 15
for i in range(4):
    fd(27*r)
    rt(90)
    fd(21*r)
    rt(90)
up()
fd(3*r)
rt(90)
fd(7*r)
lt(90)
down()
for i in range(4):
    fd(73*r)
    rt(90)
    fd(91*r)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,"blue")
update()
mainloop()