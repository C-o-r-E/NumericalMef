# -*- coding: utf-8 -*-
from __future__ import division
from sympy import *

def newtRaph(fx, xinit, tol, vr=Symbol('x'), maxIt=70):
    x = vr
    xList = [N(xinit, 55)]
    fp = fx.diff(x)

    i = 0    
    while(True):
        i += 1
        print "i = ", i
        xNext = xList[-1] - (fx.subs(x, xList[-1]))/(fp.subs(x, xList[-1]))
        xList.append(xNext)
        if Abs(N(xList[-2],55) - N(xList[-1],55)) < tol or maxIt < i:
            break;

    return xList

def threeNorm(mat):
    x1 = Symbol('x1')
    x2 = Symbol('x2')    
    x = Matrix([x1, x2])

    yx = (1 - x1**3)**Rational(1,3)

    Ax = mat*x

    eq = Ax.norm(3)
    eqx = eq.subs(x2, yx)
    eqxprime = eqx.diff(x1)

    #now we need the maxima: find the root!
    rt = newtRaph(eqxprime, 0.9, 10**-52, x1)[-1]
    
    return eqx.subs(x1, rt)
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



