import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

func = lambda x: x ** 2 - 2 * x + math.e ** (-x)
func_pr = lambda x: 2 * x - 2 + math.e ** (-x) - 1
e = math.pow(10, -7)
a = 1
b = 1.5


def println_half_division_method(table):
    tabulate_result = []
    for iteration in table:
        tabulate_result.append(list(iteration.values()))

    print("\n_half_division_method\n")
    print(
        tabulate(
            tabulate_result,
            headers=["I", "A", "B", "X"],
            tablefmt="orgtbl",
        )
    )
    print(f"\nFINAL X:{table[-1]['x']}")


def half_division_method():
    global func, e, a, b
    print(e)
    table = []
    last_x = 0
    for i in range(12):
        f_x = func((a + b) / 2)
        iteration = {
            "i": i,
            "a": a,
            "b": b,
            "x": (a + b) / 2,
        }
        table.append(iteration)
        if abs(f_x) <= e or abs(a - b) <= e or abs(iteration["x"] - last_x) <= e:
            println_half_division_method(table)
            return table
        if func(iteration['a']) * f_x < 0:
            last_x = (a + b) / 2
            b = (a + b) / 2
        else:
            last_x = (a + b) / 2
            a = min(b, iteration["x"])
            b = max(b, iteration["x"])
    println_half_division_method(table)
    return table


def draw_half_method():
    x = np.linspace(-1, 0, 100)
    y = x ** 2 - 2 * x + math.e ** (-x)

    table = half_division_method()
    plt.figure('Метод 1')
    plt.scatter(table[-1]["x"], func(table[-1]["x"]), color='red', zorder=5)
    plt.plot(x, y)
    plt.title('Метод половинного деления')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def nyton_method():
    global func, e, a, b, func_pr
    x = a + 0.1
    table = []
    x_n = x
    for i in range(12):
        x_new = x_n - func(x_n) / func_pr(x_n)

        iteration = {
            "i": i,
            "x_last": x_n,
            "x_new": x_new,
        }
        table.append(iteration)
        if (
                abs(x_n - x_new) <= e
                or abs(func(x_new)) <= e
                or abs(func(x_new) / func_pr(x_new)) <= e
        ):
            println_nuton_method(table)
            return table
        x_n = x_new
    println_nuton_method(table)
    return table


def println_nuton_method(table):
    tabulate_result = []
    for iteration in table:
        tabulate_result.append(list(iteration.values()))

    print(
        tabulate(
            tabulate_result,
            headers=["i", "x_i", "x_(i+1)"],
            tablefmt="orgtbl",
        )
    )
    print(f"\nFINAL X:{table[-1]['x_new']}")


def draw_nuton_method():
    x = np.linspace(-1, 0, 100)
    y = x ** 2 - 2 * x + math.e ** (-x)

    table = nyton_method()
    plt.figure('Метод 2')
    plt.scatter(table[-1]["x_new"], func(table[-1]["x_new"]), color='red', zorder=5)
    plt.plot(x, y)
    plt.title('Метод Ньютона')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def println_gold_method(table):
    tabulate_result = []
    for iteration in table:
        tabulate_result.append(list(iteration.values()))

    print(
        tabulate(
            tabulate_result,
            headers=["i", "a", "b", "x1", "x2"],
            tablefmt="orgtbl",
        )
    )


def gold_method():
    global func, e, a, b
    x1 = a + ((3 - pow(5, 1 / 2)) / 2) * (b - a)
    x2 = a + ((pow(5, 1 / 2) - 1) / 2) * (b - a)
    table = []
    for i in range(12):
        iteration = {
            "i": i,
            "a": "{:e}".format(a),
            "b": b,
            "x1": x1,
            "x2": x2
        }
        table.append(iteration)
        f_1 = func(x1)
        f_2 = func(x2)
        if b - a == 0 or x1==x2 <= e:
            x = (a + b) / 2
            y = func(x)
            println_gold_method(table)
            return (x, y)

        if f_1 < f_2:
            b = x2
            x2 = x1
            f_2 = f_1
        else:
            a = x1
            x1 = x2
            f_1 = f_2
    x = (a + b) / 2
    y = func(x)
    println_gold_method(table)
    return (x, y)



def draw_gold_method():
    x = np.linspace(-1, 0, 100)
    y = x ** 2 - 2 * x + math.e ** (-x)

    x_answer,y_answer =gold_method()
    plt.figure('Метод 3')
    plt.scatter(x_answer, func(x_answer), color='red', zorder=5)
    plt.plot(x, y)
    plt.title('Метод Золотого сечения')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
    print(f"FINAL X:{x_answer}")

draw_gold_method()