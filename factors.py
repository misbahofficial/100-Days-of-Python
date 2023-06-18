# A program to investigate all the factors of a given number

number = int(input("Enter number: "))

factors_list = []

for i in range(1, number + 1):
    if number % i == 0:
        factors_list.append(str(i))
factors = ", ".join(factors_list)
print(f'Factors of {number} are: {factors}')
