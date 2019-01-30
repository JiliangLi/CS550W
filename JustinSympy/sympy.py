# Name: Justin Lin & Eric Li
# Date: 1/18/2019
# Description: Sympy Code Examples
# Sources: https://www.sympy.org/en/index.html, https://docs.sympy.org/0.7.2/modules/geometry.html
# honor code: On my honor, I have neither given nor received any unauthorized aid. Justin Lin & Jiliang Li


# BASIC OPERATIONS

# pprint
import math as m
from sympy import *
# the numbers are printed differently
def sympy_printing_vs_normal_print():
    pprint(sqrt(8))
    print(sqrt(8))
    print(m.sqrt(8)) 

sympy_printing_vs_normal_print()
# this example is a function that shows the difference in symbolic and non symbolic math. It also shows the difference in printing.


# Symbol/symbols
from sympy import *
def sympy_symbols():
    a = Symbol('a') # (a) attains the variable 'a'
    b = Symbol('b') # it is an object of its own (Symbol)
    c = Symbol('c') # it isn't a list, float, int, or string.
    e = (a*b + 2*a*b)**(c**2)
    pprint(e)

    # faster way to write multiple symbols // Notice Symbol becomes symbols
    x,y,z = symbols('x,y,z') 
    print(x,y,z)

sympy_symbols()
# This function uses a sympy function called symbol(s) which allows for variables to be variables in mathematical equations.


# value substitution
from sympy import *
def sympy_substitution():
    a = Symbol('a')
    expression = a + 2
    expression = expression.subs({a: 2}) # substitutes a for the value "2"
    expression = expression.subs(a, 2)      # a different way to write the line above
    pprint(expression)

sympy_substitution()
# this allows for values or variables to be substituted by other values or variables.


# simplification
from sympy import *
def sympy_simplifier():
    x = Symbol('x')
    expression = sin(x)**2 + cos(x)**2 # this uses sin and cosin
    pprint(expression)
    pprint(simplify(expression))    # simplifies the equation if it is transformable

sympy_simplifier()
# the function above symplifies math equations.


# expansion
from sympy import *
def sympy_expand():
    x, y = symbols('x, y')

    pprint((x + 2)*(x - 3))         # equation
    pprint(expand((x + 2)*(x - 3)))     # expanded polynomial
    print('\n')
    pprint((x + 1)*(x - 2) - (x - 1)*x)     # equation
    pprint(expand((x + 1)*(x - 2) - (x - 1)*x))     # expanded polynomial

sympy_expand()
# as shown in the function above, the expand function expands equations. it expanded the factored form of the first equation. 


# solve
from sympy import *
def sympy_solve():
    x = Symbol('x')
    pprint(x**2 - 4, x)
    pprint(solveset(x**2 - 4, x))   # this solves the equation, and gives back the variable x. you have to put x after the comma
    print('')
    pprint(sin(x)/x)
    print('')
    pprint(solve(sin(x)/x))     # this solves sin(x)/x, and 0 is excluded
    pprint(solve(sin(x)/x, check=False))    # this solves sin(x)/x, and 0 is included becasue sin(x)/x has the well known limit of 1 at x = 0:
sympy_solve()
# The function above shows different forms of solveset and solve. it is very similar to simplify, and it gives the value of whatever variable you are trying to find.


# evaluation
from sympy import *
def sympy_eval():
    pprint(pi)
    print(pi.evalf(90))    # the value of pi to the 100th digit
    print('')
    pprint(sqrt(2))
    print(sqrt(2).evalf(90))   # the value of sqrt(2) to the 100th digit

sympy_eval()
# the eval function calculates irrational numbers to whatever digit of your choosing.


# equation checking
# '=='' does not check if two equations are mathematical equivalents (thus we expect the first output beneath to be False). 
# However, function expand() allows us to check if two equations are mathematical equivalents (thus we expect the first output beneath to be True)
from sympy import *
def sympy_equation_checking():
    x = Symbol('x')
    checking = (x + 1)**2 == x**2 + 2*x + 1
    print(checking)     

    checking_2 = expand((x + 1)**2) == x**2 + 2*x + 1
    print(checking_2)


sympy_equation_checking()
# the == sign checks if the equation is true or not.




# SYMPY GEOMETRY

# collinear
from sympy import *
from sympy.geometry import *
def sympy_collinear():
    x = Point(0,0) # this gives the variable a point on a graph.
    y = Point(1,1) # this gives the variable a point on a graph.
    z = Point(4,4) # this gives the variable a point on a graph.
    w = Point(-1, 2) # this gives the variable a point on a graph.
    print(x,y,z,w)
    print(Point.is_collinear(x,y,z)) # as the name suggests, it checks to see if the points given are collinear.
    print(Point.is_collinear(x,y,w)) # it will print true since it is.

sympy_collinear()
# the function checks to see if the points are in a line (collinear)


# area of triangles
from sympy import *
from sympy.geometry import *
def sympy_triangle_area():    
    x = Point(0,0) # this gives the variable a point on a graph.
    y = Point(1,1) # this gives the variable a point on a graph.
    z = Point(3,0) # this gives the variable a point on a graph.
    t = Triangle(x,y,z) # it will plot a triangle with the points given.
    print(x,y,z)
    print(t)
    pprint(t.area) #this will print and calculate the area of this triangle

sympy_triangle_area()
# calculates the area of a triangle.

# median of triangles
from sympy import *
from sympy.geometry import *
def sympy_triangle_median():  
    x = Point(0,0) # this gives the variable a point on a graph.
    y = Point(1,1) # this gives the variable a point on a graph.
    z = Point(3,0) # this gives the variable a point on a graph.
    t = Triangle(x,y,z) # it will plot a triangle with the points given.
    pprint(t.medians[x]) # calculates the medians of the triangle given.

sympy_triangle_median()
# this function calculates the median of the triangle given.




# SYMPY CALCULUS

# derivatives with single variable calculus
from sympy import *

def sympy_deriv():
    x, y = symbols('x, y')

    pprint(diff(cos(x),x))      # the derivative of equation cos(x)
    pprint(diff(cos(x),x,x))    # the second derivative of equation cos(x)
    print('\n')

    pprint(exp((x**2)*(y**2)))      # the equation
    pprint(diff(exp((x**2)*(y**2)),x))      # the derivative of the equation above

sympy_deriv()
# this functions shows examples of derivatives of different equations.


# integrals with single variable calculus
from sympy import *

def sympy_integr():
    x = Symbol('x')

    pprint(integrate(cos(x), x))    # the indefinite integral of equation cos(x)
    print('\n')

    pprint(Integral(exp(-x), (x, 0, oo)))   # the definite integral
    pprint(integrate(exp(-x), (x, 0, oo)))  # the value of the definite integral above
    print('\n')

    expr = Integral(log(x)**2, x)   # the indefinite integral
    pprint(expr)
    expr_result = expr.doit()   # result of the integration
    pprint(expr_result)
    print('\n')

    integ = Integral(1/(x**3), (x, 1, oo))  # the definite integral
    pprint(integ)
    integ_result = integ.doit()     # result of the integration
    pprint(integ_result)

sympy_integr()

# infinite series:
from sympy import Symbol, cos, sin, pprint

def sympy_infinite_series():
    x = Symbol('x')
    a = 1/cos(x)
    pprint(a.series(x, 0, 10))  # the series for sec(x) to the term where x is to the tenth power

sympy_infinite_series()



# SYMPY LINEAR ALGEBRA

# matrices
from sympy import *
def sympy_matix(): 
    M = Matrix([[1, 0, 1], [3, 0, 3], [4, 3, 2]])

    pprint(M)   # the matrix
    print(M.det())  # the matrix's determinant
    pprint(M.rref())    # the rref of the matrix (the second output is a tuple of indices of the pivot columns)

sympy_matix() 




# GRAPHS WITH SYMPY

from sympy import *
from sympy.plotting import (plot, plot_parametric,
                            plot3d_parametric_surface, plot3d_parametric_line,
                            plot3d)
def sympy_plot():0
    x, y, u, v = symbols('x, y, u, v')
    # all graphs are not shown when first created
    a = plot(x*sin(x**2), (x, 2, 4), show=False)  # cartesian plot

    b = plot(cos(x-1)*x**2, (x, -5, 5), show=False)  # cartesian plot

    c = plot3d_parametric_line(sin(x), cos(x), x, (x, 0, 20), show=False)  # 3d parametric line plot

    d = plot3d(sin(x)*cos(y)*sin(x*y), (x, -3, 3), (y, -3, 3), show=False)  # 3d surface cartesian plot3d (multivariable)

    e = plot3d_parametric_surface(cos(u)*v, sin(u)*v, sin(0.3*u*v), (u, 0, 10), (v, -2, 2), show=False)  # 3d parametric surface plot (multivariable)

    param_lines_2d = plot_parametric((x*cos(x), x*sin(x), (x, 0, 15)), 
                                    (1.1*x*cos(x), 1.1*x*sin(x), (x, 0, 15)), show=False)   # 2d parametric multiple lines plot

    param_lines_3d = plot3d_parametric_line((x*cos(x), x*sin(x), x, (x, 0, 15)),
                         (1.5*x*cos(x), 1.5*x*sin(x), x, (x, 0, 15)),
                         (2*x*cos(x), 2*x*sin(x), x, (x, 0, 15)), show=False)   # 3d parametric multiple lines plot

    for i in [a, b, c, d, e, param_lines_2d, param_lines_3d]:
        i.show()

sympy_plot()


# SymPy real Example (Monte Carlo Simulation)

import random
from sympy import *
import matplotlib.pyplot as plt

# The Hubble Space Telescope was launched by the space shuttle Discovery. 
# A prediction for the velocity of the shuttle during this mission, from liftoff at t=0 until the solid rocket boosters were jettisoned at t=126 s, is given by
# v(t) = a*t**3 - b*t**2 + c*t - d (in feet per second)
# Where a = 0.0013 ± 0.0001 
# b = 0.0902 ± 0.001
# c = 23.6 ± 1
# d = 3.08 ± 0.1
# Using this prediction, estimate the absolute minimum values of the acceleration of the shuttle between liftoff and the jettisoning of the boosters.

def space_shuttle_prediction_graph():
    # the graph of acceleration (generic) shows that the minimum value is around 21 and it occurs at the critical point
    t = Symbol('t')
    graph = plot(diff(0.0013*(t**3) - 0.0902*(t**2) + 23.6*t - 3.08), (t, 0, 126))

# using the estimations and patterns observed in the graph, we are able to run the following Monte Carlo simulation
def space_shuttle_prediction_simul():
    t = Symbol('t')
    min_values = [0 for x in range(2000,2301)]

    for x in range(3000):
        v = (0.0013+random.randrange(-10,11)/100000)*(t**3) - (0.0902+random.randrange(-10,11)/10000)*t**2 + (23.6+random.randrange(-10,11)/10)*t - (3.08+random.randrange(-10,11)/100)

        a = diff(v,t)   # take the derivative of v(t) to find the equation for a(t)
        sec_deriv_v = diff(v,t,t)   # take the second derivative of v(t) to find the equation for the derivative of a(t)
        zero = solve(sec_deriv_v)   # find the 0s in a'(t) to find the critical point
        min_acc = a.subs(t, zero[0])    # plug in the critical value to solve for a
        min_acc = round(min_acc, 2)     # round the value to 4 significant digits
        min_values[int(min_acc*100)-2000] += 1


    r = [x/100 for x in range(2000,2301)]

    plt.plot(r, min_values,'bo')
    plt.ylabel("number of occurrence")
    plt.xlabel("minimum values of acceleration (in feet/second^2)")
    plt.show()

space_shuttle_prediction_graph()
space_shuttle_prediction_simul()
