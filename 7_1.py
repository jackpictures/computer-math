import math
import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return (x**2 * y**2 + x**2)
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"



def Euler_modified(x0, y0, x, step):
    m = int(((x - x0) / step))
    y = y0
    function_grid = []
    function_grid.append(y)
    for _ in range(1, m + 1):
        y += 0.5 * step * (f(x0, y) + f(x0 + step, y + step * f(x0, y)))
        x0 += step
        function_grid.append(y)
    return function_grid

def Runge(x0,y0,h):
    yk = []
    #print("\t" + "x_i" + "\t\t\t\t" + "y_i" + "\t\t\t\t" + "k1" + "\t\t\t\t" + "k2" + "\t\t\t\t" + "k3" + "\t\t\t\t" + "k4" + "\t\t\t\t" + "y1")
    while x0<1:
        k1 = f(x0,y0)
        k2 = f(x0 + h/2,y0 + h*k1/2)
        k3 = f(x0 + h/2, y0 + h*k2/2)
        k4 = f(x0 + h,y0 + h*k3)
        y1 = h*(k1 + 2.0 * k2 + 2.0 * k3 + k4)/6
       # print("\t" + str(round(x0,4)) + "\t\t\t\t" + str(toFixed(y0,5)) + "\t\t\t" + str(toFixed(k1,5)) + "\t\t\t" + str(toFixed(k2,5)) + "\t\t\t" + str(toFixed(k3,5)) + "\t\t\t" + str(toFixed(k4,5)) + "\t\t\t" + str(toFixed(y1,5)))
        yk.append(y0)
        y0 += y1
        x0+=h
    return yk
def Euler_method(x0, y0, x, step):
    m = int(((x - x0) / step))
    y = y0
    function_grid = []
    function_grid.append(y)
    for _ in range(1, m + 1):
        y += step * f(x0, y)
        x0 += step
        function_grid.append(y)
    return function_grid

def Adams(x0, y0, x, step):
    m = int(((x - x0) / step))
    y = y0
    function = []
    function.append(y)
    runge_kutt = Runge(x0, y0, step)


    for i in range(1, 4):
        x0 += step
        function.append(runge_kutt[i])
    y = runge_kutt[3]
    for i in range(4, m + 1):
        y += step * (55 * f(x0 - step, function[i - 1]) - 59 * f(x0 - 2 * step, function[i - 2]) + 37 * f(x0 - 3 * step,
                                                                                                          function[
                                                                                                              i - 3]) - 9 * f(
            x0 - 4 * step, function[i - 4])) / 24
        x0 += step
        function.append(y)
    return function


x0 = 0
y0 = 0
h = 0.1
x=1

#print(y0)
#print(math.tan((0.3**3)/3))
x1 = np.arange(0,1+h,h)
y = [math.tan(x**3/3) for x in x1]
plt.plot(x1,y,label='точное решение')
plt.plot(x1,Runge(x0,y0,h),label='Рунге-Кутта')
k = Runge(x0,y0,h)
plt.plot(x1,Euler_method(x0,y0,x,h),label='Метод Эйлера')
plt.plot(x1,Euler_modified(x0,y0,x,h),label = 'Модифицированный метод Эйлера')
plt.plot(x1,Adams(x0,y0,x,h),label = 'Метод Адамса')
plt.legend()
plt.xlim([0, 1])
plt.show()
