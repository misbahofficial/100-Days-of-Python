'''
Problem statement:
Write a Python function that takes a list of integers as input and returns
a new list with duplicates removed. The order of elements in
the new list should be preserved.
'''

def remove_duplicates(int_list):
    new_list = []

    for number in int_list:
        if number not in new_list:
            new_list.append(number)

    return new_list

my_list = [1, 2, 3, 2, 6, 7, 3, 19]

print(remove_duplicates(my_list))