my_list = ["apple", "banana", "orange", "grape"]

# Using a for loop
for item in my_list:
    if item.startswith("a"):
        print(item)

# Using a list comprehension
filtered_list = [item for item in my_list if item.startswith("a")]
print(filtered_list)
