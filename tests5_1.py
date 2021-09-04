# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: C:\Users\Professional\PycharmProjects\pythonProject2\tests5_1.py
# Compiled at: 2021-04-20 11:14:57
# Size of source mod 2**32: 3732 bytes
import matplotlib.pyplot as plt
import numpy as np

def lab5_1tests(a):
    plt.figure(1)
    if a == 1:
        plt.close()
        y = [-0.008, -0.066, -0.209, -0.439, -0.734, -1.044, -1.31, -1.484, -1.542, -1.491, -1.366, -1.218, -1.093, -1.02, -0.998, -1,
         -0.982, -0.901, -0.733, -0.479, -0.174, 0.128, 0.372, 0.513, 0.537, 0.46, 0.323, 0.177, 0.065, 0.009, -0.002]
        print('range of x [-3;3], step = 0.2')
        print('y = ', y)
        x = np.arange(-3, 3.2, 0.2)
        dy = np.diff(y)
        y1 = []
        y1.append(dy)
        for i in range(len(y) - 2):
            dy = np.diff(dy)
            y1.append(dy)

        dy = []
        k = 0
        for j in range(len(y1[0])):
            m = 0
            for i in range(3):
                if k < len(y1[i]):
                    m += (-1) ** i * y1[i][k] / (i + 1)

            k += 1
            dy.append(m / 0.2)

        plt.plot(x, y, 'go-', label='y(x)')
        plt.plot((x[:len(x) - 1]), dy, 'r-', label="y'(x)")
        plt.legend()
        plt.show()
    if a == 2:
        plt.close()
        y = [-5, -4.597, -4.178, -3.727, -3.234, -2.688, -2.082, -1.411, -0.674, 0.131, 1, 1.929, 2.91,
         3.935, 4.99, 6.063, 7.134, 8.187, 9.198, 10.145, 11]
        x = np.arange(0, 2.1, 0.1)
        print('range of x [0;2], step = 0.1')
        print('y = ', y)
        dy = np.diff(y)
        y1 = []
        y1.append(dy)
        for i in range(len(y) - 2):
            dy = np.diff(dy)
            y1.append(dy)

        dy = []
        k = 0
        for j in range(len(y1[0])):
            m = 0
            for i in range(1):
                if k < len(y1[i]):
                    m += (-1) ** i * y1[i][k] / (i + 1)

            k += 1
            dy.append(m / 0.1)

        plt.plot(x, y, 'go-', label='y(x)')
        plt.plot((x[:len(x) - 1]), dy, 'r-', label="y'(x)")
        plt.legend()
        plt.show()
    if a == 3:
        plt.close()
        y = [0, 1.483, 2.739, 3.782, 4.647, 5.437, 6.363, 7.723, 9.749, 12.314, 14.659, 15.538,
         14.109, 11.222, 9.578, 11.331, 14.75, 15.096, 11.393, 9.66, 13.403]
        x = np.arange(0, 4.2, 0.2)
        print('range of x [0;4], step = 0.2')
        print('y = ', y)
        dy = np.diff(y)
        y1 = []
        y1.append(dy)
        for i in range(len(y) - 2):
            dy = np.diff(dy)
            y1.append(dy)

        dy = []
        k = 0
        for j in range(len(y1[0])):
            m = 0
            for i in range(1):
                if k < len(y1[i]):
                    m += (-1) ** i * y1[i][k] / (i + 1)

            k += 1
            dy.append(m / 0.2)

        plt.plot(x, y, 'go-', label='y(x)')
        plt.plot((x[:len(x) - 1]), dy, 'r-', label="y'(x)")
        plt.legend()
        plt.show()
    if a == 4:
        plt.close()
        y = [-4.045, 1.782, 2.279, 2.398, 2.322, 2.109, 1.784, 1.355, 0.83,
         0.281, 0, 0.281, 0.83, 1.355, 1.784, 2.109, 2.322, 2.398, 2.279, 1.782, -4.045]
        x = np.arange(-3, 3.3, 0.3)
        print('range of x [-3;3], step = 0.3')
        print('y = ', y)
        dy = np.diff(y)
        y1 = []
        y1.append(dy)
        for i in range(len(y) - 2):
            dy = np.diff(dy)
            y1.append(dy)

        dy = []
        k = 0
        for j in range(len(y1[0])):
            m = 0
            for i in range(1):
                if k < len(y1[i]):
                    m += (-1) ** i * y1[i][k] / (i + 1)

            k += 1
            dy.append(m / 0.3)

        plt.plot(x, y, 'go-', label='y(x)')
        plt.plot((x[:len(x) - 1]), dy, 'r-', label="y'(x)")
        plt.legend()
        plt.show()