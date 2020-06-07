import numpy as np
import sympy as sy
from random import randint

x, y = sy.symbols('x y')


def grad_diff(val):
    val = val.split("=")
    print(val)
    lhs = val[0]
    rhs = val[1]
    grad1 = sy.diff(rhs, x)
    grad2 = sy.diff(rhs, y)
    print(grad1, grad2)
    xRand = [ ]
    yRand = [ ]

    for _ in range(10):
        xRand.append(randint(0, 10))
        yRand.append(randint(0, 10))
    print(xRand)
    print(yRand)
    resultList = { }
    for i, j in zip(xRand, yRand):
        resultList[(i, j)] = [grad1.subs(x, i), grad2.subs(y, j)]

    print(resultList)


if __name__ == "__main__":
    print(grad_diff("f(z)=x**5+y**5"))
