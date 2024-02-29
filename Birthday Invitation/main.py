# the word to be replaced
PLACEHOLDER = "[name]"

# getting the file that contains the guests' names
with open("Input/names.txt") as names:
    names = names.readlines()

# getting the file that has the letter format
with open("Input/letter.txt") as letter:
    letter = letter.read()


# writing each letter to an individual file
for name in names:
    new_name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, new_name)
    with open(f"Outputs/{new_name}.txt", 'w') as f:
        f.write(new_letter)
