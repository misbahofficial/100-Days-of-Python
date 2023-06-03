# print welcome message
print("Welcome to the Tip Calculator.")

# ask for the total bill amount
total_bill = float(input("What was the total bill? $"))

# ask for the desired tip percentage
tips_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# ask for the number of people to split the bill
number_of_people = int(input("How many people to split the bill? "))

# calculate the total bill including tip
total_bill_to_be_paid = total_bill + (total_bill * (tips_percentage / 100))

# calculate the amount each person has to pay
each_person_has_to_pay = round(total_bill_to_be_paid / number_of_people, 2)

# display the amount each person should pay
print(f"Each person should pay: ${each_person_has_to_pay}")
