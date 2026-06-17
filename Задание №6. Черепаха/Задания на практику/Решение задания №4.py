from turtle import *
tracer(0)
screensize(5000,5000)
r = 3
for i in range(4):
    fd(50*r)
    lt(90)
up()
fd(50*r)
lt(135)
down()
for i in range(2):
    fd(102*r)
    lt(120)
    fd(182*r)
    lt(60)
#В этом коде можно обойтись без координат так как они только мешают
update()
mainloop()