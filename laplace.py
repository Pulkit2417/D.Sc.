from sympy import *
from sympy.abc import t, s

F = symbols('F', cls=Function)

dy0 = -8
y0 = 2

rhs = laplace_transform(6*cos(3*t)-sin(3*t), t, s)
print(rhs[0])

compute = Eq(s**2*F(s)-s*y0-dy0 - 2*(s*F(s)-y0) + 10*F(s), rhs[0])
print(compute)

Fofs = solve(compute, F(s))
print(Fofs[0])

soln = inverse_laplace_transform(Fofs[0], s, t)
print(soln)

soln_simp = expand(soln)
print(soln_simp)

final = N(soln_simp, 3)
final = final.subs(Heaviside(t), 1)
print(final)