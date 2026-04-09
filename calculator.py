
import math

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
   if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exponent(a, b):
    return a**b





