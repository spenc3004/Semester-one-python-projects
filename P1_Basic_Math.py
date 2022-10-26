
from webbrowser import get
import math


def get_diameter_of_circle(radius):
    diameter = radius * 2
    return (diameter)

def get_circumference_of_circle(radius):
    circumference = radius * 2 * math.pi
    return (circumference)

def is_even(value):
    if (value % 2) == 0:
        return ("True")
    else:
        return ("False")
    
def integer_division(dividend, divisor):
    quotient = dividend // divisor
    return (quotient)

def get_range(end):
    counter = 1
    result = []
    while(counter <= end):
        result.append(counter)
        counter += 1
    return result

def get_sum_of_numbers(numbers):
    sum = 0
    for i in numbers:
        sum = sum  + i
    return (sum)


def get_product_of_numbers(numbers):
    product = 1
    for i in numbers:
         product = product * i
    return product