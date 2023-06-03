current_age = int(input("What is your current age? "))

remaining_year = 90 - current_age
remaining_months = remaining_year * 12
remaining_days = remaining_year * 365
# remaining_weeks = round(remaining_days / 7)
remaining_weeks = remaining_year * 52

print(f"You have {remaining_days} days, {remaining_weeks} weeks, {remaining_months} months left.")