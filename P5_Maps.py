




'''
longest_string
This function takes a list of strings and returns the length of the longest string in the list.

Input: list of strings
Output: integer

Example: ['a', 'aa', 'bb', 'ccc', 'dddd'] -> 4
'''
from operator import itemgetter


def longest_string(strings):
    longest = max(strings, key = len)
    return len(longest)


'''
shift_numbers
This function takes a list of numbers and a shift value and returns a new list of numbers where each number is shifted by the shift value.

Input: list of numbers, integer
Output: list of numbers

Example: [1, 2, 3, 4, 5], 2 -> [3, 4, 5, 6, 7]
Explanation: The shift value is 2, so each number is shifted by 2.
Explanation: 1 + 2 = 3, 2 + 2 = 4, 3 + 2 = 5, 4 + 2 = 6, 5 + 2 = 7

Hint: Iterate through the given list of numbers and construct a new list of numbers.
'''
def shift_numbers(numbers, shift):
    new_list = list(map(lambda x: x + shift, numbers))
    return (new_list)
    
'''
weave_lists
This function takes two lists and returns a new list that weaves the two lists together. The lists are guaranteed to be the same length.
A weave means you take elements from each list in alternating order and build a new list.

Input: list, list
Output: list

Example: [1, 2, 3], [4, 5, 6] -> [1, 4, 2, 5, 3, 6]
Example: ['a', 'b', 'c'], ['d', 'e', 'f'] -> ['a', 'd', 'b', 'e', 'c', 'f']

Hint: Iterate through the lists and construct a new list.
Hint: You must iterate through the lists at the same time.
'''
def weave_lists(list1, list2):
    weaved = []
    i = 0
    while i < len(list1):
        weaved.append(list1[i])
        weaved.append(list2[i]) 
        i += 1
    return (weaved)

'''
characters_to_string
This function takes a list of characters and returns a string by concatenating the characters together.

Input: list of characters
Output: string

Example: ['a', 'b', 'c'] -> 'abc'

Hint: This is testing your knowledge of different data types.
'''
def characters_to_string(characters):
    result = "".join([str(item) for item in characters])
    return (result)

'''
dictionary_lookup
This function takes a dictionary and a key and returns the value associated with the key. The key is guaranteed to be in the dictionary.

Input: dictionary (maps string to string), string (key)
Output: string

Example: dictionary: {'a': 'apple', 'b': 'banana'}, key: 'a' -> 'apple'
Explanation: The key 'a' is associated with the value 'apple' in the dictionary.

Hint: You may use this dictionary in your tests: my_dict = {'a': 'apple', 'b': 'banana', 'c': 'carrot', 'd': 'donut'}
Hint: The syntax for accessing a value in a dictionary is: dictionary[key] which returns the value associated with the key.
'''
def dictionary_lookup(dictionary, key):
    return dictionary.get(key, 'no data')


'''
dictionary_shift
This function takes a dictionary of integers and a shift value and returns a new dictionary where each value is shifted by the shift value.

Input: dictionary (maps integers to integers), integer
Output: dictionary (maps integers to integers)

Example: dictionary: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, shift: 2 -> {1: 3, 2: 4, 3: 5, 4: 6, 5: 7}
Explanation: The shift value is 2, so each value is shifted by 2. The key is not shifted.

Hint: Iterate through the given dictionary and construct a new dictionary.
Hint: You can iterate through the keys of a dictionary using the same syntax as iterating through a list: for key in dictionary:
'''
def dictionary_shift(dictionary, shift):
    new_dict = {}
    for key, value in dictionary.items(): 
        new_dict[key] = value + shift
    return new_dict
'''
vowel_strings
This fucntion takes a list of lowercase strings and returns a dictionary where the keys are the number of vowels in the string and the value is a list of all the strings with that number of vowels.

Input: list of strings
Output: dictionary containing the number of vowels in the string as the key and a list of all the strings with that number of vowels as the value

Example: ['a', 'aa', 'bb', 'ccc', 'dddd'] -> {0: ['bb', 'ccc', 'dddd'], 1: ['a'], 2: ['aa']}
Explanation: 'a' has 1 vowel, 'bb' has 0 vowels, 'ccc' has 0 vowels, 'dddd' has 0 vowels, and 'aa' has 2 vowels.

Hint: The problem is extremely similar to the even_odd_strings() function you wrote above.

'''
def vowels(string):
    vowel_count= 0
    vowels = ['a','e','i','o','u']
    for i in string:
        if i in vowels:
            vowel_count += 1
        if i not in vowels:
            vowel_count +=  0
    return vowel_count

def vowel_strings(strings):
    result = {}
    for i in strings:
        vowel_count = vowels(i)
        answer = result.get(vowel_count, [])
        answer.append(i)
        result[vowel_count] = answer 
    return result



