'''
lowercase_character_to_integer
This function takes in a lowercase character and returns the corresponding integer.
Inputs: character (string)
Outputs: integer (integer)
Example: lowercase_character_to_integer('a') returns 0
Example: lowercase_character_to_integer('b') returns 1
Example: lowercase_character_to_integer('z') returns 25

Hint: Use the ord() function.
'''

import math 


def lowercase_character_to_integer(character):
    return (ord(character) - 97)
'''
get_sum_of_integer_values
This function takes a string of lowercase characters and returns the sum of the integer values of the characters in the string.
Inputs: string
Output: integer

Example: get_sum_of_integer_values('') returns 0
Explanation: The empty string has no characters, so the sum of all of the values is 0.

Example: get_sum_of_integer_values('abc') returns 3
Explanation: 'abc' is 0 + 1 + 2 = 3.

Example: get_sum_of_integer_values('xyz') returns 72
Explanation: 'xyz' is 23 + 24 + 25 = 72.

Example: get_sum_of_integer_values('hello') returns 52
Explanation: 'hello' is 7 + 4 + 11 + 11 + 14 = 52.

Hint: Use the lowercase_character_to_integer() function you wrote above.
'''
def get_sum_of_integer_values(string):
    result = 0 
    for i in string:
        result += ord(i) - 97 
    return result 
        

'''
get_simple_string_hash
This function takes a lowercase string and returns a simple hash value for the string according to the following algorithm:
For each character in the string, take the integer value of the character and add it to the position of the character in the string. Return the sum of all of these values.
Inputs: string
Output: integer

Example: get_simple_string_hash('') returns 0
Explanation: The empty string has no characters, so the sum of all of the values is 0.

Example: get_simple_string_hash('abc') returns 6
Explanation: a = 0 + 0 = 0, b = 1 + 1 = 2, c = 2 + 2 = 4, so 0 + 2 + 4 = 6

Example: get_simple_string_hash('xyz') returns 75
Explanation: x = 23 + 0 = 23, y = 24 + 1 = 25, z = 25 + 2 = 27, so 23 + 25 + 27 = 75

Example: get_simple_string_hash('hashing') returns 80
Explanation: h = 7 + 0 = 7, a = 0 + 1 = 1, s = 18 + 2 = 20, h = 7 + 3 = 10, i = 8 + 4 = 12, n = 13 + 5 = 18, g = 6 + 6 = 12, so 7 + 1 + 20 + 10 + 12 + 18 + 12 = 80

Hint: Use the lowercase_character_to_integer() function you wrote above.
Hint: Use a for loop to iterate through the string where i is the position of the character in the string and string[i] is the character.
Hint: Use range(len(string)) to build the for loop.
'''
def get_simple_string_hash(string):
    result = 0
    for i in range(len(string)):
        result += i + lowercase_character_to_integer(string[i])
    return result


''' 
is_vowel
This function takes a character and returns True if it is a vowel and False otherwise.
Inputs: character (string)
Outputs: boolean (True or False)
Example: is_vowel('a') returns True
Example: is_vowel('b') returns False

Hint: Declare a string of vowels and use the "in" operator to check if the character is in the string.
'''
def is_vowel(character):
    vowels = ['a','e','i','o','u']
    if character in vowels:
        return True
    if character not in vowels:
        return False
'''
count_vowels
This function takes in a string and returns the number of vowels in the string.
Inputs: string
Outputs: integer
Example: count_vowels('hello') returns 2
Example: count_vowels('world') returns 1

Hint: Use the is_vowel() function you wrote above.
'''
def count_vowels(string):
    vowel_count= 0
    vowels = ['a','e','i','o','u']
    for i in string:
        if i in vowels:
            vowel_count += 1
        if i not in vowels:
            vowel_count +=  0
    return vowel_count




'''
fibbonacci_number
This function accepts a number and returns the fibbonacci number of that number.
A fibbonacci number is the sum of the previous two fibbonacci numbers.
The first two fibbonacci numbers are 0 and 1.
Inputs: integer
Outputs: integer
Example: fibbonacci_number(0) returns 0
Example: fibbonacci_number(1) returns 1
Example: fibbonacci_number(2) returns 1
Example: fibbonacci_number(3) returns 2

Hint: The formula for the fibbonacci number is: fibbonacci_number(x) = fibbonacci_number(x - 1) + fibbonacci_number(x - 2)
Hint: You have to hard code the first two fibbonacci numbers.
'''
def fibbonacci_number(number):

    if number < 0:
        return None 
    elif number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibbonacci_number(number-1) + fibbonacci_number(number-2)

'''
This function accepts two integers and returns the gcd of those integers.
A gcd is the greatest common divisor.
Inputs: integer 1 (integer), integer 2 (integer)
Outputs: gcd (integer)
Example: get_gcd(12, 18) returns 6
Example: get_gcd(12, 24) returns 12

Hint: The formula for the gcd is: gcd(a, b) = gcd(b, a % b)
Hint: If one of the integers is 0, then the gcd is the other integer.
'''
def get_gcd(integer1, integer2):
    result = math.gcd(integer1, integer2)
    return result
