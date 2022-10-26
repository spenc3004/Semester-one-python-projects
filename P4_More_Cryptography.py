'''
prefix_sum
This function accepts a list of numbers and returns a list of the prefix sums of the list.
A prefix sum is the sum of all of the numbers up to and including that number.
Inputs: nums (list of numbers)
Outputs: prefix_sums (list of numbers)

Example: prefix_sum([1, 1, 1, 1, 1]) returns [1, 2, 3, 4, 5]
Example: prefix_sum([1, 2, 3, 4, 5]) returns [1, 3, 6, 10, 15]
'''
from itertools import accumulate
import math
import string

def prefix_sum(nums):
    return list(accumulate(nums))


'''
smaller_than_n
This function accepts a list of numbers and an integer and returns a list of all of the numbers in the list that are smaller than the integer.
Inputs: nums (list of numbers), n (integer)
Outputs: smaller_nums (list of numbers)

Example: smaller_than_n([1, 2, 3, 4, 5], 3) returns [1, 2]
Example: smaller_than_n([1, 2, 3, 4, 5], 0) returns []
'''
def smaller_than_n(nums, n):
    return [item for item in nums if item < n] 

'''
get_factorial_of_number
This function accepts a number and returns the factorial of that number.
A factoral is the product of all whole numbers from 1 to n.
Inputs: number (integer)
Outputs: factorial (integer)

Example: get_factorial_of_number(0) returns 1
Example: get_factorial_of_number(5) returns 120
'''
def get_factorial_of_number(number):
    return math.factorial(number)

'''
is_palindrome
This function accepts a string and returns True if the string is a palindrome and False otherwise.
A palindrome is a string that is the same forwards and backwards.
Inputs: string (string)
Outputs: boolean (True or False)

Example: is_palindrome('racecar') returns True
Example: is_palindrome('hello') returns False

Hint: There are many ways to solve this problem, but it can be done in one line of code.
Hint: A palindrome is the same forwards and backwards.
'''
def is_palindrome(string):
    if str(string) == str(string)[:: -1]:
        return("True")
    else:
        return("False")


'''
integer_to_lowercase
This function accepts an integer and returns the lowercase letter that corresponds to that integer, starting from 0.
Input: integer (integer, 0 to 25 inclusive only)
Output: lowercase letter (string)

Example: integer_to_lowercase(0) returns 'a'
Example: integer_to_lowercase(25) returns 'z'
'''
def integer_to_lowercase(integer):
    OFFSET = ord("a") 
    return chr(integer + OFFSET)


'''
caesar_cipher
This function accepts a string and an integer and returns the string encrypted with a caesar cipher.
A caesar cipher is a substitution cipher where each letter is replaced by another letter a fixed number of positions down the alphabet.
Inputs: exposed_string (string, lowercase characters only), shift (integer)
Outputs: encrypted string (string)

Example: caesar_cipher('abc', 1) returns 'bcd'
Example: caesar_cipher('abc', 26) returns 'abc'

Hint: Start with an empty string and add to it as you process each letter from the exposed string.
Hint: Use methods you have previously written to help you.
Hint: Use the modulus operator (remainder) to wrap around the alphabet.
'''
def caesar_cipher(exposed_string, shift):
    ciphertext = ""
    for i in exposed_string:
        i_unicode = ord(i)
        i_index = i_unicode - ord('a')
        new_index = (i_index + shift) % 26
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        ciphertext += new_character
    return ciphertext
    

'''
caesar_decipher
This function accepts a string and an integer and returns the string decrypted with a caesar cipher.
In other words, you can use this function on the output from caesar_cipher above in order to get the original string back.

So for example, caesar_decipher(caesar_cipher('abc', 1), 1) returns 'abc'.
original_str = 'abc'
str1 = caesar_cipher(original_str, 1)
str2 = caesar_decipher(str1, 1)
str2 == original_str # True

Inputs: exposed_string (string, lowercase characters only), shift (integer)
Outputs: encrypted string (string)

Example: caesar_decipher('bcd', 1) returns 'abc'
Example: caesar_decipher('abc', 26) returns 'abc'

Hint: Reuse the caesar_cipher() function you wrote above.
'''
def caesar_decipher(encrypted_string, shift):
    ciphertext = ""
    for i in encrypted_string:
        i_unicode = ord(i)
        i_index = i_unicode - ord('a')
        new_index = (i_index - shift) % 26
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        ciphertext += new_character
    return ciphertext
