import numpy as np
import module1 as md

def norm(a1):
    while a1 and a1[0] == 0:
        a1.pop(0)
    if a1 == []:
        a1.append(0)

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

def poly_div(a1, a2):
    a1 = a1[:]
    norm(a1)
    a2 = a2[:]
    norm(a2)
    if len(a1) >= len(a2):
        shiftlen = len(a1) - len(a2)
        a2 = a2 + [0] * shiftlen
    else:
        return [0], a1
    q = []
    div = float(a2[0])
    #print(divisor,den)
    for i in range(shiftlen + 1):
        m = a1[0] / div
        q = q + [m]
        if m != 0:
            d = [m * k for k in a2]
            a1 = [k - l for k, l in zip(a1, d)]

        a1.pop(0)
        a2.pop()
    norm(a1)
    return q, a1

def N(x,a1,f):
    if f(x,a1)<0:
        return -1
    else:
        return 1



while 1:
    a1 = list(map(float, input().split()))
    print("F(x) = ", md.print_poly(a1))
    print("Степень многочлена = ", len(a1) - 1)
    poly = []
    poly.append(a1)
    f1 = d_poly_koeffs(a1)
    poly.append(f1)
    signs_ = []
    signs0 = []
    signs = []
    for i in range(2,len(a1)):
        mod = poly_div(poly[i-2],poly[i-1])
        mod = list(map(float,mod[1]))
        for j in range(len(mod)):
            mod[j]*=-1
        poly.append(mod)
    #print(poly)
    for i in range(len(poly)):
        #print(i)
        signs_.append(N(-1000000, poly[i], f))
        signs0.append(N(0, poly[i], f))
        signs.append(N(1000000, poly[i], f))
    #print(signs_, signs0, signs)
    n1=0
    n2=0
    n3=0
    for i in range(len(signs)-1):
        if (signs_[i+1]*signs_[i]) < 0: n1 += 1
        if (signs[i + 1] * signs[i]) < 0: n3 += 1
        if (signs0[i + 1] * signs0[i]) < 0: n2 += 1
    print("Число действительных корней = %s , Число положительных корней = %s, Число отрицательных корней = %s" % (n1-n3,n2-n3,n1-n2))