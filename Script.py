import string
import random
import os

def generate_password(length, use_numbers, use_capital_letters, use_special_characters):
    # Define character sets based on user choices
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_characters:
        characters += '!@#$%^&*()_'
    
    # Generate and return the password
    return ''.join(random.choice(characters) for _ in range(length))

# Get user preferences
save_password = input("Do you want this password to be saved to your computer in a txt file? (yes/no): ")

if save_password.lower() == "yes":
    site_name = input("What is the name of the site this password is for? (Or just the name you would like to reference this password by in the future): ")
    
password_length = int(input("What is the length you want the password to be? (A digit): "))
password_numbers = input("Do you want to include numbers in the password? (yes/no): ").lower() == "yes"
capitol_letters = input("Do you want to include capital letters in the password? (yes/no): ").lower() == "yes"
special_characters = input("Do you want to include special characters in the password? (yes/no): ").lower() == "yes"

if save_password.lower() == "yes" and not os.path.exists('Passwords'):
    os.mkdir('Passwords')

# Generate and display the password
the_password = generate_password(password_length, password_numbers, capitol_letters, special_characters)

if save_password.lower() == "yes":
    # Save the password to a file
    file_path = os.path.join('Passwords', f'{site_name}_password.txt')
    with open(file_path, 'w') as file:
        file.write(the_password)
    print(f"Your password has been saved to {file_path}")
else:
    print("Your password is: " + the_password)
