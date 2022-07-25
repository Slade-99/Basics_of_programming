#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: practices_sympy_numpy_scipy.py
# Created: Monday, 25th July 2022 9:06:09 am
# Author: Azwad Aziz (azwad.a02@hotmail.com)
# -----
# Last Modified: Monday, 25th July 2022 9:07:27 am
# Modified By: Azwad Aziz (azwad.a02@hotmail.com)
# -----
# Copyright (c) 2022 Dreams
###


# for writing symbolic expressions/differentiation/integration
import sympy
from sympy import*

# for useful numerical tools
import numpy


# for unsolvable integration
import scipy
from scipy.integrate import quad
# for double integration
from scipy.integrate import dblquad

# for plotting
import matplotlib.pyplot as pt


# Making symbols
x,y,z = symbols("x y z")


# Writing expression
f = x**3 +4*x*y - 7*z

# Evaluation
answer_1 = f.subs([(x,3),(y,1),(z,5)])
print(answer_1)


# Differentiation
df = diff(f,x)
print(df)
df2 = diff(f,x,2)
print(df2)



# Using Lambdidy makes a sympy expression to a numerical expression which makes evaluation
# easier and also other packages can be used with it

f_2 = x**2 + 5*x + 7

f_2 = lambdify(x,f_2)
print(f_2(3))


# Taking indefinite integrals
f_3 = sympy.exp(-x)*(x**2)*sympy.cos(x)
print(sympy.integrate(f_3, x).simplify())


f_4 = (1+sympy.sqrt(x))**sympy.Rational(1, 3) / sympy.sqrt(x)
print(sympy.integrate(f_4, x).simplify())


# Taking definite integral ( unsing evalf() gives decimal value)
f_5 = sympy.exp(x) / sympy.sqrt(sympy.exp(x) + 9)
print(sympy.integrate(f_5, (x, 0, sympy.log(4))))
print(sympy.integrate(f_5, (x, 0, sympy.log(4))).evalf())



# For unsolvalble integrals which will not work with sympy then use quad function of scipy

f_6 = lambda x: numpy.exp(-numpy.sin(x))

# Gives both error and answer
print(quad(f_6,1,2))

# Gives only answer as it prints the first value of the tuple
print(quad(f_6, 1, 2)[0])

# For double integration
f_7 = lambda y,x: y**-2*x
print(dblquad(f_7,1,2, lambda x: 3, lambda x : 4)[0])


# Graph plotting

numbers_range = numpy.arange(-5,5)
print(f_2(numbers_range))


# naming the x axis
pt.xlabel('x - axis')

# # naming the y axis
pt.ylabel('y - axis')

# giving a title to the graph
pt.title('Shape of the Function')

# plotting the points
pt.plot(numbers_range, f_2(numbers_range))

# Plotting the graph
pt.show()


