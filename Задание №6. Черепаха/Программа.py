from turtle import * #Импортирует черепаху
tracer(0) #Отключение анимации
screensize(5000,5000) #размер окна с черепахой
r = 15 #переменная для увеличения маштаба
for i in range(2): #Количество повторений
    fd(5*r)
    rt(90)
    fd(11*r)
    rt(90)
up() #поднять хвост
fd(4*r)
rt(90)
fd(6*r)
lt(90)
down() #опустить хвост
for i in range(2):
    fd(42*r)
    rt(90)
    fd(63*r)
    rt(90)
#Отрисовка целочисленных точек
up()
for x in range(-50,50): #добавляем точки на координате x
    for y in range(-50,50): #добавляем точки по координате y
        goto(x*r,y*r)
        dot(3,"blue")
update()
mainloop()