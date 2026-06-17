from turtle import *
tracer(0)
screensize(5000,5000)
r = 5
rt(180)
for i in range(9):
    fd(75*r)
    lt(90)
    fd(134*r)
    lt(90)
up()
fd(23*r)
lt(90)
fd(37*r)
rt(90)
down()
for i in range(9):
    fd(157*r)
    rt(90)
    fd(111*r)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-150, 50):
        goto(x * r, y * r)
        dot(3, 'violet')
update()
mainloop()