# declare the three rows with same values
row_01 = ['0', '0', '0']
row_02 = ['0', '0', '0']
row_03 = ['0', '0', '0']

# making a nested list with the previously declared lists
maps = [row_01, row_02, row_03]

# displaying the column and rows to screen
print(f'{row_01}\n{row_02}\n{row_03}')

# taking user input
place = input("Where do you want to put your treasure? (Enter column and row with a space between)\n")

# splitting out the user input on the basis of spaces
formatted_place = place.split(" ")

# putting the two values in different variables to use as indices
first_index = int(formatted_place[0]) - 1
second_index = int(formatted_place[1]) - 1

# replacing the previously declared lists with new value
maps[second_index][first_index] = 'X'

# displaying results to the screen
print(f'{row_01}\n{row_02}\n{row_03}')
