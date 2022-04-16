#Массив на вход только цифры, сделать max
import random
m=[]
for i in range (random.randint(4,8)):
    m.append(int(input('Заполните массив ')))
def max(mass):
    x=-9999999
    for k in range (len(mass)):
        if mass[k]>x:
            x=mass[k]
    print('Массив: ', mass)
    print('Максимальное число в массиве: ',x)
max(m)

def min(mass):
    x=9999999
    for k in range (len(mass)):
        if mass[k]<x:
            x=mass[k]
    print('Массив: ', mass)
    print('Минимальное число в массиве: ',x)
min(m)
