import numpy as np
import sympy as sp
from math import*
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x, y, z = sp.symbols('x y z')


def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)

    return final_list


def taylor_expansion_3d(exp):

    # calculating constants
    grad_x = exp.diff(x)
    grad_y = exp.diff(y)
    print(grad_x, grad_y)

    grad_xx = grad_x.diff(x)
    grad_xy = grad_x.diff(y)
    grad_yy = grad_y.diff(y)
    grad_yx = grad_y.diff(x)

    vec1_list = []
    taylor_values = []
    vec2_list = []

    for a in np.arange(0, 3, 1):
        for b in np.arange(0, 3, 1):

            # first term ==  f(a,b)
            first_term = exp.subs(x, a)
            first_term = first_term.subs(y, b)
            # print(first_term)

            # second term == f'(a,b)*(x-a) + f'(a,b)*(y-b)
            grad_1x = grad_x.subs(x, a)
            grad_1y = grad_y.subs(y, b)
            second_term = (grad_1x*(x-a)+grad_1y*(y-b))/factorial(1)
            # print(second_term)

            # third term == (f''(a,b)*(x-a)**2 + f''(a,b)*(x-a)*(y-b) + f''(a,b)*(y-b)**2)/2
            grad_2xx = grad_xx.subs(x, a)
            grad_2yy = grad_yy.subs(y, b)
            grad_2xy = grad_xy.subs([x, y], [a, b])
            grad_2yx = grad_yx.subs([x, y], [a, b])
            third_term = (grad_2xx*(x-a)**2+(grad_2xy+grad_2yx)*(x-a)*(y-b)+grad_2yy*(y-b)**2)/factorial(2)
            # print(third_term)

            vec1_list.append([a, b])

    for xval in np.arange(0, 5, 0.5):
        for yval in np.arange(0, 5, 0.5):

            taylor_exp = first_term + second_term + third_term
            taylor_exp = taylor_exp.subs(x, xval)
            taylor_exp = taylor_exp.subs(y, yval)

            taylor_values.append(taylor_exp)
            vec2_list.append([xval, yval])

    print(vec1_list)
    print(vec2_list)
    print(taylor_values)                                    


if __name__ == "__main__":

    taylor_expansion_3d(x**3+x*y**2+y**3)