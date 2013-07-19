#!/usr/bin/python2
# -*- coding: utf-8 -*-
from sympy import *

def discreteLeastSquares(x, y, n):
    if(len(x) != len(y)):
        print "the first two params must be equal sized lists!!!"
        return
    print "Discrete Least Squares\n"
    print "Coords are as follows:"
    coords = Matrix([x, y])
    pprint(coords.transpose())

    systems = []
    #need to generate the n+1 systems of equations
    for r in range(n+1):
        s = []
        for t in range(n+1):#(r, r+n+1):
            #calculate the sum(xi^r+t) and append to s
            u = 0
            for xi in x:
                u += N((xi ** (r+t)), 5)
            s.append(u)
        v = 0
        for i in range(len(x)):
            v += N(y[i] * (x[i] ** (r)), 5)
        s.append(v)
        systems.append(s)

    print "\nTo construct the discrete least squares polynomial of degree ",
    print n,
    print " the following normal equations are produced:"
    for s in systems:
        for a in range(len(s)-2):
            print str(s[a]) + "⋅a" + str(a) + " + ",
        print str(s[-2]) + "⋅a" + str(len(s)-2) + " = ",
        print str(s[-1])

    return systems
"""
    sysMat = Matrix(systems)
    syms = numbered_symbols('a')
    symbols = [syms.next() for i in xrange(sysMat.rows)]
    soln = solve_linear_system(sysMat, *symbols)
    

    print "\nSolving for the equations, the coeffients of the polynomial:"
    for s in soln:
        print str(s) + " = " + str(soln[s])

    var_x = Symbol('x')
    P = 0
    c = 0
    print "\nGiving a degree " + str(n) + " polynomial:"
    print "P" + str(n) + "(x) ="
    for s in soln:
        P += soln[s] * (var_x ** c)
        c += 1
    pprint(P)

    total_error = 0;
    print "\nHere is a table of coords now that we have our polynomial..."
    print "xi\t\tyi\t\tP(xi)\t\tyi-P(xi)"
    for i in range(len(x)):
        pTmp = N(P.subs(var_x, x[i]),5) 
        eTmp = N(y[i] - pTmp, 5)
        total_error += eTmp**2
        print x[i], "\t\t", y[i], "\t\t",
        print pTmp, "\t\t",
        print eTmp

    print "\nTotal Error = ", total_error, "\n\n\n"
"""


#xList = [0, 0.25, 0.50, 0.75, 1.00]
#yList = [1.0, 1.2840, 1.6487, 2.1170, 2.7183]
#test = discreteLeastSquares(xList, yList, 2)

init_printing()

x = Symbol('x')
y = Symbol('y')
sx = numbered_symbols('x')
sy = numbered_symbols('y')
xList = [sx.next() for r in range(2)]
yList = [sy.next() for r in range(2)]
#xList = [x]
#yList = [y]

"""
tmp = discreteLeastSquares(xList, yList, 1)

m = Matrix([ tmp[0][:-1], tmp[1][:-1]])


xList.append(sx.next())
yList.append(sy.next())

tmp = discreteLeastSquares(xList, yList, 1)

n = Matrix([ tmp[0][:-1], tmp[1][:-1]])


xList.append(sx.next())
yList.append(sy.next())

tmp = discreteLeastSquares(xList, yList, 1)

o = Matrix([ tmp[0][:-1], tmp[1][:-1]])
"""

tmp = discreteLeastSquares(xList, yList, 2)
test = Matrix([ tmp[0][:-1], tmp[1][:-1], tmp[2][:-1]])

xList.append(sx.next())
yList.append(sy.next())
tmp = discreteLeastSquares(xList, yList, 2)
test2 = Matrix([ tmp[0][:-1], tmp[1][:-1], tmp[2][:-1]])
