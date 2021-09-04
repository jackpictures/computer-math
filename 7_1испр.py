import math
import matplotlib.pyplot as plt


def f(x, y):
    return (x**2 * y**2 + x**2)


def F(x):
    return math.tan(x**3/3)


def Euler_method_modified(x0, y0, x, step):
    m = int(((x - x0) / step))
    y = y0
    function_grid = []
    function_grid.append(y)
    for _ in range(1, m + 1):
        y += 0.5 * step * (f(x0, y) + f(x0 + step, y + step * f(x0, y)))
        x0 += step
        function_grid.append(y)
    return function_grid


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


def Runge_Kutta_45(x0, y0, x, step):
    m = int(((x - x0) / step))
    y = y0
    function = []
    function.append(y)
    for _ in range(1, m + 1):
        k1 = step * f(x0, y)
        k2 = step * f(x0 + 0.5 * step, y + 0.5 * k1)
        k3 = step * f(x0 + 0.5 * step, y + 0.5 * k2)
        k4 = step * f(x0 + step, y + k3)

        y += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        function.append(y)
        x0 += step
    return function


def Adams_method(x0, y0, x, step):
    m = int(((x - x0) / step))
    y = y0
    function = []
    function.append(y)
    runge_kutt = Runge_Kutta_45(x0, y0, x, step)

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


if __name__ == "__main__":
    step = 0.1
    a, b = 0, 1
    y1 = 0
    n = int((b - a) / step)
    argument_grid = []
    argument_grid.append(a)
    while a < b:
        a += step
        argument_grid.append(a)
    a, b = 0, 1
    function = Runge_Kutta_45(a, y1, b, step)
    exact_function = []
    for i in argument_grid:
        exact_function.append(F(i))
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.plot(argument_grid, exact_function, 'tab:blue', label='Точное решение')
    ax1.plot(argument_grid, Euler_method(a, y1, b, step), 'tab:orange', label='Метод Эйлера')
    ax1.plot(argument_grid, Euler_method_modified(a, y1, b, step), 'tab:red', label='Модифицированный метод Эйлера')
    ax1.legend()
    ax2.plot(argument_grid, exact_function, 'tab:blue', label='Точное решение')
    ax2.plot(argument_grid, function, 'tab:green', label='Метод Рунге-Кутты')
    ax2.legend()
    ax3.plot(argument_grid, exact_function, 'tab:blue', label='Точное решение')
    ax3.plot(argument_grid, Adams_method(a, y1, b, step), 'tab:red', label='Метод Адамаса')
    ax3.legend()
    plt.xlim([1, 2])
    plt.show()
