# Using a list comprehension, create a new list called "newlist" 
# out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [number for number in numbers if number > 0]
# print(newlist)

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

# Use a dictionary comprehension to count the length of each word in a sentence.

# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by