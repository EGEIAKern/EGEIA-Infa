from turtle import *
tracer(0)
screensize(5000,5000)
r = 5
for i in range(2): # 1
    fd(150*r)
    rt(120)
rt(300)
for i in range(2): # 2
    fd(75*r)
    rt(120)
    fd(75*r)
    lt(120)
rt(180)
for i in range(2):
    fd(150*r)
    rt(120)
lt(60)
fd(75*r)
#В этом коде можно обойтись без координат так как они только мешают
update()
mainloop()
