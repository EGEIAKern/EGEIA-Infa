# https://inf-ege.sdamgia.ru/problem?id=15990
def f (x,y):
    if x > y: return 0
    if x == y: return 1
    else: return f(x+2,y) + f(x*2,y) + f(x+3,y)
print(f(2,11) * f(11,22))

# https://inf-ege.sdamgia.ru/problem?id=72608
def f (x,y):
    if x < y: return 0
    if x == y: return 1
    else: return f(x-2, y) + f(x//2, y) + f(x//3, y)
print(f(38, 12) * f(12,3))
# https://inf-ege.sdamgia.ru/problem?id=89206
def f (x,y):
    if x > y: return 0
    if x == y: return 1
    else: return f(x**2, y) + f(x+3, y) + f(x+4,y)
print(f(4,7) * f(7,18) * f(18, 41))

"""
Авторское задание:
1.) Прибавить + 4
2.) Умножить на 3
3.) Возвести в квадрат
Сколько существует программ, которые преобразуют исходное число 1 в число 105 и 
при этом траектория вычислений не содержит числа 10 и 21?
"""
def f (x,y):
    if x > y: return 0
    if x == y or x == 10 or x == 21: return 1
    else: return f(x+4, y) + f(x*3, y) + f(x*2, y)
print(f(1,105))