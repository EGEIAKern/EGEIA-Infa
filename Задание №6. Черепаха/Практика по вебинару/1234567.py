from turtle import *
tracer(0)
screensize(5000,5000)
r = 40

for i in range(14):
    lt(180)
    for p in range(3):
        fd(3*r)
        rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,"blue")
update()
mainloop()