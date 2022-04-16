#This is calculator
#Блок с переменными и функциями
#Ввод с одной строки !!!!!!!
d=0 #Счёт второго числа для римских
k=0 #Счёт первого числа для римских
rim=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L','LI','LII','LIII','LIV','LV','LVI','LVII','LVIII','LIX', 'LX','LXI','LXII','LXIII','LXIV','LXV','LXVI','LXVII','LXVIII','LXIX', 'LXX','LXXI','LXXII','LXXIII','LXXIV','LXXV','LXXVI','LXXVII','LXXVIII','LXXIX', 'LXXX','LXXXI','LXXXII','LXXXIII','LXXXIV','LXXXV','LXXXVI','LXXXVII','LXXXVIII','LXXXIX', 'XC','XCI','XCII','XCIII','XCIV','XCV','XCVI','XCVII','XCVIII','XCIX','C'] #Римские цифры до 100
def rimplus(x,y):
    v=x+y
    print(rim[x-1],'+',rim[y-1],'=',rim[v-1])
def rimminus(x,y):
    v=x-y
    if v<0:
        print ('Ошибка: разность чисел меньше 0')
        exit(0)
    if v==0:
        print (rim[x-1], '-', rim[y-1], '=', 'I')
    else:
        print (rim[x-1], '-', rim[y-1], '=', rim[v-1])
def rimmulti(x,y):
    v=x*y
    print (rim[x-1], '*', rim[y-1], '=', rim[v-1])
def rimdivision(x,y):
    v=int(x/y)
    print (rim[x-1], '/', rim[y-1], '=', rim[v-1])    
def plus(x,y):
    v=x+y
    print(x, '+', y, '=', v)
def multi (x,y):
    v=x*y
    print (x, '*', y, '=', v)
def division(x,y):
    if y==0:
        print ('Ошибка: на ноль делить нельзя')
        exit(0)
    v=int(x/y)
    print (x, '/', y, '=', v)
def minus (x,y):
    v=x-y
    if v<0:
        print ('Ошибка: разность чисел меньше 0')
        exit(0)
    print (x, '-', y, '=', v)
#Блок того, что вводит пользователь
a=(input('Введите первое число (от 0 до 10) '))
znak=str(input('Введите знак операции для этих чисел (+, -, /, *) '))
b=(input('Введите второе число (от 0 до 10) ' ))
for i in range (10): #Определение числа 
    if a==rim[i]:
        k=i+1
    if b==rim[i]:
        d=i+1
while (k==0 and d!=0) or (k!=0 and d==0): #Числа входят в работу
    print ('Ошибка: введите все числа либо как римские, либо как арабские (и строго от 0 до 10)')
    exit(0)
if k==0 and d==0:
    a=int(a)
    b=int(b)
elif k!=0 and d!=0:
    a=int(k)
    b=int(d)
#Второй шанс для тех, кто неправильно что-то написал (только для арабских чисел) 
while a<0 or a>10:
    print('Ошибка ввода первого числа (оно меньше 0 или больше 10 ')
    a=int(input('Введите первое число (от 0 до 10) '))
    if a>=0 and a<=10:
        break
while b<0 or b>10:
    print('Ошибка ввода второго числа (оно меньше 0 или больше 10 ')
    b=int(input('Введите второе число (от 0 до 10) '))
    if b>=0 and b<=10:
        break
#Второй шанс для тех, кто неправильно знак поставил
while znak!='+' and znak!='*' and znak!='/' and znak!='-':
    print('Ошибка в знаке! Используйте только предложенные')
    znak=str(input('Введите знак операции для этих чисел (+, -, /, *) '))
    if znak=='+' or znak=='*' or znak=='/' or znak=='-':
        break
#Конечный блок
if znak=='+' and (k!=0 and d!=0): 
    rimplus (a,b)
elif znak=='-' and (k!=0 and d!=0):
    rimminus(a,b)
elif znak=='*' and (k!=0 and d!=0):
    rimmulti(a,b)
elif znak=='/' and (k!=0 and d!=0):
    rimdivision(a,b)
if znak=='+' and (k==0 and d==0):
    plus(a,b)
elif znak=='*' and (k==0 and d==0):
    multi(a,b)
elif znak=='/' and (k==0 and d==0):
    division(a,b)
elif znak=='-' and (k==0 and d==0):
    minus(a,b)
