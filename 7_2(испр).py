import math
import numpy as np
import matplotlib.pyplot as plt

__name__="main"

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def f1(x,y,z):
    return z

def f(x,y,z):
    return 2*math.tan(x)*z-3*y


def Runge(x0,y0,z0,h):
    yk = []
    der = []
    print(
        "\t" + "x_i" + "\t\t\t\t" + "y_i" + "\t\t\t\t" + "z_i" + "\t\t\t\t" + "k1" + "\t\t\t\t\t" + "k2" + "\t\t\t\t\t" + "k3" + "\t\t\t\t\t" + "k4" + "\t\t\t\t\t" + "y1")
    while x0 < 1.:
        k1 = h * f(x0, y0, z0)
        m1 = h * f1(x0, y0, z0)

        k2 = h * f(x0 + h / 2, y0 + m1 / 2, z0 + k1 / 2)
        m2 = h * f1(x0 + h / 2, y0 + m1 / 2, z0 + k1 / 2)

        k3 = h * f(x0 + h / 2, y0 + m2 / 2, z0 + k2 / 2)
        m3 = h * f1(x0 + h / 2, y0 + m2 / 2, z0 + k2 / 2)

        k4 = h * f(x0 + h, y0 + m3, z0 + k3)
        m4 = h * f1(x0 + h, y0 + m3, z0 + k3)

        z1 = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y1 = (m1 + 2 * m2 + 2 * m3 + m4) / 6
        yk.append((y0))
        der.append(z0)
        print("\t" + str(round(x0, 4)) + "\t\t\t\t" + str(toFixed(y0, 5)) + "\t\t\t" + str(
            toFixed(z0, 5)) + "\t\t\t" + str(toFixed(k1, 5)) + "\t\t\t" + str(
            toFixed(k2, 5)) + "\t\t\t" + str(toFixed(k3, 5)) + "\t\t\t" + str(toFixed(k4, 5)) + "\t\t\t" + str(
            toFixed(y1, 5)))
        y0 += y1
        z0 += z1
        x0 += h
    return [yk, der]

def Euler_method(x0, y0, z0,h):
    function = []
    function.append(y0)
    while x0<1:
        y0 += h*f1(x0, y0, z0)
        z0 += h*f(x0, y0, z0)
        x0 += h
        function.append(y0)
    print(len(function))
    return function[:-1]

def Euler_modified(x0, y0, z0,h):
    function = []
    derivative = [z0]
    function.append(y0)
    while x0<1:
        y0 += 0.5*h*(f1(x0, y0, z0) + f1(x0+h, y0+h*f1(x0, y0, z0), z0+h*f(x0, y0, z0)))
        z0 += 0.5*h*(f(x0, y0, z0) + f(x0+h, y0+h*f(x0, y0, z0), z0+h*f(x0, y0, z0)))
        x0 += h
        function.append(y0)
        derivative.append(z0)
    return function[:-1]

def Adams(x0, y0, z0, step):
    m=int((1 - x0)/h)
    y = y0
    z = z0
    function = []
    function.append(y0)
    derrivative = [z0]
    runge = Runge(x0, y0, z0, h)
    for i in range(1, 4):
        x0 += h
        function.append(runge[0][i])
        derrivative.append(runge[1][i])
    y = runge[0][3]
    z = runge[1][3]
    for i in range(4, m+1):
        z += h*(55*f(x0 - h, function[i-1], derrivative[i-1]) - 59*f(x0-2*step, function[i-2], derrivative[i-2]) + 37*f(x0-3*step, function[i-3], derrivative[i-3]) - 9*f(x0-4*step, function[i-4], derrivative[i-4]))/24
        y += h*(55*f1(x0 - h, function[i-1], derrivative[i-1]) - 59*f1(x0-2*step, function[i-2], derrivative[i-2]) + 37*f1(x0-3*step, function[i-3], derrivative[i-3]) - 9*f1(x0-4*step, function[i-4], derrivative[i-4]))/24
        x0 += h
        derrivative.append(z)
        function.append(y)
    return function

if __name__=="main":
    x0 = 0
    y0 = 1
    z0 = 2
    h = 0.1
    x = np.arange(0,1+h,h)
    print(len(x))
    y = [(math.cos(2*i)+math.sin(2*i))/(math.cos(i)) for i in x]
    plt.plot(x,y,label="точное значение")
    plt.plot(x,Runge(x0,y0,z0,h)[0],label="Метод Рунге-Кутта")
    plt.plot(x,Euler_method(x0,y0,z0,h),label = "Метод Эйлера")
    plt.plot(x,Euler_modified(x0,y0,z0,h),label="Модифицированный метод Эйлера")
    plt.plot(x,Adams(x0,y0,z0,h),label='Метод Адамса')
    plt.legend()
    plt.show()