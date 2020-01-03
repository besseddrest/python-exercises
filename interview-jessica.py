# ["Mark", "Lisa", "John", "Maddy"] => "Mark, Lisa, John and Maddy"

list1 = []
list2 = ["Maddy"]
list3 = ["Mark", "Lisa"]
list4 = ["Mark", "Lisa", "John"]
list5 = ["Mark", "Lisa", "John", "Maddy"]

def namesToString(names):
    """
    names   @list of names
    returns @string
    """
    
    if len(names) == 0:
        return ''
    
    if len(names) == 1:
        return names[0]
    
    if len(names) == 2:
        return ' and '.join(names)
    
    last_name = names.pop()
    
    name_string = ', '.join(names) + ' and ' + last_name
    
    return name_string

# print(namesToString(list5))

# Source: https://leetcode.com/problems/two-sum/
#
# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

nums = [4, 6, 8, 15]

target = 10

def two_sum(numbers, total):
    indices = []

    for number in numbers:
        # break if we found 2 indices
        if len(indices) > 1:
            break

        # copy list, pluck current number out of list
        list_copy = numbers.copy()
        list_copy.remove(number)

        # check current number against the rest of list
        for num in list_copy:
            # find number in copied list that adds up to total
            if num + number == total: 
                # if match found, find position of that number in original list
                indices.append(numbers.index(number))
                indices.append(numbers.index(num))
                # we found the pair, break out of the inner loop
                break

    # return a message if there are no pairs
    if len(indices) < 2:
        return "No two indices add up to {}".format(total)

    return indices

# print(two_sum(nums, target))

# TODO: doesn't work for list with repeated values [5, 5] target = 10
#  list.index() will return the lowest index (first occurance)
#
# but cool, works for negative ints
def two_sum2(numbers, total):
    indices = []

    for number in numbers:
        partner = total - number
        
        try:
            if numbers.index(partner) > -1:
                indices.append(numbers.index(number))
                indices.append(numbers.index(partner))
                break
        except ValueError:
            continue
    
    # return a message if there are no pairs
    if len(indices) < 2:
        return "No two indices add up to {}".format(total)

    return indices

print(two_sum2(nums, target))

# print(nums.index(5))