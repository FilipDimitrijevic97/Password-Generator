import random
import string

# Generate a random password of a given length
# Author: Filip Dimitrijevic
# Date: 2023-01-26

# This function generates a random password of a given length
def generate_password(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters + string.digits + string.punctuation) for i in range(length))

# Get the desired length of the password from the user
while True:
    length_input = input("Enter the desired length of the password: ")
    if length_input.isdigit():
        length = int(length_input)
        break
    else:
        print("Invalid input. Please enter a number.")

# Print the generated password
print(generate_password(length))
