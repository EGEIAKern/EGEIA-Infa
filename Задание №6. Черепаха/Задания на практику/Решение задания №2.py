from turtle import *
tracer(0)
screensize(5000,5000)
r = 5
for i in range(6):
    fd(71*r)
    rt(90)
    fd(73*r)
    rt(90)
up()
fd(18*r)
rt(90)
fd(22*r)
lt(90)
down()
for i in range(6):
    fd(45*r)
    rt(90)
    fd(58*r)
    rt(90)
up()
for x in range(-20,100):
    for y in range(-100,25):
        goto(x*r,y*r)
        dot(3, 'blue')
update()
mainloop()