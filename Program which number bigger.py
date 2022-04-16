c=int(input())
q=int(input())
def bol(x, y):
    k=str(x)
    p=0
    w=0
    l=10
    for i in range (len(k)):
        if x%l!=x:
            l=l*10
            p+=1
        elif x%l==x:
            break
    k=str(y)
    l=10
    for j in range (len(k)):
        if y%l!=y:
            l=l*10
            w+=1
        elif y%l==y:
            break
    if w==p:
        print('Одинаково', x)
    elif w>p:
        print('Второе число больше ', y)
    elif w<p:
        print('Первое число больше', x)
bol(c, q)

