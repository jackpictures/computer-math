import numpy as np
import copy
import module1 as md


def d_poly_koeffs(a1):
    deg = len(a1) - 1
    k = []
    for i in range(deg):
        k.append(deg * a1[i])
        deg -= 1
    return k

def f(x,a1):
    k = 0
    for i in range(len(a1)):
        k+=float(a1[i])*(x**(len(a1)-1-i))
    return k


while 1:
    a1 = list(map(float, input().split()))
    print("F(x)=",md.print_poly(a1))
    if (float(a1[0])<0):
        for i in range(len(a1)):
            a1[i]*=-1
    polll = list(map(float,a1))
    a_poly = np.array(list(a1),dtype = float)
    c=list(range(1,100))
    for i in range(len(c)):
        flag = 1
        der = copy.deepcopy(a1)
        if f(c[i],der)<0:continue
        for j in range(len(der)):
            der = d_poly_koeffs(der)
            if f(c[i],der)<0:
                flag = 0
                break
        if flag==1:
            up = c[i]
            break
    try:
        print(up)
    except:
        print("NONE")