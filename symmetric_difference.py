'''
Problem statement:
Write a Python function that takes two sets as input and returns a
new set containing elements that are present in either of the sets, but not in both.
'''

def sym_diff(set1, set2):
    return set1.symmetric_difference(set2)

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 4, 6, 8}

print(sym_diff(s1, s2))