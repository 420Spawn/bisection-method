import math
import sympy as sp


def samesign(a, b):
    return a * b > 0


def difsign(a, b):
    return a * b < 0


def checkMaxIterations(high, low, exp=10 ** -10):
    maxIterations = -math.log(exp / (high - low)) / math.log(2)
    if maxIterations > round(maxIterations):
        maxIterations = round(maxIterations) + 1
    else:
        maxIterations = round(maxIterations)
#    print("this is max iterations test, the max is: ", maxIteration s)
    return maxIterations


def sbisect(func, low, high, tolerance=0.0001):
    """"receives a func, the start point, the end point and the tolerance """
    maxIterations = checkMaxIterations(high, low, tolerance)
    for i in range(maxIterations):
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint
        if tolerance is not None and abs(high - low) < tolerance:
            break
    return midpoint



def bbisect(func, low, high, numOfSections):
    """"receives a func, the start point, the end point and the number of sections to divide and check separately """
    step = 0.1
    start = low
    while low < high:
        if difsign(func(low), func(low + step)):
            x = sbisect(f, low, low + step, tolerance)
            print(x)
        low += step
    x = sp.symbols('x')
    deriv = sp.diff(f(x))
    deriv = sp.lambdify(x, deriv, 'math')
    low = start
    while low < high:
        if difsign(deriv(low), deriv(low + step)):
            x = sbisect(deriv, low, low + step, tolerance)
            if math.isclose(func(x), 0, abs_tol=tolerance):
                print(x)
        low += step


def f(x):
    return x ** 4 + x ** 3 - 3 * (x ** 2)


high = 2
low = -3
tolerance = 0.0001
numOfSections = 10

bbisect(f, low, high, numOfSections)


