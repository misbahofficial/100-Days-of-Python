'''
Problem statement:
Write a Python function that takes two tuples as input and returns
a new tuple containing elements that are common to both tuples.
'''

def common_elements(tuple1, tuple2):
    new_tuple = ()

    for element in tuple1:
        if element in tuple2:
            new_tuple += (element,)

    return new_tuple

t1 = (3, 4, 5, 1, 3, 4, 5)
t2 = (3, 5, 12, 1, 4, 9)

print(common_elements(t1, t2))