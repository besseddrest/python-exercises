# Source: https://leetcode.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.
#

"""
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

list1 = [1, 2, 4]
list2 = [1, 3, 4]

def mergeTwoLists(l1, l2):
    max_length = max(len(l1), len(l2))
    new_list = []

    # TODO: LINKED LISTS DUMMY

    # store = []

    # for i in range(0, max_length):
    #     if len(store) > 0 and store[0] <= l1[i] and store[0] <= l2[i]:
    #         new_list.append(store.pop()) 

    #     if l1[i] == l2[i]:
    #         new_list.extend([l1[i], l2[i]])
    #         continue

    #     if l1[i] < l2[i]:
    #         new_list.append(l1[i])
    #         store.append(l2[i])
    #         continue
                
    #     if l2[i] < l1[i]:
    #         new_list.append(l2[i])
    #         store.append(l1[i])
    #         continue

    #     if i == max_length - 1 and len(store) > 0:
    #         new_list = new_list + store

    return new_list

print(mergeTwoLists(list1, list2))