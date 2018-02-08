# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

import math 
from collections import namedtuple
import scipy.integrate as integrate

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n<0:
        raise(ValueError)
    if n<2:
        return 1
    else:
        return n*fact(n-1)
    
def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + c = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
    to the roots of the ax^2 + bx + c polynomial.
    """

    result = namedtuple("result",['x1','x2'])
    delta = (b ** 2) - (4 * a * c)

    if a == 0:
        print("veuilliez donner une equaiton du second degré")

    if delta < 0:
        return result("","")

    if delta > 0:
        x1 = float((- b - math.sqrt(delta)) / (2*a))
        x2 = float((- b + math.sqrt(delta)) / (2*a))

        return result("{}","{}".format(x1, x2))

    if delta == 0:
        x1 = (-b - math.sqrt(delta)/(2*a))
        return result("{}".format(x1))

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """



if __name__ == '__main__':
    print(fact(5))
    print(roots(3, 3, 0))
    print(integrate('x ** 2 - 1', -1, 1))
