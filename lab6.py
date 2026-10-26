
# Part 1 - Printing a Vigenere Square

def vigenere_sq(alphabet):
    # Print the header row
    print("|   |", end="")
    for letter in alphabet:
        print(f" {letter} |", end="")
    print()

    # Print the separator row
    print("|---|" + "---|" * len(alphabet))

    # Print each row of the Vigenere square
    for row in range(len(alphabet)):
        print(f"| {alphabet[row]} |", end="")

        for col in range(len(alphabet)):
            index = (row + col) % len(alphabet)
            print(f" {alphabet[index]} |", end="")

        print()


# Part 2 - Encryption

# Convert a letter to its index in the alphabet
def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


# Convert an index to its corresponding letter
def index_to_letter(index, alphabet):
    return alphabet[index]


# Find the encrypted letter using the key and plaintext letter
def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)

    cipher_index = (key_index + plaintext_index) % len(alphabet)

    return index_to_letter(cipher_index, alphabet)


# Encrypt the plaintext using the key
def encrypt_vigenere(key, plaintext, alphabet):
    ciphertext = ""
    key_position = 0

    # Go through each character in the plaintext
    for letter in plaintext:

        # Keep spaces and punctuation unchanged
        if letter not in alphabet:
            ciphertext += letter
        else:
            # Cycle through the key letters
            key_letter = key[key_position % len(key)]

            # Encrypt the current letter
            encrypted_letter = vigenere_index(
                key_letter, letter, alphabet
            )

            ciphertext += encrypted_letter

            # Move to the next key letter
            key_position += 1

    return ciphertext


# Main program

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Print the Vigenere square
vigenere_sq(alphabet)

# Choose a key and plaintext
key = "CORSAIR"
plaintext = "WELCOME TO THE WOODS"

# Convert the plaintext to uppercase
key = key.upper()
plaintext = plaintext.upper()

# Encrypt the message
ciphertext = encrypt_vigenere(key, plaintext, alphabet)

# Print the results
print()
print("Key:", key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)


