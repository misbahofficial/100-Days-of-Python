'''
Problem statement:
Write a Python function that takes a list of integers as input and returns a new list containing only the even numbers from the original list.
'''

def keep_even(num_list):
    for number in num_list:
        if not number%2 == 0:
            num_list.remove(number)

    return num_list

my_list = [2, 3, 4, 7, 6, 7, 10]

print(keep_even(my_list))
