import string
import random
import os

# settings

save_password = input("Do you want this password to be saved to your computer in a txt file? (yes/no): ") #note that this is not a safe way to store passwords at all. Passwords should NOT be stored in laintext on your desktop, but this is mainly just a script for messing around and if I ever end up actually wanting to use it for storage I will come up with a better solution to storage and security.

if save_password == "yes":
    site_name = input("What is the name of the site this password if for? (Or just the name you would like to reference this buy password by in the future): ")
    
password_length = int(input("What is the length you want the password to be? (A digit): "))
password_numbers = input("Do you want to include numbers in the password? (yes/no): ")
capitol_letters = input("Do you want to include capitol letters in the password? (yes/no): ")
special_characters = input("Do you want to include special characters in the password? (yes/no): ")

if not os.path.exists('Passwords'):
    os.mkdir('Passwords')

# All of the possibilities (this was very annoying to make but I guess it could be worse)
if password_numbers == "yes" and capitol_letters == "yes" and special_characters == "yes":
    the_password = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*()_', k=password_length))
    print("Your password is: " + str(the_password))

elif password_numbers == "yes" and capitol_letters == "yes" and special_characters == "no":
    the_password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
    print("Your password is: " + str(the_password))
    
elif password_numbers == "no" and capitol_letters == "yes" and special_characters == "yes":
    the_password = ''.join(random.choices(string.ascii_letters + '!@#$%^&*()_', k=password_length))
    print("Your password is: " + str(the_password))

elif password_numbers == "no" and capitol_letters == "yes" and special_characters == "no":
    the_password = ''.join(random.choices(string.ascii_letters, k=password_length))
    print("Your password is: " + str(the_password))

elif password_numbers == "yes" and capitol_letters == "no" and special_characters == "yes":
    the_password = ''.join(random.choices(string.digits + string.ascii_lowercase + '!@#$%^&*()_', k=password_length))
    print("Your password is: " + str(the_password))

elif password_numbers == "yes" and capitol_letters == "no" and special_characters == "no":
    the_password = ''.join(random.choices(string.digits, + string.ascii_lowercase, k=password_length))
    print("Your password is: " + str(the_password))

elif password_numbers == "no" and capitol_letters == "no" and special_characters == "yes":
    the_password = ''.join(random.choices('!@#$%^&*()_', k=password_length))
    print("Your password is: " + str(the_password))

elif password_numbers == "no" and capitol_letters == "no" and special_characters == "no":
    the_password = ''.join(random.choices(k=password_length))
    print("Your password is: " + str(the_password))

else:
    print('You have not entered valid responses, please try again')
