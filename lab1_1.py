import numpy as np
import module1 as md
import copy
import matplotlib.pyplot as plt
from pyparsing import (Literal, CaselessLiteral, Word, Combine, Group, Optional,
                           ZeroOrMore, Forward, nums, alphas, oneOf)
import math
import operator

def lab1_1(a,b):
    a1 = list(map(float, a.split()))
    polll = list(map(float, a1))
    st = ''
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
            if (st[i] == '1') and (st[i + 3] == "*"):
                st = st[:i] + st[(i + 4):]
    if (st[0] == '+'):
        print("F(x):", st[1:])
    else:
        print("F(x):", st)
    print("Степень многочлена = ", len(a1) - 1)
    x1 = float(b)
    p = 0
    n1 = len(a1) -1
    i1=0
    while n1 > 0:
        p = (p + float(a1[i1])) * x1
        n1 -= 1
        i1+=1
    p += float(a1[len(a1)-1])
    print(p)

def lab1_2(a,b):
    a1 = list(map(float, a.split()))
    polll = list(map(float, a1))
    st = ''
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
        if (i <= len(st) - 3):
            if (st[i] == '1') and (st[i + 3] == "*"):
                st = st[:i] + st[(i + 4):]
    if (st[0] == '+'):
        print("F(x):", st[1:])
    else:
        print("F(x):", st)
    print("Степень многочлена = ", len(a1) - 1)
    a_poly = np.array(list(a1), dtype=float)
    k = float(b)
    k *= -1
    k_poly = np.array(list([1, k]), dtype=float)
    div = (np.polydiv(a_poly, k_poly))
    divr = list(div[0])
    divr = np.reshape(divr, (1, len(divr)))
    divr = divr.tolist()
    print(divr)
    divr1 = divr[0]
    polll = list(map(float, divr1))
    st = ''
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
        if (i <= len(st) - 3):
            if (st[i] == '1') and (st[i + 3] == "*"):
                st = st[:i] + st[(i + 4):]
    if (st[0] == '+'):
        print("G(x):", st[1:])
    else:
        print("G(x):", st)

def lab1_3(a,b):
    div1 = []
    a1 = list(map(float, a.split()))
    polll = list(map(float, a1))
    st = ''
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
        if (i <= len(st) - 3):
            if (st[i] == '1') and (st[i + 3] == "*"):
                st = st[:i] + st[(i + 4):]
    if (st[0] == '+'):
        print("F(x):", st[1:])
    else:
        print("F(x):", st)
    print("Степень многочлена  = ", len(a1) - 1)
    a_poly = np.array(list(a1), dtype=float)
    k = float(b)
    print("Число а = %s"%k)
    k = float(b)
    k *= -1
    k_poly = np.array(list([1, k]), dtype=float)
    div = np.polydiv(a_poly, k_poly)
    for i in range(len(a1)):
        div1.append(list(div[len(div) - 1]))
        div = np.polydiv(div[0], k_poly)
    divr = list(reversed(div1))
    divr = np.reshape(divr, (1, len(divr)))
    divr = divr.tolist()
    divr1 = divr[0]
    polll = list(map(float, divr1))
    st = ''
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
        if (i < len(st) - 3):
            if (st[i] == '1') and (st[i + 3] == "*"):
                st = st[:i] + st[(i + 4):]
    if (st[0] == '+'):
        print("G(x):", st[1:])
    else:
        print("G(x):", st)
    # print(list(reversed(div1)))
    div1 = []
def lab1_4(a):
    nums = np.arange(-1000, 1000, 1).tolist()
    def lim(a_poly,nums):
        upper = 0
        l = []
        for i in range(len(nums)):
            k = float(nums[i])
            if k == 0: continue
            k *= -1
            k_poly = np.array(list([1, k]), dtype=float)
            div = np.polydiv(a_poly, k_poly)
            flag = 1
            for j in range(len(div[0])):
                if (float(div[0][j]) < 0): flag = 0
            if (float(div[1]) < 0): flag = 0
            if flag:
                upper = k
                break
        return upper

    a1 = list(map(float, a.split()))
    polll = list(map(float, a1))
    if (float(a1[0]) < 0):
        for i in range(len(a1)):
            a1[i] *= -1
    a_poly = np.array(list(a1), dtype=float)
    st = ''
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
        if (i <= len(st) - 3):
            if (st[i] == '1') and (st[i + 3] == "*"):
                st = st[:i] + st[(i + 4):]
    if (st[0] == '+'):
        print("F(x):", st[1:])
    else:
        print("F(x):", st)
    print("Степень многочлена = ", len(a1) - 1)
    upp = -1 * lim(a_poly, nums)
    if (len(a1) - 1) % 2 == 0:
        for i in range(len(a1)):
            if i % 2 != 0:
                a1[i] *= -1
        for i in range(len(a1)):
            a1[i] *= (-1) ** (len(a1) - 1)
    else:
        for i in range(len(a1)):
            if i % 2 == 0:
                a1[i] *= -1
        for i in range(len(a1)):
            a1[i] *= (-1) ** (len(a1) - 1)
    a_poly = np.array(list(a1), dtype=float)
    low = lim(a_poly, nums)
    # print(low)
    print('Верхняя граница = ', upp, ' Нижняя граница = ', low)

def lab1_5(a):
    def f(x, a1):
        k = 0
        for i in range(len(a1)):
            k += float(a1[i]) * (x ** (len(a1) - 1 - i))
        return k

    nums = np.arange(-100, 100, 1).tolist()
    a1 = list(map(float, a.split()))
    polll = list(map(float, a1))
    if (float(a1[0]) < 0):
        for i in range(len(a1)):
            a1[i] *= -1
    st = md.print_poly(polll)
    if (st[0] == '+'):
        print("F(x):", st[1:])
    else:
        print("F(x):", st)
    a_poly = np.array(list(a1), dtype=float)
    print("Степень многочлена = ", len(a1) - 1)
    up = -1 * md.upper(a_poly, nums)
    if (len(a1) - 1) % 2 == 0:
        for i in range(len(a1)):
            if i % 2 != 0:
                a1[i] *= -1
        for i in range(len(a1)):
            a1[i] *= (-1) ** (len(a1) - 1)
    else:
        for i in range(len(a1)):
            if i % 2 == 0:
                a1[i] *= -1
        for i in range(len(a1)):
            a1[i] *= (-1) ** (len(a1) - 1)
    a_poly = np.array(list(a1), dtype=float)
    low = md.upper(a_poly, nums)
    print("Верхняя граница = ", up, "Нижняя граница = ", low)
    x = []
    x1 = md.half_divide_method(up, low, f, polll)
    x.append(x1)
    up1 = up
    up = low + 0.1
    i = 0
    # костыль для поиска всех корней
    while up < up1:
        # костыль для костыля
        if (md.sign(f(low, polll)) != md.sign(f(up, polll))):
            x1 = md.half_divide_method(up, low, f, polll)
            if (type(x1) == float):
                x1 = round(x1, 1)
                x.append(x1)
            if x1 in x:
                low += 0.1
            low = up
            up += 0.1
        else:
            up += 0.1
        i += 1
        if i > 10000: break
    x = np.unique(x)
    print(x)
    x2 = []
    for i in range(len(x)):
        k = 1 * float(x[i])
        k_poly = np.array(list([1, k]), dtype=float)
        div = (np.polydiv(a_poly, k_poly))
        divr = list(div[1])
        if (divr[0] == 0):
            x2.append(x[i])
        # print(divr,x[i],",",a_poly,",",k_poly,",",div)
        while 1:
            if float(divr[0]) != 0: break
            k_poly = np.array(list([1, k]), dtype=float)
            div1 = np.array(list(div[0]), dtype=float)
            div = (np.polydiv(div1, k_poly))
            #   print(div, ",", x[i])
            divr = list(div[1])
            if float(divr[0] == 0):
                x2.append(x[i])
    print("Корни: ", x2)

def lab2_1(a):
    def d_poly_koeffs(a1):
        deg = len(a1) - 1
        k = []
        for i in range(deg):
            k.append(deg * a1[i])
            deg -= 1
        return k

    # значение многочлена в т. x
    def poly(x, poly_koeffs):
        n = len(poly_koeffs)
        deg = n - 1
        p = 0
        if (len(poly_koeffs) != 1):
            for i in range(n):
                xx = x ** deg
                p += poly_koeffs[i] * xx
                deg -= 1
        return p

    a1 = list(map(float, a.split()))
    s = md.print_poly(a1)
    print("F(x)=", s)
    der = d_poly_koeffs(a1)
    s = md.print_poly(der)
    print("F'(x)=", s)

def lab2_2(a,b):
    nums = np.arange(-100, 100, 1).tolist()

    def f(x, a1):
        k = 0
        for i in range(len(a1)):
            k += float(a1[i]) * (x ** (len(a1) - 1 - i))
        return k

    def chord(x_prev, x_curr, f, a1, e=0.001):
        x_next = 0
        while 1:
            tmp = x_next
            if (f(x_prev, a1) - f(x_curr, a1) != 0):
                x_next = x_curr - f(x_curr, a1) * (x_prev - x_curr) / (f(x_prev, a1) - f(x_curr, a1))
            x_prev = x_curr
            x_curr = tmp
            if ((abs(x_next - x_curr) <= e)): break
        return x_next

    a1 = list(map(float, a.split()))
    polll = list(map(float, a1))
    if (float(a1[0]) < 0):
        for i in range(len(a1)):
            a1[i] *= -1
    if (len(a1) - 1) % 2 == 0:
        for i in range(len(a1)):
            if i % 2 != 0:
                a1[i] *= -1
        for i in range(len(a1)):
            a1[i] *= (-1) ** (len(a1) - 1)
    else:
        for i in range(len(a1)):
            if i % 2 == 0:
                a1[i] *= -1
        for i in range(len(a1)):
            a1[i] *= (-1) ** (len(a1) - 1)
    a_poly = np.array(list(a1), dtype=float)
    low = md.upper(a_poly, nums)
    up = float(b) + 0.5
    x = []
    up1 = up - 0.5
    st = md.print_poly(polll)
    if (st[0] == '+'):
        print("F(x)=", st[1:])
    else:
        print("F(x)=", st)
    a_poly = np.array(list(a1), dtype=float)
    print("Степень многочлена = ", len(a1) - 1)
    while low <= up1:
        # print("up1=",up1,"f(up1)=",f(up1,polll),"up=",up,"f(up)=",f(up,polll))
        if (f(up1, polll) * f(up, polll) <= 0):
            x1 = chord(up, up1, f, polll)
            # print(x1)
            x1 = round(x1, 1)
            x.append(x1)
            up = up1
            up1 = up - 0.5
        up1 -= 0.5
        i += 1
        if i > 10000: break
    x = np.unique(x)
    x2 = []
    for i in range(len(x)):
        k = 1 * float(x[i])
        k_poly = np.array(list([1, k]), dtype=float)
        div = (np.polydiv(a_poly, k_poly))
        divr = list(div[1])
        if (divr[0] == 0):
            x2.append(x[i])
        # print(divr,x[i],",",a_poly,",",k_poly,",",div)
        while 1:
            if float(divr[0]) != 0: break
            k_poly = np.array(list([1, k]), dtype=float)
            div1 = np.array(list(div[0]), dtype=float)
            div = (np.polydiv(div1, k_poly))
            #   print(div, ",", x[i])
            divr = list(div[1])
            if float(divr[0] == 0):
                x2.append(x[i])

    print("Корни:", x2)
    print("Максимальный корень:", max(x))

def lab2_3(a,b):
    nums = np.arange(-100, 100, 1).tolist()

    def f(x, a1):
        k = 0
        for i in range(len(a1)):
            k += float(a1[i]) * (x ** (len(a1) - 1 - i))
        return k

    def newton(a, b, f, a1, der, e=0.001):
        try:
            if (f(a, a1) * f(a, d_poly_koeffs(der))) > 0:
                x0 = a
            else:
                x0 = b
            if (f(x0, der) == 0): return x0
            xn = x0 - f(x0, a1) / f(x0, der)
            while abs(x0 - xn) > e:
                x0 = xn
                xn = x0 - f(x0, a1) / f(x0, der)
            return xn
        except ValueError:
            print("Value not invalidate")

    def d_poly_koeffs(a1):
        deg = len(a1) - 1
        k = []
        for i in range(deg):
            k.append(deg * a1[i])
            deg -= 1
        return k

    a1 = list(map(float, a.split()))
    der = d_poly_koeffs(a1)
    polll = list(map(float, a1))
    if (float(a1[0]) < 0):
        for i in range(len(a1)):
            a1[i] *= -1
    if (len(a1) - 1) % 2 == 0:
        for i in range(len(a1)):
            if i % 2 != 0:
                a1[i] *= -1
        for i in range(len(a1)):
            a1[i] *= (-1) ** (len(a1) - 1)
    else:
        for i in range(len(a1)):
            if i % 2 == 0:
                a1[i] *= -1
        for i in range(len(a1)):
            a1[i] *= (-1) ** (len(a1) - 1)
    a_poly = np.array(list(a1), dtype=float)
    low = md.upper(a_poly, nums)
    up = float(b) + 0.5
    x = []
    up1 = up - 0.5
    st = md.print_poly(polll)
    if (st[0] == '+'):
        print("F(x)=", st[1:])
    else:
        print("F(x)=", st)
    a_poly = np.array(list(a1), dtype=float)
    print("Степень многочлена = ", len(a1) - 1)
    while low <= up1:
        # print("up1=",up1,"f(up1)=",f(up1,polll),"up=",up,"f(up)=",f(up,polll))
        if (f(up1, polll) * f(up, polll) <= 0):
            x1 = newton(up, up1, f, polll, der)
            # print(x1)
            x1 = round(x1, 1)
            x.append(x1)
            up = up1
            up1 = up - 0.5
        up1 -= 0.5
        i += 1
        if i > 10000: break
    x = np.unique(x)
    x2 = []
    for i in range(len(x)):
        k = 1 * float(x[i])
        k_poly = np.array(list([1, k]), dtype=float)
        div = (np.polydiv(a_poly, k_poly))
        divr = list(div[1])
        if (divr[0] == 0):
            x2.append(x[i])
        # print(divr,x[i],",",a_poly,",",k_poly,",",div)
        while 1:
            if float(divr[0]) != 0: break
            k_poly = np.array(list([1, k]), dtype=float)
            div1 = np.array(list(div[0]), dtype=float)
            div = (np.polydiv(div1, k_poly))
            #   print(div, ",", x[i])
            divr = list(div[1])
            if float(divr[0] == 0):
                x2.append(x[i])
    print("Корни:", x2)
    print("Максимальный корень:", max(x))

def lab2_4(a1,b):
    def horner(m, x, y):
        while len(m) > 1:
            for i in range(len(m[0])):
                m[0][i] = m[0][i] * x + m[1][i]
            m = m[:1] + m[2:]
        m = m[0]
        while len(m) > 1:
            m[0] *= y
            m[1] += m[0]
            m = m[1:]
        return m
    a = []
    a0 = ''
    for i in range(len(a1)):
        if (a1[i] != ';'):
            a0+=a1[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    print(a)
    m = np.array(a).astype(float).tolist()
    s = ''
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 0:
                if (len(m[i]) - 1 - j) != 0 or ((len(m) - 1 - i) != 0):
                    f = 1
                    if (len(m[i]) - 1 - j) != 0:
                        s += str(m[i][j]) + 'x^' + str(len(m[i]) - j - 1)
                    else:
                        s += str(m[i][j]) + 'y^' + str(len(m) - 1 - i)
                        f = 0
                    if (len(m) - 1 - i) != 0 and (f == 1):
                        s += 'y^' + str(len(m) - 1 - i)
                    s += '+'
                else:
                    s += str(m[i][j])

    for i in range(len(s)):
        if (i < len(s) - 4):
            if (((s[i] == '1') and (s[i + 1] == ".") and (s[i - 1] == '+' or s[i - 1] == '-')) or (
                    (s[i] == '1') and (s[i + 1] == '.') and (s[i + 3] == 'x' or s[i + 3] == 'y'))):
                s = s[:i] + s[(i + 3):]
    for i in range(len(s)):
        if (i < len(s) - 1):
            if (s[i] == '^') and (s[i + 1] == '1'):
                s = s[:i] + s[(i + 2):]
    for i in range(len(s)):
        if (i < len(s) - 1):
            if (s[i] == '+') and (s[i + 1] == '-'):
                s = s[:i] + s[(i + 1):]
    n1 = len(m) * len(m[0])
    x, y = map(float, b.split())
    k = horner(m, y, x)
    ans = float(k[0])
    print("F(x)=", s)
    print("F(x0,y0)=", k)
def lab2_5(a1):
    def dx(m_1):
        m1 = []
        for i in range(len(m_1)):
            m1.append(m_1[i][:(len(m_1[i]) - 1)])
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                m1[i][j] *= (len(m_1[i]) - 1 - j)
        return m1

    def dy(m_2):
        m1 = []
        for i in range(len(m_2) - 1):
            m1.append(m_2[i])
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                m1[i][j] *= (len(m_2) - 1 - i)
        return m1

    def print_poly(m):
        s = ''
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] != 0:
                    if (len(m[i]) - 1 - j) != 0 or ((len(m) - 1 - i) != 0):
                        f = 1
                        if (len(m[i]) - 1 - j) != 0:
                            s += str(m[i][j]) + 'x^' + str(len(m[i]) - j - 1)
                        else:
                            s += str(m[i][j]) + 'y^' + str(len(m) - 1 - i)
                            f = 0
                        if (len(m) - 1 - i) != 0 and (f == 1):
                            s += 'y^' + str(len(m) - 1 - i)
                        s += '+'
                    else:
                        s += str(m[i][j])

        for i in range(len(s)):
            if (i < len(s) - 4):
                if (((s[i] == '1') and (s[i + 1] == ".") and (s[i - 1] == '+' or s[i - 1] == '-')) or (
                        (s[i] == '1') and (s[i + 1] == '.') and (s[i + 3] == 'x' or s[i + 3] == 'y'))):
                    s = s[:i] + s[(i + 3):]
        for i in range(len(s)):
            if (i < len(s) - 1):
                if (s[i] == '^') and (s[i + 1] == '1'):
                    s = s[:i] + s[(i + 2):]
        for i in range(len(s)):
            if (i < len(s) - 1):
                if (s[i] == '+') and (s[i + 1] == '-'):
                    s = s[:i] + s[(i + 1):]
        return s

    a = []
    a0 = ''
    for i in range(len(a1)):
        if (a1[i] != ';'):
            a0 += a1[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    m = np.array(a).astype(float).tolist()
    print(a)
    print("F(x)=", print_poly(m))
    m_1 = m.copy()
    m_2 = m.copy()
    m1 = dx(m_1)
    m2 = dy(m_2)
    print("d/dx=", print_poly(m1), "\nA(d/dx)=", m1)
    print("d/dy=", print_poly(m2), "\nA(d/dy)=", m2)

def lab2_6(a1,b):
    def d_poly_koeffs(a1):
        deg = len(a1) - 1
        k = []
        for i in range(deg):
            k.append(deg * a1[i])
            deg -= 1
        return k

    def print_poly(m):
        s = ''
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] != 0:
                    if (len(m[i]) - 1 - j) != 0 or ((len(m) - 1 - i) != 0):
                        f = 1
                        if (len(m[i]) - 1 - j) != 0:
                            s += str(m[i][j]) + 'x^' + str(len(m[i]) - j - 1)
                        else:
                            s += str(m[i][j]) + 'y^' + str(len(m) - 1 - i)
                            f = 0
                        if (len(m) - 1 - i) != 0 and (f == 1):
                            s += 'y^' + str(len(m) - 1 - i)
                        s += '+'
                    else:
                        s += str(m[i][j])

        for i in range(len(s)):
            if (i < len(s) - 4):
                if (((s[i] == '1') and (s[i + 1] == ".") and (s[i - 1] == '+' or s[i - 1] == '-')) or (
                        (s[i] == '1') and (s[i + 1] == '.') and (s[i + 3] == 'x' or s[i + 3] == 'y'))):
                    s = s[:i] + s[(i + 3):]
        for i in range(len(s)):
            if (i < len(s) - 1):
                if (s[i] == '^') and (s[i + 1] == '1'):
                    s = s[:i] + s[(i + 2):]
        for i in range(len(s)):
            if (i < len(s) - 1):
                if (s[i] == '+') and (s[i + 1] == '-'):
                    s = s[:i] + s[(i + 1):]
        if s[len(s) - 1] == '+':
            s = s[:len(s) - 1]
        return s

    def dx(m):
        m_1 = copy.deepcopy(m)
        m1 = []
        for i in range(len(m_1)):
            m1.append(m_1[i][:(len(m_1[i]) - 1)])
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                m1[i][j] *= (len(m_1[i]) - 1 - j)
        return m1

    def dy(m):
        m_2 = copy.deepcopy(m)
        m1 = []
        for i in range(len(m_2) - 1):
            m1.append(m_2[i])
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                m1[i][j] *= (len(m_2) - 1 - i)
        return m1

    def f1(x, y, m):
        k = 0
        for i in range(len(m)):
            for j in range(len(m[i])):
                k += float(m[i][j]) * (x ** (len(m[i]) - j - 1) * (y ** (len(m) - 1 - i)))
        return k

    def f2(x, a1):
        k = 0
        for i in range(len(a1)):
            k += float(a1[i]) * (x ** (len(a1) - 1 - i))
        return k

    def J(xn, yn, m1, m2, f):
        l = f1(xn, yn, dx(m1)) * f1(xn, yn, dy(m2)) - f1(xn, yn, dy(m1)) * f1(xn, yn, dx(m2))
        return l

    def horner(m1, x, y):
        m = copy.deepcopy(m1)
        while len(m) > 1:
            for i in range(len(m[0])):
                m[0][i] = m[0][i] * x + m[1][i]
            m = m[:1] + m[2:]
        m = m[0]
        '''
        while len(m)>1:
            m[0]*=y
            m[1]+=m[0]
            m = m[1:]
        '''
        return m

    def fsolve(m_1, x1, m_2, x2, f1):
        m1 = copy.deepcopy(m_1)
        m2 = copy.deepcopy(m_2)
        eps = 0.000001
        # print("//////////",m1,m2)
        while 1:
            xprev = x1
            yprev = x2
            hn = -1.0 / J(x1, x2, m1, m2, f1) * (
                        f1(x1, x2, m1) * f1(x1, x2, dy(m2)) - f1(x1, x2, dy(m1)) * f1(x1, x2, m2))
            kn = -1.0 / J(x1, x2, m1, m2, f1) * (
                        f1(x1, x2, dx(m1)) * f1(x1, x2, m2) - f1(x1, x2, m1) * f1(x1, x2, dx(m2)))
            x1 += hn
            x2 += kn
            if (abs(x2 - yprev) < eps):
                break
        roots = [round(x1, 5), round(x2, 5)]
        return roots

    def complex_roots(p):

        p = p.copy()
        p = p.astype(np.complex64)
        non_zero = np.nonzero(p)[0]

        if len(non_zero) == 0:
            return np.zeros(0, dtype=p.dtype)

        trailing_zeros = len(p) - non_zero[-1] - 1

        p = p[int(non_zero[0]):int(non_zero[-1]) + 1]

        N = len(p)
        if N > 1:
            A = np.diag(np.ones((N - 2,), p.dtype), -1)
            A[0, :] = -p[1:] / p[0]
            roots, _ = np.linalg.eig(A)
        else:
            roots = np.zeros(0, dtype=p.dtype)

        for k in range(roots.shape[0]):
            if abs(roots[k].imag) < 1.0E-6:
                roots[k] = complex(roots[k].real, 0.0)
        for k in range(roots.shape[0]):
            if abs(roots[k].real) < 1.0E-6:
                roots[k] = complex(0.0, roots[k].imag)

        roots = np.concatenate((roots, np.zeros(trailing_zeros, roots.dtype)))

        return roots

    a = []
    a0 = ''
    for i in range(len(a1)):
        if (a1[i] != ';'):
            a0 += a1[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    m = np.array(a).astype(float).tolist()
    a = []
    a0 = ''
    for i in range(len(b)):
        if (b[i] != ';'):
            a0 += b[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    m1 = np.array(a).astype(float).tolist()

    n1 = len(m) * len(m[0])
    # x,y=map(float,input().split())
    # k = horner(m,0,1)
    # ans = float(k[0])
    #ans = np.array(k)
    print("F(x,y)=", print_poly(m))
    print("G(x,y)=", print_poly(m1))
    # print("SSSSSSSs",m,m1)
    # print(f1(x,y,m1))
    '''
    m = [[0, 0, 0, -1.0], [0, 0, 0, 0], [2.0, 0, 0, -1.0]]
    m1 = [[1.0, 0], [0, 0], [0, -1.0], [0, -4.0]]
    '''
    roots = []
    x = -25.0
    y = -25.0
    roots.append(fsolve(m, x, m1, y, f1))
    x1 = x
    y1 = y
    # супер костыль
    for i in range(100):
        y += 0.5
        k = fsolve(m, x, m1, y, f1)
        if k not in roots:
            roots.append(k)
    y = y1
    for i in range(100):
        x += 0.5
        k = fsolve(m, x, m1, y, f1)
        if k not in roots:
            roots.append(k)
    x = 25
    y = 25
    x1 = x
    y1 = y
    for i in range(100):
        y -= 0.5
        k = fsolve(m, x, m1, y, f1)
        if k not in roots:
            roots.append(k)
    y = y1
    for i in range(100):
        x -= 0.5
        k = fsolve(m, x, m1, y, f1)
        if k not in roots:
            roots.append(k)
    # конец костыля
    roots1 = []
    for i in range(len(roots)):
        if (f1(roots[i][0], roots[i][1], m) < 0.001 and f1(roots[i][0], roots[i][1], m1) < 0.001):
            roots1.append(roots[i])
    print("Real roots [x_i,y_i]:", roots1)
    for i in range(len(roots) - 1):
        k = horner(m, roots[i][1], 1)
        if ((f2(-10000, k) > 0 and f2(roots[i][1], d_poly_koeffs(k)) > 0 and f2(10000, k) > 0) or (
                f2(-10000, k) > 0 and f2(roots[i][1], d_poly_koeffs(k)) > 0 and f2(10000, k) > 0)):
            r = complex_roots(np.array(k))
            print("Complex roots:\n x_i = ", r)
            y_i = []
            for p in range(len(r)):
                y_i.append(roots[i][1])
            print(" y_i = ", y_i)
            break

def lab3_1(a1,b):
    def r(a):
        a = np.array(a)
        # print(a)
        k = []
        # print(a[0:int((len(a))//2),0:int((len(a[0]))//2)])
        m = a[0:int((len(a)) // 2), 0:int((len(a[0])) // 2)]
        # print(m)
        k.append([])
        k[0].append([])
        k[0][0] = m
        m = a[0:int(((len(a)) // 2)), int((len(a[0])) // 2):]
        k[0].append([])
        k[0][1] = m
        m = a[int((len(a)) // 2):, 0:int((len(a[0])) // 2)]
        k.append([])
        k[1].append([])
        k[1][0] = m
        m = a[int((len(a)) // 2):, int((len(a[0])) // 2):]
        k[1].append([])
        k[1][1] = m
        # k = [x for x in k if len(x)>0]
        return k

    def mult(a1, a2, m1, m2):
        c = []
        c.append([])
        c[0].append([0])
        c[0].append([0])
        c.append([])
        c[1].append([0])
        c[1].append([0])
        # print(c,len(a1),len(a2),len(c),len(c[0]))
        for i in range(len(a1)):
            for k in range(len(a2[0])):
                l = 0
                for q in range(len(a1)):
                    # print("I = %s Q = %s K = %s, a1[i][q] = %s,a2[q][k] = %s , np.dot = %s\n" % (i,q,k,a1[i][q],a2[q][k],np.dot(a1[i][q],a2[q][k])))
                    c[i][k] += (np.dot(a1[i][q], a2[q][k]))
        c[0] = np.concatenate((c[0][0], c[0][1]), axis=1)
        c[1] = np.concatenate((c[1][0], c[1][1]), axis=1)
        c = np.concatenate((c[0], c[1]), axis=0)
        return c

    a = []
    a0 = ''
    for i in range(len(a1)):
        if (a1[i] != ';'):
            a0 += a1[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    m = np.array(a).astype(float).tolist()
    a = []
    a0 = ''
    for i in range(len(b)):
        if (b[i] != ';'):
            a0 += b[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    m1 = np.array(a).astype(float).tolist()

    n1 = len(m) * len(m[0])
    # print("F(x,y)=",print_poly(m))
    # print("G(x,y)=",print_poly(m1))
    k1 = r(m)
    # print("K1=",k1[0],k1[1],len(k1),k1)
    # print("////////////////")
    k2 = r(m1)
    # print("K2 = ",k2)
    print(mult(k1, k2, m, m1))

def lab3_2(a_1):
    def mult(a1, a2):
        c = []
        c.append([])
        c[0].append([0])
        c[0].append([0])
        c.append([])
        c[1].append([0])
        c[1].append([0])
        # print(c,len(a1),len(a2),len(c),len(c[0]))
        for i in range(len(a1)):
            for k in range(len(a2[0])):
                l = 0
                for q in range(len(a1)):
                    # print("I = %s Q = %s K = %s, a1[i][q] = %s,a2[q][k] = %s , np.dot = %s\n" % (i,q,k,a1[i][q],a2[q][k],np.dot(a1[i][q],a2[q][k])))
                    c[i][k] += (np.dot(a1[i][q], a2[q][k]))
        c[0] = np.concatenate((c[0][0], c[0][1]), axis=1)
        c[1] = np.concatenate((c[1][0], c[1][1]), axis=1)
        c = np.concatenate((c[0], c[1]), axis=0)
        return c

    class matrix:
        def __init__(self):
            self.values = []

        def block(self, x):
            a = np.array(x)
            # print(a)
            k = []
            # print(a[0:int((len(a))//2),0:int((len(a[0]))//2)])
            m = a[0:int((len(a)) // 2), 0:int((len(a[0])) // 2)]
            # print(m)
            k.append([])
            k[0].append([])
            k[0][0] = m
            m = a[0:int(((len(a)) // 2)), int((len(a[0])) // 2):]
            k[0].append([])
            k[0][1] = m
            m = a[int((len(a)) // 2):, 0:int((len(a[0])) // 2)]
            k.append([])
            k[1].append([])
            k[1][0] = m
            m = a[int((len(a)) // 2):, int((len(a[0])) // 2):]
            k[1].append([])
            k[1][1] = m
            return k

        def rev(self):
            block = self.block(self.values)
            X = np.dot(block[0][0], block[0][1])
            Y = np.dot(block[1][0], np.linalg.inv(block[0][0]))
            theta = block[1][1] - np.dot(Y, block[0][1])
            theta = np.linalg.inv(theta)
            A_inv = []
            A_inv.append([])
            A_inv[0].append([])
            A_inv[0][0] = np.linalg.inv(block[0][0]) + mult(self.block(mult(self.block(X), self.block(theta))),
                                                            self.block(Y))
            A_inv[0].append([])
            A_inv[0][1] = mult(self.block(-X), self.block(theta))
            A_inv.append([])
            A_inv[1].append([])
            A_inv[1][0] = mult(self.block(-theta), self.block(Y))
            A_inv[1].append([])
            A_inv[1][1] = theta
            # print(theta,"\n",Y)
            A_inv[0] = np.concatenate((A_inv[0][0], A_inv[0][1]), axis=1)
            A_inv[1] = np.concatenate((A_inv[1][0], A_inv[1][1]), axis=1)
            A_inv = np.concatenate((A_inv[0], A_inv[1]), axis=0)
            return A_inv

        def getMatrixMinor(self, m, i, j):
            return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

        def getMatrixDeternminant(self, m):
            if len(m) == 2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]

            determinant = 0
            for c in range(len(m)):
                determinant += ((-1) ** c) * m[0][c] * self.getMatrixDeternminant(self.getMatrixMinor(m, 0, c))
            return determinant

    a1 = matrix()
    a = []
    a0 = ''
    for i in range(len(a_1)):
        if (a_1[i] != ';'):
            a0 += a_1[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    m = np.array(a).astype(float).tolist()
    a1.values = m
    if (a1.getMatrixDeternminant(a1.values)) != 0:
        print("A^(-1)=", a1.rev())
        print("det(A)=%s" % a1.getMatrixDeternminant(a1.values))
    else:
        print("Не существует")
        print("det(A)=%s" % a1.getMatrixDeternminant(a1.values))
def lab4_1(a2):
    def coeffs(traces):
        a = []
        for i in range(len(traces)):
            a_i = traces[i]
            for j in range(len(a)):
                a_i += a[j] * traces[len(a) - j - 1]
                # print("tr = ",traces[-j])
                # print("a_i=",a[j])
            a_i = -a_i / (i + 1)
            # print(a_i,'//////////////')
            a.append(a_i)
            # print('lena=',len(a),'///////////////')
        return a

    class matrix:
        def __init__(self):
            self.values = []


        def getMatrixMinor(self, m, i, j):
            return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

        def getMatrixDeternminant(self, m):
            if len(m) == 2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]

            determinant = 0
            for c in range(len(m)):
                determinant += ((-1) ** c) * m[0][c] * self.getMatrixDeternminant(self.getMatrixMinor(m, 0, c))
            return determinant

    a1 = matrix()
    a = []
    a0 = ''
    for i in range(len(a2)):
        if (a2[i] != ';'):
            a0 += a2[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    m = np.array(a).astype(float).tolist()
    a1.values = m
    a_1 = []
    a_1.append(a1.values)
    traces = []
    for i in range(len(a1.values) - 1):
        a_1.append(np.dot(a_1[i], a1.values))
        traces.append(np.trace(a_1[i]))
    traces.append(np.trace(a_1[-1]))
    # print(a_1,traces)
    coef = coeffs(traces)
    coef = [1] + coef
    print(coef)
    print(md.print_poly(coef))
def lab4_2(a2):
    def coeffs(traces):
        a = []
        for i in range(len(traces)):
            a_i = traces[i]
            for j in range(len(a)):
                a_i += a[j] * traces[len(a) - j - 1]
                # print("tr = ",traces[-j])
                # print("a_i=",a[j])
            a_i = -a_i / (i + 1)
            # print(a_i,'//////////////')
            a.append(a_i)
            # print('lena=',len(a),'///////////////')
        return a

    class matrix:
        def __init__(self):
            self.values = []

        def getMatrixMinor(self, m, i, j):
            return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

        def getMatrixDeternminant(self, m):
            if len(m) == 2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]

            determinant = 0
            for c in range(len(m)):
                determinant += ((-1) ** c) * m[0][c] * self.getMatrixDeternminant(self.getMatrixMinor(m, 0, c))
            return determinant

    a1 = matrix()
    a = []
    a0 = ''
    for i in range(len(a2)):
        if (a2[i] != ';'):
            a0 += a2[i]
        else:
            a.append(list((a0.split())))
            a0 = ''
    a.append(list(a0.split()))
    m = np.array(a).astype(float).tolist()
    a1.values = m
    a_1 = []
    a_1.append(a1.values)
    traces = []
    for i in range(len(a1.values) - 1):
        a_1.append(np.dot(a_1[i], a1.values))
        traces.append(np.trace(a_1[i]))
    traces.append(np.trace(a_1[-1]))
    # print(a_1,traces)
    coef = coeffs(traces)
    coef = [1] + coef
    print(coef)
    print(md.print_poly(coef))
    k = np.unique(np.roots(coef))
    k1=[]
    k2=[]
    for i in range(len(k)):
        if abs(k[i].imag)<0.00001:
            k1.append(k[i].real)
        else:
            k2.append(k[i])
    print("real λ_i = ", k1)
    print("complex λ_i =",k2)
    print("max λ = ",max(k1))

def cmp(a, b):
    return (a > b) - (a < b)

class NumericStringParser(object):

    def pushFirst(self, strg, loc, toks):
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        if toks and toks[0] == '-':
            self.exprStack.append('unary -')

    def __init__(self):
        point = Literal(".")
        e = CaselessLiteral("E")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))) +
                          Optional(e + Word("+-" + nums, nums)))
        ident = Word(alphas, alphas + nums + "_$")
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        pi = CaselessLiteral("PI")
        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                 (ident + lpar + expr + rpar | pi | e | fnumber).setParseAction(self.pushFirst))
                | Optional(oneOf("- +")) + Group(lpar + expr + rpar)
                ).setParseAction(self.pushUMinus)
        factor = Forward()
        factor << atom + \
        ZeroOrMore((expop + factor).setParseAction(self.pushFirst))
        term = factor + \
               ZeroOrMore((multop + factor).setParseAction(self.pushFirst))
        expr << term + \
        ZeroOrMore((addop + term).setParseAction(self.pushFirst))
        self.bnf = expr
        epsilon = 1e-12
        self.opn = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "^": operator.pow}
        self.fn = {"sin": math.sin,
                   "cos": math.cos,
                   "tan": math.tan,
                   "exp": math.exp,
                   "log": math.log,
                   "abs": abs,
                   "trunc": lambda a: int(a),
                   "round": round,
                   "sgn": lambda a: abs(a) > epsilon and cmp(a, 0) or 0}

    def evaluateStack(self, s):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack(s)
        if op in "+-*/^":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        elif op == "PI":
            return math.pi  # 3.1415926535
        elif op == "E":
            return math.e  # 2.718281828
        elif op == "j":
            return complex(0, 1)
        elif op in self.fn:
            return self.fn[op](self.evaluateStack(s))
        elif op[0].isalpha():
            return 0
        else:
            return float(op)

    def eval(self, num_string, parseAll=True):
        self.exprStack = []
        results = self.bnf.parseString(num_string, parseAll)
        val = self.evaluateStack(self.exprStack[:])
        return val

def lab5_1(s,s1):
    import numpy as np
    import sympy

    def f(x, func):
        nsp = NumericStringParser()
        func = func.replace('x', str(x))
        func = func.replace('-e', '-1*e')
        func = func.replace('**', '^')
        return nsp.eval(func)

    def dx(func):
        x, y = sympy.symbols('x y')
        func = func.replace('e^(', 'exp(')
        d_x = sympy.diff(func, x)
        d_x = str(d_x)
        d_x = d_x.replace('exp', 'e^')
        d_x = d_x.replace('**', '^')
        return d_x
    plt.close()
    a,b,step = map(float,s1.split())
    y = []
    x = np.arange(a, b, step)
    for i in range(len(x)):
        y.append(f(x[i], s))
    plt.plot(x, y,label='y(x)')
    y1 =[]
    k = dx(s)
    for i in range(len(x)):
        y1.append(f(x[i],k))
    print("d/dx(f(x)) = ",dx(s))
    plt.plot(x,y1,'go-',label = 'y\'(x)')
    plt.legend()
    plt.show()

def lab5_2(s,s1):
    def integrate(y, a, b):
        sigma2 = 0
        for i in range(2, len(y) - 2, 2):
            sigma2 += y[i]
        sigma1 = 0
        for i in range(1, len(y), 2):
            sigma1 += y[i]
        return ((b - a) / (len(y) - 1)) / 3 * (y[0] + y[-1] + 4 * sigma1 + 2 * sigma2)

    def f(x, func):
        nsp = NumericStringParser()
        func = func.replace('-x','-1*x')
        func = func.replace('x', str(x))
        func = func.replace('-e', '-1*e')
        func = func.replace('**', '^')
        return nsp.eval(func)

    y=[]
    a, b, h = map(float, s1.split())
    x = np.arange(a, b + h, h)
    for i in range(len(x)):
        y.append(f(x[i],s))
    f1 = lambda x:x if abs(x)<1e+10 else "integral does not converge"
    print("∫(%s)dx from %s to %s = %s"%(s,a,b,f1(integrate(y,a,b))))

def laba6_1(a1):
    polll = list(map(float, a1))
    a_poly = np.array(list(a1), dtype=float)
    print("F(x)=", md.print_poly(a1))
    print("Степень многочлена = ", len(a1) - 1)
    if a1[len(a1) - 1] == 0:
        a1 = a1[:len(a1) - 1]
    # print(a1)
    low = 1.0 / (1.0 + float(abs(max((a1[:(len(a1) - 1)]), key=abs))) / float(abs(a1[len(a1) - 1])))
    up = 1.0 + float(abs(max(a1[1:], key=abs))) / abs(a1[0])
    print("Границы положительных корней=", up, low)
    print("Границы отрицательных корней=", -up, -low)

def laba6_2(a1):
    if (float(a1[0]) < 0):
        for i in range(len(a1)):
            a1[i] *= -1
    print("F(x)=", md.print_poly(a1))
    polll = list(map(float, a1))
    a_poly = np.array(list(a1), dtype=float)
    if a1[len(a1) - 1] == 0:
        a1 = a1[:len(a1) - 1]
    for i in range(len(a1)):
        if a1[i] < 0:
            first = i
            B = a1[i]
            break
    for i in range(len(a1)):
        if a1[i] < B:
            B = a1[i]
    # print(a1)
    up = 1.0 + (abs(B) / a1[0]) ** (1 / first)
    print(up)

def laba6_3(a1):
    def d_poly_koeffs(a1):
        deg = len(a1) - 1
        k = []
        for i in range(deg):
            k.append(deg * a1[i])
            deg -= 1
        return k

    def f(x, a1):
        k = 0
        for i in range(len(a1)):
            k += float(a1[i]) * (x ** (len(a1) - 1 - i))
        return k
    print("F(x)=", md.print_poly(a1))
    if (float(a1[0]) < 0):
        for i in range(len(a1)):
            a1[i] *= -1
    polll = list(map(float, a1))
    a_poly = np.array(list(a1), dtype=float)
    c = list(range(1, 100))
    for i in range(len(c)):
        flag = 1
        der = copy.deepcopy(a1)
        if f(c[i], der) < 0: continue
        for j in range(len(der)):
            der = d_poly_koeffs(der)
            if f(c[i], der) < 0:
                flag = 0
                break
        if flag == 1:
            up = c[i]
            break
    try:
        print(up)
    except:
        print("NONE")
