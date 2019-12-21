# -----------------------------------------------------------
# list comprehension exercises in python
# -----------------------------------------------------------   


# Source: https://www.learnpython.org/en/List_Comprehensions

# Using a list comprehension, create a new list called "newlist" 
# out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [number for number in numbers if number > 0]
# print(newlist)


# Source: https://www.reddit.com/r/learnpython/comments/4d2yl7/i_need_list_comprehension_exercises_to_drill/

# Find all of the numbers from 1-1000 that are divisible by 7
divisible_by_7 = [i for i in range(1, 1000) if i % 7 == 0]
# print(divisible_by_7)

# Find all of the numbers from 1-1000 that have a 3 in them
number_has_3 = [i for i in range(1000) if '3' in str(i)]
# print(number_has_3)

# Count the number of spaces in a string
lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eu mi id quam rhoncus consectetur'
spaces_in_string = sum([1 for i in lorem if i == ' '])
# print(spaces_in_string)

# Remove all of the vowels in a string
vowels = ('a', 'e', 'i', 'o', 'u')
remove_all_vowels = ''.join([i for i in lorem if not i in vowels])
# print(remove_all_vowels)

# Find all of the words in a string that are less than 4 letters
less_than_4 = [word for word in lorem.split(' ') if len(word) < 4]
# print(less_than_4)

# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
# note: this is out of context, sounds like we should use a dictionary here to display which numbers are divisible by which single digit
divisible_by_single_digit = [number for number in range(1, 1000) if [single for single in range(2, 9) if number % single == 0]]
# print(divisible_by_single_digit)

# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by


# Source: https://github.com/besseddrest/python-exercises/blob/master/list-comprehensions.py

# Given a list of numbers, write a list comprehension that produces a copy of the list.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_list_copy = [number for number in number_list]
# print(number_list_copy)

# Given a list of numbers, write a list comprehension that produces a list of each number doubled.
doubled = [number * 2 for number in number_list]
# print(doubled)

# Given a list of numbers, write a list comprehension that produces a list of the squares of each number.
squares = [number ** 2 for number in number_list]
# print(squares)

# Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
only_even = [number for number in number_list if number % 2 == 0]
# print(only_even)

# Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.
only_odd = [number for number in number_list if number % 2 > 0]
# print(only_odd)

# Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
numbers_list2 = [-1, 1, -3, -4, 5, 8, -9, -10, 11, 12, -13]
only_positive = [number for number in numbers_list2 if number > 0]
# print(only_positive)

# Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
numbers_list3 = [11, 15, 22, 25, 33, 35, 40, 44, 45, 50, 55, 56, 60]
divisible_by_5 = [str(number) for number in numbers_list3 if number % 5 == 0]
# print(divisible_by_5)

# Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
fox = 'The quick brown fox jumped over the lazy dog'
word_lengths = [len(word) for word in fox.split(' ') if word.lower() != 'the']
# print(word_lengths)

# Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.
word_with_vowels = 'ALUMINOSILICATES'
list_of_vowels = []
[list_of_vowels.append(letter) for letter in word_with_vowels if letter.lower() in ('a', 'e', 'i', 'o', 'u')]
print(list_of_vowels)



# Given a string representing a word, write a set comprehension that produces a set of all the vowels in that word.

# Given a sentence, return the sentence with all vowels removed.

# Given a list of number, return the list with all even numbers doubled, and all odd numbers turned negative.

# Given a sentence, return the setence will all it's letter transposed by 1 in the alphabet, but only if the letter is a-y.