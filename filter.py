# the function Filter filters an iterable by leaving only the items that match a condition

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_nums = list(filter(lambda x: x%2 == 0, nums))

print(new_nums)