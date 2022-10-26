'''
get_average_of_numbers
This function accepts a list of numbers and returns the average of those numbers.
Inputs: numbers (list of integers or floating point numbers)
Outputs: average (integer or floating point number)
Example: get_average_of_numbers([1, 4, 6]) returns 3.666666666666666

Hint: Use the sum() function to add all the numbers in the list and the len() function to get the number of items in the list.
'''
from multiprocessing.sharedctypes import Value
from os import lstat
import statistics
from collections import Counter


def get_average_of_numbers(numbers):
    lst = []
    return sum(numbers) / len(numbers)
    # You must implement this function

'''
get_median_of_numbers
This function accepts a list of numbers and returns the median of those numbers.
Inputs: numbers (list of integers or floating point numbers)
Outputs: median (integer or floating point number)
Example: get_median_of_numbers([5, 4, 3, 2, 1]) returns 3

Hint: Use the sort() function to sort the list of numbers.
'''
def get_median_of_numbers(numbers):
    lst = []
    return statistics.median(numbers)

    # You must implement this function
    
'''
get_mode_of_numbers
This function accepts a list of numbers and returns the mode of those numbers.
Inputs: numbers (list of integers or floating point numbers)
Outputs: mode (integer or floating point number)
Example: get_mode_of_numbers([1, 2, 2, 3, 3, 3]) returns 3

Hint: Use a dictionary to count the number of times each number appears in the list.
The syntax to create a dictionary is: my_dict = {}
Then the syntax to add a key-value pair to the dictionary is: my_dict[key] = value
Then the syntax to get the maximum value in a dictionary is: max(my_dict, key=my_dict.get)
'''
def get_mode_of_numbers(numbers):
    current_mode = numbers[0]
    current_mode_count = 1
    for i in numbers:
        current_count_testing = numbers.count(i)
        if (current_count_testing > current_mode_count):
            current_mode = i
            current_mode_count = current_count_testing
    return current_mode
    
'''
get_range_of_numbers
This function accepts a list of numbers and returns the range of those numbers.
Inputs: numbers (list of integers or floating point numbers)
Outputs: range (integer or floating point number)
Example: get_range_of_numbers([1, 2, 3, 4, 5]) returns 4

Hint: Use the max() and min() functions to get the maximum and minimum values in the list.
'''
def get_range_of_numbers(numbers):
    lst = []
    minimum = min(numbers)
    maximum = max(numbers)
    return (maximum - minimum)

    # You must implement this function
    

'''
get_sum_of_even_numbers
This function accepts a list of numbers and returns the sum of the even numbers only.
Inputs: numbers (list of integers or floating point numbers)
Outputs: sum (integer or floating point number)
Example: get_sum_of_even_numbers([1, 2, 3, 4, 5]) returns 6

Hint: Use the % operator to determine if a number is even or odd, or use the function you already wrote in the previous assignment.
'''
def get_sum_of_even_numbers(numbers):
    lst = []
    s = sum([num for num in numbers if num % 2 == 0])
    return s


    # You must implement this function
# Remember to test your code before submitting it!

'''
power
This function accepts a base and an exponent and returns the base raised to the exponent.
Inputs: base (integer) and exponent (integer)
Outputs: base raised to the exponent (integer)
Example: power(2, 3) returns 8

Hint: Use the ** operator to raise a number to a power where x ** y is the same as x^y.
'''
def power(base, exponent):
    return base ** exponent
    # You must implement this function
# Remember to test your code before submitting it!

'''
get_sum_of_numbers_squared
This function accepts a list of numbers and returns the sum of the squares of those numbers.
Inputs: numbers (list of integers or floating point numbers)
Outputs: sum (integer or floating point number)
Example: get_sum_of_numbers_squared([1, 2, 3, 4, 5]) returns 55

Hint: Use the ** operator to raise a number to a power where x ** y is the same as x^y.
'''
def get_sum_of_numbers_squared(numbers):
    lst = []
    return sum(map(lambda i : i * i, numbers))
    # You must implement this function # Remember to test your code before submitting it!
