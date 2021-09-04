import numpy as np
import module1 as md
import copy
import math

def Scheme(polinom, a):
    output = [polinom[0]]
    for i in range(len(polinom) - 1):
        output.append(a * output[i] + polinom[i + 1])
    return output
def bounds(a2):
    def Lab_4(polinom):
        answer = [0, 0]
        # нахождение верхней границы
        if polinom[0] < 0: polinom = [i * -1 for i in polinom]
        for i in range(1000000):
            temp = Scheme(polinom, i)
            f = True
            for j in temp:
                if j < 0:
                    f = False
                    break
            if f == True:
                answer[1] = i
                break
        # нахождение нижней границы
        polinom = [i * (-1) ** (len(polinom) - 1) for i in polinom]
        for i in range(len(polinom)):
            polinom[i] = polinom[i] * (-1) ** (len(polinom) - i - 1)
        for i in range(1000000):
            temp = Scheme(polinom, i)
            f = True
            for j in temp:
                if j < 0:
                    f = False
                    break
            if f == True:
                answer[0] = -1 * i
                break

        return answer
    b = Lab_4(a2)
    up = b[0]
    low = b[1]
    return up,low

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

def root_count(a1,a,b):
    #print(a1)
    poly = []
    poly.append(a1)
    f1 = d_poly_koeffs(a1)
    poly.append(f1)
    signs_ = []
    signs0 = []
    signs = []
    for i in range(2,len(a1)):
        mod = np.polydiv(poly[i - 2], poly[i - 1])
        mod = list(map(float, mod[1]))
        for j in range(len(mod)):
            mod[j] *= -1
        poly.append(mod)
    for i in range(len(poly)):
        # print(i)
        signs_.append(N(a, poly[i], f))
        signs0.append(N(0, poly[i], f))
        signs.append(N(b, poly[i], f))
    # print(signs_, signs0, signs)
    n1 = 0
    n2 = 0
    n3 = 0
    for i in range(len(signs) - 1):
        if (signs_[i + 1] * signs_[i]) <0: n1 += 1
        if (signs[i + 1] * signs[i]) <0: n3 += 1
        if (signs0[i + 1] * signs0[i]) <0: n2 += 1
    #print(n1,n2,n3)
    #print("Число действительных корней = %s , Число положительных корней = %s, Число отрицательных корней = %s" % (
    #n1 - n3, n2 - n3, n1 - n2))
    return n1 - n3

def roots(a1,a,b):
    def MPD(a, b,a1, eps=1e-5):
        while abs(b - a) > eps:
            x = (a + b) / 2.0
            fx = f(x,a1)
            fa = f(a,a1)
            if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
                a = x
            else:
                b = x
        return x

    der = d_poly_koeffs(a1)
    polll = list(map(float, a1))
    x = MPD(a,b,polll)
    return x

roots1=[]
intervals = []
def sturm_roots(a1,a,b,low):
    if a<low:return
    if root_count(a1, a, b) == 0:
        sturm_roots(a1,a-1,b-1,low)
    else:
        if (root_count(a1, a, b)) == 1:
            if round(roots(a1, a, b),4) not in roots1:
                roots1.append(round(roots(a1, a, b),4))
                intervals.append([round(a,4), round(b,4)])
            sturm_roots(a1,a-1,b-1,low)
        else:
            sturm_roots(a1,b-(b-a)/2,b,low)
            sturm_roots(a1,a,a+(b-a)/2,low)



'''
a2 = a
    b2 = b
    print(a2,b2)
    if b2>up:return
    if root_count(a1,a2,b2,)>1:
        print(">1")
        sturm_roots(a2,a2+abs(b2-a2)/2,a1,up)
    if root_count(a1,a2,b2,)==0:
        print(0)
        sturm_roots(a2+1,b2+1,a1,up)
    if root_count(a1,a2,b2,)==1:
        print(1)
        print(roots(a1,a2,b2))
        intervals.append([a2,b2])
        roots1.append(roots(a1,a2,b2))
        sturm_roots(b2,b2+1,a1,up)
'''

while 1:
    s=input()
    s1 = '1 -4 -42 104 361 -420'
    s3 = '-1 -2 -2 -5 0 -3 -4 2 -5 0'
    s4 = '1 1.4 -13.85 1.842 6.264'
    s5 = '1 0 -4'
    s6 = '1 0 -37 24 180'
    a1 = list(map(float,s.split()))
    print("F(x) = ", md.print_poly(a1))
    print("Степень многочлена = ", len(a1) - 1)
    low,up = bounds(a1)
    print(up,low)
    eps = 1e-12
    #print(root_count(a1,-2,3))
    roots1=[]
    intervals=[]
    sturm_roots(a1,up-1,up,low)
    print(roots1)
    print(intervals)
    break



