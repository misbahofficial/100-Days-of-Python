# use recursion to find the summation of an algebraic series

def summation_recursive(n):
    if n == 1:  # Base case: The sum of 1 is 1
        return 1
    else:
        # Recursive case: Sum of numbers from 1 to n = n + Sum of numbers from 1 to (n-1)
        return n + summation_recursive(n - 1)


# Calculate the summation of numbers from 1 to 10
result = summation_recursive(10)
print("Sum of numbers from 1 to 10:", result)

print(summation_recursive(10))
