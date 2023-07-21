'''
Problem statement:
Given a tuple of strings, write a Python function that returns a new tuple where each string is reversed.
'''

def reversed_tuple_string(given_tuple):
    temp_list = list(given_tuple)
    new_list = []

    for item in temp_list:
        reversed_item = item[::-1]
        new_list.append(reversed_item)

    return tuple(new_list)


my_tuple = ('misbah', 'ahmed', 'razu')

print(reversed_tuple_string(my_tuple))