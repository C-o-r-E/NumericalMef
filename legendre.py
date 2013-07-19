#!/usr/bin/python2
# -*- coding: utf-8 -*-
from __future__ import division
from sympy import *

def newtRaph(fx, xinit, tol):
    x = Symbol('x')
    xList = [xinit]
    fp = fx.diff(x)

    i = 0    
    while(True):
        i += 1
        print "i = ", i
        xNext = xList[-1] - (fx.subs(x, xList[-1]))/(fp.subs(x, xList[-1]))
        xList.append(xNext)
        if Abs(N(xList[-2],55) - N(xList[-1],55)) < tol or 50 < i:
            break;

    return xList
    

def legPoly(degree, fx):
    if degree == 0:
        return 1
    if degree == 1:
        return 2*fx

    l = [1, 2*fx]

    for n in range(2, degree+1):
        phi = ((4*n - 2)/n * x * l[-1]) - ((4*n - 4)/n * l[-2])
        l.append(phi)

    return l

def legCoef(roots, i):
    x = Symbol('x')
    num = i - 1
    ret = 1
    
    cnt = 0
    while cnt < len(roots):
        if cnt == num:
            cnt += 1
            continue
        ret = ret * (x-roots[cnt]) / (roots[num] - roots[cnt])
        cnt += 1
    
    return ret

x = Symbol('x')
z = legPoly(8, x)

e8 = simplify(z[-1])

r = []
tmp = N(-1.0)

for n in range(21):
    r.append(tmp)
    tmp += N(0.1, 51)

pts = [e8.subs(x, n) for n in r]

rts = [newtRaph(e8, n, 10**-53)[-1] for n in r]

rewts = sorted(rts)

lul = [1,4,5,7,10,13,15,16]

uroots = [rewts[n] for n in lul]

c = [legCoef(uroots, n) for n in range(1, 9) ]

d = map(expand, c)

print "begin \n"

#for n in d:
#    print latex(n)
