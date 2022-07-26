import string
import random

# settings
password_length = int(input("What is the length you want the password to be? (A digit): "))
password_numbers = input("Do you want to include numbers in the password? (yes/no): ")
capitol_letters = input("Do you want to include capitol letters in the password? (yes/no): ")
special_characters = input("Do you want to include special characters in the password? (yes/no): ")

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
