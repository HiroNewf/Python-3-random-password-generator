import string
import random

# settings
password_length = int(input('What is the length you want the password to be? (A digit): '))
password_numbers = input("Do you want to include numbers in the password? (yes/no): ")
capitol_letters = input("Do you want to include capitol letters in the password? (yes/no): ")

if password_numbers == "yes" and capitol_letters == "yes":
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

elif password_numbers == "no" and capitol_letters == "yes":
    res = ''.join(random.choices(string.ascii_letters, k=password_length))
    
elif password_numbers == "yes" and capitol_letters == "no":
    res = ''.join(random.choices(string.digits, + string.ascii_lowercase, k=password_length))
    
elif password_numbers == "no" and capitol_letters == "no":
    res = ''.join(random.choices(k=password_length))
    
else:
    print('You have not entered valid responses, please try again')

print("Your password is: " + str(res))
