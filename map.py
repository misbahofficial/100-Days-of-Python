# map is a higher-order function which operates on list or similar iterables

salaries = [100, 250, 300, 455, 550, 1000]

new_salaries = list(map(lambda x: x * 2, salaries))

print(new_salaries)