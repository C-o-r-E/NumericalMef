# -*- coding: utf-8 -*-
from __future__ import division
from sympy import *

def newtRaph(fx, xinit, tol, vr=Symbol('x'), maxIt=70):
    x = vr
    xList = [N(xinit,55)]
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
    print "rt = ", rt
    
    return eqx.subs(x1, rt)
#############################

m = Matrix([[1,1],[0,1]])

ans = threeNorm(m)



