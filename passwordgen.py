import random
import string
def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(letters)
    return password
length = int(input("How many characters should the password be? "))
password = generate_password(length)
print("Your random password is: " + password)
