alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', ' ', ':', '*', '+', ',', ';', "'", '/', '{', '}',
            '@', '!', '#', '$', '%', '&', '(', ')', '[', ']',
            '.', '?', '-', '<', '>']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encrypted_text = ""

    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        encrypted_text += alphabet[new_position]
    print(f"Your encrypted text is: {encrypted_text} ")

def decrypt(encrypted_text, shift_amount):
    plain_text = ""

    for char in encrypted_text:
        position = alphabet.index(char)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"Your decrypted text is: {plain_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Wrong command. Try again.")

