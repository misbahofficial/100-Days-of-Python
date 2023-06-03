# This code checks if a given year is a leap year.

# Get the year from the user.
given_year = int(input("Which year do you want to check? "))

# Check if the year is divisible by 4.
if given_year % 4 == 0:

    # If the year is divisible by 100, check if it is divisible by 400.
    if given_year % 100 == 0:

        # If the year is divisible by 400, it is a leap year.
        if given_year % 400 == 0:
            print(f"{given_year} is a Leap year.")

        # Otherwise, the year is not a leap year.
        else:
            print(f"{given_year} is not a Leap year.")

    # Otherwise, the year is divisible by 4 but not by 100, so it is a leap year.
    else:
        print(f"{given_year} is a Leap year.")

# Otherwise, the year is not divisible by 4, so it is not a leap year.
else:
    print(f"{given_year} is not a Leap year.")

'''
#Simplified version of the above program
# Get the year from the user
given_year = int(input("Enter a year: "))

# Check if it is a leap year
if given_year % 4 == 0 and (given_year % 100 != 0 or given_year % 400 == 0):
    print(f"{given_year} is a leap year.")
else:
    print(f"{given_year} is not a leap year.")

'''
