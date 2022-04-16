a=int(input())
b=int(input())
c=int(input())
v=int(input())
def nod(x,y,z,o):
    p1=1
    p2=1
    p3=1
    p4=1
    k1=1
    k2=1
    k3=1
    k4=1
    d=0
    for i in range (1000):
            if x%p1!=0:
                p1+=1
            elif x%p1==0:
                k1=p1
                p1+=1
            if y%p2!=0:
                p2+=1
            elif y%p2==0:
                k2=p2
                p2+=1
            if z%p3!=0:
                p3+=1
            elif z%p3==0:
                k3=p3
                p3+=1
            if o%p4!=0:
                p4+=1
            elif o%p4==0:
                k4=p4
                p4+=1
            if k1==k2 and k2==k3 and k3==k4 and k1==k3 and k1==k4 and k4==k2:
                d=k1
    print('НОД равен ', d)

nod(a,b,c,v)
            
        
    
