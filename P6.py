'''
shift_character
This function accepts a character and an integer and returns the character that is shifted by the integer with wrapping.

Inputs: character (lowercase characters only), shift (integer)
Outputs: character

Example: shift_character('a', 1) returns 'b'
Example: shift_character('a', 2) returns 'c'
Example: shift_character('z', 1) returns 'a'

Hint: You already implemented this exact functionality as part of a previous problem.
'''


def shift_character(char, shift):
    ciphertext = ""
    for i in char:
        i_unicode = ord(i)
        i_index = i_unicode - ord('a')
        new_index = (i_index + shift) % 26
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        ciphertext += new_character
    return ciphertext

'''
number_of_steps
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Input: integer
Output: integer

Example: number_of_steps(14) -> 6
Explanation: 14 is even, so divide by 2 and obtain 7. 7 is odd, so subtract 1 and obtain 6. 6 is even, so divide by 2 and obtain 3. 3 is odd, so subtract 1 and obtain 2. 2 is even, so divide by 2 and obtain 1. 1 is odd, so subtract 1 and obtain 0.

Example: number_of_steps(8) -> 4
Explanation: 8 is even, so divide by 2 and obtain 4. 4 is even, so divide by 2 and obtain 2. 2 is even, so divide by 2 and obtain 1. 1 is odd, so subtract 1 and obtain 0.
'''
def number_of_steps(num):
    step = 0
    while (abs(num) > 0):
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        step += 1
    return step


'''
count_characters
This function takes a string and returns a dictionary with each character in the string as a key and the number of times that character appears in the string as the value. The characters in the string are all lowercase letters and there should be no entry in the dictionary for any character that does not appear in the string.

Input: string
Output: dictionary

Example: count_characters('hello') -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
'''
def count_characters(string):
    all_freq = {}
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

'''
scrambled_cipher
This function takes in a lowercase string and a dictionary containing a mapping for each letter in the alphabet to a different letter in the alphabet. Your must return a string that is the result of applying the mapping to the input string.

Input: string, dictionary
Output: string

Example: scrambled_cipher('abc', {'a': 'b', 'b': 'c', 'c': 'a'}) returns 'bca'
Explanation: The dictionary maps 'a' to 'b', 'b' to 'c', and 'c' to 'a'.
Explanation: 'abc' becomes 'bca' by replacing 'a' with 'b', 'b' with 'c', and 'c' with 'a'.
Example: scrambled_cipher('hello', {'h': 'z', 'e': 'p', 'l': 'k', 'o': 'a'}) returns 'zpkka'
Explanation: The dictionary maps 'h' to 'z', 'e' to 'p', 'l' to 'k', and 'o' to 'a'.
Explanation: 'hello' becomes 'zpkka' by replacing 'h' with 'z', 'e' with 'p', 'l' with 'k', and 'o' with 'a'.

Hint: You may use this sample dictionary to test your function: my_dict = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
Hint: Iterate through the string and replace each character with the corresponding character in the dictionary.
Hint: The syntax to access a dictionary value is: my_dict[item] which returns the value associated with the key 'item'.
'''
def scrambled_cipher(string, dictionary):
    new_string = ''
    for letter in string:
        new_letter = dictionary[letter]
        new_string += new_letter
    return new_string


'''
even_odd_strings
This function takes a list of strings and returns a dictionary with two keys, 'even' and 'odd'. The value for the key 'even' is a list of all the strings with even length, and the value for the key 'odd' is a list of all the strings with odd length.
Input: list of strings
Output: dictionary with two keys, 'even' and 'odd'

Example: ['a', 'bb', 'ccc', 'dddd'] -> {'even': ['bb', 'dddd'], 'odd': ['a', 'ccc']}
Explanation: 'a' has length 1, which is odd, 'bb' has length 2, which is even, 'ccc' has length 3, which is odd, and 'dddd' has length 4, which is even.

Hint: use the len() function to get the length of a string
Hint: use the syntax mydict = {} to create an empty dictionary
Hint: use the syntax my_dict[key] = [] to add a new key to a dictionary where the value is an empty list
Hint: use the syntax my_dict[key].append(value) to add a value to the list stored in a dictionary for a given key
Hint: print(my_dict) to see what your dictionary looks like
'''
def even_odd_strings(strings):
    result = {'even': [], 'odd': [] } 
    for i in strings:
        length = len(i)%2
        if length == 0:
            result['even'].append(i) 
        else:
            result['odd'].append(i)
    return result

'''
is_anagram
This function takes two strings and returns True if the strings are anagrams of each other and False otherwise. Two strings are anagrams of each other if they contain the same letters, but in a different order. For example, 'listen' and 'silent' are anagrams of each other.

Input: string, string
Output: boolean (True or False)

Example: is_anagram('listen', 'silent') -> True

Hint: This can be done in one line of code.
'''
def is_anagram(string1, string2):
        if(sorted(string1)== sorted(string2)):
            return True
        else:
            return False


'''
shift_dictionary
This function takes an integer and a dictionary where the keys are lowercase characters and the values are lowercase characters. Your function must return a dictionary where each value is shifted by the integer with wrap around for the characters (z wraps around back to a).

Input: integer, dictionary
Output: dictionary

Example: shift_dictionary(1, {'a': 'a', 'b': 'b', 'c': 'c'}) -> {'a': 'b', 'b': 'c', 'c': 'd'}
Example: shift_dictionary(2, {'a': 'a', 'b': 'b', 'c': 'c'}) -> {'a': 'c', 'b': 'd', 'c': 'e'}
Example: shift_dictionary(3, {'a': 'x', 'b': 'y', 'c': 'z'}) -> {'a': 'a', 'b': 'b', 'c': 'c'}

Hint: You already wrote a function to do the shifting.
'''

def shift_dictionary(integer, dictionary):
    for k, v in dictionary.items():
        dictionary[k] = shift_character(v, integer)
    return dictionary
        
