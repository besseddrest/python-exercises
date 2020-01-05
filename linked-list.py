# Source: https://www.youtube.com/watch?v=JlMyYuY1aXU
#
# just trying to understand Linked Lists

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    # constructor
    def __init__(self):
        self.head = ListNode()

    # inserts a node at the next empty slot
    def add(self, val):
        # create a new node and pass in input value
        new_node = ListNode(val)

        # for all LinkedList methods, this declaration creats a 'temp' node
        current_node = self.head

        # For the very first item, the temp node .next IS `None`, so we bypass this...        
        while current_node.next != None:
            current_node = current_node.next

        # ...and then assign our new node in the first empty space
        current_node.next = new_node

    
    # removes the node at the specified index
    def remove(self, index):
        # check if index is too large for this list, or a negative int
        if index >= self.length() or index < 0:
            print("Out of bounds, man!")
            return None

        # again, temp node
        current_node = self.head
        current_index = 0

        # when we iterate here, we keep track of the previous node and the current node
        while current_node:
            last_node = current_node
            current_node = current_node.next

            # if we find the index of the node to remove...
            if current_index == index:
                # ...then we just point the previous node's .next to the .next of the item we are removing
                last_node.next = current_node.next
                return

            current_index += 1

    # returns the length of the linked list
    def length(self):
        count = 0
        current_node = self.head

        # increments a counter as we iterate over the nodes, until we hit a node that doesn't have a .next
        while current_node.next != None:
            count += 1
            current_node = current_node.next

        return count


    # displays the contents of the linked list
    def display(self):
        elements = []
        current_node = self.head

        # appends a new list
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.val)

        # note we're only printing an ARRAY that displays the elements of the LinkedList
        print(elements)


    # gets the value of the node at the specified index
    def get(self, index):
        # check if index is too large for this list, or a negative int
        if index >= self.length() or index < 0:
            print("Out of bounds, man!")
            return None

        current_node = self.head
        current_index = 0

        # iterate until we find the current_index, then return
        while current_node:
            current_node = current_node.next

            if current_index == index:
                print("Element at index {} is {}".format(index, current_node.val))
                return current_node.val

            current_index += 1


my_list = LinkedList()

my_list.add('hello')
my_list.add('world')
my_list.add('lorem')
my_list.add('ipsum')
my_list.display()
my_index = 2
my_list.get(my_index)
my_list.remove(1)
my_list.display()