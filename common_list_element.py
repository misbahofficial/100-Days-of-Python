'''
Problem statement:
Write a Python function that takes two lists as input and returns
a new list containing elements that are present in both lists.
'''

def common_elements(list1, list2):
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)

    return common_items


f_list = [1, 3, 5, 6, 7, 12]
s_list = [3, 4, 6, 8, 12, 45, 1]

print(common_elements(f_list, s_list))
