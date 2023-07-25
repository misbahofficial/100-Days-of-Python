# print 10 to 1 downward with python recursion


def print_number(n):
    if n < 1:
        return
    print(n)
    print_number(n - 1)


print_number(10)
