import numpy as np
import module1 as md

def print_poly(a):
    st = ''
    polll = list(map(float, a))
    for i in range(len(polll)):
        if (float(polll[i])) != 0.0:
            if ((len(polll) - 1 - i)) > 1:
                if (float(polll[i]) > 0):
                    st += '+' + str(polll[i])
                    st += '*x^'
                    st += str((len(polll) - 1 - i))
                else:
                    st += str(polll[i])
                    st += '*x^'
                    st += str((len(polll) - 1 - i))
            if ((len(polll) - 1 - i)) < 1:
                if (float(polll[i]) > 0):
                    st += '+' + str(polll[i])
                else:
                    st += str(polll[i])
            if ((len(polll) - 1 - i)) == 1:
                if (float(polll[i]) > 0):
                    st += '+' + str(polll[i])
                    st += '*x'
                else:
                    st += str(polll[i])
                    st += '*x'
    for i in range(len(st)):
        if (i <= len(st) - 4):
            if (st[i] == '1') and (st[i + 3] == "*") and (st[i-1]== '+' or st[i-1] == '-'):
                st = st[:i] + st[(i + 4):]
    if st!='':
        if (st[0] == '+'):
            st = st[1:]
    else: st += '0'
    return st

def norm(a1):
    while a1 and a1[0] == 0:
        a1.pop(0)
    if a1 == []:
        a1.append(0)

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




while 1:
    a1 = list(map(float, input().split()))
    a2 = list(map(float, input().split()))
    print("F(x) = ",md.print_poly(a1))
    print("G(x) = ",md.print_poly(a2))
    print("Степень многочлена F(x) = ",len(a1)-1)
    print("Степень многочлена G(x) = ",len(a2)-1)
    q,r = poly_div(a1,a2)
    print(q,r)
    print("F(x)/G(x) = %s , остаток = %s" % (print_poly(q),print_poly(r)))
    #print(np.polydiv(a1,a2))


