from itertools import *
def f (x,y,w,z):
    return (ФУНКЦИЯ)
for a in product([0,1], repeat = 3): # repeat = 3 - это количество пустых значений в таблице
    table = [ЗНАЧЕНИЯ] # как пример [(0,1,0,a[0]), (1,1,a[1],1),(a[2],0,0,0)
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r)))for r in table] == [0,0,0]
                print(p)