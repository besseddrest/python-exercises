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