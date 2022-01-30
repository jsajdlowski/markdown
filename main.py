import os 
import math


def factorial(n) -> int:
    if n >= 1:
        fact = 1
        for num in range(2, n + 1):
            fact *= num
        return fact

    
def subtraction(x,y) -> int:
    return math.floor(x-y)
