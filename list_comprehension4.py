'''
Problem statement:
Write a Python function that takes a list of integers as input and returns
a new list where each element is multiplied by 2,
but only if the original element is greater than 5.
'''

def get_list(given_list):
    new_list = [i*2 for i in given_list if i > 5]

    return new_list

my_list = [2, 3, 4, 5, 6, 7, 8]

print(get_list(my_list))