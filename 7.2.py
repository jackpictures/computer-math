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






if __name__=="main":
    x0 = 0
    y0 = 1
    z0 = 2
    h = 0.1
    yk=[]
    x = np.arange(0,1+h,h)
    y = [(math.cos(2*i)+math.sin(2*i))/(math.cos(i)) for i in x]
    print(x)
    print("\t" + "x_i" + "\t\t\t\t" + "y_i" + "\t\t\t\t" + "z_i" + "\t\t\t\t" + "k1" + "\t\t\t\t\t" + "k2" + "\t\t\t\t\t" + "k3" + "\t\t\t\t\t" + "k4" + "\t\t\t\t\t" + "y1")
    while x0<1.:
        k1 = h * f(x0,y0,z0)
        m1 = h * f1(x0,y0,z0)

        k2 = h * f(x0 + h/2,y0 + m1/2, z0 + k1/2)
        m2 = h * f1(x0 + h/2,y0 + m1/2, z0 + k1/2)

        k3 = h * f(x0 + h/2,y0 + m2/2,z0 + k2/2)
        m3 = h * f1(x0 + h/2,y0 + m2/2,z0 + k2/2)

        k4 = h * f(x0 + h,y0 + m3,z0 + k3)
        m4 = h * f1(x0 + h,y0 + m3,z0 + k3)

        z1 = (k1 + 2 * k2 + 2 * k3 + k4)/6
        y1 = (m1 + 2 * m2 + 2 * m3 + m4)/6
        yk.append((y0))
        print("\t" + str(round(x0, 4)) + "\t\t\t\t" + str(toFixed(y0, 5)) + "\t\t\t" + str(toFixed(z0,5)) + "\t\t\t" + str(toFixed(k1, 5)) + "\t\t\t" + str(
            toFixed(k2, 5)) + "\t\t\t" + str(toFixed(k3, 5)) + "\t\t\t" + str(toFixed(k4, 5)) + "\t\t\t" + str(
            toFixed(y1, 5)))
        y0 += y1
        z0 += z1
        x0+=h
    print("точное значение y=",y)
    print("приближенное значение y=",yk)
    plt.plot(x,y,label="точное значение y")
    plt.plot(x,yk,label="приближенное значение y")
    plt.legend()
    plt.show()