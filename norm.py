# -*- coding: utf-8 -*-
from __future__ import division
from sympy import *

def newtRaph(fx, xinit, tol):
    x = Symbol('x')
    xList = [N(xinit, 55)]
    fp = fx.diff(x)

    i = 0    
    while(True):
        i += 1
        print "i = ", i
        xNext = xList[-1] - (fx.subs(x, xList[-1]))/(fp.subs(x, xList[-1]))
        xList.append(xNext)
        if Abs(N(xList[-2],55) - N(xList[-1],55)) < tol or 7 < i:
            break;

    return xList

def threeNorm(mat):
    x1 = Symbol('x1')
    x2 = Symbol('x2')    
    x = Matrix([x1, x2])

    Ax = mat*x

    eq = Ax.norm(3)

    sols = []
    sols.append(eq.subs(x1, N(1, 51)).subs(x2, 0))
    sols.append(eq.subs(x1, 0).subs(x2, N(1, 51)))
    return max(sols)
#############################

mats = [Matrix([ [N(1, 51), N(n,51)], [N(0,51),N(1,51)] ]) for n in range(1, 10)]

ans = map(threeNorm, mats)

lam = 1
for a in ans:
    print "λ =", lam, "->", N(a, 51)
    lam += 1


#############################

x = Symbol('x')
y = Symbol('y')
yx = (1 - x**3)**Rational(1,3)

print "\n\ny = \n"
pprint(yx)

N = (x+y)**3 + y**3
Nx = N.subs(y, yx)
dn = (-3/y**2)*(x**4 + y*2*x**3 + (x**2)*(y**2) - 2*x*y**3 - y**4)
dnx = dn.subs(y, yx)

Nxprime = Nx.diff()

"""
print "\nN = \n"
pprint(N)
print latex(N)
print "\nSubbing in gives N = \n"
pprint(Nx)
print latex(Nx)
print "\nDifferentiating N gives N' = \n"
pprint(Nxprime)
print latex(Nxprime)
print "\nTaking \n"
pprint(dn)
print latex(dn)
print "\nand subbing in y yields: \n"
pprint(dnx)
print latex(dnx)
print "subtracting N' from that produces 0 showing that"
print "if ...\n\n\n"
"""



