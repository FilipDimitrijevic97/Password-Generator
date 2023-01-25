import random
import string

def generate_password(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters + string.digits + string.punctuation) for i in range(length))

length = int(input("Enter the desired length of the password: "))
print(generate_password(length))