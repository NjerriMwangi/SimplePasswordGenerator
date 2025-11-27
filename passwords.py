import random
import string

print("Simple Password Generator 🚀...\n")
while True:
    try:
        password_length = int(input("How many characters for your password? "))
        if password_length <= 0:
            print("Please enter a positive number.")
        break
    except ValueError:
        print("Please enter a valid value!")

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters, k=password_length))
print("\nYour generated password is:")
print(password)